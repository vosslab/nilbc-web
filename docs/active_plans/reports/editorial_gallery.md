# Editorial gallery verification

Date: 2026-10-29. No commit or deployment.

## Delivered

Shared D revisions retain all 45 selected archive photographs across seven shows.
Photographic cards carry venue, month/year, and computed count. The gallery alone omits
its generic mascot banner. Native expandable albums retain lazy local thumbnails,
full-frame links, keyboard viewer controls, and no-JavaScript browsing.

Explicit sequences are stored in `design_d_revised/data/photo_shows.yml`; the hook verifies
that each is a duplicate-free exact match for that show's photographs. The lead doubles as
cover. Optional `album_caption` strips repeated event text only in the album. Full upload
attribution remains in the viewer, with a static credits/source link near the introduction.
No new imagery, crops, maker claims, or archive copies were introduced.

- Alpha: clean three-column exhibition catalog, two columns on intermediate widths and one
  on phones; source order begins with the establishing scene.
- Beta: larger opening photograph followed by paired details; one column on phones.
- Gamma: paper cards with selected offsets and handwritten captions; no phone rotation.

All 45 thumbnails were visually reviewed in `output_checks/editorial_contact.jpg`; the seven
leads were reviewed at larger resolution in `output_checks/editorial/leads.jpg`. The lead
subjects are streetscape, castle yard, Classic Space craft, sailboat, winter market,
fortress, and forest riverbank. Existing source-qualified captions were retained.

## Commands and outcomes

| Verification | Actual outcome |
| --- | --- |
| First `npm test` before final catalog refinement | Passed eight strict builds, 136 page checks, 24 journeys |
| Final `npm test` | Eight strict builds passed; 136 page checks and 16 journeys completed; original C search timed out at `designs_smoke.mjs:183` |
| One unchanged `npm test` retry | Same original C search timeout; final full suite is not green |
| Isolated original C search diagnostic | Four result links / two matching documents for Bensenville after bounded wait; no original C code changed |
| `node output_checks/editorial_probe.mjs` | Nine responsive cases, 63 album viewer sessions, three no-JavaScript journeys passed |
| `node output_checks/editorial_extra.mjs` | All three revisions passed dark mode, failed-image recovery, close/focus return, direct image, credits, and images-blocked navigation |
| Provenance hash calculation | All 135 selected-original and derivative hashes matched manifest |
| `git diff --check` | Passed; untracked plan/report/show YAML/gallery Markdown also passed no-index whitespace checks (expected difference exit 1, no diagnostics) |
| In-memory invalid sequence probes | Omission, duplicate ID, and foreign-show ID each raised the intended ValueError |
| `git diff --name-only -- design_a design_b design_c design_d` | Empty; originals unchanged |

Final full-suite logs are `output_checks/editorial_npm_test.log` and
`output_checks/editorial_npm_retry.log`. Final suite receipt is
`output_checks/designs_report.json`. Focused receipts are in
`output_checks/editorial/report.json` and `extra_report.json`. The isolated pass does not
convert the two canonical failures into passing evidence. No tests were weakened.

Repository pytest was not rerun for this task. The parent's previously recorded host Podman
budget failure remains a separate environment limitation; no host resources were removed.

## Live control evidence

| Control / behavior | Evidence |
| --- | --- |
| Seven photographic show links | Enter opens correct album and hash target in every responsive case |
| Native album summary | Enter closes; native click opens without JavaScript |
| Photo links | Enter opens full-frame viewer; all seven albums exercised in each case |
| Previous / Next | Real button clicks change image within the current album |
| Left / right arrows | Wrap last-to-first correctly within album |
| Tab / Shift+Tab | Both modal boundaries wrap between Close and direct-image link |
| Escape | Dismisses dialog and restores exact opener focus |
| Close button | Click dismisses and restores opener focus in each revision |
| Direct-image link | Navigates to actual local full image in each revision |
| Credits link | Navigates to credits page with uploader attribution |
| Viewer image failure | Aborted first image announces unavailable; Next recovers to loaded second image |
| No JavaScript | All three revisions open native album and follow direct image |
| Images blocked | Cover labels still open correct native album; no horizontal overflow |
| Lazy loading | All 45 album images retain lazy attributes; no full-image fetch before opening viewer |
| Theme switch | Dark gallery covers rendered and captured for each revision |

All focused responsive cases checked absence of metadata stacks, 45 figures, seven covers,
no gallery hero, full-frame `contain`, no horizontal overflow, and zero page errors.

## Screenshot evidence

33 PNG screenshots in ignored `output_checks/editorial/`:

- `{d-alpha,d-beta,d-gamma}_{390,1440,2560}_covers.png`: actual viewport and chrome.
- `{d-alpha,d-beta,d-gamma}_{390,1440,2560}_viewport.png`: actual open-album viewport.
- `{d-alpha,d-beta,d-gamma}_{390,1440,2560}_album0.png`: full Northbrook album detail.
- `{d-alpha,d-beta,d-gamma}_1440_album1.png`: portrait-led Ela Area album detail.
- `{d-alpha,d-beta,d-gamma}_390_dark.png`: dark mobile covers.

Long album element captures temporarily hide only fixed `.md-header`/`.md-tabs` during the
screenshot to avoid sticky chrome appearing halfway down the stitched image. Actual viewport
captures retain unmodified chrome and demonstrate no overlap at the album start. Images are
decoded and individually scrolled into view before long captures to avoid raster-culling
blank rectangles. This is capture preparation, not a production image-loading change.

Visual review confirmed balanced final alpha grid, clear beta lead/detail hierarchy, readable
gamma offsets, mobile labels, and bounded very-wide composition. Portrait side margins are
intentional full-frame containment, not missing images. The final alpha/very-wide gamma
viewport checks confirmed that sticky navigation does not obscure the album opening.

## Changed paths for this task

- `design_d_revised/data/photo_shows.yml`
- `design_d_revised/data/photos.yml`
- `design_d_revised/site_hooks/data_blocks.py`
- `design_d_revised/site_src/shows/gallery.md`
- `design_d_revised/site_src/stylesheets/gallery.css`
- `design_d_revised/site_src/stylesheets/beta.css`
- `design_d_revised/site_src/stylesheets/gamma.css`
- `docs/HUMAN_GUIDANCE.md`
- `docs/DESIGN_DECISIONS.md`
- `docs/INSTALL.md`
- `docs/CHANGELOG.md`
- `docs/active_plans/EDITORIAL_GALLERY.md` (new)
- `docs/active_plans/reports/editorial_gallery.md` (new)

The scripts and captures under `output_checks/` are one-time implementation evidence, not
new permanent tests. Existing authorized dirty files and imported archive assets were preserved.
No JavaScript changes were necessary: the existing viewer already retained complete attribution.
