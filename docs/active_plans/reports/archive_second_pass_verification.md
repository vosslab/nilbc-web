# Archive second-pass verification

## Outcome

Five additional selections extend the first pass to eight archive photographs. The second
pass preserves first-pass work and changes only shared D revision content/styles and records.
Original A/B/C/D, Matchstick, the guitar group image, navigation, and variant architecture stay
unchanged. No commit, deployment, Discord writes, or repeat archive download occurred.

## Selection evidence

Reviewed Ela Area 000/024, Northbrook 000/024, Schaumburg 024, and Wheaton 024 contact sheets;
inspected seven full-size candidates. Selected finished details from the established local
library-show batches, not ambiguous external LUG content, planning, visitors, or promotional
posters. Rejected the seal enclosure and haunted facade as crowded/soft or reflection-heavy.

All five new sources were uploaded by Kerbear. Uploader does not establish photographer or
builder identity. Source IDs, timestamps, hashes, unchanged original paths, and ten derivative
hashes are in `ARTIFACTS/discord_archive_shows/provenance.json`.

| New stem | Original | Attachment ID |
| --- | --- | --- |
| ela_spacecraft_2026 | IMG_3514.jpg | 1549075846545940530 |
| ela_characters_2026 | IMG_3517.jpg | 1549075845493030912 |
| ela_dog_2026 | IMG_3495.jpg | 1549075978654064800 |
| ela_market_2026 | IMG_3492.jpg | 1549076018130718880 |
| northbrook_boating_2026 | IMG_3944.jpg | 1561047922282336286 |

## Placement

- Screen/story card: white-and-blue spacecraft, lower cockpit-focused crop.
- Creatures card: white dog; complete desktop frame and face-focused phone crop.
- Other cards: individual locomotive, street, and castle focal positions.
- Homepage: three detail photos after the unchanged guitar group, before existing stats.
- Visiting page: six complementary photos in three desktop columns, compact mobile cards.
- Theme galleries/credits: all five additions; castle and street retain their first-pass lead.
- Full-image viewer: uncropped local WebP frames. Phone archive credits stay visible.
- Alpha retains plain presentation; beta/gamma retain existing selective notes and frames.

## Executed checks

- `npm test -- --capture`: passed eight strict builds, 130 page checks, 21 integration journeys,
  zero errors. Repeated after final crop and manifest-order corrections.
- Temporary focused Playwright probe: passed 18 route/viewport cases (three revisions,
  home and visiting, widths 390/1440/2560), including decoded photos, no page overflow,
  expected gallery counts, category-link destinations, and no page errors.
- All six show photographs opened by keyboard and dismissed with Escape at each variant/width:
  54 viewer opens, with exact full-frame image destinations asserted.
- Verified all eight selected original SHA-256 values and all sixteen derivative hashes.
- `git diff --check`: passed. Original A/B/C/D source/config diff against HEAD is empty.
- `source source_me.sh && python3 -m pytest tests/`: 1,439 passed, one failure in 40.12 seconds.
  The existing host Podman disk-budget failure remains: 35.23 GB versus 20 GB. No host
  resources removed and no check weakened.

## Visual evidence

Inspected generated category, gallery, and complete homepage screenshots with vision tools:
phone alpha/gamma, desktop beta, and wide gamma gallery, with representative show-gallery
screenshots. Review led to preserving the dog's complete desktop frame instead of a cramped
cover crop. Complete final homepages show no serious layout defects; variant character,
mascot, and guitar feature remain intact. Compact phone character crops are intentionally
closer than full viewer frames. Selected beta scrapbook note remains an intentional exception
to uniform gallery cards. Sticky navigation crossing element-only screenshots is capture
positioning, not content removal; full-page captures were reviewed separately.

Ignored evidence: `output_checks/second_pass/` contains focused PNGs, JSON, build/browser log,
and pytest log. Standard captures remain in `output_checks/screenshots/` and the all-route
report in `output_checks/designs_report.json`.

## Control evidence boundary

| Controls | Status | Evidence |
| --- | --- | --- |
| Six show-gallery image links | Live-proven | 54 keyboard opens and Escape dismissals |
| Screen/story category links | Live-proven | Nine variant/width destinations |
| Existing menus, search, image viewers, theme switch | Live-proven | 21 standard integration journeys |
| Local links/assets and new gallery fragment link | Retrieval-proven | 130 generated-route checks |
| External email, Discord sources, map links | Not activated | No external side effects; local href checks only |

Local Chromium verification does not claim physical-device or public-deployment testing.
