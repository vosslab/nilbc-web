# Image-forward accessibility audit

## Scope and method

Audited the actual generated `output_site/d-alpha`, `d-beta`, and `d-gamma` pages through a local HTTP server at `http://127.0.0.1:8765/{design}/`. The build artifacts were not rebuilt or edited. Injected isolated axe-core 4.10.3 into Chromium with Playwright and ran WCAG 2.0/2.1 A/AA rules on Home, Trains, Shows, Join, and Timeline at 390px and 1440px (30 light-mode page/viewport runs), plus Home, Trains, and Join at 1440px with dark color scheme (9 runs). Total: 39 real-browser axe runs. Rule results and node-level details are in ignored `output_checks/a11y_audit_raw.json`; runner/dependency are under ignored `output_checks/a11y_tools/`.

Command: `node output_checks/a11y_tools/audit.cjs` -> exit 0; 39 runs. Axe findings were deduplicated conceptually below by rule and common selector. Axe has no violations on 36/39 runs; three runs report `color-contrast` violations. This is not a clean audit: contrast checks are incomplete where overlays, gradients, or pseudo-elements defeat automated background resolution, and those remain review items, not passes.

## Actionable failures

| Priority | Variant / state and exact selector | Rule / impact | Measured evidence | Recommended follow-up |
| --- | --- | --- | --- | --- |
| P1 | Gamma, dark, Home/Trains/Join: `.md-header__topic:nth-child(1) > .md-ellipsis` | `color-contrast`, serious | `#fffdf7` on `#e8edf0`, 1.15:1; 18px bold; expected 4.5:1 | Correct gamma dark palette tokens so header text is on its intended dark surface. The sampled computed background is near-white despite dark color scheme. |
| P1 | Gamma, dark, Join: `.md-button` | `color-contrast`, serious | `#fff` on `#ff978c`, 2.08:1; 17.2px normal; expected 4.5:1 | Dark-state button foreground/background pair needs sufficient contrast. |
| P1 | Gamma, dark, Home: `.md-button[href$="join/"]` | `color-contrast`, serious | `#fff` on `#e8edf0`, 1.17:1; 16px normal; expected 4.5:1 | Same primary CTA must use a button fill that contrasts with white text in dark mode. |
| P1 | Gamma, dark, Home: `.nb-hero__eyebrow`, `em` | `color-contrast`, serious | `#f3cd77` on `#e8edf0`, 1.28:1; eyebrow 14px normal (4.5:1 required), emphasis 54.72px bold (3:1 required) | Restore a dark hero background or choose foreground colors suited to the rendered surface. |
| P1 | Gamma, dark, all three sampled pages: `.md-search__input` | `color-contrast`, serious | `#fff` on `#acafb2`, 2.2:1; 16px normal; expected 4.5:1 | Dark-mode search input surface/text pair fails. |
| P1 | Gamma, dark, Trains/Join: `.md-footer__link--prev > .md-footer__title > .md-footer__direction`, `.md-footer__link--prev > .md-footer__title > .md-ellipsis`, corresponding `--next` selectors | `color-contrast`, serious | direction `#fcfbf6` on `#e9eef1`, 1.12:1; title `#fffdf7` on `#e9eef1`, 1.14:1; expected 4.5:1 | Correct footer navigation text/surface in dark mode. |
| P1 | Gamma, dark, all three sampled pages: `.md-copyright__highlight` | `color-contrast`, serious | `#d5dce8` on `#e8edf0`, 1.16:1; 14.4px normal; expected 4.5:1 | Correct copyright foreground or rendered footer surface. |

Counts: Home has six distinct failing nodes; Trains has seven; Join has eight. The common gamma header/search/copyright findings reproduce across all three dark page types. All six or eight are the same `color-contrast` rule, not separate rule IDs.

## Automated contrast items requiring human review

Axe marks `color-contrast` incomplete, not passed, when it cannot resolve a background. The actual results include:

- Gradient-backed hero text and CTA, including `#many-interests-one-club`, `em`, `.nb-hero__lede`, `.md-button[href$="join/"]`, and `.nb-hero__meet`; reported `bgGradient`, so no numeric ratio is established.
- Pseudo-element overlays on caption/date treatments: `.nb-photo__world`, `.nb-photo__show`, `.nb-photo__credit`; on Shows, `.nb-show__date[aria-hidden="true"] > .nb-show__month`, `... > .nb-show__days`, and `... > .nb-show__year` (repeated for the three show entries). Axe cannot determine background due to `pseudoContent`.
- Pseudo-element card/link treatments, including `.nb-step-link[href$="visiting/"]`, `.nb-step-link[href$="creations/"]`, `.nb-step-link[href$="join/"]`, and Gamma train collection links `#trains > a[href$="trains/"]`, `#cities-and-landmarks > a[href$="cities/"]`, `#screen-and-story > a[href$="screen/"]`, `#castles > a[href$="castles/"]`, `#creatures-and-characters > a[href$="creatures/"]`; Gamma `.nb-world-card--lime > p` is also incomplete.
- Page-hero title/kicker on Shows and Join and active tab on Gamma Join are incomplete because their backgrounds involve pseudo-elements.

The full run-level selector list and expected thresholds are recorded in `output_checks/a11y_audit_raw.json`. Review rendered color at representative pixels/states or simplify the overlay treatment so a measurement can be made; do not count these as green.

## Navigation and keyboard spot check

At 390px, all variants expose the intended primary page links in the rendered navigation (`Home`, `Shows`, `Worlds we build`, `Join`, `About`) and keyboard focus is visible on sequentially focused links (computed outline: solid, 3px). The Material mobile-menu affordance is a `<label for="__drawer">` containing only an SVG, rather than a button with a programmatic name; axe did not flag it. The menu icon is a label for `#__drawer` with no `tabindex` (and no accessible name). It is skipped by native sequential Tab focus; making it focusable only through temporary DOM instrumentation allowed Enter to toggle the checkbox, but that does not establish the shipped control as keyboard operable. Treat keyboard menu activation as unresolved and fix/verify in a follow-up. The desktop nav is rendered as links, not menu buttons; no unnamed primary-nav buttons were found.

## Fix order

1. Correct Gamma dark-mode surface/palette mapping first; it creates the highest-severity failures across the header, hero, search, CTA, footer, and copyright.
2. Re-run the same dark-mode three-page axe matrix and verify each measured ratio meets its threshold.
3. Resolve or manually measure gradient and pseudo-element contrast for shared captions, date badges, hero, and card/link styles across all variants.
4. Verify the mobile drawer opens and closes with keyboard activation, has an accessible name/state, and retains visible focus.

## Limits

This is an automated browser audit plus a targeted navigation/focus spot check, not full assistive-technology testing. No source, configuration, stylesheet, suite, or package manifest was changed. Axe does not assess all WCAG criteria, and no claim of full WCAG conformance is made.
