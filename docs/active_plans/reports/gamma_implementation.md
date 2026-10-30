# Gamma implementation report

## Result

Implemented the gamma-only **working atlas** direction: task-specific visual compositions for
Home, events and visiting, albums/logbook, Join/Standards, About/history, Matchstick/credits,
and all five collections. It preserves Material navigation/search, shared content, and the
existing photo viewer. Gamma-only wrapping uses `extra.revision: gamma`; inherited alpha/beta
remain on the original content branch.

## Changed files

- `mkdocs_d_gamma.yml`
- `design_d_revised/theme/main.html`
- `design_d_revised/site_src/stylesheets/gamma.css`
- `design_d_revised/site_src/stylesheets/gamma-layout.css`
- `docs/active_plans/reports/gamma_direction.md`
- `docs/active_plans/reports/gamma_implementation.md`
- `docs/DESIGN_DECISIONS.md`
- `docs/CHANGELOG.md`

Temporary probes, isolated manifest/hook copies, build output, and screenshots are under ignored
`output_checks/`. No shared hook, Markdown, manifest, photos, alpha/beta config/styles, timeline
source/style, permanent smoke, original A-D, or deployed output were edited here.

## Verification evidence

- Strict isolated build passed repeatedly:
  `source source_me.sh && python3 -m mkdocs build --strict -f output_checks/mkdocs_gamma_probe.yml`.
  The probe config points to a temporary hook/manifest copy because the concurrent shared
  manifest currently lacks required `homepage_photos` and show `event_date` entries. Its
  temporary records use the already documented homepage image IDs and show labels; no shared
  data was altered.
- Browser probe passed: `node output_checks/gamma_probe.mjs` reported **3 homepage widths, 15
  phone routes, 15 train photos, viewer Escape/close, direct-image link with JavaScript disabled,
  no horizontal overflow, and no page errors**.
- A subsequent enhancement to the probe that scrolls every image before every full-page capture
  timed out at 420 seconds. Do not count that rerun as passed. A separate real-browser check
  decoded all three homepage show images and produced
  `output_checks/gamma_screenshots/home-390-final.png`; the visual inspection confirmed all
  images loaded and found no urgent mobile defect.
- Earlier screenshot paths: `output_checks/gamma_screenshots/home-390.png`,
  `home-1440.png`, `home-2560.png`, and `phone-<route>.png`. Their full-page captures may show
  blank lazy thumbnails because the probe originally decoded only viewport images. The 1440px
  and 2560px homepage compositions and 390px homepage cards were inspected. Mobile world cards
  were corrected from a collapsed grid to a readable single-column stack. Desktop gallery/card
  overlap was corrected with explicit grid placement and content-sized figures.
- `node --check output_checks/gamma_probe.mjs`, Python `compileall` for the temporary probe files,
  and `git diff --check` for gamma-owned and documentation files passed.

## Remaining integration and review boundary

1. The shared `data_blocks.py` now requires non-empty `homepage_photos` and verified show
   `event_date`; the shared `photos.yml`/`photo_shows.yml` visible during this work did not yet
   provide those fields. Manager must rerun the **real** `mkdocs_d_gamma.yml` strict build once
   that concurrent data contract lands. Do not merge the probe-only config or temporary data.
2. Full-phone visual inspection was sampled on Home, Visiting, Join, and Trains. The broader
   route probe exercised 15 mobile routes, but the automated screenshot-capture rerun timed out;
   therefore every route's screenshot is not claimed as inspected. Parent should independently
   review the actual artifact and decide whether to dispatch focused fixes.
3. At very wide desktop the hero mascot is suppressed to protect the content/buttons; the club
   identity remains in the header logo. Reduced-motion, dark styling, keyboard focus, and native
   controls have CSS/source coverage, but no complete accessibility audit was performed.
4. No commits, push, deployment, shared rebuild, or full project smoke test were run.

Manager next steps: integrate the shared manifest contract; run the real gamma strict build;
inspect the actual screenshots/artifact independently; coordinate full smoke only after concurrent
builds stop cleaning outputs.
