# D revision and flyer completion

## Delivered

D&alpha;, D&beta;, and D&gamma; use the same revised source with three visual treatments.
Alpha is conservative; beta emphasizes photographs; gamma adds poster lettering, offset frames,
colored brick statistics, and a miniature exhibition composition. They retain
D's light/dark controls, mascot, card edges, and baseplate. Their original A-D reference sites
are unchanged. All 166 original runtime/config files were compared with HEAD byte for byte.

The [wording review](D_REVISIONS_WORDING.md) shows every Markdown change from D. The humanizer
pass retained specific club details and the requested slogan. A's guitar feature, B's slogan and
visitor invitation, and C's clear membership checklist informed the revised content.

The editable flyer master and export instructions are in [../../../marketing/README.md](../../../marketing/README.md).
`npm run flyer` exports the master to `output/pdf/nilbc_club_flyer.pdf` and a PNG preview.
The inspected PDF render is `output/pdf/nilbc_club_flyer.webp`.

## Evidence

- Eight strict MkDocs builds pass, including the three revision configurations.
- `node tests/playwright/designs_smoke.mjs --capture`: 130 page checks and 21 interaction
  journeys pass. The checked routes include every design at desktop and phone widths.
- Eight one-time combinations of variant, width (1440/390), and light/dark preference pass:
  matching homepage text, intended background patterns, no string lights, and visible keyboard
  focus. Results are in `output_checks/revisions/acceptance.json`.
- Both variants' theme controls switch and persist on reload. Browser screenshots are in
  `output_checks/screenshots/`; inner-page captures are in `output_checks/revisions/`.
- Visual review of joining instructions caught unsupported nested lists in the steps layout.
  The final source uses a plain six-item checklist. A fresh browser check verifies each item,
  matching text across variants, and the absence of step numbering; final phone captures were
  inspected. Earlier desktop joining captures predate this markup correction.
- `source source_me.sh && python3 -m pytest tests/ -q`: 1,213 checks passed before final docs.
  The October 26 in-memory discovery run passed 1,421 checks, including new files, without staging
  or changing Git.
- PDF inspection: one US Letter page, 612 by 792 points; Barlow Condensed Bold and DM Sans
  Regular/Bold embedded as subsets; expected text extracts; QR decodes from the rasterized PDF
  to `https://niltc.org/`. SVG XML, unique IDs, embedded references, and text margins pass.
- The website and flyer exports use existing dependencies. The machine's `inkscape` command is
  a stub; Chromium exports the SVG directly so the master remains the only layout authority.

## Limits

The preview and evidence are local. No commit, push, or remote deployment was performed.
Phone checks use Chromium viewport emulation. Real-device Safari and a physical print proof
are optional follow-up checks, not gates for completing this local demo and flyer task.
The SVG logo is approved raster artwork; its other visible elements and typography are vectors.

## 2026-10-27 refinement evidence

- Shared copy is shorter and no longer implies non-train builders were previously unwelcome.
  On phones, the slogan and actions precede a smaller Matchstick illustration.
- Twenty-four variant/viewport/scheme checks cover 320, 390, 768, and 1440 pixels in both
  color schemes. All have matching main content, visible keyboard focus, and no page overflow.
- Gamma hover straightens photo cards; enlarged text retains a usable page width. Screenshots
  include gamma's shows, joining, and creations pages. Reduced motion suppresses entrance effects.
- New dark-text/yellow and dark-text/tan pairs measure 12.86:1 and 10.32:1 respectively;
  existing hero white/blue pairs also exceed 4.5:1. Exact measured results are in
  `output_checks/three/contrast.json`.
- Screenshots are in `output_checks/three/` with variant, width, and scheme in each filename.
  Compare matching widths and schemes. Responsive evidence is in `checks.json`.
- The flyer is unchanged. No new dependency or content copy was introduced for gamma.

- Final October 27 verification: eight strict builds, 130 browser page checks, 21 interaction
  journeys, 24 responsive combinations, and 1,428 repository checks passed. Original A-D's
  166 runtime/config files still match HEAD. Plan-specific temporary probes were removed.
- Fixed the inherited reduced-motion mascot delay and added a permanent browser assertion
  that the revised mascot has no entrance animation when reduced motion is requested.
- Source references: the local `MARKDOWN_BOOKS/css-creative/Unleashing_the_Power_of_CSS-2023.md`
  responsive-spacing discussion informed compact layouts; `CSS_in_Depth_Second_Edition-2024.md`
  informed keeping variant overrides last. The existing component CSS remains the implementation
  owner; no book examples or external stylesheets were copied into the site.

## Selective photo treatments

Beta and gamma use selected paper frames and live Kalam handwritten notes. Gamma adds
wood-style frames to Paris and the museum, a CSS feather mask on the jet photograph, and
an isolated frog derivative. Original-photo links and credits remain. Alpha retains simple borders.
The owner confirmed that older archive photographs belong alongside newer Instagram material.

Verification passed eight strict builds, 130 browser pages, 21 interaction journeys, and
12 photo-treatment combinations across variants, phone/desktop, and light/dark modes.
The cutout's original-image dialog is covered by the permanent browser check. Typography,
visibility, overflow, and treatment screenshots were checked with a temporary probe, then
removed. Repository checks passed 1,437 tests. Evidence is in `output_checks/frames/`.

The original frog and Unikitty u2net attempts were rejected after visual inspection. The accepted
frog uses rembg's isnet-general-use mask with ImageMagick alpha cleanup and front-foot restoration
from the original photograph. No rembg dependency was added to the website build.

## Autonomous closeout

The local demo and flyer scope is complete; no milestone requires a human response.
Existing automated build, browser, and PDF checks supply the acceptance evidence above.
Publication is outside this local closeout scope.

Twelve fresh gallery checks verified the final descriptive frog caption, no horizontal
overflow, and variant-specific cutout visibility across all three revisions, both color
schemes, and 390/1440-pixel widths. Frog screenshots now reflect the final caption;
results are in `output_checks/frames/final-caption-checks.json`.

## Pre-sharing refinements

The subsequent review shortened gamma's mobile category photo panels to 7rem and placed
beta first on the comparison page, with restrained alpha and playful gamma alternatives.
Eight strict builds, 130 page checks, and 21 interaction journeys pass. A focused check at
320, 390, 704, 768, and 1440 pixels confirms the mobile height and absence of horizontal
overflow. Refreshed homepage screenshots are in `output_checks/screenshots/`; the phone
render was visually inspected.

The requested castle photograph is still blocked on a verified club source. Local assets,
earlier Instagram records, and the public castle standards page did not provide one. The
diagram remains in place, and a source URL was requested. The other refinements are complete.
