"""
MkDocs hook for blocks filled from data files rather than written on the page.

Pages use the same `/// name` block syntax as the layout blocks in markdown_blocks.py; the
blocks below have no body and are swapped for HTML before the Markdown is converted:

- /// gallery | THEME        every photo in data/photos.yml with that theme
- /// photos | ID ID ID      the named photos, in order
- /// shows                  upcoming shows from the `shows:` front matter of shows/index.md
- /// next-show              a ticket for the first upcoming show
- /// diagram | PATH         an SVG file inlined so it follows the color scheme
- /// castle-module          the 15 by 60 inch castle module standard drawn as a plate

Each block closes with a `///` line. Keeping photo and show facts in one place means
captions and dates cannot drift between pages. Shows whose last day has passed
drop off automatically at the next build.
"""

# Standard Library
import os
import re
import html
import datetime

# PIP3 modules
import yaml
import PIL.Image

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST_FILE = os.path.join(REPO_ROOT, 'data', 'photos.yml')
PHOTO_DIR = os.path.join(REPO_ROOT, 'site_src', 'assets', 'photos')
SHOWS_PAGE = os.path.join(REPO_ROOT, 'site_src', 'shows', 'index.md')


DATA_BLOCK_NAMES = (
	'gallery', 'photos', 'shows', 'next-show', 'diagram', 'castle-module',
)
# one data block: opening line with optional argument, then the closing `///` line
DATA_BLOCK = re.compile(
	r'^/// (' + '|'.join(DATA_BLOCK_NAMES) + r')(?: *\| *(.*?))? *\n/// *$',
	re.MULTILINE,
)
# href values that are relative file paths (not URLs, fragments, or root paths)
RELATIVE_HREF = re.compile(r'href="(?![a-z]+:|#|/)([^"]+)"')

#============================================
def load_photos() -> dict:
	"""
	Load manifest photos keyed by id, in manifest order.
	"""
	with open(MANIFEST_FILE, 'r') as handle:
		manifest = yaml.safe_load(handle)
	by_id = {}
	for photo in manifest['photos']:
		# each photo carries its world's display name from the `themes:` table
		photo['theme_name'] = manifest['themes'][photo['theme']]
		by_id[photo['id']] = photo
	return by_id

#============================================
def load_themes() -> dict:
	"""
	Theme id to world name, from the `themes:` table in the photo manifest.
	"""
	with open(MANIFEST_FILE, 'r') as handle:
		themes = yaml.safe_load(handle)['themes']
	return themes

#============================================
def read_front_matter(path: str) -> dict:
	"""
	Read the YAML front matter at the top of a Markdown page.
	"""
	with open(path, 'r') as handle:
		text = handle.read()
	# front matter sits between the first two `---` lines
	front = text.split('---\n')[1]
	meta = yaml.safe_load(front)
	return meta

#============================================
def check_show(show: dict, number: int) -> None:
	"""
	Fail with a plain message when a show entry is missing a field or has a bad date.
	"""
	where = f"site_src/shows/index.md: show {number} ({show.get('venue', 'no venue')})"
	for key in ('venue', 'start', 'end', 'address'):
		if key not in show:
			raise ValueError(f"{where} needs `{key}:` (start and end are both required, "
				"even for a one-day show)")
	for key in ('start', 'end'):
		# YAML reads 2026-11-14 as a date; anything else stays text
		if not isinstance(show[key], datetime.date):
			raise ValueError(f"{where}: `{key}: {show[key]}` must be a date written YYYY-MM-DD")
	if show['end'] < show['start']:
		raise ValueError(f"{where}: `end` is before `start`")

#============================================
def upcoming_shows(today: datetime.date) -> list:
	"""
	Shows from the shows page front matter whose last day is today or later, by date.
	"""
	shows = read_front_matter(SHOWS_PAGE)['shows']
	for number, show in enumerate(shows, start=1):
		check_show(show, number)
	upcoming = [show for show in shows if show['end'] >= today]
	upcoming.sort(key=lambda show: show['start'])
	return upcoming

