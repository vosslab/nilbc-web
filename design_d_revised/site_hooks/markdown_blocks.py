"""
MkDocs hook that adds the site's layout blocks to Markdown.

Editors write ordinary Markdown inside a block; the block arranges it into the club's
components. Blocks open with `/// name` (optionally `/// name | argument`) and close with
`///`. They nest. The full list, with examples, is in docs/USAGE.md:

hero, steps, cards, worlds, stats, split, callout, columns, social, parts, world, train

Blocks with no body (gallery, photos, shows, castle-module, and others) live in
data_blocks.py, which swaps them for HTML before parsing, so they nest anywhere.

Blocks run while Markdown is parsed into a tree, before inline Markdown (bold, links,
images) is converted, so they read list items and headings as raw Markdown text. A final
tree pass runs after inline conversion to finish what needs real elements (figures,
section kickers, train cars).
"""

# Standard Library
import re
import xml.etree.ElementTree

# PIP3 modules
import markdown
import pymdownx.blocks
import pymdownx.blocks.block

Element = xml.etree.ElementTree.Element
SubElement = xml.etree.ElementTree.SubElement

# a paragraph that holds only one Markdown image, with optional { attributes }
IMAGE_ONLY = re.compile(r'^!\[[^\]]*\]\([^)]*\)(\{[^}]*\})?$')
# leading bold text of a list item: "**2001: Started** rest"
LEAD_BOLD = re.compile(r'^\*\*(.+?)\*\*\s*')
# leading icon shortcode of a card heading: ":material-earth: He goes everywhere"
LEAD_ICON = re.compile(r'^(:[a-z0-9_-]+:)\s*')
# hex color written as inline code: `#AC78BA`
HEX_CODE = re.compile(r'`(#[0-9A-Fa-f]{6})`')
# trailing emphasized note on a parts item: _Medium Lavender `#AC78BA`_
TRAILING_NOTE = re.compile(r'\s*_([^_]+)_\s*$')
# a paragraph that is only a stashed raw HTML block (such as a data block)
STASHED = re.compile(markdown.util.HTML_PLACEHOLDER % r'\d+')
# color cycles for repeated cards
CARD_COLORS = ('red', 'azure', 'lavender', 'yellow')
WORLD_COLORS = ('red', 'azure', 'lavender', 'grey', 'lime')
# marks a paragraph to be replaced by its children once inline Markdown is converted
UNWRAP = 'data-nb-unwrap'
# the page being converted, so block errors can name it (MkDocs converts one page at a time)
CURRENT_PAGE = {'path': ''}

#============================================
class BlockError(ValueError):
	"""
	A block written in a shape it cannot read; the message names the page and the fix.
	"""

	def __init__(self, message: str) -> None:
		super().__init__(f"site_src/{CURRENT_PAGE['path']}: {message}")

#============================================
def add_class(element: Element, name: str) -> None:
	"""
	Append a CSS class to an element.
	"""
	classes = element.get('class', '').split()
	classes.append(name)
	element.set('class', ' '.join(classes))

#============================================
def text_of(element: Element) -> str:
	"""
	Raw Markdown text of a paragraph or list item, stripped.
	"""
	# etree leaves text as None on elements that start with a child
	text = ''
	if element.text is not None:
		text = element.text.strip()
	return text

#============================================
def is_image_paragraph(element: Element) -> bool:
	"""
	True when the element is a paragraph holding a single Markdown image.
	"""
	result = element.tag == 'p' and IMAGE_ONLY.match(text_of(element)) is not None
	return result

#============================================
def is_stashed(element: Element) -> bool:
	"""
	True when the element is a paragraph holding only a raw HTML block.
	"""
	result = element.tag == 'p' and STASHED.fullmatch(text_of(element)) is not None
	return result

#============================================
def item_target(item: Element) -> Element:
	"""
	The element holding a list item's text: the item itself, or its first paragraph.
	"""
	# loose lists wrap each item's text in a paragraph
	target = item
	if not text_of(item) and len(item) > 0 and item[0].tag == 'p':
		target = item[0]
	return target

#============================================
def group_by_heading(block: Element, tag: str, name: str) -> list:
	"""
	Split a block's children into one group per heading; nothing may come before the first.
	"""
	groups = []
	for child in list(block):
		if child.tag == tag:
			groups.append([child])
		elif groups:
			groups[-1].append(child)
		else:
			# text before the first heading has no card or column to go in
			level = '#' * int(tag[1])
			raise BlockError(f"/// {name}: start with a `{level} ` heading; found "
				f"'{text_of(child)[:60]}' before it")
	return groups

