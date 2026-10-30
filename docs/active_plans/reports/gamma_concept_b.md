# Gamma proposal B: Exposed connections

## Recommendation

Make gamma a website that visibly **comes apart into useful pieces and connects them again**.
The visitor reads an open construction diagram, not a miniature exhibition or a scrapbook.
An event is a date connected to a place and a practical action. Membership is an invitation
connected to requirements and a real email. A collection is many individual builds connected
by shows. The club's many interests share a structural system without looking identical.

Use an exposed joint as the recurring device: two rectangular surfaces separated by a narrow
open seam, with a short connector crossing it. Change what the seam does on each page. It can
separate dates from venues, collection labels from pictures, requirements from the email
checklist, or years from history. Geometry explains relationships instead of decorating cards.

This is a proposed direction, not a settled decision or an implemented result. Recommend it
if the team can change inner-page composition and add small semantic presentation hooks.
A CSS-only recoloring of the current gamma will not deliver this concept.

## Evidence and boundaries

Read the governing final creative brief in
[2026-10-30_132757-image-forward-d-revisions.md](../../../.hermes/plans/2026-10-30_132757-image-forward-d-revisions.md),
[DESIGN_BRIEF.md](../../DESIGN_BRIEF.md), and [ASSETS.md](../../ASSETS.md).
Inspected current gamma CSS, configuration, shared homepage, template, Shows, Join, and About.

Current [gamma.css](../../../design_d_revised/site_src/stylesheets/gamma.css) mainly rotates
cards, enlarges letters, adds colored borders, and changes photo frames. Inner-page banners
still use the shared heading-plus-art structure. This proposal replaces that presentation
logic rather than adding another layer of rotations.

Keep one shared Markdown/data tree, MkDocs Material, local images, current routes, and existing
photo viewer. The collection and timeline agents own content/data expansion; gamma consumes
their output. Do not hard-code photo counts, dates, club claims, or a second timeline.
No new photograph, font, service, framework, mascot adaptation, or private-source access is
necessary. Use date-verified recent club-show photographs for prominent documentary placements;
never treat the guitar filename or an upload directory as a capture date.

## The construction grammar

- Desktop pages have a narrow **index edge**, an open seam, and a wider **working surface**.
  Use approximately one quarter of the width for section labels and three quarters for facts
  or images. This is not a permanent dashboard sidebar: the edge changes with page content.
- Sections do not become identical bordered cards. A collection spreads across the surface;
  prose occupies a readable column; an event becomes a row; joining becomes an open spread.
  Large blank joints between sections expose the page background and make boundaries visible.
- Alternate which surface projects into the seam at major section transitions, without
  changing DOM order. Never overlap text, focus rings, or clickable regions. All type stays
  upright. Preserve body reading width rather than stretching paragraphs with the viewport.
- Use flat near-black structural lines and restrained azure connection marks. Warm light
  reading surfaces and one lavender or red interruption per major section reference the
  approved identity. These are proposed roles, not contrast-verified color pairs.
- The most unusual scale change is from a page-width assembly to a small precise information
  joint, not an enormous heading. Photographs remain rectangular, unmasked evidence.
- Matchstick occupies one intentional junction on Home and a larger identity study on his
  page. Remove the repeated surprise-peeking game from gamma. Do not disassemble the supplied
  mascot image or pretend a rendering is a physical club model photograph.
- No stud wallpaper, paper textures, fake screws, arbitrary skewing, pseudo-technical numbers,
  spinning pieces, or universal decorative frames. The empty seam must do real layout work.

## Home: one club, visible connections

The shared Markdown remains the source for the approved slogan, explanation, actions, five
interests, show data, photos, and history. Add semantic section wrappers where necessary;
do not extract copy into gamma's template or use visual CSS ordering to contradict reading order.
Coordinate any shared section movement with the alpha/beta implementers.

Opening composition:

1. Put the slogan and short club introduction on the left working surface. Immediately below
   them, put the existing Shows and Join links on the same straight baseline.
2. Put the real next-show block at the right edge, joined to that action line across an open
   gap. Keep its full date/status visible, including honest missing-hours or no-show text.
3. Begin the interest section directly below with five named rows. Each row has a label on
   the index edge, its existing short description, and a real photograph across the seam.
   Make the first two rows share the available horizontal span; the next three resolve into
   a different width rhythm. Keep labels and reading order explicit, not a visual treasure hunt.
4. Show all five named interests early, before historical statistics and long introductory
   steps. Keep the opening compact enough that a real recent club photo is present at common
   desktop sizes; do not turn the first viewport into a mascot or concept explanation.
