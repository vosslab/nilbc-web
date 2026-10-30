# Image-forward D revisions

Status: proposed implementation plan, 2026-10-30. No website changes in this planning pass.

## Outcome and evidence

Make the three MkDocs revisions unmistakably different in composition, not merely frame
styles, while sharing accurate club content and a substantially richer photographic collection.
Visitors should reach a dense train-photo collection directly from the homepage, or browse
completed club exhibits by show. Recent, date-supported work leads; historical favorites remain.

The original direction in [HUMAN_GUIDANCE.md](../HUMAN_GUIDANCE.md) was conservative alpha,
middle-road beta, and kitchen-sink creative gamma. Subsequent work narrowed gamma to selective
frames and offsets, while preserving the common homepage composition. The later
[EDITORIAL_GALLERY.md](EDITORIAL_GALLERY.md) explicitly excluded other pages and new imagery.
The [D_REVISIONS_COMPLETION.md](reports/D_REVISIONS_COMPLETION.md) records successful technical
checks, not evidence that the three concepts remained sufficiently different.

Current source inspection establishes:

- Beta and gamma inherit alpha and change stylesheets, including shared photo-frame styling.
  Their homepage still follows the same long section sequence.
- The shared manifest has 66 photographs, including only 10 tagged trains. The 45 curated
  archive selections span seven shows; five of those archive selections are railway views.
- The guitar caption says "a recent show" without a verified capture date. Its source URL
  has a 2026 upload directory; the frog's has a 2017 directory. Neither establishes capture date.
  Both deployed WebP files have empty EXIF. The owner's early-2010s guitar estimate is a lead,
  not a confirmed date. Do not infer dates from IDs such as `club_group_2026` either.
- Prior work reviewed all 72 contact sheets, but individually inspected only a subset of the
  1,336 preserved attachments. Existing review exclusions must inform, not replace, new curation.
- Gallery figures already use thumbnails and an on-demand viewer. The missing pieces are
  collection depth, visual density, dating, and homepage priority, not a new gallery framework.

## 1. Establish dates and expand curation

Work from the preserved archive at `/home/vosslab/nsh/niltc_archive_shows/`, its catalogs,
and the existing review/provenance records. Do not redownload or expose private discussions.

- Extract available capture-date EXIF from preserved sources, including DateTimeOriginal and
  timezone where present. Keep capture date, upload date, and event date separate. Filesystem
  timestamps and upload-folder names are not capture evidence; camera clocks can also be wrong.
- Corroborate dates with the existing show-context records. Record date value, precision, basis,
  and any conflict in the curation ledger. Use the verified show date when appropriate; preserve
  unknowns rather than inventing exact dates. Review conflicts before recent-first selection.
- Audit every existing public photo's age claims. Remove unsupported "recent" wording; move
  the guitar group and frog out of leading placements. Retain them as archive/history material.
  Keep existing identifiers stable where possible rather than renaming files to assert new dates.
- Review show batches newest first, sorting usable work by trains, cities, castles, screen/story,
  and creatures. For trains, distinguish locomotives, rolling stock, layouts, and railway details
  in the working ledger; add public subfilters only if collection size makes them useful.
- Aim for roughly 100 distinct worthwhile train thumbnails. This is a curation target, not a
  permission to duplicate frames, include ambiguous exhibits, or manufacture a count. Inspect
  full frames for admission, deduplicate, and retain source/show/uploader evidence. Report the
  actual eligible count and shortfall if the archive cannot support the target.
- Continue the completed-club-work-at-shows rule: exclude WIP, setup, home/workbench photos,
  other clubs, and unclear ownership. Do not let a numerical target weaken this boundary.
- Publish a compact contact-sheet review report with accepted counts by theme/show, date
  coverage, exclusions, and strongest recent candidates. Keep originals and private catalogs
  outside deployment. Preserve current selections unless a provenance problem is discovered.

Dependency: complete the date/eligibility inventory before choosing homepage lead images or
promising collection counts. If additional sources are needed, identify that gap explicitly;
new private-source access is not assumed by this plan.

## 2. Make browsing thumbnail-first

- Give each theme a dedicated static collection page. The homepage's Trains link opens the
  train collection, not an anchor halfway down a mixed-category page. Preserve old category
  anchors with onward links. Keep show albums as a second view of the same photo records.
- Show the real photo count, compact show/year captions, and newest verified shows first;
  put undated/archive material after dated work. Shared photos keep consistent metadata.
- Render a dense responsive grid with lazy local thumbnails and reserved image dimensions.
  Use explicit source sizes appropriate to phone and desktop tiles; do not download original
  camera files. Preserve legible subjects through crop review or full-frame containment.
- Start with one static lazy grid per theme, including around 100 entries if supported. Avoid
  pagination APIs, virtual scrolling, and infinite-scroll dependencies. Reconsider static page
  splits only if measured loading/DOM costs justify them.
- Keep larger optimized views optional, loaded only on activation. Preserve direct links,
  keyboard navigation, focus return, visible credits, and no-JavaScript access. Raw originals
  remain preservation assets, not a requirement for browsing or deployment.

