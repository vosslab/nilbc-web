# Shared content refinements

## Changes

- Put the curated show preview inside the existing homepage stage beside the welcome and
  show/join actions. The next-show ticket now follows the preview as a sibling. Added useful
  alternative text to all five homepage theme photos.
- Added one representative, directly linked photo for each theme on the worlds overview and
  explicit section IDs for trains, cities, screen, castles, and creatures.
- Moved upcoming show cards directly below the page title. Added the shared membership email
  action after the Join introduction, removed duplicated About history details in favor of the
  sourced timeline, and removed repeated historical statistics from the homepage.
- Collection show/date headings link to their show albums. Each photo caption uses
  `album_caption` or falls back to `caption`; full-image links and the viewer's show/date context
  remain. A no-show archive group receives its own heading.

## Verification

- Strict builds passed with exit code 0 for `mkdocs_d_alpha.yml`, `mkdocs_d_beta.yml`, and
  `mkdocs_d_gamma.yml`. Outputs are isolated under
  `output_checks/refinement_content/d-alpha/`, `d-beta/`, and `d-gamma/`.
- A temporary assert-based check of each generated variant confirmed: home stage/photo/ticket
  order; upcoming Downers Grove dates (November 14-15, 2026), venue, and show-page link; five
  stable theme anchors with linked images and non-empty alt text; Join CTA placement; show cards
  before explanatory copy; About timeline link without duplicated event detail; linked collection
  headings with show/date; subject-only visible captions; and direct full-image links.
- `git diff --check` passed.
- The host date was 2026-10-30. The November Downers Grove event was upcoming and appeared on
  the shows page. The missing homepage ticket came from nesting the data block inside the custom
  hero block; moving it to a sibling position restored the ticket without changing dates.

## Limits

No full browser suite or visual screenshot review was run for this content-only subtask. The
assert-based generated-HTML check was temporary; no permanent browser assertions were added.
