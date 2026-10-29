## 2026-10-29

### Behavior or Interface Changes

- Redesigned shared D show galleries with seven photographic cover cards, compact page
  heading, explicit lead/detail sequences, and short album captions. Full viewer attribution
  and credits remain accessible. Preserved all 45 photographs and their original bytes.
- Distinguished alpha's clean catalog, beta's lead-led photo essay, and gamma's selectively
  offset handwritten scrapbook. Other pages, homepage identity, original A/B/C/D unchanged.

### Fixes and Maintenance

- Verified nine responsive gallery cases, 63 album viewer sessions, three no-JavaScript
  journeys, dark mode, failed-image recovery, direct links, and credits. All 135 provenance
  hashes match. Screenshots and exact evidence: `active_plans/reports/editorial_gallery.md`.
- Final `npm test` built eight sites and passed 136 route checks/16 journeys before original
  C's Material search timed out; the single unchanged retry failed there too. Isolated C search
  subsequently returned results. No test weakening or unrelated original-design changes.

## 2026-10-28

### Additions and New Features

- Broad archive pass: reviewed all 72 contact sheets across 32 folders and 46 candidate
  original frames; added 37 completed-show photographs, bringing the archive selection to
  45 distinct photographs across seven library shows. Preserved originals and 135 hashes.
- Added show navigation, native expandable albums, lazy local thumbnails, and group-local
  Previous/Next and keyboard viewer navigation. Expanded category galleries and refreshed
  the three-photo homepage preview without enlarging it into the full collection.
- Second photo pass: added five full-size-reviewed source selections and ten local WebP
  derivatives; eight archive selections now have preserved originals and exact provenance.
- Added a three-photo homepage preview and six-photo library-show gallery; replaced weak
  Screen/story and Creatures cards, tuned responsive focal positions, and kept archive credits
  visible on phones. No changes to original A/B/C/D, Matchstick, or the guitar group image.
- Copied all 1,336 image attachments across 34 Archive Shows channels after complete pagination
  of 8,167 messages; preserved 2,039,029,563 CDN-served bytes outside the repository.
- Organized originals by show, retained provenance/hashes, and generated 72 contact sheets.
- Added three reviewed Ela Area/Northbrook exhibit photographs, preserved selected originals,
  and produced six optimized local WebP derivatives with uploader attribution.

### Behavior or Interface Changes

- Recorded the explicit no-WIP/home/setup/other-LUG boundary and the correction that eight
  selections were inadequate. Ambiguous candidates remain unpublished; source context is
  corroborated without publishing raw private messages. Original A/B/C/D remain unchanged.
- Replaced the D revisions' Castles homepage diagram with a real club castle scene; refreshed
  train/city cards and galleries and illustrated the visiting page. Original A/B/C/D stay unchanged.
- Preserved alpha/beta/gamma treatments and corrected credits to distinguish uploaders from makers.

### Fixes and Maintenance

- Broad-pass verification: eight strict builds, 136 page checks and 24 browser journeys
  passed; 9 responsive cases exercised all seven albums with 63 viewer sessions. Verified
  135 hashes, no-JavaScript/images-blocked navigation, image failure recovery, and modal
  keyboard focus. One Material search timeout passed the single unchanged retry.
  Pytest: 1,442 passed; the existing 35.23 GB host Podman budget failure remains.
  See [broad review report](active_plans/reports/archive_broad_review.md).
- Second-pass verification: eight strict builds, 130 page checks, 21 journeys, 18 focused
  route/viewport cases, 54 keyboard viewer opens, and all 24 source/derivative hashes passed.
  Final homepage/card/gallery screenshots were inspected. Pytest: 1,439 passed; the same
  host Podman budget failure remains. See
  [second-pass report](active_plans/reports/archive_second_pass_verification.md).
