# Archive image verification

## Executed checks

- `npm test -- --capture`: PASS, all eight strict builds, 130 desktop/mobile page checks,
  21 integration journeys, zero reported errors. Final successful run followed the category
  heading-permalink fix; log: `/home/vosslab/.hermes/cache/scratch/nilbc_npm_test.log`.
- Focused live Chromium probe: PASS, 12 cases across alpha/beta/gamma. Nine cases use
  390/1440/2560-pixel widths; three use JavaScript disabled and all images blocked.
  Evidence: `output_checks/archive_images_report.json` and `output_checks/screenshots/`.
- All 1,336 full archive files rehashed against the catalog; all 34 pagination records end
  in an empty page. Three selected source hashes and six derivative hashes/dimensions pass;
  derivatives contain no EXIF metadata and total 896,414 bytes.
- `git diff --check`: PASS. Original A/B/C/D directories and configurations match HEAD.
- `source source_me.sh && python3 -m pytest tests/ -q`: 1,438 passed, one host-environment
  failure: Podman storage is 35.23 GB against a 20 GB budget. No Podman resources changed.
- Focused documentation/whitespace checks: 261 passed. The suite auto-trimmed whitespace in
  an unrelated historical wording report; that incidental edit was restored byte-for-byte.

## Live control evidence

| Control | Status | Observed result |
| --- | --- | --- |
| Castles category card | Live-proven | Click reaches creations/#castles in each revision at all three widths. |
| Castle gallery photograph | Live-proven | Opens full local WebP in the image dialog. |
| Escape | Live-proven | Closes the image dialog. |
| Image-free, JavaScript-free Castles link | Live-proven | Still reaches the correct creation section in all revisions. |
| Menus, search, existing viewers | Live-proven by existing suite | 21 integration journeys pass. |
| Discord links | Not exercised in public browser | Access-restricted provenance links, not a visitor dependency. |

The first focused click probe exposed invisible heading permalinks intercepting the category
card link. The shared stylesheet now hides these redundant permalinks within the category row.
The corrected probe passed without forced clicks. No original proposal stylesheet changed.

## Visual evidence

Inspected actual rendered beta 1440-pixel, gamma 390-pixel, and alpha 2560-pixel category
screenshots. Text, card boundaries, and responsive layout are intact. The castle image reads
as a medieval scene detail rather than a whole fortress; full-frame gallery viewing retains
its battlements and animal yard. This is accurately described in the caption.
The existing compact mobile gamma panels and restrained alpha tinting remain unchanged.

## Boundaries

The first browser run required installing declared Node dependencies. One subsequent search
journey timed out; the next two complete runs passed without changing search or its assertions.
This is reported as observed instability, not a proven repaired search bug. No remote deployment,
Discord write, or commit occurred. Copyright is not inferred from access: uploader attribution
and owner-requested demo use do not establish a general external reuse license.
