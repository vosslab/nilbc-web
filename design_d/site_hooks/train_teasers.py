"""Reuse the current train selection for original D's dedicated teaser page."""
import html
from pathlib import Path

from mkdocs.structure.files import File
import yaml

SHARED = Path(__file__).resolve().parents[2] / 'design_d_revised'


def train_photos() -> list:
	manifest = yaml.safe_load((SHARED / 'data/photos.yml').read_text())
	return [photo for photo in manifest['photos'] if photo['theme'] == 'trains']


def on_files(files: object, config: object) -> object:
	"""Copy shared previews into D's output without duplicating source images."""
	for photo in train_photos():
		uri = f"assets/photos/{photo['id']}_thumb.webp"
		existing = files.get_file_from_path(uri)
		if existing is not None:
			files.remove(existing)
		files.append(File(uri, str(SHARED / 'site_src'), config['site_dir'], config['use_directory_urls']))
	return files


def on_page_markdown(markdown: str, page: object, config: object, files: object) -> str:
	if page.file.src_uri != 'creations/trains.md':
		return markdown
	photos = train_photos()
	parts = [f'<p class="nb-collection-count">{len(photos)} photos</p>', '<div class="nb-train-previews">']
	for photo in photos:
		parts.append(f'<figure><img src="../../assets/photos/{photo["id"]}_thumb.webp" '
			f'alt="{html.escape(photo["alt"], quote=True)}" loading="lazy" decoding="async">'
			f'<figcaption>{html.escape(photo.get("album_caption", photo["caption"]))}'
			'</figcaption></figure>')
	parts.append('</div>')
	return markdown.replace('<!-- train previews -->', ''.join(parts))
