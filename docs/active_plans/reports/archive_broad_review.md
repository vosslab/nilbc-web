# Broad archive curation and gallery

## Scope and implementation

The full local archive is already preserved. This pass reviews all 72 contact sheets across
32 nonempty show folders, then original candidate frames and read-only source context.
Only completed club exhibits photographed at shows qualify. No other-LUG, home/workbench,
setup/teardown, planning, promotional overlay, private discussion, or ambiguous images.

Implement a shared show gallery under Shows, with show navigation and native expandable
albums. Local lazy thumbnails open uncropped optimized images in the existing accessible
viewer. Categories remain available under Worlds we build; only three selected details
appear in the homepage preview. Preserve the mascot, guitar group, original A/B/C/D, and
the three revised variants' independent visual treatments.

## Verification plan

- Validate source/derivative hashes, unique selections, and published counts from manifests.
- Build all eight sites and run `npm test -- --capture` without weakening checks.
- Exercise show navigation, native albums, category filtering, viewer controls and keyboard
  focus at phone, desktop, and very wide widths; inspect screenshots with vision.
- Check no-JavaScript fallback, lazy loading, local-only assets and source metadata exclusion.
- Run repository pytest and report host-budget blockers without deleting host resources.

## Review findings

All 72 contact sheets were visually reviewed individually, not inferred from filenames.
Many older folders consist largely of planning, memes, venue logistics, or personal images.
Convention folders mix clubs and cannot establish ownership by location. Promotional posters
were not used as photographs or treated as proof that their inset models attended that show.

Candidate original frames were opened individually. Very large source images produced
misleading tightly focused descriptions, so uncropped EXIF-oriented 1,400-pixel review copies
were inspected to verify the full composition. These scratch review copies are not deployed.
Captions follow the verified full frames, not speculative contact-sheet identifications.

Read-only Discord context confirmed seven library-show photo batches through post-show
photo requests, club exhibit discussion, and host/show completion messages. No raw messages,
private operational notes, access tokens, or signed CDN URLs are included in public output.
The local catalogs retain complete source information outside the repository.

## Final collection

- 45 distinct archive photographs across seven shows: 37 new, eight preserved selections.
- 66 photographs in the shared manifest including the 21 pre-existing website photographs.
- All 72 contact sheets, 32 nonempty folders, and 1,336 tiles reviewed; 46 candidate originals
  inspected individually. Eight candidates withheld; one candidate was already selected.
- Show counts: Northbrook 9, Ela Area 10, Algonquin 6, Wheaton 4, Arlington Heights 7,
  Oswego 5, Barrington 4. The homepage preview contains three photographs.
- Source manifest: `ARTIFACTS/discord_archive_shows/provenance.json`.
  Review ledger: `ARTIFACTS/discord_archive_shows/review.json`.
- 135 source/derivative hashes verified, plus all 45 external original hashes rechecked.
  No duplicate source hashes; supplementary 64-bit difference-hash comparison found no
  selected pair within six bits. This screening supplements visual review, not ownership proof.
- All 90 WebP derivatives decode, have recorded dimensions, and contain no EXIF metadata.
  The selected originals total 95,200,225 bytes; derivatives total 13,277,066 bytes,
  including 2,755,140 thumbnail bytes. No full archive, review sheets, source originals,
  or private catalog files are deployed.

## Final execution results

- `npm test -- --capture`: eight strict builds, **136 desktop/mobile page checks and
  24 integration journeys passed**, zero browser/resource errors in the final report.
- One preceding full run timed out waiting for Material search. The requested single
  unchanged retry passed. The search implementation and test timeout were not weakened.
  Failure receipt: `output_checks/archive_broad/search_timeout_report.json`.
- Focused browser matrix: **9 cases** across Dalpha/Dbeta/Dgamma at **390, 1440, and 2560 px**.
  All seven albums navigated in each case: **63 album/viewer sessions**. All cases verified
  the exact 45-photo set, no horizontal overflow, category filtering, and three-photo preview.
- Initial gallery loads requested **5-9 thumbnails and zero full photographs**. Closed albums
  did not eagerly load their entire image collection. Every gallery image has native lazy loading.
- No-JavaScript: native album opening and direct full-image navigation passed in all variants.
- Images blocked: homepage-to-gallery-to-album navigation passed in all variants.
- Controlled failed image request: visible error/direct-link feedback and recovery through
  Next passed. The first focus-cycle probe exposed a native-dialog edge; explicit Tab and
  Shift+Tab wrapping was added, exercised successfully, and retained in the smoke journey.
- Dark gallery checks passed at 390/1440; final gallery, category, preview and viewer
  screenshots were inspected at phone, desktop and very wide sizes. An early capture ran
  before lazy images decoded; final captures await visible-image decoding and show all images.
- Repository pytest: **1,442 passed; one known host Podman budget failure**, 35.23 GB versus
  20 GB. No host resources were deleted and the check was not skipped or weakened.
- Hook/JavaScript syntax and `git diff --check` passed. Six untracked textual deliverables
  also passed direct no-index whitespace checks. New text sources are below the line limit.
- Original `design_a`, `design_b`, `design_c`, `design_d` and their MkDocs configurations have
  no changes. Existing authorized revision work, Matchstick and guitar-group artwork remain.

## Control evidence matrix

| Control | Evidence | Outcome |
| --- | --- | --- |
| Show navigation links | Live-proven, all seven across nine viewport/variant cases | Correct album opens and URL hash identifies it |
| Native album summary | Live-proven by Enter; no-JavaScript click | Opens/closes, including keyboard focus |
| Thumbnail viewer | Live-proven, 63 sessions | Correct full frame and alt text, local image only |
| Next / Previous | Live-proven with clicks | Changes within the current album |
| ArrowLeft / ArrowRight | Live-proven, including first-to-last wrap | Correct album-local sequence |
| Tab / Shift+Tab | Live-proven after repair; permanent smoke coverage | Focus wraps within the dialog |
| Escape / close button | Live-proven | Closes and restores opener focus |
| Direct-image fallback | Live-proven without JavaScript | Navigates to local WebP |
| Image failure / recovery | Controlled request-abort proof | Error announced; Next loads the next image |
| Screen/story and Creatures filters | Live-proven in nine cases | Only the requested category remains visible |
| Homepage gallery CTA | Live-proven with and without images | Reaches the gallery within the variant prefix |

## Evidence locations and retention

Generated receipts and screenshots are in ignored `output_checks/archive_broad/`:
`artifact_report.json`, `browser_report.json`, `fallback_report.json`, and PNG captures.
The canonical smoke receipt is `output_checks/designs_report.json`; homepage captures are
in `output_checks/screenshots/`. These are local verification artifacts, not deployed content.

The lasting regression lives in `tests/playwright/designs_smoke.mjs`: three variant journeys
for album navigation, viewer sequence, modal focus wrapping and return, and native closing.
One-time exhaustive matrix/failure-probe scripts were removed from `tests/_temp/` after
execution; their receipts and this report retain the evidence without expanding the fast suite.
No commit, deployment, Discord write, redownload, or host-resource cleanup was performed.
