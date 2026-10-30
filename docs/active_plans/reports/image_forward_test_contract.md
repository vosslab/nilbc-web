# Image-forward browser test contract

This report records permanent browser acceptance for the D revisions. The tests run against the
built static artifact served over the repository's loopback helper; they do not make appearance,
font, geometry, or fixed photo-count assumptions.

## Retained browser contracts

`tests/playwright/designs_smoke.mjs` keeps all pre-existing A-D route crawling, original D gallery
journey, responsive overflow, navigation, search, and existing revision show-gallery keyboard
checks. The image-forward journey is limited to D-alpha, D-beta, and D-gamma:

- Homepage `Trains` links navigate directly to `/creations/trains/`.
- The selected `trains` collection's rendered photo count equals its displayed count. The assertion
  reads the output instead of requiring a fixed count.
- Collection and homepage images use thumbnail WebP URLs distinct from each linked image. A fresh
  context records requests before navigation, verifies no collection original is requested before
  selection, then verifies the selected original is requested and decoded in the dialog.
- The dialog's Next/Previous buttons change and restore the selected image, Escape closes it, and
  focus returns to its opener. Each collection interaction runs at 390px and 1440px; no styling
  treatment is asserted.
- The About navigation's `Our story` link reaches `/about/timeline/`; timeline images are local
  and their URLs return HTTP 200.

Selectors are tied to the intended shared contracts: `.nb-home-stage`, `.nb-home-photos`,
`.nb-gallery.nb-collection`, `.nb-photo__link`, `.nb-lightbox`, and the named About navigation
link. The theme's style treatment and the number of selected photos remain free to evolve. Timeline
chronology is produced at build time from `event_date`; the browser does not reimplement sorting.
The D-gamma frog journey follows the ordinary thumbnail on `/creations/creatures/` to `frog.webp`;
it does not require a cutout to be visible.

## Existing-design coverage

The original D creations journey stays on `/creations/`. It is not redirected to the new train
collection. A, B, C, original D, and the existing theme, album, search, navigation, route, and asset
checks remain unchanged in scope.

## Execution and status

Run the integrated acceptance after owners finish and the manager rebuilds all outputs:

```bash
npm test
```

The previously reported `npm test` attempt was an unauthorized reviewer run with a 30-second timeout; it is excluded from acceptance evidence. During this scoped review, `npm test` was also attempted once, triggered the canonical pretest build, then timed out after 40 seconds while the Playwright crawl was navigating to D-alpha About (`net::ERR_ABORTED`); it is incomplete and is not acceptance evidence. No integrated GREEN is claimed. A focused browser run was not completed against a coherent current alpha build because the canonical pretest rebuild was interrupted by the timeout. Any final integrated rebuild/test must be run after shared runtime edits are complete. No-JavaScript fallback and unavailable-image
failure paths are not duplicated as another permanent framework: the established `href` fallback
remains a temporary acceptance check if needed.
