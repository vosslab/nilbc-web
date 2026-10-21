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
