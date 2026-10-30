# Gamma concept B: Field notes from a living archive

## Recommendation

Make gamma feel like a **field notebook used by a curious visitor**: each page is an
observation made while moving through the club's real exhibits. The visitor is not
inside a miniature world and not looking at a poster. They are following an editorial
trail of sightings, routes, dates, and practical notes. The visual grammar borrows from
naturalist notebooks and expedition logs, but documents brick-built work rather than
pretending the site is an actual field survey.

The central device is a continuous, thin **survey line**: a drawn route that links
navigation, section markers, photo sequences, event dates, and the footer. It branches
and changes scale at useful decision points, not around every card. Paired with a
high-contrast ink palette, giant numbered field marks, one restrained display face,
and uncluttered photographic plates, it creates a whole-site composition without
requiring new art or unsupported stories. Recent documented show work leads; older
archive material is labeled as archive material. Do not attach capture dates unless
verified by the existing evidence process.

This is deliberately neither alpha's quiet catalog nor beta's magazine essay. Alpha
uses faint studs and regular tiles; beta uses solid surfaces and an editorial image
lead. Gamma instead makes **wayfinding and sequence** the identity: a route through
connected observations, with real facts treated as evidence and user actions treated
as destinations. It remains visually distinctive with all motion off.

## Visual and content system

- Use a dark-ink base, warm paper surface, and one saturated route color sampled from
'the approved identity palette, with a second accent reserved for active locations.
  Keep text/surface contrast measurable; mascot colors are not a mandate for site-wide
  backgrounds.
- Use a locally available, readable sans for body and navigation; use the existing
  display face only for short route labels and large section numerals. Body copy,
  captions, and data remain conventional and calm.
- Construct a small SVG/CSS route mark: a line, junction, location dot, and numbered
  plate. Use it consistently, not as bespoke scenery on every section. Treat it as
  decorative (`aria-hidden`) when the adjacent heading names the destination.
- Give photo plates a crisp edge and clear caption; do not add a different frame to
  every thumbnail. Photo details stay honest and sourced from the shared manifest.
  Where show/date metadata is unavailable, say archive or date not established, not a
  guessed year or member attribution.
- Keep text in Markdown and facts in the existing shared data. Theme-specific styling
  consumes current classes and page metadata; no copied page trees or duplicated photo
  facts.

## How the site behaves

### Header and navigation

Keep Material's top bar, search, theme switch, mobile drawer, and skip link. Recast the
header as a compact route register: a small line connects five explicit text destinations
(Home, Worlds, Shows, Join, About), while a filled marker and `aria-current="page"`
identify the current route. Material's generated navigation remains the semantic source;
CSS can add the connecting line and active marker. Do not replace the drawer with a
custom map or make the line itself the only cue. At mobile widths, collapse to the
existing Material menu and retain persistent visible route labels once opened.

### Homepage

Open on a **field index**, not a full-bleed hero: the slogan and two plain actions (shows,
join) sit in a compact top band; below, three verified recent-show photos become large
numbered observations with visible captions and a direct "Browse the show photographs"
link. Then present all five building interests as a single connected index with clear
text labels and their actual club-work thumbnails. Use scale contrast—one wide lead
observation, two smaller plates—without hiding or overlapping subjects. Put the practical
"visit / explore / bring your builds" steps after this image-led evidence, and historical
statistics later. Matchstick can appear as a small margin annotation on desktop, but the
header logo/identity remains sufficient at phone widths.

### Fast train-photo browser

The train route is a contact index, not a scenic scroll experience. At top: concise
"Trains" heading, actual manifest-derived count, links to all worlds and show albums, and
an optional native `details` panel for the short orientation sentence. The grid uses
responsive 4:3 thumbnail plates, compact captions, stable reserved dimensions, and
`loading="lazy"`; a single thin route spine and small section labels mark transitions
between verified shows. Keep each transition heading outside the image grid's repetitive
caption rhythm; do not use fake subcategories or repeat heavy borders around roughly 100
photos. The show sequence/order comes from shared `photo_shows.yml`; undated records
follow dated show sequences as specified by the plan. The existing `.nb-gallery` and
`.nb-photo__link` preserve one collection-wide viewer, direct optimized-image links,
keyboard operation, focus restoration, and no-JavaScript access. Captions/credits remain
available through the visible link and credit page, not hidden in hover.