5. Let the later small-scenes section temporarily erase the index edge: pictures span the
   whole surface, then the following text returns to the measured reading column. This
   temporary change in scale is the surprise, not a random collage.

Hover/focus on an interest link fills only its short connector and underlines the title. The
image does not move, expand, reveal essential text, or initiate a slideshow. Clicking navigates
to the existing collection route or anchor. On touch the connections are already visible.
The concept is legible in a static screenshot with images disabled.

## Collections: spread, then inspect

The collection overview is an index of five open shelves: names at the left, source-derived
counts if available, one approved preview, and a direct collection link. Not five theatrical
worlds that each need a separate design language.

For dense trains and other collections:

- Put the collection name and available show-anchor links above the grid. Use ordinary links
  that wrap; never a horizontally scrolling carousel required to reach an older show.
- Each show starts a full-width seam: show name/date on the index edge, its thumbnails on
  the surface. Preserve the renderer's chronological and within-show order. The seam bridges
  all rows in that group rather than outlining every photo.
- Use a regular compact grid with thumbnail subjects contained, not cropped by different
  decorative apertures. Allow more columns as width permits; retain two useful columns on
  ordinary phones and one when zoom or narrow width demands it. No masonry reordering.
- A tiny index tick at each image edge becomes a continuous high-contrast focus outline on
  keyboard focus. Caption and image form one intelligible target; credit access stays visible.
- Optionally offer a real "Larger thumbnails" toggle above long collections. It changes only
  grid density, not filtering, order, selection, URL, or content. Use a labeled button with
  `aria-pressed`; no preference persistence is necessary. Omit it if it delays core delivery.
- The existing modal is the inspection surface: full image, caption, credits, close, previous,
  and next. Its surrounding margin echoes the open seam. Do not implement another viewer,
  add mandatory swipe gestures, or distort modal image sizing to fit the metaphor.
- Native show-album expansion opens a shelf downward in normal flow. Its summary retains
  the show name, date, and count. Full photos load only when actually inspected; thumbnails
  stay lazy. Do not animate album height or fetch all large images on opening a shelf.

Distinction from beta: the collection's show grouping and relation to the index are its
composition, not an editorial heading above an otherwise unchanged photo wall. Density and
consistent photo geometry remain intentionally conventional.

## Shows: dates physically meet places

Replace floating tickets with a connected schedule. Each event is one semantic row: a large
but compact date block, an open vertical seam, then venue, address, hours, status, and existing
outbound actions. A short horizontal connector aligns the date to the venue's first baseline.
Separate events with generous whitespace rather than stacked boxes.

Keep dates visible while scanning venue names. Do not make users open an event to learn hours
or address. Unconfirmed dates and missing hours are text at the same hierarchy as confirmed
information, not tooltips. The next-show marker comes from existing data logic.

On a phone, date and venue share a top row; hours/address continue beneath the venue. At high
zoom everything stacks in reading order. With no upcoming events, keep the same empty seam
but state "No upcoming shows listed" and expose the existing Visiting and gallery routes.
No fake loading signal, animated departure board, or inferred live status.

## Join: an open conversation spread

Use a split **read / write** composition, not a staged application wizard.

The invitation and member activities form the upper reading surface. The existing requirements
callout forms a compact reference rail beside the existing contact checklist. Label both with
actual Markdown headings. The email link remains visible next to the checklist, not behind
completion of it. Render the checklist as a semantic list with generous line spacing, not
interactive checkboxes that imply submitting an application.

Separate "what to include" from "before you write" with a broad seam; connect them with one
small elbow line. This makes their relationship visible while leaving fees, age, transportation,
and meeting uncertainty explicit. Do not invent membership eligibility tests, response times,
forms, accounts, or locally saved personal information. Native FAQ disclosures stay native.
On phones the requirements precede the email checklist in DOM and visual order if a shared
content reorder is approved; otherwise keep the existing order and avoid CSS-only reordering.

## Timeline and remaining surfaces

- **About/timeline:** years occupy the index edge, milestone text extends into the working
  surface. A straight line has deliberate breaks between dated entries; do not imply the
  spacing measures elapsed years. Photographs attach only to supported milestones, not the
  nearest convenient year. Unknown dates stay unknown. New timeline output supplies all facts.
- **Visiting:** existing practical headings become successive open cross-sections. Put each
  question on the edge and its answer beside it; arrival, viewing, and access information stay
  exposed. This is a readable briefing, not a route to unlock or a map of an invented venue.
- **Standards:** a specification spread, with section labels in the edge and tables/code in
  the surface. Preserve units, anchors, table headers, and readable horizontal overflow where
  unavoidable. Only draw diagrams for already sourced dimensions; decoration never resembles
  an unverified engineering specification.