## 3. Give each version a different composition

Share photo facts, Markdown copy, routes, and gallery behavior. Allow presentation-specific
markup/layout hooks where necessary: sharing content must not force identical page geometry.
Keep Material navigation, search, accessibility, approved identity, and static Pages output.

### Dalpha: orderly photo catalog

A restrained club site with a compact identity/header, a clear upcoming-show action, and recent
show photography immediately visible. Use aligned rectangular thumbnails, quiet typography,
generous but economical spacing, and consistent rows. Theme navigation is explicit and plain.
Matchstick is a small identity accent. No tilted photographs, decorative animation, paper notes,
or layered collage. Conservative means clear and photo-rich, not text-heavy.

### Dbeta: contemporary club magazine

A recent-show photographic lead paired with concise club text and useful actions, followed by
an asymmetric but orderly grid: a larger feature beside smaller details. Use editorial typography,
selective color, compact theme preview strips, and a curated latest-shows section. Give Matchstick
a supporting role. Avoid borrowing gamma's scrapbook treatment; distinguish beta through scale,
whitespace, and sequencing, not extra ornaments. Collection pages remain efficient to scan.

### Dgamma: exhibition workbench and loud club poster

Replace the shared stacked-card composition with an intentional CSS-built exhibition scene:
large poster type, layered recent-photo contact sheets, oversized theme labels, brick-like tabs,
and a railway path connecting content zones. Combine a miniature display world with a workbench
collage rather than applying small rotations to otherwise identical cards.

Use CSS Grid spans, controlled overlaps, masking, cut-paper edges, bold color fields, and selected
model cutouts only where they preserve the real build. Matchstick can bridge a section boundary;
important text and controls cannot be obscured. The first viewport must read as a different
composition from alpha and beta even with the same photo subjects and no animation.

The homepage may be exuberant; a 100-photo train collection must still be usable. Give collection
headings and show dividers the poster/workbench treatment while keeping thumbnail order and
keyboard navigation predictable. Phones retain bold type, color, layers, and deliberate rhythm
without relying on tiny photos or wide overlaps. Reduced motion removes motion, not the identity.
No scroll hijacking, autoplay, mandatory animation, or inaccessible drag-only browsing.

Across all three: move recent photography ahead of explanatory steps and historical statistics.
Retain the slogan, recognizable Matchstick, visible show/join actions, and all building interests.
The old requirement to preserve the guitar-led homepage composition is superseded here.

## 4. Implement and verify

Implement the shared collection/date work first, then the three compositions. Before polishing,
capture comparable homepage and train-page screenshots at phone and desktop widths. If the
variants still read as one layout with different decoration, revise composition rather than
adding more borders. This is an implementation checkpoint, not a required human approval wait.

Expected file scope:

- `design_d_revised/data/photos.yml`, `data/photo_shows.yml`: shared metadata and selections.
- `design_d_revised/site_hooks/data_blocks.py` and existing Markdown hooks: collection output
  and minimal variant hooks, after tracing their current interfaces.
- `design_d_revised/site_src/index.md`, `creations/`, `shows/`, `about/credits.md`: image-first
  hierarchy, collection routes, factual captions, and credits.
- Shared/variant stylesheets, existing gallery JavaScript only where behavior needs change,
  and `mkdocs_d_alpha.yml`, `mkdocs_d_beta.yml`, `mkdocs_d_gamma.yml` for navigation/layout wiring.
- Optimized photo derivatives and `ARTIFACTS/discord_archive_shows/` selected provenance/review
  records; do not commit the full archive or private catalogs.
- Existing Playwright journey, source/asset documentation, changelog, and settled decisions.

Completion evidence:

- Calculate unique photo counts from the manifest; verify all referenced derivatives and source
  provenance. State actual train coverage, missing dates, and withheld candidates honestly.
- Prove homepage-to-Trains opens the dedicated collection and exposes its advertised count;
  exercise thumbnail opening, next/previous, close, focus return, show links, and fallback access.
- Inspect request logs: collection browsing loads thumbnails, not large viewer images or raw
  originals; viewer activation fetches the selected optimized image on demand.
- Visually inspect all three homepages and train collections at 390, 1440, and 2560 pixels,
  plus dark mode and reduced motion. Verify mobile legibility, focus, contrast, no overflow,
  and distinguishability through composition, not merely colors. Save comparison screenshots.
- Run `npm test -- --capture` (includes all strict builds),
  `source source_me.sh && python3 -m pytest tests/`, and `git diff --check`. Investigate failures;
  do not weaken checks to pass. Prior reports note original C search timeouts and a host Podman
  budget failure; establish their current state rather than assuming they still apply.
- Extend the existing browser journey for stable collection behavior. Use temporary checks for
  visual/performance evidence, not brittle permanent CSS-geometry assertions.
- Confirm original A/B/C/D remain unchanged. Report technical verification separately from
  visual review. No commit, push, deployment, or external writes are included.
