# Shared image-forward implementation

## Outcome

Implemented and verified the shared alpha/beta collection and homepage path on the current
curation snapshot. The shared hook now supports `/// collection | theme` and
`/// featured-photos`; collection counts come from selected manifest records. Each collection
keeps one `.nb-gallery.nb-collection`, preserving the existing photo viewer's collection scope.
Visible show headings mark transitions without breaking that scope.

The homepage uses `.nb-home-stage`, `.nb-home-photos`, and `.nb-mosaic`; the existing
`.nb-hero__matchstick` hook remains present for browser checks. Homepage photo IDs come from the
curated `homepage_photos` list, not Python or Markdown constants. The block validates the list,
unique IDs, photo references, and verified event dates. It does not select candidates automatically.

Alpha uses faint hero studs and a compact, regular catalog grid. Beta has a desktop editorial
text/photo split and larger collection images with a blue-accented show heading; its collection
grid is three columns at the tested desktop widths and remains two columns on phones. Beta's
mobile hero is shorter and suppresses the separate mascot illustration; the header logo remains.

Alpha's About navigation includes `Our story: about/timeline.md`; `timeline.css` is loaded by both
alpha and beta. Beta explicitly lists it because its `extra_css` replaces alpha's list.

## Date and selection contract

The implementation follows the user-approved D-DATES direction:

- `photo_shows.yml` owns verified `event_date` values as ISO strings: `YYYY-MM` or
  `YYYY-MM-DD`. The existing visitor-facing `date` label is unchanged.
- Parsing rejects non-string values, unsupported syntax, invalid months/days, and invalid calendar
  dates. A month-only value remains month-only; no day is inferred from IDs, upload times, or labels.
- Dated shows sort newest first; equal verified dates sort by show ID. Each show's explicit photo
  sequence is retained. Shows without a verified date and then non-show archive photos follow,
  with show-ID ordering for the undated shows.
- For a month containing both month-precision and exact-day records, exact-day evidence sorts first;
  the month-level record remains imprecise. No day value is assigned to it.
- Public photo `show` references resolve through the show record. No event date is duplicated in
  photo metadata.
- Collection headings and thumbnail captions lead with the existing show label/date. Undated
  material is labeled “Club archive; date not established.” A separate `capture_date` is rendered
  only if such a field is actually supplied; none is present in the current snapshot.

## Verification

### RED/GREEN and builds

The chronological-order test was run RED before replacing insertion-order behavior. It returned the
older show first despite a newer verified `event_date`. The final synthetic case also covers reversed
YAML insertion order, equal-date show-ID ties, show sequence preservation, exact-day/month precision,
undated shows, and archive material.

Final focused test result:

```text
source source_me.sh && python3 -m pytest tests/_temp/test_image_forward_collection.py -q
4 passed
```

`python3 -m py_compile design_d_revised/site_hooks/data_blocks.py` passed.

Both independent strict builds passed against the current data snapshot:

```text
source source_me.sh && python3 -m mkdocs build --strict -f mkdocs_d_alpha.yml
Documentation built in 2.48 seconds

source source_me.sh && python3 -m mkdocs build --strict -f mkdocs_d_beta.yml
Documentation built in 2.49 seconds
```

The rendered browser probe passed after those builds:

```text
node --check tests/_temp/image_forward_shared.mjs && node tests/_temp/image_forward_shared.mjs
PASS alpha/beta home, collections and viewer at 390, 1440, 2560; 12 screenshots
```

It exercised the visible mobile drawer using `.md-header__button[for="__drawer"]` on both
revisions and navigated to Shows, clicked all five homepage-to-theme routes, checked the legacy
category anchors, compared each rendered count against its rendered figures, opened the viewer,
advanced with ArrowRight, closed with Escape, and verified focus returned to the opener. A
JavaScript-disabled journey verified thumbnail links still open the corresponding full local image.

The separate network probe passed:

```text
node --check tests/_temp/image_forward_network.mjs && node tests/_temp/image_forward_network.mjs
PASS alpha/beta fetch thumbnails first; selected full photo waits for activation
```

### Current data/count snapshot

The final local builds and count comparison used 71 manifest photo records, seven show records with
verified month-precision dates, and three curated homepage IDs. Generated alpha and beta HTML each
matched manifest-derived counts and unique photo IDs:

| Collection theme | Alpha | Beta |
| --- | ---: | ---: |
| Trains | 15 | 15 |
| Cities | 22 | 22 |
| Screen and story | 10 | 10 |
| Castles | 9 | 9 |
| Creatures | 12 | 12 |

These are build-snapshot values, not constants or a final archive-completeness claim. The current
snapshot has 15 train-tagged records; the plan's approximately 100-photo train target is unmet here,
but this is not a claim that the archive has no further eligible candidates. See
[image_forward_curation.md](image_forward_curation.md) for its review boundary; the manager's final
archive-availability and source-coverage gate remains authoritative.

### Visual review

Playwright captured twelve current-workspace screenshots; they were reviewed with vision at all
three requested widths for both homepages and Trains collections:

