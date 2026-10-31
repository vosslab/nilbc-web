# Presentation polish verification

Date: 2026-10-30.

## Visible changes

Alpha keeps its traditional two-column opening, with the next show directly below the
introduction and compact horizontal photo entries on phones. Beta now places the introduction
and next-show information above a balanced three-photo spread. Nunito replaces its playful
heading type throughout the site. Gamma uses a full-width poster opening, a staggered photo
strip, and its existing numbered exhibition navigation. Shared featured captions use the short
subject description; linked show labels retain venue and date, and credits remain visible.

The cascade changes are in `alpha-layout.css`, `beta-layout.css`, and `gamma-layout.css` under
`design_d_revised/site_src/stylesheets/`. Shared markup and gallery behavior remain in the
existing hooks. Beta's secondary button explicitly uses the theme link color on its new light
surface; the light and dark captures were inspected after that correction.

## Repository photo organization

[README.md](../../photos/README.md) leads to six theme sheets, seven ordered show albums,
a measured asset inventory, and a folder-by-folder archive review summary. The catalog covers
73 website selections and links existing thumbnails, full derivatives, and 52 preserved
archive originals. The review summary exposes the recorded coverage of 1,336 image references,
72 contact sheets, and 32 folders without importing the external archive or its raw metadata.

[build_photo_catalog.py](../../../devel/build_photo_catalog.py) generates the catalog from
existing manifests, image files, and committed review evidence. It rejects duplicate IDs,
unknown themes/shows, missing assets, and inconsistent album sequences. `--check` detects stale
outputs. Event dates, capture dates, crop focus, dimensions, sizes, and hashes remain distinct.
No new photographs were selected and no image bytes changed in this pass.

## Verification

- Strict combined build of the landing page and all seven variants passed.
- The full browser smoke check passed 172 desktop/mobile page checks and 25 journeys.
- A focused rendered probe passed 54 route/width/scheme checks: home, trains, and timeline;
  alpha/beta/gamma; 390, 768, and 1440 pixels; light and dark. No horizontal overflow or
  broken images. Computed grid columns and heading font families were recorded.
- Fresh screenshots are in `output_checks/polish/`; the focused probe and JSON report remain
  local verification artifacts. Desktop and phone captures were visually inspected, including
  dark Beta and tablet Gamma. Reduced motion was enabled for this probe.
- Catalog/link checks passed 132 tests. Scoped content/guidance checks passed 143 tests
  before adding the archive review index.
- Final broad Python run: 1,869 passed, four failures in unchanged files. The failures are
  the XML parser Bandit finding and executable-bit check in `devel/index_archive_metadata.py`,
  plus typing and support-directory import checks in `tests/test_archive_metadata.py`.
  Those files have no diff from the starting commit. The host Podman disk-budget check was
  excluded; it is unrelated to this website pass.
- The broad suite's ASCII fixer rewrote historical reports. Those incidental rewrites were
  restored to their starting bytes and are not included in this change.
- `git diff --check` passed. Original A-D sources/configurations are unchanged.

No deployment or commit was performed. Verification uses Chromium, not a new cross-browser
or screen-reader audit. No new numerical contrast audit was performed.
