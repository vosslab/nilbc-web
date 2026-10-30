# Gamma featured-photo visibility fix

## Scope and change

- Changed only `design_d_revised/site_src/stylesheets/gamma-layout.css` and this report.
- Removed the homepage rule hiding every featured `.nb-photo` after the first. All curated figures and their existing viewer links now render. Desktop keeps the first image full-width in the photo column and the other links in a compact two-column row.
- At phone widths (<=60em), the lead remains full-width and the other two links share a compact thumbnail row; supporting captions are visually suppressed while links retain image alt text and viewer attribution. No gallery JavaScript or source data changed.

## Verification

- Gamma-only strict MkDocs build succeeded: `source source_me.sh && python3 -m mkdocs build --strict -f mkdocs_d_gamma.yml --site-dir output_checks/gamma_featured_fix/d-gamma` (exit 0).
- Inline Node/Playwright probe served that exact build with repository `serveBuild()` and closed browser/server in `finally`.
- At 390px: 3/3 links visible; boxes 332×120, 67.19×105, 67.19×105; `scrollWidth=390`; PASS.
- At 1440px: lead 549.94×412.45; secondaries 268.97×201.72 each; `scrollWidth=1440`; all 3 links visible and >=44×44; PASS.
- At 2560px: lead 660.36×495.27; secondaries 323.17×242.38 and 323.19×242.39; `scrollWidth=2560`; all 3 visible and >=44×44; PASS.
- At 1440px, clicked lead and pressed Next twice; viewer hrefs matched all three decoded featured hrefs in sequence. Escape closed viewer and restored focus to lead link. PASS.
- Screenshot `output_checks/gamma_featured_fix/home-1440.png` was captured after the correction. Visual image inspection was attempted but the image-analysis request failed with a connection error; the browser geometry confirms full-span lead and side-by-side secondaries.