#============================================
def lead_bold(target: Element, name: str, form: str) -> re.Match:
	"""
	Match the bold text that must start a list item, or explain the expected form.
	"""
	match = LEAD_BOLD.match(text_of(target))
	if match is None:
		raise BlockError(f"/// {name}: each item must look like {form}; "
			f"got '{text_of(target)[:60]}'")
	return match

#============================================
def find_list(block: Element, name: str, tags: tuple) -> Element:
	"""
	The list a block wraps, or an explanation of what the block expects.
	"""
	for tag in tags:
		found = block.find(tag)
		if found is not None:
			return found
	raise BlockError(f"/// {name}: write a list inside this block")

#============================================
def move_children(source: Element, target: Element) -> None:
	"""
	Move every child of one element to the end of another.
	"""
	for child in list(source):
		source.remove(child)
		target.append(child)

#============================================
class LayoutBlock(pymdownx.blocks.block.Block):
	"""
	Base for layout blocks: a div with a class, content parsed as block Markdown.
	"""
	CSS = ''
	ARGUMENT = None

	def on_markdown(self) -> str:
		return 'block'

	def on_create(self, parent: Element) -> Element:
		element = SubElement(parent, 'div', {'class': self.CSS})
		return element

	def _end(self, block: Element) -> None:
		# pymdownx closes an outer block early when an empty block is nested inside it,
		# then closes it again; fail loudly instead of losing content
		if block.get('data-nb-closed'):
			raise BlockError(f"/// {self.NAME} closed twice: a block with no body is nested inside it")
		block.set('data-nb-closed', '1')
		super()._end(block)

#============================================
class StepsBlock(LayoutBlock):
	"""
	/// steps (or /// steps | timeline): a numbered list drawn as instruction-booklet steps.
	Each item starts with a bold title. In a timeline the title starts with its date:
	`1. **2001: Started** The club began...`.
	"""
	NAME = 'steps'
	CSS = 'nb-steps'

	def on_end(self, block: Element) -> None:
		source = find_list(block, self.NAME, ('ol', 'ul'))
		# the block itself becomes the list
		block.remove(source)
		block.tag = 'ol'
		move_children(source, block)
		if self.argument == 'timeline':
			add_class(block, 'nb-steps--timeline')
			for item in block:
				target = item_target(item)
				form = '`1. **2001: Started** text`'
				match = lead_bold(target, 'steps | timeline', form)
				if ': ' not in match.group(1):
					raise BlockError(f"/// steps | timeline: put the date first, as in {form}; "
						f"got '{match.group(1)}'")
				date, title = match.group(1).split(': ', 1)
				item.set('data-year', date)
				target.text = f"**{title}** " + text_of(target)[match.end():]

#============================================
class CardsBlock(LayoutBlock):
	"""
	/// cards: each `### :icon-name: Title` heading and the text under it becomes a card.
	"""
	NAME = 'cards'
	CSS = 'nb-cards'

	def on_end(self, block: Element) -> None:
		groups = group_by_heading(block, 'h3', self.NAME)
		for child in list(block):
			block.remove(child)
		if len(groups) == 3:
			add_class(block, 'nb-cards--3')
		for index, group in enumerate(groups):
			color = CARD_COLORS[index % len(CARD_COLORS)]
			card = SubElement(block, 'div', {'class': f'nb-brick nb-brick--{color}'})
			heading = group[0]
			match = LEAD_ICON.match(text_of(heading))
			# the heading's leading icon shortcode moves above the title
			if match:
				icon = SubElement(card, 'p', {'class': 'nb-brick__icon'})
				icon.text = match.group(1)
				heading.text = text_of(heading)[match.end():]
			for child in group:
				card.append(child)