#============================================
def slugify(text: str) -> str:
	"""
	Anchor id for a venue name, matching the heading ids MkDocs would generate.
	"""
	slug = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
	return slug

#============================================
def image_size(filename: str) -> tuple:
	"""
	Return the pixel size of a built photo derivative.
	"""
	path = os.path.join(PHOTO_DIR, filename)
	if not os.path.exists(path):
		raise FileNotFoundError(f"site_src/assets/photos/{filename} is not built yet: run "
			"devel/fetch_club_photos.py and devel/build_site_assets.py -p (see docs/USAGE.md)")
	with PIL.Image.open(path) as image:
		size = image.size
	return size

#============================================
def figure_html(photo: dict, prefix: str) -> str:
	"""
	Build one gallery figure: thumbnail linking to the large image, caption.
	"""
	photo_id = photo['id']
	width, height = image_size(f"{photo_id}_thumb.webp")
	full_src = f"{prefix}assets/photos/{photo_id}.webp"
	thumb_src = f"{prefix}assets/photos/{photo_id}_thumb.webp"
	caption = html.escape(photo['caption'])
	alt = html.escape(photo['alt'], quote=True)
	theme_name = photo['theme_name']
	text = f'<figure class="nb-photo" data-world="{photo["theme"]}">'
	text += f'<a class="nb-photo__link" href="{full_src}" data-caption="{caption}">'
	text += f'<img src="{thumb_src}" alt="{alt}" width="{width}" height="{height}"'
	# optional focal point keeps the subject in frame when the card crops the photo
	if 'focus' in photo:
		text += f' style="object-position: {photo["focus"]}"'
	text += ' loading="lazy" decoding="async"></a>'
	text += f'<figcaption><span class="nb-photo__world">{theme_name}</span>'
	text += caption
	text += '</figcaption></figure>'
	return text

#============================================
def gallery_html(photos: dict, theme: str, prefix: str) -> str:
	"""
	Build the figure grid for every photo in a theme.
	"""
	themes = load_themes()
	if theme not in themes:
		raise ValueError(f"unknown gallery theme '{theme}'; use one of {sorted(themes)}")
	figures = [figure_html(p, prefix) for p in photos.values() if p['theme'] == theme]
	text = f'<div class="nb-gallery" data-world="{theme}">' + ''.join(figures) + '</div>'
	return text

#============================================
def mosaic_html(photos: dict, ids: list, prefix: str) -> str:
	"""
	Build a mosaic of named photos for feature sections.
	"""
	for photo_id in ids:
		if photo_id not in photos:
			raise ValueError(f"/// photos names '{photo_id}', which is not an id in data/photos.yml")
	figures =[figure_html(photos[photo_id], prefix) for photo_id in ids]
	text = '<div class="nb-mosaic">' + ''.join(figures) + '</div>'
	return text

#============================================
def long_date(day: datetime.date) -> str:
	"""
	A date written out for visitors, such as "Saturday, November 14".
	"""
	text = f"{day.strftime('%A, %B')} {day.day}"
	return text

#============================================
def dates_sentence(show: dict) -> str:
	"""
	The full dates line on a show card, with the year once at the end.
	"""
	start = show['start']
	end = show['end']
	if start == end:
		text = f"{long_date(start)}, {start.year}"
	else:
		text = f"{long_date(start)} and {long_date(end)}, {end.year}"
	return text

#============================================
def day_span(show: dict) -> str:
	"""
	Short day range such as "14&ndash;15", for the date tile and the ticket.
	"""
	start = show['start']
	end = show['end']
	if start == end:
		text = str(start.day)
	elif start.month == end.month:
		text = f"{start.day}&ndash;{end.day}"
	else:
		text = f"{start.day}&ndash;{end.strftime('%b')} {end.day}"
	return text

