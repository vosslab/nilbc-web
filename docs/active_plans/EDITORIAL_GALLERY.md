# Editorial show gallery

## Contract

Preserve the 45 selected show photographs and all seven albums, original A/B/C/D,
homepage identity, provenance, and full-frame native-link browsing. Change only the
shared revised show-gallery presentation and its scoped styles. No new imagery.

## Implementation

- Replace the gallery-only mascot banner with the existing compact Markdown heading.
- Give each show a photographic cover and explicit complete sequence in photo_shows.yml.
  Lead with a scene or legible exhibit, then related details; reject missing/duplicate IDs.
- Render short album captions without repeated metadata, keeping full viewer attribution
  and a visible credits link. Keep other photo placements unchanged.
- Alpha: quiet exhibition catalog. Beta: larger lead and paired details. Gamma: selective
  paper offsets and handwritten captions; simplify on phones. Preserve source order.
- Retain native details, lazy thumbnails, direct full-image links and viewer controls.

## Evidence

Inspect the 45-image contact sheet and seven lead frames; test all albums and viewer
controls at 390, 1440 and 2560 widths under the project prefix. Capture covers and open
albums, check no-JavaScript and image-failure browsing, run npm test and diff checks.
Record actual outcomes in the verification report; do not weaken existing checks.
