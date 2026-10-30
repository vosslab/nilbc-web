"""Test archive metadata extraction without opening the preserved collection."""

import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock

from PIL import Image

import devel.index_archive_metadata as archive_metadata


def make_source(tmp_path: Path, local_path: str, attachment_id: str) -> dict:
	path = tmp_path / local_path
	path.parent.mkdir(parents=True, exist_ok=True)
	image = Image.new("RGB", (2, 3), "red")
	exif = Image.Exif()
	exif[274] = 6
	exif[36867] = "2024:05:06 07:08:09"
	image.save(path, exif=exif)
	return {
		"channel": "2024-01-example",
		"attachment_id": attachment_id,
		"message_id": "message-" + attachment_id,
		"filename": path.name,
		"content_type": "image/jpeg",
		"size": path.stat().st_size,
		"received_bytes": path.stat().st_size,
		"size_matches_metadata": True,
		"status": "downloaded",
		"decode": "verified",
		"local_path": local_path,
		"sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
		"timestamp": "2024-01-02T03:04:05+00:00",
	}


def test_image_record_separates_capture_upload_and_event_dates(tmp_path: Path) -> None:
	source = make_source(tmp_path, "show/photo.jpg", "attachment-1")
	record = archive_metadata.image_record(tmp_path, source)
	assert record["capture_date"] == "2024:05:06 07:08:09"
	assert record["upload_date"] == source["timestamp"]
	assert record["event_date"] is None
	assert record["image"]["width"] == 3
	assert record["image"]["height"] == 2
	assert record["image"]["aspect_ratio"] == 1.5


def test_index_keeps_exact_duplicate_references(tmp_path: Path) -> None:
	source_a = make_source(tmp_path, "show/photo-a.jpg", "attachment-a")
	path_a = tmp_path / source_a["local_path"]
	path_b = tmp_path / "show/photo-b.jpg"
	path_b.write_bytes(path_a.read_bytes())
	source_b = dict(source_a, attachment_id="attachment-b", filename=path_b.name, local_path="show/photo-b.jpg")
	(tmp_path / "downloads.json").write_text(json.dumps([source_a, source_b]))
	index = archive_metadata.build_index(tmp_path)
	assert index["record_count"] == 2
	assert index["duplicate_group_count"] == 1
	assert len(index["exact_duplicate_groups"][0]["references"]) == 2


def test_xmp_create_date_is_not_reported_as_capture_date(tmp_path: Path) -> None:
	source = make_source(tmp_path, "show/xmp.jpg", "attachment-xmp")
	path = tmp_path / source["local_path"]
	xmp = b'<x:xmpmeta xmlns:x="adobe:ns:meta/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xmp="http://ns.adobe.com/xap/1.0/"><rdf:RDF><rdf:Description xmp:CreateDate="2025-01-02T03:04:05Z" /></rdf:RDF></x:xmpmeta>'
	Image.new("RGB", (2, 3), "blue").save(path, xmp=xmp)
	source["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
	record = archive_metadata.image_record(tmp_path, source)
	assert record["capture_date"] is None
	assert record["image"]["metadata"]["xmp"]["create_date"] == "2025-01-02T03:04:05Z"


def test_iptc_keyword_dataset_is_extracted() -> None:
	image = SimpleNamespace(info={"photoshop": {0x0404: b"\x1c\x02\x19\x00\x04cats"}})
	assert archive_metadata.iptc_metadata(image)["keywords"] == ["cats"]


def test_malformed_iptc_datasets_are_rejected_without_partial_fields() -> None:
	malformed = (
		b"\x1c\x02\x19\x00\x04cat",  # Payload shorter than declared.
		b"\x1c\x02",  # Truncated dataset header.
		b"\x1c\x02\x19\x80\x02\x00x",  # Truncated extended length.
	)
	for iptc in malformed:
		image = SimpleNamespace(info={"photoshop": {0x0404: iptc}})
		try:
			archive_metadata.iptc_metadata(image)
		except ValueError:
			pass
		else:
			raise AssertionError(f"Malformed IPTC accepted: {iptc!r}")


def test_image_record_warns_on_malformed_iptc_and_keeps_other_metadata(tmp_path: Path, monkeypatch) -> None:
	source = make_source(tmp_path, "show/photo.jpg", "attachment-iptc")
	image = MagicMock(size=(2, 3), format="JPEG", info={"photoshop": {0x0404: b"\x1c\x02\x19\x00\x04cat"}})
	image.getexif.return_value = {36867: "2024:05:06 07:08:09"}
	image.__enter__.return_value = image
	monkeypatch.setattr(archive_metadata.Image, "open", lambda path: image)

	record = archive_metadata.image_record(tmp_path, source)
	assert record["image"]["metadata"]["iptc"] == {}
	assert record["image"]["metadata"]["exif"]["DateTimeOriginal"] == "2024:05:06 07:08:09"
	assert "Malformed embedded IPTC was not parsed." in record["warnings"]
