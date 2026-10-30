# Image-forward photo curation report

## Result

- The shared photo catalog now contains **71 distinct records**: 50 Discord show selections
  and 21 pre-existing site photographs. Five new, visually reviewed completed-show railway
  photographs were added, expanding the archive total from 45 to **50**.
- There are **15 train-tagged records** overall, including the five additions. This is the
  eligible reviewed train selection, not a claim that 15 is the maximum possible across all
  1,336 preserved attachments. The about-100 target is unmet; available visual evidence does
  not justify filling it with scenery, ambiguous club ownership, or WIP/setup frames.
- The five new frames cover Northbrook (2) and Algonquin (3). Previously selected coverage
  includes train views from Northbrook, Ela Area and Barrington. Train-tagged photo totals by
  show are: Northbrook 5, Ela Area 1, Algonquin 3, Barrington 1; the other four selected show
  albums currently have no train-tagged photo.
- Other existing archive selections remain. Existing 45 selections were retained.

## Review and evidence boundary

The prior broad pass reviewed all **72 contact sheets / 1,336 tiles**, but individually inspected
only a subset of original frames. This pass revisited the newest Northbrook and Ela sheets,
Algonquin train candidates, the other selected recent show source sheets, and reviewed candidate
originals individually before selection. Archive folders/channel names alone were not treated as
ownership evidence. Eligibility relies on existing read-only show-batch context references in the
selected provenance and existing broad-review ledger. No new private channels or credentials
were accessed. Contact-sheet review excludes posters, memes, venue/setup images and unfinished
track/chassis work. A model depicting construction can still be a finished vignette; it is not
rejected merely for that theme.

Selection prioritizes LEGO MOCs and build/documentary value, not people portraits. Incidental
visitors/builders in public show photographs are not an exclusion criterion, consistent with the
owner's clarification. Uploader is credited as uploader, never represented as maker or photographer.

Five selected new source frames:

- Northbrook: purple piano-themed railcar and decorated 1999 railcar. These are distinct
  rolling-stock subjects; full-frame review found both visibly completed-looking exhibit builds.
- Algonquin: steam locomotive and freight cars, character-themed engines, and industrial
  freight cars. These are distinct train scenes; all appear as completed show displays.

The banana-carrying red recycling truck was individually reviewed but rejected: it is a road
vehicle and no track or train is visible. This explicit rejection prevents a misleading category
assignment and is included in the external review ledger.

This is not a claim that every archive image has been individually reviewed at full frame.
The durable external ledger `/home/vosslab/nsh/niltc_archive_shows/image_forward_review.json`
records the six new source identities, hashes, upload/event/capture date evidence, and verdicts.
The repository's `ARTIFACTS/discord_archive_shows/review.json` was extended with the six
full-frame selections. Raw message content, signed CDN URLs, credentials, and GPS are not added.

## Dates and featured photos

`photo_shows.yml` records normalized `event_date` at supported **YYYY-MM** precision for all
seven selected library shows. The existing human-readable month/year labels are unchanged. The
photo source EXIF was checked including the EXIF sub-IFD: the six additions have no camera
capture timestamp. Discord upload timestamps are kept separate in the private ledger and are
not presented as capture dates. Therefore event month labels are the supported dates; no exact
camera day is claimed.

The catalog's hand-curated `homepage_photos` remain `northbrook_street_2026`,
`ela_castle_2026`, and `ela_spacecraft_2026`. These are subject-forward recent show photographs;
no train image was substituted based solely on its train category.

The guitar caption's unsupported phrase “at a recent show” was removed. No early-2010s date
was inferred from recollection or upload-folder naming. The frog's 2017 upload directory is not
used as a creation date.

## Provenance and derivatives

Six unchanged archive source originals were copied into `ARTIFACTS/discord_archive_shows/` and
SHA-256 verified against their preserved local source bytes. Twelve WebP derivatives were
created in `design_d_revised/site_src/assets/photos/`: EXIF-oriented RGB, Lanczos, longest edge
640 at quality 78 and 1600 at quality 82, method 6, no upscaling, metadata removed. Source and
derivative hashes, dimensions, processing, uploader credit, rights limitation, and existing
show-context references are recorded in the selected provenance manifest.

All prior 45 selections remain intact. The user-requested demo use does not establish a general
redistribution license; uploader credit does not imply authorship.

## D-DATES handoff

Per manager-approved D-DATES, public show records carry `event_date` values in ISO month or day
precision supported by evidence; unknown dates would be null/omitted, never inferred from an ID.
Per-photo `show` keys provide their event date; no duplicate per-photo date field was added.
Future rendering should prioritize verified event date, supported capture date only when present,
then an honest undated/archive label. The homepage preview is intentionally hand-selected and
validated for unique known IDs by the shared hooks implementation; do not auto-select a quota.

The latest event-eligible train pool reviewed is October 2026 Northbrook and May 2026 Algonquin,
with existing September 2026 Ela and September 2025 Barrington train frames. Newer available
Northbrook content yielded only a handful of distinct, finished-looking rail vehicles; many
remaining frames depict other MOCs, promo material, or setup/WIP. Refresh from those show batches
first if a future full-frame review finds stronger train candidates. The broader archive still
requires individual full-frame and context review before any additional candidate can be called
eligible.