#============================================
def show_card_html(show: dict, is_next: bool) -> str:
	"""
	One show card: date tile, status tags, venue, dates, hours, address, and a map link.
	"""
	start = show['start']
	venue = html.escape(show['venue'])
	address = html.escape(show['address'])
	css = 'nb-show nb-show--next' if is_next else 'nb-show'
	text = f'<article class="{css}" id="{slugify(show["venue"])}">'
	text += '<div class="nb-show__date" aria-hidden="true">'
	text += f'<span class="nb-show__month">{start.strftime("%b")}</span>'
	text += f'<span class="nb-show__days">{day_span(show)}</span>'
	text += f'<span class="nb-show__year">{start.year}</span></div><div>'
	if is_next:
		text += '<span class="nb-tag nb-tag--listed nb-tag--star">Next show</span>'
	# a show without hours yet is labeled so visitors know to check back
	hours = show.get('hours')
	if hours is None:
		text += '<span class="nb-tag nb-tag--check nb-tag--clock">Hours coming soon</span>'
		hours = 'Posted closer to the show'
	dates = dates_sentence(show)
	# an optional note qualifies the dates, such as "Dates may still shift"
	if 'note' in show:
		dates += '. ' + show['note']
	text += f'<h3>{venue}</h3><dl>'
	text += f'<dt>Dates</dt><dd>{html.escape(dates)}</dd>'
	text += f'<dt>Hours</dt><dd>{html.escape(hours)}</dd>'
	text += f'<dt>Address</dt><dd>{address}</dd></dl>'
	query = re.sub(r'[ ,]+', '+', show['address'])
	text += f'<p><a class="nb-map-link" href="https://www.google.com/maps/search/?api=1&amp;query={query}">'
	text += 'Map</a></p></div></article>'
	return text

#============================================
def shows_html(shows: list) -> str:
	"""
	Every upcoming show as a card, the first marked as the next show.
	"""
	cards = [show_card_html(show, index == 0) for index, show in enumerate(shows)]
	text = '<div class="nb-shows">' + ''.join(cards) + '</div>'
	if not shows:
		text = '<p>New dates are on the way. Check back soon.</p>'
	return text

#============================================
def ticket_html(shows: list, prefix: str) -> str:
	"""
	The next-show ticket linking to its card on the shows page.
	"""
	if not shows:
		text = f'<a class="nb-ticket" href="{prefix}shows/"><span class="nb-ticket__label">'
		text += 'Shows</span><span class="nb-ticket__where">New dates coming soon</span></a>'
		return text
	show = shows[0]
	start = show['start']
	end = show['end']
	weekdays = start.strftime('%a')
	if end != start:
		weekdays += f"&ndash;{end.strftime('%a')}"
	when = f"{weekdays}, {start.strftime('%b')} {day_span(show)}, {end.year}"
	text = f'<a class="nb-ticket" href="{prefix}shows/#{slugify(show["venue"])}">'
	text += '<span class="nb-ticket__label">Next show</span>'
	text += f'<span class="nb-ticket__when">{when}</span>'
	text += f'<span class="nb-ticket__where">{html.escape(show["venue"])}</span>'
	text += '<span class="nb-ticket__go" aria-hidden="true">&rarr;</span></a>'
	return text

#============================================
def diagram_html(svg_rel: str, docs_dir: str, prefix: str) -> str:
	"""
	Inline an SVG diagram so it inherits the page's colors and fonts.
	"""
	with open(os.path.join(docs_dir, svg_rel), 'r') as handle:
		svg_text = handle.read()
	# file-relative hrefs inside the SVG resolve through the SVG's own folder
	svg_dir = os.path.dirname(svg_rel)
	svg_text = RELATIVE_HREF.sub(f'href="{prefix}{svg_dir}/\\1"', svg_text)
	# one raw HTML block: no blank lines inside it
	lines = [line for line in svg_text.splitlines() if line.strip()]
	text = '<figure class="nb-anatomy-figure">\n' + '\n'.join(lines) + '\n</figure>'
	return text

#============================================
def castle_module_html() -> str:
	"""
	The castle module standard as a 16 x 4 stud plate with its two dimensions.
	"""
	text = '<div class="nb-module" aria-hidden="true"><span class="nb-module__plate"></span>'
	text += '<span class="nb-module__w"><b>60 in</b></span>'
	text += '<span class="nb-module__d"><b>15 in</b></span></div>'
	return text