- **Matchstick:** one intact approved image beside visible descriptive labels connected to
  its margin, not arbitrary hotspots over the character. On narrow screens labels become a
  normal list. Preserve the supplied colors and recognizable construction; mark render provenance.
- **Credits:** a plain ledger with source groups on the edge and complete attribution on the
  surface. Keep links selectable and visible. Do not compress credits into hover interactions.
- **Show logbook:** date-first ledger sharing the Shows row structure, with archive links
  instead of future-event emphasis. Never make historical entries appear upcoming.

## Navigation and small states

Keep Material's actual navigation, search, color toggle, skip link, and mobile drawer. Restyle
the desktop header as a narrow fastening strip: plain labeled destinations with one short
projecting tab for the current destination. `aria-current`, text, and shape identify it, not
color alone. The inner-page section index uses existing anchors, not a parallel custom router.

Search opens the familiar Material surface. Align its results to the same label/content seam;
retain excerpts, keyboard selection, loading feedback, clear control, and actual empty message.
An empty result offers a clear query-edit path and normal navigation. Do not inject arbitrary
"try this" queries or replace search logic. A 404 says the page was not found, with Home,
Shows, and Creations links; its broken connector is decorative, not the only error signal.

The footer closes the working surface with an exposed final seam and a compact set of real
onward links, credits, and existing legal text. It is not a second giant hero or a new set of
club claims. Ordinary page navigation remains instant, with no transition overlay or scroll
capture. Hover and focus use the same connector-fill response; pressed controls can change
border weight without translating their targets. No information appears only on hover.

## Phone, motion, and dark mode

On narrow screens, turn the side index into a short heading strip above each surface. Keep
one visible joint between heading and content; do not merely remove the desktop design until
it resembles alpha. No horizontal page panning, draggable canvas, sideways text, or fixed
bottom action bar. Ensure sticky chrome cannot cover anchors or focused controls.

Use no automatic motion. Optional connector-color transitions are brief and cosmetic; under
reduced motion all state changes are immediate. Expanded content, chosen density, focus, and
active page remain equally recognizable. Dark mode swaps surface/ink roles while keeping seam
widths, image appearance, and contrast; do not invert photography or make all surfaces black.

## Practical implementation scope

1. Replace gamma's final stylesheet instead of appending another override pile. Explicitly
   neutralize inherited scrapbook/photo-frame treatment where gamma requires plain evidence.
2. Add a gamma identity flag in configuration and a small body/page-kind presentation hook in
   the shared template. Gate structural template differences to gamma; keep alpha/beta output
   unchanged. Reuse Material's blocks and behavior rather than copying whole upstream templates.
3. Add only the semantic wrappers needed around shared Markdown sections and existing renderer
   groups. Use page-kind/section classes, not brittle `nth-child` rules tied to current copy.
   Keep content edits shared and agreed with the homepage, collection, and timeline owners.
4. Implement the common seam/index system, then Home, Shows, Join, collections, and history.
   Finish Visiting, Standards, Matchstick, Credits, search, footer, and error states before
   calling it whole-site. The optional density button is the only proposed new JavaScript.
5. Reuse the existing photo dialog and native disclosures. No new dependency or asset pipeline.

Core effort is a gamma stylesheet replacement, small configuration/template hooks, and limited
renderer semantics. It is not a rebuild of navigation or data. The largest integration risk is
shared Markdown section ordering; settle that with the other implementers before styling.
The largest design risk is turning the seam motif into decoration while leaving every page a
stack of cards. Reject that outcome in review.

## Acceptance and handoff

Implementation should prove, rather than assume:

- Home, Shows, Join, and a dense collection have visibly different information compositions,
  yet share one recognizably coherent structural language without relying on motion or photos.
- A visitor can reach show details, requirements/email, and a train image using keyboard alone;
  dialog closing restores focus; search and mobile navigation retain their existing behaviors.
- All theme groups, retained photos, source facts, and chronological timeline entries survive.
  Public copy remains editable in shared Markdown/data; no duplicate facts enter templates.
- Narrow phone, desktop, wide-screen, dark, reduced-motion, enlarged-text, and images-blocked
  reviews show no obscured facts, lost focus, unreadable seams, or horizontal page overflow.
- Strict build, project-subpath links, and existing tests pass after implementation. Capture
  Home, Shows, Visiting, Join, Standards, About, a collection, search-empty, and mobile states.
  Use a fresh network context for lazy-loading checks, not the eager screenshot-decode journey.

This proposal makes no runtime or verification claim. Per the delegated scope, only this report
is written; the integrating agent records any selected direction and changelog entry later.
