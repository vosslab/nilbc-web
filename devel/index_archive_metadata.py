#!/usr/bin/env python3
"""Index factual image metadata from the preserved NILTC archive."""

import argparse
import json
import os
import tempfile
import xml.etree.ElementTree
from collections import defaultdict
from pathlib import Path

from PIL import Image


def text_value(value: object) -> str | list[str]:
	if isinstance(value, bytes):
		return value.decode("utf-8", errors="replace").strip("\x00 ")
	if isinstance(value, (list, tuple)):
		return [text_value(item) for item in value]
	return str(value).strip("\x00 ")


def exif_metadata(image: Image.Image) -> dict:
	exif = image.getexif()
	metadata = {}
	for tag_id, value in exif.items():
		name = Image.ExifTags.TAGS.get(tag_id, str(tag_id))
		if name in {"DateTimeOriginal", "DateTimeDigitized", "DateTime", "ImageDescription", "Copyright", "Artist", "XPTitle", "XPComment", "XPKeywords", "XPSubject"}:
			metadata[name] = text_value(value)
	if 0x8769 in exif:
		for tag_id, value in exif.get_ifd(0x8769).items():
			name = Image.ExifTags.TAGS.get(tag_id, str(tag_id))
			if name in {"DateTimeOriginal", "DateTimeDigitized", "OffsetTimeOriginal", "OffsetTimeDigitized", "SubSecTimeOriginal", "ImageDescription", "Copyright", "Artist"}:
				metadata[name] = text_value(value)
	return metadata


def iptc_metadata(image: Image.Image) -> dict:
	iptc = image.info.get("photoshop", {}).get(0x0404)
	if not iptc:
		return {}
	field_names = {
		(2, 5): "title", (2, 25): "keywords", (2, 55): "date_created",
		(2, 60): "time_created", (2, 62): "digital_creation_date",
		(2, 63): "digital_creation_time", (2, 80): "creator",
		(2, 105): "headline", (2, 110): "credit", (2, 120): "description",
	}
	metadata = {}
	offset = 0
	while offset < len(iptc):
		if iptc[offset] != 0x1C:
			offset += 1
			continue
		if len(iptc) - offset < 5:
			raise ValueError("Truncated IPTC dataset header.")
		record, dataset = iptc[offset + 1], iptc[offset + 2]
		length = int.from_bytes(iptc[offset + 3:offset + 5], "big")
		offset += 5
		if length & 0x8000:
			length_size = length & 0x7FFF
			if length_size == 0 or len(iptc) - offset < length_size:
				raise ValueError("Truncated IPTC extended length.")
			length = int.from_bytes(iptc[offset:offset + length_size], "big")
			offset += length_size
		if len(iptc) - offset < length:
			raise ValueError("Truncated IPTC dataset payload.")
		value = text_value(iptc[offset:offset + length])
		offset += length
		key = (record, dataset)
		if key in field_names:
			name = field_names[key]
			if name == "keywords":
				metadata.setdefault(name, []).append(value)
			else:
				metadata[name] = value
	return metadata


def xmp_metadata(image: Image.Image) -> dict:
	xmp = image.info.get("xmp")
	if not xmp:
		return {}
	if isinstance(xmp, str):
		xmp = xmp.encode("utf-8")
	root = xml.etree.ElementTree.fromstring(xmp)
	namespaces = {
		"dc": "http://purl.org/dc/elements/1.1/",
		"photoshop": "http://ns.adobe.com/photoshop/1.0/",
		"xmp": "http://ns.adobe.com/xap/1.0/",
		"iptc": "http://iptc.org/std/Iptc4xmpCore/1.0/xmlns/",
	}
	fields = {
		"title": "dc:title", "description": "dc:description",
		"creator": "dc:creator", "rights": "dc:rights",
		"create_date": "xmp:CreateDate", "keywords": "dc:subject",
		"date_created": "iptc:DateCreated",
	}
	metadata = {}
	for key, path in fields.items():
		prefix, local_name = path.split(":")
		qualified_name = "{" + namespaces[prefix] + "}" + local_name
		values = [element.attrib[qualified_name] for element in root.iter() if qualified_name in element.attrib]
		if not values:
			element = root.find(".//" + path, namespaces)
			if element is not None:
				values = [child.text for child in element.iter() if child.text and child.text.strip()]
		if values:
			metadata[key] = values if key in {"creator", "keywords"} else values[0]
	for key, path in (("headline", "photoshop:Headline"), ("credit", "photoshop:Credit"), ("copyright", "photoshop:Copyright")):
		prefix, local_name = path.split(":")
		qualified_name = "{" + namespaces[prefix] + "}" + local_name
		values = [element.attrib[qualified_name] for element in root.iter() if qualified_name in element.attrib]
		if not values:
			element = root.find(".//" + path, namespaces)
			if element is not None and element.text:
				values.append(element.text.strip())
		if values:
			metadata[key] = values[0]
	return metadata


