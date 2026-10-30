# Gamma overview gallery fix

Removed the gamma creations-index rule that hid `.nb-gallery:not(.nb-collection)`. The retained club photos now occupy a full-width row beneath their existing world heading/link, constrained to the world section width; compact overview links remain unchanged.

Verification (2026-10-30): strict gamma-only MkDocs build passed to `output_checks/gamma_gallery_fix/d-gamma`. Served the build parent with the existing `serveBuild(absolutePath)` helper and tested `/nilbc-web/d-gamma/creations/` in Chromium at 390px and 1440px. At both widths the first photo was visible and clickable, the viewer loaded the linked original `club_group_2026.webp`, Escape closed the viewer and restored focus to the opener, and document width equaled viewport width (no horizontal overflow). No screenshots saved.
