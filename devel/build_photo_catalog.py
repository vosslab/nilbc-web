#!/usr/bin/env python3
"""Build the repository photo catalog from the site's authoritative manifests."""

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'design_d_revised/data'
PHOTOS = ROOT / 'design_d_revised/site_src/assets/photos'
DEST = ROOT / 'docs/photos'


def asset_metadata(path: Path) -> dict:
	"""Read actual asset properties without modifying its image bytes."""
	with Image.open(path) as image:
		width, height = image.size
	return {
		'path': path.relative_to(ROOT).as_posix(),
		'width': width, 'height': height, 'bytes': path.stat().st_size,
		'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
	}


def build_catalog() -> dict:
	"""Produce linked theme sheets, show sequences, and a portable asset inventory."""
	manifest = yaml.safe_load((DATA / 'photos.yml').read_text())
	shows = yaml.safe_load((DATA / 'photo_shows.yml').read_text())
	photos = manifest['photos']
	ids = [photo['id'] for photo in photos]
	if len(ids) != len(set(ids)):
		raise ValueError('Photo IDs must be unique')
	inventory = []
	for photo in photos:
		photo_id = photo['id']
		if not photo_id.replace('_', '').isalnum():
			raise ValueError(f'Invalid photo ID: {photo_id}')
		if photo['theme'] not in manifest['themes']:
			raise ValueError(f'Unknown theme for {photo_id}')
		if photo.get('show') and photo['show'] not in shows:
			raise ValueError(f'Unknown show for {photo_id}')
		record = {key: photo[key] for key in ('id', 'theme', 'show', 'caption', 'alt', 'credit', 'focus') if key in photo}
		record['homepage'] = photo_id in manifest['homepage_photos']
		record['event_date'] = str(shows.get(photo.get('show'), {}).get('event_date', 'unknown'))
		record['capture_date'] = str(photo.get('capture_date', 'unknown'))
		record['full'] = asset_metadata(PHOTOS / f'{photo_id}.webp')
		record['thumbnail'] = asset_metadata(PHOTOS / f'{photo_id}_thumb.webp')
		original = ROOT / 'ARTIFACTS/discord_archive_shows' / f'{photo_id}.jpg'
		if original.exists():
			record['original'] = asset_metadata(original)
		inventory.append(record)
	outputs = {'inventory.yml': yaml.safe_dump(inventory, sort_keys=False, allow_unicode=False)}
	index = ['# Photo catalog', '',
		'Generated from the shared site manifests. Edit the manifests, then regenerate; do not edit these sheets.', '',
		f'{len(photos)} selected photo records. Browse the theme contact sheets below or [shows.md](shows.md).', '',
		'| Theme | Photos |', '| --- | --- |']
	for theme, title in manifest['themes'].items():
		selected = [record for record in inventory if record['theme'] == theme]
		index.append(f'| [{title}]({theme}.md) | {len(selected)} |')
		lines = [f'# {title}', '', '[README.md](README.md) / [shows.md](shows.md)', '']
		for record in selected:
			photo_id = record['id']
			full, thumb = record['full'], record['thumbnail']
			lines.extend([f'## {photo_id}', '',
				f"[![{record['alt']}](../../{thumb['path']})](../../{full['path']})", '', record['caption'], '',
				f"- Event date: {record['event_date']}; capture date: {record['capture_date']}.",
				f"- Full image: {full['width']} x {full['height']} pixels; {full['bytes']:,} bytes.",
				f"- Crop focus: {record.get('focus', 'center (default)')}. Focus controls display framing; follow the image link to inspect the full derivative.",
				f"- Homepage pick: {'yes' if record['homepage'] else 'no'}.",
				f"- Credit: {record['credit']}."])
			if record.get('show'):
				show = shows[record['show']]
				lines.append(f"- Show: [{show['title']}](shows.md#{record['show']}).")
			if 'original' in record:
				original = record['original']['path']
				lines.append(f'- Preserved original: [{Path(original).name}](../../{original}).')
			lines.append('')
		outputs[f'{theme}.md'] = '\n'.join(lines)
	index.extend(['', '## Metadata and editing', '',
		'- [inventory.yml](inventory.yml): dimensions, byte sizes, SHA-256 hashes, dates, categories, and crop focus.',
		'- [photos.yml](../../design_d_revised/data/photos.yml): captions, alt text, categories, credits, and homepage picks.',
		'- [photo_shows.yml](../../design_d_revised/data/photo_shows.yml): verified event dates and album order.',
		'- [provenance.json](../../ARTIFACTS/discord_archive_shows/provenance.json): original source and processing evidence.',
		'- [review.md](review.md): folder-by-folder review coverage for the full archive.',
		'- [review.json](../../ARTIFACTS/discord_archive_shows/review.json): source review evidence.', '',
		'## Selection boundaries', '',
		'This catalog covers the selected website photographs, not all 1,336 archive records.',
		'The full archive and its metadata index stay outside Git. No new photo rights are implied;',
		'uploader credit does not identify the photographer or builder. Event dates are not capture dates.',
		'Existing site photos without preserved archive originals retain their original source credits.',
		'See [DISCORD_ARCHIVE.md](../DISCORD_ARCHIVE.md) for the evidence and permitted demo-use scope.', '',
		'## Regenerate', '', '```bash',
		'source source_me.sh && python3 devel/build_photo_catalog.py',
		'source source_me.sh && python3 devel/build_photo_catalog.py --check', '```', '',
		'The catalog links to existing image files and adds no duplicate image copies.',
		'It lives in repository documentation and is not included in the club website.', ''])
	outputs['README.md'] = '\n'.join(index)
	by_id = {record['id']: record for record in inventory}
	lines = ['# Photographs by show', '', '[README.md](README.md)', '',
		'Albums are listed by verified event date, newest first. Image order follows the site manifest.', '']
	for show_id, show in sorted(shows.items(), key=lambda item: str(item[1].get('event_date', '')), reverse=True):
		associated = {record['id'] for record in inventory if record.get('show') == show_id}
		if set(show['sequence']) != associated or len(show['sequence']) != len(associated):
			raise ValueError(f'Incomplete or duplicate sequence for {show_id}')
		lines.extend([f'## {show_id}', '', f"{show['title']} - {show['date']}", '', show['description'], '',
			'| Preview | Photograph | Theme |', '| --- | --- | --- |'])
		for photo_id in show['sequence']:
			record = by_id[photo_id]
			lines.append(f"| ![{photo_id}](../../{record['thumbnail']['path']}) | [{photo_id}]({record['theme']}.md#{photo_id}) | {manifest['themes'][record['theme']]} |")
		lines.append('')
	outputs['shows.md'] = '\n'.join(lines)
	review = json.loads((ROOT / 'ARTIFACTS/discord_archive_shows/review.json').read_text())
	folders = {}
	for sheet in review['sheets']:
		folders.setdefault(sheet['channel'], []).append(sheet)
	lines = ['# Archive review coverage', '', '[README.md](README.md)', '',
		'This is the recorded visual review of the full archive, grouped by source folder.',
		'Folder names are source labels, not proof of event or capture dates. Review notes describe',
		'the selection pass; they do not establish that every unselected image is unusable.', '',
		f"{sum(sheet['tiles'] for sheet in review['sheets'])} image references across {len(review['sheets'])} contact sheets and {len(folders)} folders.", '',
		'Original contact sheets and unselected files remain in the external archive.',
		'Notes below are copied from the committed [review.json](../../ARTIFACTS/discord_archive_shows/review.json).', '']
	for folder, sheets in sorted(folders.items()):
		lines.extend([f'## {folder}', '',
			f"{sum(sheet['tiles'] for sheet in sheets)} image references; {len(sheets)} contact sheets.", ''])
		for note in dict.fromkeys(sheet['review'] for sheet in sheets):
			lines.extend([note, ''])
	outputs['review.md'] = '\n'.join(lines)
	return outputs


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('-c', '--check', dest='check', action='store_true', help='Check for stale catalog files without writing')
	args = parser.parse_args()
	outputs = build_catalog()
	if args.check:
		stale = [name for name, text in outputs.items() if not (DEST / name).exists() or (DEST / name).read_text() != text]
		if stale:
			raise SystemExit('Regenerate stale catalog: ' + ', '.join(stale))
	else:
		DEST.mkdir(parents=True, exist_ok=True)
		for name, text in outputs.items():
			(DEST / name).write_text(text)
	print(f'Photo catalog: {len(outputs)} files verified')


if __name__ == '__main__':
	main()
