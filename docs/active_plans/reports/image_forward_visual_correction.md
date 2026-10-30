# Image-forward visual correction

## Result

Corrected the alpha/beta homepage hierarchy after tracing computed CSS. The original beta panel was blue because `home.css` used `.md-typeset .nb-hero` (specificity 0-2-0) while the beta rule `.nb-home-stage .nb-hero` (0-2-0) appeared earlier, allowing the legacy stylesheet order/cascade to win. The scoped `.md-typeset .nb-home-stage .nb-hero` override now wins and computes to `rgb(39, 104, 165)`. Alpha similarly overrides legacy hero padding and removes the repeated identity eyebrow while retaining announcement/header identity.

Homepage photos now precede the long-form intro. At 390 × 844, the first documentary photo begins at y=265 and occupies 356 × 267 px in both variants. Alpha uses a subdued three-card/catalog treatment; beta gives the desktop lead photo an expansive 16:10 magazine feature and shows one large 4:3 lead on phones, with supporting photos retained on desktop. Full image links/viewer behavior are unchanged. The slogan and shows/join actions remain in the page, but are below the first photo rather than in the first phone viewport; this is an intentional trade-off to meet the early-photo goal, and a visible conversion action is consequently not present in the initial phone screen.

## Verification

Strict independent builds passed:

```text
source source_me.sh && python3 -m mkdocs build --strict -f mkdocs_d_alpha.yml
Documentation built in 2.51 seconds
source source_me.sh && python3 -m mkdocs build --strict -f mkdocs_d_beta.yml
Documentation built in 2.54 seconds
```

A rendered Playwright check at 390, 1440, and 2560 verified zero horizontal overflow and recorded first-photo boxes:

| Variant | 390: y / size | 1440: y / size | 2560: y / size |
|---|---|---|---|
| Alpha | 265 / 356×267 | 325 / 374×281 | 390 / 449×337 |
| Beta | 265 / 356×267 | 325 / 1186×741 | 390 / 1424×890 |

Beta computed hero background was `rgb(39, 104, 165)`; alpha was white (`rgb(255, 255, 255)`). Mobile tests opened and closed the photo viewer, verified the Shows and Join CTA destinations, and opened the drawer and navigated to Shows in both variants. All passed. Vision review of alpha phone/desktop and beta phone/desktop confirms the photo-led presentation, legibility, and no visible clipping/overflow. On beta phone the slogan/actions are below the initial viewport; on alpha desktop the catalog precedes the slogan, so the slogan is visible lower on the page rather than leading the page.

Screenshot artifacts (390, 1440, 2560 each):

- `output_checks/image_forward_visual_correction/d-alpha-390.png`
- `output_checks/image_forward_visual_correction/d-alpha-1440.png`
- `output_checks/image_forward_visual_correction/d-alpha-2560.png`
- `output_checks/image_forward_visual_correction/d-beta-390.png`
- `output_checks/image_forward_visual_correction/d-beta-1440.png`
- `output_checks/image_forward_visual_correction/d-beta-2560.png`

The older temporary `image_forward_shared.mjs` probe is no longer structurally applicable: it asserts that photos live inside `.nb-home-stage`, whereas this correction intentionally puts the photo section before the stage. It was attempted and failed on that stale location assertion. Equivalent navigation, viewer, overflow, CTA, responsive-size, and strict-build checks were run against the corrected structure. No full npm test/combined build was run; no commits made.

## Files changed

- `design_d_revised/site_src/index.md`
- `design_d_revised/site_src/stylesheets/alpha-layout.css`
- `design_d_revised/site_src/stylesheets/beta-layout.css`
- `docs/active_plans/reports/image_forward_visual_correction.md`

No hooks, data, configs, theme, gamma/timeline files, other pages, permanent tests, or shared docs were changed.