def image_record(archive: Path, source: dict) -> dict:
	path = archive / source["local_path"]
	warnings = []
	with Image.open(path) as image:
		original_width, original_height = image.size
		orientation = image.getexif().get(274, 1)
		width, height = (original_height, original_width) if orientation in {5, 6, 7, 8} else image.size
		metadata = {"exif": exif_metadata(image), "iptc": {}}
		try:
			metadata["iptc"] = iptc_metadata(image)
		except ValueError:
			warnings.append("Malformed embedded IPTC was not parsed.")
		try:
			metadata["xmp"] = xmp_metadata(image)
		except xml.etree.ElementTree.ParseError:
			metadata["xmp"] = {}
			warnings.append("Malformed embedded XMP was not parsed.")
		info = {
			"format": image.format,
			"width": width,
			"height": height,
			"aspect_ratio": round(width / height, 6),
			"encoded_width": original_width,
			"encoded_height": original_height,
			"metadata": metadata,
		}
		if not any(metadata.values()):
			warnings.append("No EXIF, IPTC, or XMP descriptive metadata found.")
		if info["format"] not in {"JPEG", "PNG", "WEBP", "TIFF", "GIF", "BMP"}:
			warnings.append(f"Uncommon decoded image format: {info['format']}.")
	return {
		"channel": source["channel"],
		"attachment_id": source["attachment_id"],
		"message_id": source["message_id"],
		"filename": source["filename"],
		"content_type": source["content_type"],
		"advertised_bytes": source["size"],
		"received_bytes": source["received_bytes"],
		"size_matches_metadata": source["size_matches_metadata"],
		"download_status": source["status"],
		"decode_status": source["decode"],
		"local_path": source["local_path"],
		"sha256": source["sha256"],
		"timestamp": source["timestamp"],
		"upload_date": source["timestamp"],
		"capture_date": metadata["exif"].get("DateTimeOriginal"),
		"event_date": None,
		"image": info,
		"warnings": warnings,
	}


def build_index(archive: Path) -> dict:
	sources = json.loads((archive / "downloads.json").read_text())
	records = [image_record(archive, source) for source in sources]
	by_hash = defaultdict(list)
	for record in records:
		by_hash[record["sha256"]].append({"attachment_id": record["attachment_id"], "local_path": record["local_path"]})
	duplicates = [{"sha256": digest, "references": refs} for digest, refs in sorted(by_hash.items()) if len(refs) > 1]
	return {"source": "downloads.json", "record_count": len(records), "duplicate_group_count": len(duplicates), "records": records, "exact_duplicate_groups": duplicates}


def write_atomic(path: Path, content: dict) -> None:
	path.parent.mkdir(parents=True, exist_ok=True)
	with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as temporary:
		temporary.write(json.dumps(content, indent=2, ensure_ascii=True) + "\n")
		temporary_path = Path(temporary.name)
	os.replace(temporary_path, path)


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("archive", nargs="?", type=Path, default=Path("/home/vosslab/nsh/niltc_archive_shows"))
	args = parser.parse_args()
	index = build_index(args.archive)
	write_atomic(args.archive / "metadata.json", index)
	print(f"Indexed {index['record_count']} images; {index['duplicate_group_count']} exact duplicate groups.")


if __name__ == "__main__":
	main()
