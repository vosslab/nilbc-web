# Gamma SPEC review — blocked / not accepted yet

## Result

**Do not record SPEC acceptance from this review.** The real strict MkDocs build passed, but rendered-browser evidence could not be obtained in the allotted review window: the preview returned HTTP 404/empty documents while attempting to mount the `d-gamma` artifact under the required GitHub Pages prefix. Therefore I am **not** claiming the requested visual or interaction checks passed, and I am not asserting a specific visual defect based on the blank browser result.

## Verified

- Read `docs/DESIGN_BRIEF.md` and `docs/ASSETS.md`. The brief calls for a distinctive, polished, responsive, accessible, verified site, while leaving metaphor/layout open. Photos and real club work should be prominent and non-train builders welcomed.
- Built the real, shared-data configuration (no copied/fake config):
  `source source_me.sh && python3 -m mkdocs build --strict -f mkdocs_d_gamma.yml --site-dir output_checks/gamma_review/d-gamma`
  Result: exit 0; MkDocs reported “Documentation built” in 2.50s.
- Inspected `design_d_revised/site_src/index.md`: home content has the “Many interests. One club.” headline, hero Matchstick image, next-show block, curated show-photo section, five world cards, visitor/membership paths, and stats. Source order looks meaningful, but actual first-viewport visibility and image dominance remain unverified.
- Inspected `design_d_revised/theme/main.html`: gamma-only `.nb-atlas` wrapper is conditional on `extra.revision == gamma`; other revisions stay on the existing `super()` path. This is source inspection only, not alpha/beta browser regression evidence.

## Not exercised / acceptance evidence still needed

- 390×844 and 1440×1000 rendered screenshots for Home and representative Trains, Shows, Join, Timeline, and Standards pages; visual review of image-forward emphasis, differentiation beyond blue panels/photos, spacing, clipping/overlap, and reading order.
- Real image viewer journey: train count, open original, next/previous, Escape and restored focus; direct train navigation; desktop/mobile navigation and drawer.
- Timeline navigation and next-show link targets.
- Actual dark-scheme and reduced-motion rendering; no-JS navigation and direct image behavior.
- Sampled routes beyond the representative pages, browser console/network errors, and broader accessibility audit. No accessibility conformance claim is made.

## Evidence paths

- Real build output: `output_checks/gamma_review/d-gamma/`
- Review screenshot paths reserved: `output_checks/gamma_review/home-390.png`, `home-1440.png`; attempted captures were empty because the preview server returned 404, so they are **not valid visual evidence**.
- Source anchors: `design_d_revised/site_src/index.md`; `design_d_revised/theme/main.html`; gamma CSS: `design_d_revised/site_src/stylesheets/gamma.css` and `gamma-layout.css`.

## Follow-up

Retry with a correctly mounted static server rooted at `output_checks/gamma_review` and the requested `/nilbc-web/d-gamma/` prefix; confirm a 200 response and non-empty document before taking screenshots. Keep the remaining review scoped to the user's named routes and interactions. No runtime/source files were modified by this review.