### Shows and visiting

On Shows, turn the existing upcoming-show renderer into a **route schedule**: each event
is a numbered stop with its actual venue, date span, available hours, address, map/action
link, and clear "next" marker based on the existing renderer. Keep event copy editable in
front matter and use the existing date logic; do not copy dates into a template. Visiting
becomes a short arrival guide with three practical stations—before leaving, at the venue,
and while viewing—built only from existing approved text. Show albums are observation
sets: native expandable album controls, a cover and its actual images, concise show label,
and the current keyboard viewer. The affordance should read as an ordinary expandable
album even if the visual treatment resembles a notebook tab.

### Joining and standards

Join becomes a **three-step handoff**: bring an interest, check the actual requirements,
write to the existing membership email. Each step gets a numbered margin mark, but all
six existing requested email details, age/transport/cost/dues/meeting information, and
actual email action remain visible in ordinary text; no gated reveal or application form.
A small assembly-sequence rule can connect the steps, but not turn them into a game.
Standards is a technical field sheet: retain existing dimension language, SVG diagram,
stable anchors, and readable tables. Use measured dimension callouts as annotations
around—not instead of—the standard content.

### Worlds, about, credits, footer

The Worlds overview is a labeled index of five actual collections with the established
anchors and counts if the renderer can derive them safely. Each dedicated collection
route shares the same efficient grid and viewer, with the survey-line treatment changing
only at show dividers (a stop marker, street junction, gate, mission waypoint, or habitat
label may distinguish its heading). These are labels, not claims about undocumented
photographic dates or builders.

About/history should read as a dated route only where the source has dates; do not fill
gaps with invented milestones. Matchstick gets a concise identity page with labeled
features grounded in approved asset documentation, not imagined backstory. Credits are a
plain, scannable ledger grouped by actual image/source categories; attribution and
provenance never depend on decorative styling. End each page at a shared **return point**:
three practical links (browse work, see shows, join) plus the next route destinations.
The 404 page says the page was not found and offers those same useful routes.

## Small interactions

- Hover, focus, and current-route states move the location dot and strengthen the route
  line; keyboard focus gets an equally clear outline and no motion-dependent meaning.
- A collection show marker can highlight its corresponding section heading when focused
  or activated, while normal anchor navigation remains available. Avoid scroll hijack.
- Native `details` provides optional extra context on collections and albums. It is never
  required to find photos, event facts, membership requirements, or credits.
- The existing photo dialog remains the only modal. Preserve Escape/close, previous/next,
  focus confinement/return, and direct image fallback; do not add a parallel lightbox.
- Material search and no-results UI remain intact; style result emphasis as a route
  destination and provide a clear empty-state link back to the route index.

## Implementation in this repository

1. Keep one shared `design_d_revised/site_src/` and data source for alpha, beta, gamma;
   leave original A/B/C/D trees/configs untouched. Use `mkdocs_d_gamma.yml`'s final
   gamma stylesheet slot for the variant treatment. If a semantic current-route marker
   is absent from Material output, add it in the existing `design_d_revised/theme/main.html`
   through a narrowly scoped gamma-only wrapper/attribute; do not fork page content.
2. Reuse `site_hooks/data_blocks.py` output: current `.nb-gallery`, `.nb-photo`, show
   gallery, show ticket, and world classes already carry the needed targets. For a
   dense collection, extend the existing renderer only to emit a semantic heading when
   the show changes, keeping all figures under one viewer-compatible `.nb-gallery`.
   Keep route labels and public copy in Markdown; do not hard-code captions, dates, or
   totals in Jinja/CSS.
