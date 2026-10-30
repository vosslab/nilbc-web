# Gamma contrast repair

## Change

Introduced separate structural surface and foreground tokens in `design_d_revised/site_src/stylesheets/gamma.css`: `--gamma-structure` / `--gamma-on-structure`. In slate mode the structure is `#101b22` and foreground `#f4f7f8`; the inverted slate `--gamma-ink` remains reserved for semantic text/surface roles and no longer supplies the header, hero, footer, and collection-count background. Search/header/footer Material tokens are explicitly aligned with that dark structure. Gamma-specific join buttons use a deep red in slate rather than the light-mode accent. `gamma-layout.css` edits are color declarations only; mosaic geometry is untouched.

## Measured pairs

Ratios use WCAG 2.x relative luminance; 4.5:1 is required for normal text and 3:1 for large text. Source audit baseline values are recorded in `image_forward_accessibility.md` and `output_checks/a11y_audit_raw.json`.

| Target | Before (dark) | After (dark) | Result |
| --- | --- | --- | --- |
| Header title/search foreground | `#fffdf7` on computed `#e8edf0`, 1.15:1 | `#f4f7f8` on `#101b22`, 16.23:1 | Pass |
| Hero eyebrow | `#f3cd77` on `#e8edf0`, 1.28:1 | `#f3cd77` on `#101b22`, 11.49:1 | Pass |
| Primary join CTA | `#fff` on `#ff978c`, 2.08:1 | `#fff` on `#77160f`, 10.1:1 | Pass |
| Footer text/link | `#fffdf7` on computed light `#e8edf0`, 1.12:1 | `#f4f7f8` on `#101b22`, 16.23:1 | Pass |
| Collection count | inherited slate inversion could pair light foreground/light surface | `#f4f7f8` on `#101b22`, 16.23:1 | Pass |
| Hero large title | foreground inherited `#203542` on `#e8edf0` (1.35:1) | `#f4f7f8` on `#101b22`, 16.23:1 | Pass |

Ratios above are computed from the measured pair colors. Automated run output: `output_checks/gamma_contrast/axe_results.json`; focused rendered computed-style probe confirmed header background `rgb(16, 27, 34)`, hero background `rgb(16, 27, 34)`, footer background `rgb(16, 27, 34)`, and hero eyebrow `rgb(243, 205, 119)`.

## Verification

Built only Gamma to `output_checks/gamma_contrast/d-gamma` using `source source_me.sh && python3 -m mkdocs build -f mkdocs_d_gamma.yml --site-dir output_checks/gamma_contrast/d-gamma`. Served at the existing inline-prefix test base (`http://127.0.0.1:8765/`, also supporting `/nilbc-web/`). Axe WCAG 2.1 A/AA audit: Home, Trains, Join, light and dark at 1440px: **0 violations in all six runs**. Mobile Home at 390px, light and dark: **0 violations in both runs**. Remaining color-contrast results marked incomplete by axe are unresolved pseudo-element/image-overlay checks on the home mosaic/world cards; they are not counted as passes. The dark-mode representative computed backgrounds were inspected directly; patterned photo captions remain manual-review items because their image/pseudo-element backgrounds are not determinable via computed solid color.

No theme was disabled. No templates, typography, shared CSS, original design A–D, or mosaic grid geometry were changed.
