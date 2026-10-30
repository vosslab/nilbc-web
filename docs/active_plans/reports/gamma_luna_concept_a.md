# Gamma concept A — The Club, in Motion

## Concept

Make NILBC feel like a **live, hand-built club workshop**, not a miniature theme park or a static catalog. Visitors move through a series of work surfaces: a long train-layout bench, a show-night control board, a shared parts/build table, and a wall of dated club snapshots. This is a visual and navigational grammar, not a fictional claim that the site depicts the club's literal current room. Real club photographs are windows onto completed work; crisp schematic marks, registration lines, punched labels, and oversized sectional numerals are the invented layer.

The experience has a deliberate rhythm: **look at what members made → find where/when to see it → understand how to take part**. The page itself feels actively assembled: content bands align and break across the viewport like plans spread over a workbench; hard changes in scale and color establish distinct stations. Avoid the default stack of same-shaped cards. Avoid scrapbook handwriting, photo collages as the whole idea, fabricated dates/builders, and decoration that obscures information.

This differs from beta's photo essay: gamma is spatial and procedural, with strong bands, long rules, and variable-width work surfaces. It differs from the plan's exhibition-world candidate by centering people making and sharing things, rather than themed districts. The site's metaphor never gates access: ordinary named links, dates, requirements, and email remain visible HTML.

## Three wireframes

### Home — open bench / current work

**Desktop, top to bottom:**

1. A dark, compact global fascia: NILBC identity at left; named destinations arranged as short labeled stations; search/theme controls stay native. A bright, high-contrast location tab marks Home. A thin rule continues under the fascia into the content as the bench's datum line.
2. A wide opening work surface, not a centered poster: left side holds the approved slogan, one-sentence welcome, and two unmistakable actions (“See the trains” and “Find a show”); right side holds one large, genuine recent-show photograph with a small date/context label only when supported. A small Matchstick identity detail can sit at the edge, never as the main event.
3. “On the workbench” uses the curated recent photographs in a deliberately asymmetric strip: one broad lead image, two smaller observations, captions and show links. This reads as evidence, not a scrapbook; no decorative frames around every photo.
4. Five interest routes appear as a continuous ruled index with distinct typographic widths and simple schematic accents, not five cards. Trains is prominent but city, castles, screen/story, and creatures remain equal discoverable links. Each has a text description and existing count where available.
5. A practical next-show/date band and a clear join invitation close the first journey. Longer club explanation follows below.

**Phone:** fascia collapses to the existing Material menu; the opening copy/actions come first, then the lead photo at full width, a horizontally scrollable only-if-labeled thumbnail strip with native links (prefer a normal stacked layout if scroll affordance is unclear), and a two-column interest index. No sideways page overflow, hidden labels, or content reordered away from keyboard order.

### Trains — the long layout plan

A dense, fast-scanning contact sheet: title and honest image count at top; a narrow left-side (desktop) show index provides real show names/dates as anchors, while the main area is a compact regular thumbnail grid. Each show transition is a full-width, high-contrast **layout-break marker**—show label and verified date/context, then the next continuous run of photos. The marker evokes a seam in a long train layout, but photos keep consistent low-chrome treatment; no repeated heavy frames or bespoke fake train metadata. Existing source order, captions, viewer dialog, and collection-wide keyboard navigation remain intact. On phones, show anchors become a simple horizontal text index or native disclosure, followed by the same dense grid and full-width dividers. Full images load only through existing viewer activation; thumbnails remain lazy.

### Joining — the shared build table

A broad numbered sequence reads left-to-right on desktop and top-to-bottom on mobile: **01 Bring an interest → 02 Check the real requirements → 03 Contact the club**. Each stage is a clean open band joined by a continuous fine rule and a large section number, not a set of cards. Put the existing six requirements together in a plainly labeled checklist under step 02; none is hidden behind interaction. Step 03 ends in the actual email action with the supplied address. A short welcome explicitly includes builders beyond trains. No invented fee, application, attendance promise, or eligibility rule.

## One playful interaction: the alignment jig

On the Home interest index, a visitor can select a labeled interest (click, keyboard, or touch). A small **alignment cursor** shifts along the shared bench rule to that item's index and the corresponding link gains a clear selected outline; no page scroll hijack, no hidden content, no drag gesture, and no dependence on hover. It is progressive enhancement only: all five links and descriptions exist and work without JavaScript. Respect reduced motion by switching the cursor instantly; under normal motion use a brief restrained translation. The interaction is useful orientation, not a game.

## Whole-site language

