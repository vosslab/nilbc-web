# Browser smoke repair

## Change

Removed the malformed duplicate drawer setup fragments from
`tests/playwright/designs_smoke.mjs`. The previous fragments injected drawer
behavior into the page under test, so the assertions did not exercise the
shipped JavaScript. The smoke test now checks the page's own drawer role,
accessible name, `aria-controls`, expanded state, keyboard operation, focus,
and desktop tab order. It checks the real checkbox state after keyboard and
pointer actions.

Removed the assertion that equated `.md-nav--primary.isVisible()` with the
drawer checkbox state. Playwright visibility only reports whether an element
is rendered; it does not report whether Material's navigation drawer is open.
The test keeps direct checkbox and `aria-expanded` state checks and separately
follows the drawer link to the Shows route.

## Verification

- `node --check tests/playwright/designs_smoke.mjs` passed.
- `npm test -- --capture` rebuilt all seven sites and crawled routes through
  D-gamma. The first run stopped at the invalid visibility assertion.
- After removing that assertion, the live d-alpha check failed at the Enter
  assertion: `aria-expanded` remained `false` after pressing Enter. The page
  was not modified by the test. Runtime repair and a final suite rerun are
  pending.

## Search diagnosis and test repair

The later combined run reached all 172 desktop/mobile page checks and 17
journeys, then timed out awaiting a search result. The old readiness predicate
also passed when the metadata element was absent, because `undefined` differs
from `Initializing search`.

The shipped Material bundle's source map identifies the triggering behavior in
`components/search/query/index.ts`: search observes worker readiness, `keyup`,
and focus events. It does not observe the `input` event emitted by Playwright's
`fill()`. A fill after worker readiness can therefore leave its text unqueried.

The test now clicks the visible Search field, waits for the actual
`Type to start searching` state, and enters `Bensenville` with
`pressSequentially()`. This generates real keyboard events and retains the
visible-result click and same-design Shows navigation assertion. No page state,
search results, or shipped scripts are injected or replaced.

A bounded isolated browser check passed this exact user sequence for original
C and D plus alpha, beta, and gamma. All five searches opened the Shows route
under their own `/nilbc-web/<design>/` prefixes. The D results retain their
normal `?h=bensenville` highlighting query. Syntax verification with
`node --check tests/playwright/designs_smoke.mjs` also passed.

## Final combined browser result

`node tests/playwright/designs_smoke.mjs --capture` exited successfully:

```text
PASS: 172 desktop/mobile page checks; 25 integration journeys.
```

The run used the manager's completed combined build, without rebuilding or
changing shipped source. It covered all seven designs, local references and
anchors, mobile menus/drawers, alpha's keyboard drawer contract, viewer and album
journeys, and all five searchable designs. The downstream image-forward checks
also passed for each revision at 390 and 1440 pixels: homepage-to-Trains
navigation, advertised/rendered photo count, thumbnail-only initial requests,
selected-original viewer loading, previous/next navigation, focus return, and
the Our story timeline route with local photographs. Dark-mode persistence and
switching back also passed for every revision.

The terminal report is `output_checks/designs_report.json`; it contains 172
page records, 25 journey records, an empty browser/resource error list, and no
failure. Homepage and dark-mode screenshots were refreshed in
`output_checks/screenshots/`. No test expectations were removed or weakened to
pass search, collection, or timeline behavior.