3. Use `theme/main.html` only for global presentation hooks (header/current route and
   footer route register) and preserve `super()` for Material behavior. Inspect the
   installed Material template blocks before overriding header/footer/search. Prefer
   Material's existing nav, search, color toggle, and mobile drawer over custom controls.
4. Scope CSS beneath a gamma wrapper/data attribute. Existing tokens, `base.css`,
   `components.css`, `gallery.css`, `home.css`, and `pages.css` define shared behavior;
   use a final `gamma.css` layer for route line, plate, schedule, and page-specific
   composition. Avoid global selector overrides and `!important`.
5. Create the route spine using pseudo-elements or a small inline decorative SVG with
   `pointer-events:none`; reserve its space in layout. Any inline SVG must be marked
   decorative when adjacent text provides its meaning. Do not encode labels in generated
   pseudo-element content.
6. Responsive behavior: at desktop, route-register header and asymmetrical home index;
   around tablet, reduce overlap and let the spine terminate at section boundaries; on
   phones, source-order becomes one readable column, use compact numbered markers and
   two-column photo tiles where image subjects remain clear. Never CSS-reorder focusable
   content. At 200% zoom, allow the route register to wrap/collapse with Material and
   keep all links reachable.
7. Dark mode uses the same route geometry with theme variables for ink/paper/lines and
   tested contrast; do not invert photographic imagery. Under `prefers-reduced-motion`,
   remove dot travel, transition, and reveal effects while leaving location markers,
   route lines, and composition present. With JavaScript disabled, links, native details,
   full-image anchors, and Material fallback navigation still work.

## Useful, surprising, conventional

- **Useful:** a single route grammar explains where you are, what comes next, and how a
  show/collection relates to the rest of the site. Dense photos remain one-scan content.
- **Surprising:** the survey line crosses page types—joining steps, event stops, photo
  sequence dividers, and the footer—so inner pages are not just gamma-colored Material
  docs. The route is editorial scaffolding, not a literal claim that every club activity
  happened in a geographic sequence.
- **Conventional by design:** real text links, familiar search, menu, theme toggle,
  headings, event details, gallery controls, and membership requirements remain ordinary
  and operable. The visual experiment is in their relationship and composition, not in
  making visitors learn novel controls.

## Pitfalls and safeguards

- **Risk: line becomes decoration with no information.** Only use it to connect labeled
  sections/current destination; test that removing motion does not erase its meaning.
- **Risk: notebook styling becomes faux-history.** No invented dates, handwritten
  personal notes, member names, or provenance; use generic field labels and source-backed
  facts only.
- **Risk: dense rail overlays the photos.** Keep it in a reserved gutter and away from
  captions, targets, and focus outlines; check narrow screens and 200% zoom.
- **Risk: the result slides back toward a poster or miniature-world theme park.** Keep
  the route system restrained and relational; do not add portals, fake terrain, random
  rotations, or a frame around every image.
- **Risk: the 100-photo collection is slow or unwieldy.** Begin with the plan's static
  lazy grid and thumbnail dimensions; measure requests/DOM before considering pagination.
  Load optimized large views only on viewer activation, and verify with a fresh browser
  context rather than a test that eagerly decodes every image.
- **Risk: accessibility becomes secondary to the visual metaphor.** Keep semantic
  navigation, heading order, persistent focus, actual alt text, visible counts, contrast,
  touch-size links, no hover-only data, and a no-JavaScript direct image path.
- **Risk: overclaiming rights or chronology.** Reuse only admitted local derivatives and
  documented sources; do not infer capture dates from upload folders, filenames, or IDs.

## Recommendation to the selecting manager

Advance this concept if the manager wants gamma's distinction to come from **a connected
wayfinding experience across every route**, rather than a more decorated homepage. It is
implementable with the existing Material navigation/template inheritance, Markdown source,
photo hooks, CSS, and native browser controls. Keep the survey line as the single visual
idea; let photographs, accurate event/member information, and useful actions remain the
substance.