- Fixed heading permalinks intercepting clicks on revised homepage category cards.
- Passed `npm test -- --capture`: eight strict builds, 130 page checks, 21 integration journeys.
- Passed 12 focused image/navigation cases at 390/1440/2560 widths, including gallery opening,
  Escape dismissal, no overflow, and images-blocked/no-JavaScript navigation. Inspected screenshots.
- Repository pytest: 1,438 passed; one unrelated host Podman disk-budget failure (35.23 GB
  versus 20 GB). Did not remove host resources or weaken the check. `git diff --check` passes.

### Removals and Deprecations

- None. No commits, deployments, or Discord writes.

### Decisions and Failures

- Full archive stays at `/home/vosslab/nsh/niltc_archive_shows/`, outside Git/deployment.
  See [DISCORD_ARCHIVE.md](DISCORD_ARCHIVE.md) for source IDs and copy/curation boundaries.
- 401 valid CDN images differ in size from Discord attachment metadata; preserve received bytes
  and record both sizes rather than claim pre-upload originals. Selected files match metadata.
- Initial urllib retrieval received HTTP 403; the requests client with Discord bot User-Agent
  succeeded. Installed declared Node dependencies after missing Playwright blocked browser checks.
- One initial search journey timed out; unchanged search code passed two subsequent complete runs.

## 2026-10-27

### Additions and changes

- Shortened gamma's mobile category photo panels and presented beta first as the suggested
  direction, with restrained alpha and playful gamma alternatives. Requested a verified club
  castle-photo source; the existing diagram remains until that source is available.
- Closed the local revision work without human review gates; refreshed final frog screenshots
  and passed twelve caption, overflow, and cutout-visibility checks. Recorded device and paper
  checks as optional follow-ups rather than unfinished plan milestones.
- Added selective paper frames with Kalam handwritten captions to beta and gamma, picture
  frames and a feathered jet photograph to gamma, and a transparent frog archive-photo
  derivative. Full-image links retain the original photographs.
- Recorded the frog archive-photo provenance. The owner confirmed older photographs are
  appropriate. Rejected background-removal outputs that damaged model details.


- Expanded the D revisions to conservative alpha, photographic beta, and creative gamma.
  Shared content and assets serve all three; beta and gamma add independent stylesheets.
- Tightened homepage copy, moved the slogan and actions before a compact phone mascot,
  enlarged beta's member photograph, and added gamma's poster lettering, colorful brick tiles,
  varied photo grid, and short reduced-motion-aware entrance effect.
- Added gamma to builds, navigation comparisons, browser journeys, and documentation.
- Checked eight strict builds, all design routes and journeys, and a 24-case responsive matrix.
  Captured light/dark comparisons, measured new text/surface pairs, and preserved original A-D.
- Fixed the reduced-motion entrance delay that briefly hid Matchstick. Added a browser
  regression assertion. Final checks passed 130 pages, 21 journeys, and 1,428 repository checks.
- Kept the flyer unchanged. Nothing has been published remotely.

## 2026-10-26

### Additions and changes

- Added D&alpha; and D&beta; from one shared `design_d_revised/` source. Both remove the
  Christmas lights and body textures; alpha keeps faint banner studs, beta uses solid banners.
- Used "Many interests. One club." as the headline, featured the club's brick-built guitars,
  clarified public-show access, and made joining requirements a plain email checklist.
- Applied a light humanizer pass and corrected the powered-track description to battery-powered
  trains. Recorded the full wording diff in the revision report.
- Added a self-contained, editable club flyer SVG and `npm run flyer` for a US Letter PDF
  and preview. The flyer uses blue type on white, the approved logo, embedded local fonts,
  and a vector QR code linking to the club website.
- Extended the comparison page, build, browser checks, and documentation for both revisions.
  Recorded owner guidance and attributed club feedback separately.

### Verification and limitations

- All seven strict site builds pass. Browser checks pass 108 desktop/phone page checks and
  17 interaction journeys, including both revisions' light/dark persistence.