#============================================
class WorldsBlock(LayoutBlock):
	"""
	/// worlds: each `### [World](link)` heading, its photo, and its text becomes a world card.
	A card can show a data block (such as /// castle-module) instead of a photo.
	"""
	NAME = 'worlds'
	CSS = 'nb-worlds'

	def on_end(self, block: Element) -> None:
		groups = group_by_heading(block, 'h3', self.NAME)
		for child in list(block):
			block.remove(child)
		for index, group in enumerate(groups):
			color = WORLD_COLORS[index % len(WORLD_COLORS)]
			card = SubElement(block, 'div', {'class': f'nb-world-card nb-world-card--{color} nb-card-link'})
			stage = SubElement(card, 'div', {'class': 'nb-world-card__stage'})
			for child in group:
				if is_image_paragraph(child) and len(stage) == 0:
					child.set(UNWRAP, '1')
					stage.append(child)
				elif is_stashed(child) and len(stage) == 0:
					add_class(stage, 'nb-world-card__stage--spec')
					stage.append(child)
				else:
					card.append(child)

#============================================
class StatsBlock(LayoutBlock):
	"""
	/// stats: a list of `- **number** label` items shown as a numbers band.
	"""
	NAME = 'stats'
	CSS = 'nb-band'

	def on_end(self, block: Element) -> None:
		source = find_list(block, self.NAME, ('ul',))
		block.remove(source)
		block.set('role', 'list')
		# the optional argument names the band for screen readers
		label_text = 'The club in numbers'
		if self.argument:
			label_text = self.argument
		block.set('aria-label', label_text)
		for item in source:
			target = item_target(item)
			match = lead_bold(target, self.NAME, '`- **2001** Founded in late summer`')
			cell = SubElement(block, 'div', {'class': 'nb-band__item', 'role': 'listitem'})
			value = SubElement(cell, 'span', {'class': 'nb-band__value'})
			value.text = match.group(1)
			label = SubElement(cell, 'span', {'class': 'nb-band__label'})
			label.text = text_of(target)[match.end():]

#============================================
class SplitBlock(LayoutBlock):
	"""
	/// split: two columns side by side, separated by a `---` line.
	"""
	NAME = 'split'
	CSS = 'nb-split'

	def on_end(self, block: Element) -> None:
		if self.argument:
			add_class(block, f'nb-split--{self.argument}')
		children = list(block)
		if not any(child.tag == 'hr' for child in children):
			return
		for child in children:
			block.remove(child)
		column = SubElement(block, 'div')
		for child in children:
			if child.tag == 'hr':
				column = SubElement(block, 'div')
			else:
				column.append(child)

#============================================
class CalloutBlock(LayoutBlock):
	"""
	/// callout | Label: a boxed note with a label tab. Starting the body with Matchstick's
	picture makes it a note from Matchstick.
	"""
	NAME = 'callout'
	CSS = 'nb-callout'
	ARGUMENT = True

	def on_end(self, block: Element) -> None:
		children = list(block)
		for child in children:
			block.remove(child)
		label = Element('span', {'class': 'nb-callout__label'})
		label.text = self.argument
		body = block
		if children and is_image_paragraph(children[0]):
			# picture on the left, label and text together on the right
			add_class(block, 'nb-callout--matchstick')
			picture = children.pop(0)
			picture.set(UNWRAP, '1')
			block.append(picture)
			body = SubElement(block, 'div')
		body.append(label)
		for child in children:
			body.append(child)

#============================================
class ColumnsBlock(LayoutBlock):
	"""
	/// columns: each `## Heading` and what follows it becomes one column on wide screens.
	"""
	NAME = 'columns'
	CSS = 'nb-columns'

	def on_end(self, block: Element) -> None:
		groups = group_by_heading(block, 'h2', self.NAME)
		for child in list(block):
			block.remove(child)
		for group in groups:
			column = SubElement(block, 'div')
			for child in group:
				column.append(child)

#============================================
class SocialBlock(LayoutBlock):
	"""
	/// social: a paragraph of links shown as a row of small bricks.
	"""
	NAME = 'social'
	CSS = 'nb-social'