- `output_checks/image_forward_shared/d-alpha-home-390.png`
- `output_checks/image_forward_shared/d-alpha-home-1440.png`
- `output_checks/image_forward_shared/d-alpha-home-2560.png`
- `output_checks/image_forward_shared/d-alpha-trains-390.png`
- `output_checks/image_forward_shared/d-alpha-trains-1440.png`
- `output_checks/image_forward_shared/d-alpha-trains-2560.png`
- `output_checks/image_forward_shared/d-beta-home-390.png`
- `output_checks/image_forward_shared/d-beta-home-1440.png`
- `output_checks/image_forward_shared/d-beta-home-2560.png`
- `output_checks/image_forward_shared/d-beta-trains-390.png`
- `output_checks/image_forward_shared/d-beta-trains-1440.png`
- `output_checks/image_forward_shared/d-beta-trains-2560.png`

Alpha reads as the quieter catalog; the mobile Matchstick label and action labels fit after the
responsive adjustment. Beta reads as a distinct editorial spread on desktop, with larger lead
photography and solid surfaces; its mobile first photo begins near 707 px and fits with its caption
in the captured 1000 px view. Both collection layouts remain two columns at 390 px. No visible
horizontal overflow or accidental clipping was found. Repeated venue/date captions are consistent
but do not distinguish each image's subject; this is a remaining editorial trade-off.

## Files in this handoff

- `design_d_revised/site_hooks/data_blocks.py`
- `design_d_revised/site_src/index.md`
- `design_d_revised/site_src/creations/trains.md`
- `design_d_revised/site_src/creations/cities.md`
- `design_d_revised/site_src/creations/screen.md`
- `design_d_revised/site_src/creations/castles.md`
- `design_d_revised/site_src/creations/creatures.md`
- `design_d_revised/site_src/stylesheets/image-forward.css`
- `design_d_revised/site_src/stylesheets/alpha-layout.css`
- `design_d_revised/site_src/stylesheets/beta-layout.css`
- `mkdocs_d_alpha.yml`
- `mkdocs_d_beta.yml`
- `tests/_temp/test_image_forward_collection.py`
- `tests/_temp/image_forward_shared.mjs`
- `tests/_temp/image_forward_network.mjs`
- `output_checks/image_forward_shared/` (ignored local screenshots)
- `docs/active_plans/reports/image_forward_shared.md`

The category overview (`creations/index.md`), initial homepage/hook edits, and shared CSS/config
scaffolding were already present in the partial worktree when this task began; those edits were
preserved rather than reverted. Timeline page/style content was owned by its worker; only the
alpha/beta navigation and stylesheet integration were added here. No commit or deploy was made.
This handoff did not edit gamma config/template/CSS, manifests, image assets/provenance, timeline
contents, the permanent smoke suite, or shared changelog/guidance documents.

## Editing guidance for the docs integrator

- Keep `homepage_photos` in the root of `design_d_revised/data/photos.yml` as the manually reviewed
  ordered list of photo IDs. Update it only after eligibility and crop review; never replace it with
  a highest-date/automatic-selection query. The renderer now consumes that list directly.
- Keep each photo's `show` reference pointed at the authoritative show record. Add a quoted
  `event_date` to `design_d_revised/data/photo_shows.yml` only from verified event evidence. Use
  month precision when that is all the evidence supports; preserve the existing visitor-facing
  `date` label. Do not infer a day from an ID, upload folder, or image timestamp.
- Keep show photo sequences complete and explicit. Counts are calculated from selected manifest
  records, so page copy and tests should not encode quotas.
- Preserve the existing privacy boundary: no private Discord messages, signed URLs, camera GPS,
  raw source archive, or private curation ledger in deployed pages or public reports. Continue to
  use the established public credits/provenance fields.
- Routine page copy stays in Markdown. Use `/// featured-photos` for the curated homepage preview
  and `/// collection | <theme>` for complete theme routes; retain each collection as one
  `.nb-gallery` so viewer navigation is collection-wide.

## Gamma integration advice

Gamma remains outside this ownership and was not edited. Its config should retain the shared
`featured-photos` and `collection` hook contracts and the `.nb-home-stage`, `.nb-home-photos`,
`.nb-mosaic`, and `.nb-hero__matchstick` class hooks. Load `stylesheets/image-forward.css` before
Gamma's final `stylesheets/gamma-layout.css`; do not copy alpha/beta layout files into gamma. Keep
`timeline.css` in gamma's stylesheet list when the timeline page is published, and preserve the
`Our story` navigation item if gamma overrides rather than inherits alpha's `nav` mapping. Apply
Gamma-specific visual treatment to the shared collection divider/photo hooks without splitting the
single `.nb-gallery` viewer container.

## Limits

This handoff does not certify that the archive review is complete or that a particular photo quota
is reachable. The current manifest contains 15 train photos; curation has explicitly continued
beyond this snapshot. The complete permanent `npm test`/smoke suite was not run here; the reported
prior smoke failure at the Material drawer selector came from a run without a rebuild and is not
attributed to source behavior. After the independent alpha/beta rebuilds, the same drawer selector
was visible and its Shows route was exercised successfully in the temporary browser probe. The
manager's post-owner integration run remains the release gate.