- An eight-case visual check covers both revisions, two widths, and light/dark schemes:
  matching homepage text, intended backgrounds, absent lights, and visible keyboard focus.
- Inner-page screenshot review caught nested bullets becoming numbered steps. Replaced that
  markup with a plain checklist; both final joining pages render six items and matching text.
- The flyer PDF has one 612 by 792 point page, selectable text, and three embedded font subsets.
  Its QR code decodes from the PDF render to `https://niltc.org/`; the rendered PDF was inspected.
- All 166 original A-D runtime/config files match HEAD. No original proposal was edited.
- Repository tests passed 1,421 checks with new files included through an in-memory discovery
  list; the Git index was not changed. The earlier tracked-file-only run passed 1,213 checks.
- Verification is local Chromium and PDF-render evidence. Nothing was published remotely, and
  a physical paper proof remains to be checked before printing a batch.

## 2026-10-20

### Additions and New Features

- Removed the landing page's sidebar navigation so visitors choose A, B, C, or D from the
  central links. Labeled the section "Choose a design" to describe its purpose accurately.
- Reworked the README for club members reviewing the designs, with direct comparison links,
  shared visitor tasks, specific-feedback guidance, and optional developer documentation.
- Imported four independent complete MkDocs designs for an A/B/C/D vote, with separate
  source directories, root configurations, and output URL prefixes.
- Added a neutral comparison homepage, a combined strict build command, and one GitHub Pages
  workflow that deploys all four sites together.
- Added import provenance hashes and a focused browser check for navigation, assets, mobile
  layouts, search, and galleries under the new prefixes.

### Decisions and Failures

- Preserve the four competing implementations; no design is selected or blended with another.
  Keep OTHER_REPOS unchanged and independent of the integrated build.

### Developer Tests and Notes

- The first GitHub Actions run passed all builds, browser checks, and artifact upload; deployment
  failed with a 404 because Pages was not enabled. Added an early Pages setup check, updated all
  six actions to their latest stable releases, and kept write permissions in the deployment job.
- Documented the one-time GitHub Actions Pages source setting and automatic builds on push.
  In-progress deployments finish before the next run; individual live-preview commands are unchanged.
- Updated workflow passes actionlint 1.7.12. All four `mkdocs serve` commands return HTTP 200
  at their project prefixes with file watching and LiveReload enabled; imported and original
  source hashes still match. The revised workflow awaits a push and Pages enablement.
- All four design configurations and the neutral landing page pass strict MkDocs builds.
- Browser verification passes 64 desktop/phone page checks and nine integration journeys.
  All 64 fresh original/imported screenshot pairs match exactly; 16 paired interactions pass.
- Verified unchanged hashes for all 162 imported files and unchanged original working trees.
  The normal repository suite passes 793 checks; an unstaged-file-inclusive scan passes 1,211.
- Kept one focused integration browser check; removed temporary visual-comparison probes after
  recording evidence. Live GitHub Pages deployment is not claimed.

## 2026-10-19

### Added

- Shared designer goal distilled from the website brief for independent implementation.
- Minimal MkDocs Material starter with pinned build dependencies, a homepage, and approved banner.
- Website brief granting full repository ownership and unrestricted implementation choices within
  MkDocs Material and GitHub Pages compatibility.
- Asset inventory and full-body Matchstick frame from the supplied presentation.
- Matchstick's provisional digital palette, updated to Dark Azure wings, and recognizable features.
- macOS installation, local preview, static build, and repository-check instructions.

### Changed

- Renamed ARTIFACTS/image.png to nilbc_banner.png and updated its asset reference.
- Renamed six new ARTIFACTS screenshots by their depicted mascot, logo, and teaching content;
  preserved image bytes and added them to the asset inventory.
- Added website guidance to the agent entry point and project context to the README.
- Made the Bash startup file optional so a new Mac can use the starter without a personal bashrc.
- Documented human guidance and replaceable starter decisions; ignored local environment caches.