#============================================
class PartsBlock(LayoutBlock):
	"""
	/// parts: a numbered list of Matchstick's parts with color chips. Each item reads
	`1. **Horns** Two tall horns. _Medium Lavender `#AC78BA`_`; the hex codes in the
	trailing note color the chip.
	"""
	NAME = 'parts'
	CSS = 'nb-swatches nb-parts'

	def on_end(self, block: Element) -> None:
		source = find_list(block, self.NAME, ('ol',))
		block.remove(source)
		block.tag = 'ol'
		move_children(source, block)
		for item in block:
			target = item_target(item)
			text = text_of(target)
			colors = HEX_CODE.findall(text)
			note = TRAILING_NOTE.search(text)
			if not colors or note is None:
				raise BlockError("/// parts: end each item with the color in italics, as in "
					f"`_Red `#C91A09`_`; got '{text[:60]}'")
			chip = Element('span', {'class': 'nb-swatch__chip'})
			# two colors (white and black) draw an eye; one color fills the chip
			if len(colors) == 2:
				add_class(chip, 'nb-swatch__chip--eye')
			else:
				chip.set('style', f'--chip: {colors[0]}')
			chip.tail = text[:note.start()]
			target.text = ''
			target.insert(0, chip)
			swatch = SubElement(target, 'span', {'class': 'nb-swatch__hex'})
			swatch.text = note.group(1).replace('`', '')

#============================================
class WorldBlock(LayoutBlock):
	"""
	/// world: one filterable world section on the gallery page, titled by its `## Heading`.
	"""
	NAME = 'world'
	CSS = 'nb-world'

	def on_create(self, parent: Element) -> Element:
		element = SubElement(parent, 'section', {'class': self.CSS})
		return element

#============================================
class HeroBlock(LayoutBlock):
	"""
	/// hero | Eyebrow line (aside): the home page opener. Body: a `#` title (emphasis
	drops to the second line), a paragraph, button links, Matchstick's picture, a link under
	the picture, and an optional /// next-show ticket.
	"""
	NAME = 'hero'
	CSS = 'nb-hero'
	ARGUMENT = True

	def on_create(self, parent: Element) -> Element:
		element = SubElement(parent, 'section', {'class': self.CSS})
		return element

	def on_end(self, block: Element) -> None:
		children = list(block)
		for child in children:
			block.remove(child)
		inner = SubElement(block, 'div', {'class': 'md-grid nb-hero__inner'})
		copy = SubElement(inner, 'div', {'class': 'nb-hero__copy'})
		art = SubElement(inner, 'div', {'class': 'nb-hero__art'})
		SubElement(art, 'div', {'class': 'nb-hero__plate', 'aria-hidden': 'true'})
		extra = SubElement(block, 'div', {'class': 'md-grid'})
		# eyebrow: the argument, with a parenthetical aside in a lighter style
		eyebrow = SubElement(copy, 'p', {'class': 'nb-hero__eyebrow'})
		name, _, aside = self.argument.partition(' (')
		eyebrow.text = name + ' '
		if aside:
			was = SubElement(eyebrow, 'span', {'class': 'nb-hero__was'})
			was.text = aside.rstrip(')')
		for child in children:
			text = text_of(child)
			if child.tag == 'h1':
				add_class(child, 'nb-hero__title')
				copy.append(child)
			elif is_image_paragraph(child):
				child.set(UNWRAP, '1')
				art.append(child)
			elif is_stashed(child):
				extra.append(child)
			elif '.md-button' in text:
				add_class(child, 'nb-hero__actions')
				copy.append(child)
			elif len(art) > 1:
				# a link under the picture
				child.set(UNWRAP, '1')
				art.append(child)
			else:
				add_class(child, 'nb-hero__lede')
				copy.append(child)

#============================================
class TrainBlock(LayoutBlock):
	"""
	/// train: the home finale. Body: a `##` title, a button link, then a paragraph of
	pictures; each picture rides a flatcar and the last one is the engine.
	"""
	NAME = 'train'
	CSS = 'nb-layout'
	ARGUMENT = False

	def on_create(self, parent: Element) -> Element:
		element = SubElement(parent, 'section', {'class': self.CSS})
		return element

	def on_end(self, block: Element) -> None:
		children = list(block)
		for child in children:
			block.remove(child)
		head = SubElement(block, 'div', {'class': 'md-grid nb-layout__head'})
		track = SubElement(block, 'div', {'class': 'nb-layout__track', 'aria-hidden': 'true'})
		train = SubElement(track, 'div', {'class': 'nb-layout__train'})
		for child in children:
			if child.tag == 'h2':
				add_class(child, 'nb-layout__title')
				head.append(child)
			elif text_of(child).startswith('!['):
				child.set(UNWRAP, '1')
				train.append(child)
			else:
				child.set(UNWRAP, '1')
				head.append(child)