- **Navigation/search/footer/404:** treat the header as the workbench's labeled control rail, with explicit current-route indicator. Keep Material's search, drawer, theme switch, skip link, and all native behaviors. Search results/no-results use the same ruled index; 404 states “Page not found” plainly and offers Home, Shows, and Join as onward links. Footer is a quiet end-of-bench directory.
- **Shows index:** event dates become the strongest anchors in a high-contrast schedule strip; venue, address, status, and map links remain readable and literal. Past/upcoming status is factual, not simulated live telemetry.
- **Show albums:** each album opens under a named show/date work label, then a dense image contact sheet. Use native existing expansion and viewer; avoid animated curtain gimmicks.
- **Visiting:** practical arrival sequence—before you go, find the venue, what to expect—with directions/map and show details in ordinary text. No scavenger hunt.
- **Timeline/history:** a long horizontal datum becomes a vertical timeline on phones. Only supported milestones and dates appear; archive photographs are labeled with honest archive context when capture date is unknown.
- **Standards:** blueprint-like dimension leaders around the actual supplied diagrams/specifications, while explanatory text and anchors stay conventional. Never infer dimensions from the art.
- **Matchstick:** an inspection sheet with labels for the approved brick-built features, retaining supplied recognizable art and distinguishing rendering from physical-photo provenance.
- **Credits:** a compact, searchable-feeling but static ledger grouped by asset/source, with real attribution and provenance links; no attribution hidden on hover.
- **Five interest collections:** collection headers/dividers can vary subtly by subject, but all retain the same dense, efficient image rhythm and one viewer. No invented taxonomy.

## Color, type, motion, and accessibility

Use a dark ink/navy structural field, warm light work surfaces, and a very limited bright signal color drawn from the approved identity palette; the mascot's provisional colors do not dictate all UI colors. Build contrast from semantic tokens and check actual combinations in both Material light/dark schemes. Large condensed display numerals may give scale; body/captions remain a highly readable sans serif. Avoid all-caps paragraph copy and tiny technical labels.

At narrow widths, convert wide benches to stacked readable sequences, preserve visible section joins, and keep full subject crops (use `object-fit: contain` where cropping would cut a build). Native source order equals visual/focus order. Visible focus, skip link, descriptive image alt/captions, touch-sized controls, and 200% zoom are non-negotiable. Reduced-motion mode removes cursor travel and all nonessential transitions without removing the alignment state or any information. Dark mode changes surfaces and rules coherently, not merely inverts text.

## Minimum implementation surface (gamma only)

Keep `design_d_revised/` as the shared source and preserve accurate Markdown/photo data, identifiers, original A–D, Material, static GitHub Pages output, current gallery renderer/viewer, and existing assets. Add no copied content tree or external service.

- `mkdocs_d_gamma.yml`: explicit gamma revision flag and gamma-only stylesheet registration, inheriting shared content as now.
- `design_d_revised/theme/main.html`: only if required, a gamma-conditional wrapper around Material's content block for route-scoped styling; leave alpha/beta template output unchanged. Preserve native search/drawer/theme controls.
- `design_d_revised/site_src/stylesheets/gamma-layout.css`: global fascia, work-surface grid/rules, responsive/dark/reduced-motion states, plus route-specific visual grammar.
- `design_d_revised/site_hooks/data_blocks.py`: avoid changes if existing emitted classes suffice. Add only semantic show-divider/section wrappers if the current renderer lacks hooks; do not hard-code facts or duplicate Markdown content.
- Existing content surfaces to style, not duplicate: `site_src/index.md`, `site_src/creations/trains.md` (or current generated train collection route), `site_src/shows/index.md`, `shows/gallery.md`, `shows/visiting.md`, `shows/logbook.md`, `join/index.md`, `join/standards.md`, `about/index.md`, `about/matchstick.md`, `about/credits.md`.
- `site_src/javascripts/worlds.js`: do not replace viewer. A tiny separate gamma enhancement script is justified only for the optional alignment cursor, and must leave links functional without JS.

Before implementation, inspect actual rendered classes/routes; the names above follow the plan's existing architecture and should be checked against source. Do not create a new information architecture if existing routes already serve these tasks.

## Verification receipts expected from implementation

Build only gamma with the documented strict MkDocs command, then exercise Home → Trains → viewer → show album → Visiting → Shows → Join → Standards → About → Matchstick → Credits. Capture Home, dense Trains, Shows, Visiting, Join, Standards, History, and a collection at desktop and phone widths. Test light/dark, reduced motion, keyboard-only, 200% zoom, no-JS photo links, image-load failure, native menu/search, and that exact email/map/date/photo targets still work. Verify no train totals or recent-photo dates are invented. No build, runtime change, or commit is part of this concept proposal.

## Assumptions to challenge

- “Recent” should mean explicitly associated with a recent completed show when that context is verified—not infer capture date from upload folders or missing EXIF. Keep dates and archive labels factual.
- A shared visual idiom should not turn every page into identical ruled panels; the principle is making-in-public, while each task gets its own useful composition.
- More visual energy is not more motion. The concept should still be unmistakably gamma in a static screenshot.
