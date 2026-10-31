# Train previews and visit invitations

Date: 2026-10-30.

## Public behavior

Original D's Rail yards card now opens `d/creations/trains/`, rather than a section on the
creations overview. Its heading permalink previously intercepted the card click; the
permalink no longer receives the stretched card hit area. Alpha, Beta, and Gamma retain
their own dedicated `creations/trains/` pages, now titled Rail yards.

All four train pages contain 23 distinct train photographs, rendered as static thumbnails,
and a prominent "See the trains in person" link to upcoming shows. Revised collections and
show albums no longer open an image viewer. Descriptive alternatives, captions, source credits,
and show context remain available. Theme collections use a continuous grid while preserving
the existing verified event-date ordering. Native show-album expansion still works.

This change targets the revised galleries and original D's train page. Original D's other
galleries and the original A-C proposals retain their existing behavior. Larger derivatives
remain available for selected editorial uses and repository review; the train pages do not
request them. Existing photo originals are unchanged.

## Selection and image sizes

Six additions come from existing verified Barrington and Wheaton photo-message batches:
gantry crane, Metra coaches, city-and-railway overview, container consists, rail depot, and
a blue character engine. Full-frame inspection and source-batch references are recorded in
[train_teaser_review.json](../../../ARTIFACTS/discord_archive_shows/train_teaser_review.json)
and [provenance.json](../../../ARTIFACTS/discord_archive_shows/provenance.json).

One initial candidate duplicated the existing Barrington yard photograph. It was replaced
with the distinct city-and-railway view before completion. The catalog test now checks
source-image uniqueness within the train selection. An existing cross-theme reuse of the
Northbrook party/1999 railcar frame remains; total catalog counts refer to records.

All train thumbnails have a maximum 480-pixel edge and total 805,046 bytes. Before resizing,
the 23-image draft totaled 1,298,168 bytes. The website lazily loads the previews. New larger
repository derivatives are capped at 720 pixels. Original D's build hook reuses shared train
thumbnails, avoiding duplicate source assets and keeping its own URL prefix.

The repository catalog now contains 79 records, including 58 archive selections and 23 train
records. Browse [README.md](../../photos/README.md). Verified event dates remain distinct from
unknown capture dates; uploader credits do not identify builders or photographers.

## Verification

- Strict combined build passed for the landing page and all seven designs.
- Final whole-site browser run passed 174 desktop/mobile page checks and 23 interaction
  journeys, including the original D Rail yards card and revised keyboard visit links.
- Sixteen focused checks passed: four train pages, 390/1440-pixel widths, JavaScript on/off.
  Each has 23 images, every train image is at most 480 pixels, only thumbnail photo URLs are
  requested, no gallery image links open larger files, and the visit link reaches that
  design's shows page. No horizontal overflow. Fresh captures are in
  `output_checks/train_teasers/` and were visually inspected.
- Scoped catalog, content, local-link, and guidance checks passed 147 tests.
- All 58 preserved archive-original hashes match their provenance records, including the
  replacement selected after the duplicate check.
- `git diff --check` passed.

No commit or deployment was performed. The host Podman budget check and the previously
reported unrelated archive-utility lint/security failures were not rerun during this pass.
Browser verification uses Chromium; no new cross-browser or screen-reader audit was performed.