#============================================
class FinishTreeprocessor(markdown.treeprocessors.Treeprocessor):
	"""
	After inline Markdown: unwrap marked paragraphs, add section kickers, captioned
	figures, hero picture class, and train cars.
	"""

	def run(self, root: Element) -> None:
		for element in root.iter():
			element.attrib.pop('data-nb-closed', None)
		parents = {child: parent for parent in root.iter() for child in parent}
		for element in list(root.iter()):
			if element.get(UNWRAP):
				self.unwrap(element, parents)
		parents = {child: parent for parent in root.iter() for child in parent}
		for element in list(root.iter()):
			if element.tag in ('h2', 'h3') and element.get('data-kicker'):
				self.kicker(element, parents[element])
			elif element.tag == 'p' and self.is_captioned_image(element):
				self.figure(element)
			elif 'nb-hero__art' in element.get('class', ''):
				for image in element.iter('img'):
					add_class(image, 'nb-hero__matchstick')
				for link in element.iter('a'):
					add_class(link, 'nb-hero__meet')
			elif 'nb-layout__train' in element.get('class', ''):
				self.cars(element)
			elif element.tag == 'ol' and 'nb-steps' in element.get('class', ''):
				self.step_links(element)

	def step_links(self, steps: Element) -> None:
		# a link that ends a step is its call to action, shown on its own line
		for item in steps:
			target = item_target(item)
			if len(target) == 0:
				continue
			last = target[-1]
			ends_step = last.tail is None or not last.tail.strip()
			if last.tag == 'a' and ends_step:
				add_class(last, 'nb-step-link')

	def unwrap(self, paragraph: Element, parents: dict) -> None:
		# replace the paragraph by its children, keeping text order
		parent = parents[paragraph]
		index = list(parent).index(paragraph)
		parent.remove(paragraph)
		for offset, child in enumerate(list(paragraph)):
			parent.insert(index + offset, child)

	def kicker(self, heading: Element, parent: Element) -> None:
		# `## Title { data-kicker="Start here" }` gets a small label line above it
		label = Element('p', {'class': 'nb-section-kicker'})
		label.text = heading.attrib.pop('data-kicker')
		parent.insert(list(parent).index(heading), label)

	def is_captioned_image(self, paragraph: Element) -> bool:
		# `![alt](src "Caption")` alone in a paragraph
		children = list(paragraph)
		result = (len(children) == 1 and children[0].tag == 'img'
			and children[0].get('title') and not text_of(paragraph))
		return bool(result)

	def figure(self, paragraph: Element) -> None:
		image = paragraph[0]
		paragraph.tag = 'figure'
		paragraph.set('class', 'nb-figure')
		caption = SubElement(paragraph, 'figcaption')
		caption.text = image.attrib.pop('title')

	def cars(self, train: Element) -> None:
		images = [child for child in list(train) if child.tag == 'img']
		for child in list(train):
			train.remove(child)
		for index, image in enumerate(images):
			image.tail = None
			car = SubElement(train, 'span', {'class': 'nb-car'})
			if index == len(images) - 1:
				add_class(car, 'nb-car--engine')
			car.append(image)

#============================================
class NilbcBlocksExtension(pymdownx.blocks.BlocksExtension):
	"""
	Registers the layout blocks and the finishing tree pass.
	"""
	BLOCKS = (
		StepsBlock, CardsBlock, WorldsBlock, StatsBlock, SplitBlock,
		CalloutBlock, ColumnsBlock, SocialBlock, PartsBlock, WorldBlock, HeroBlock,
		TrainBlock,
	)

	def block_names(self) -> set:
		# data_blocks.py reads these to check block names on every page
		names = {block.NAME for block in self.BLOCKS}
		return names

	def extendMarkdownBlocks(self, md: markdown.Markdown, block_mgr: object) -> None:
		for block in self.BLOCKS:
			block_mgr.register(block, {})
		# after inline conversion (20) and attribute lists (8), before the table of contents
		md.treeprocessors.register(FinishTreeprocessor(md), 'nilbc_finish', 6)

#============================================
def on_config(config: object) -> object:
	"""
	MkDocs event: add the layout blocks to the Markdown extensions.
	"""
	config['markdown_extensions'].append(NilbcBlocksExtension())
	return config

#============================================
def on_page_markdown(markdown_text: str, page: object, config: object, files: object) -> str:
	"""
	MkDocs event: note which page is about to be converted, for error messages.
	"""
	CURRENT_PAGE['path'] = page.file.src_path
	return markdown_text