#============================================
def path_prefix(page_url: str) -> str:
	"""
	Relative prefix from a page's directory URL back to the site root.
	"""
	# directory URLs such as "shows/visiting/" sit two levels below the root
	depth = page_url.count('/')
	prefix = '../' * depth
	return prefix

#============================================
def check_banner_photo(markdown: str, page: object, photos: dict) -> None:
	"""
	Fail the build when a page banner names an unknown photo or repeats a body photo.
	"""
	# banners are optional; `matchstick` shows the mascot render instead of a photo
	art = page.meta.get('art')
	if art is None or art == 'matchstick':
		return
	if art not in photos:
		raise ValueError(f"{page.file.src_path}: banner art '{art}' is not in data/photos.yml")
	# photos shown in the body: listed ids plus every photo of each gallery theme
	body_ids = set()
	for name, argument in DATA_BLOCK.findall(markdown):
		if name == 'photos':
			body_ids.update(argument.split())
		elif name == 'gallery':
			body_ids.update(pid for pid, p in photos.items() if p['theme'] == argument)
	if art in body_ids:
		raise ValueError(f"{page.file.src_path}: banner photo '{art}' repeats in the page body")

#============================================
def check_blocks(markdown: str, src_path: str, config: object) -> None:
	"""
	Fail the build on an unknown block name or a block missing its closing `///` line.
	"""
	known = set(DATA_BLOCK_NAMES)
	# the layout block extension added by markdown_blocks.py lists its own names
	for extension in config['markdown_extensions']:
		if hasattr(extension, 'block_names'):
			known |= extension.block_names()
	opened = []
	in_code = False
	for number, line in enumerate(markdown.splitlines(), start=1):
		# fenced code may show block syntax as an example
		if line.startswith('```'):
			in_code = not in_code
			continue
		if in_code:
			continue
		stripped = line.strip()
		if stripped == '///':
			if not opened:
				raise ValueError(f"site_src/{src_path}:{number}: a `///` closes no open block")
			opened.pop()
		elif stripped.startswith('/// '):
			name = stripped[4:].split('|')[0].strip()
			if name not in known:
				raise ValueError(f"site_src/{src_path}:{number}: unknown block `/// {name}`; "
					f"known blocks: {', '.join(sorted(known))}")
			opened.append((name, number))
	if opened:
		name, number = opened[-1]
		raise ValueError(f"site_src/{src_path}:{number}: `/// {name}` has no closing `///` line")

#============================================
def on_config(config: object) -> object:
	"""
	MkDocs event: share the announcement from the home page front matter with the theme.
	"""
	home_meta = read_front_matter(os.path.join(config['docs_dir'], 'index.md'))
	config['extra']['announcement'] = home_meta['announcement']
	return config

#============================================
def on_page_markdown(markdown: str, page: object, config: object, files: object) -> str:
	"""
	MkDocs event: swap data blocks for HTML before Markdown conversion.
	"""
	check_blocks(markdown, page.file.src_path, config)
	photos = load_photos()
	check_banner_photo(markdown, page, photos)
	prefix = path_prefix(page.url)
	shows = upcoming_shows(datetime.date.today())

	def replace_block(match: re.Match) -> str:
		name = match.group(1)
		# the argument is optional: `/// shows` has none
		argument = ''
		if match.group(2) is not None:
			argument = match.group(2).strip()
		if name == 'gallery':
			block = gallery_html(photos, argument, prefix)
		elif name == 'photos':
			block = mosaic_html(photos, argument.split(), prefix)
		elif name == 'shows':
			block = shows_html(shows)
		elif name == 'next-show':
			# a block-level wrapper keeps the link a raw HTML block, not inline text
			block = '<div class="nb-ticket-row">' + ticket_html(shows, prefix) + '</div>'
		elif name == 'castle-module':
			block = castle_module_html()
		else:
			block = diagram_html(argument, config['docs_dir'], prefix)
		# blank lines keep the HTML a raw block, also inside a layout block
		wrapped = '\n' + block + '\n'
		return wrapped

	markdown = DATA_BLOCK.sub(replace_block, markdown)
	return markdown
