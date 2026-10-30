# Install, preview, and publish

The repository contains four original proposals, three revisions of D, and a comparison landing page.
See [DESIGNS.md](DESIGNS.md) for the A/B/C/D mapping and source boundaries.

## Install

Use Bash and Python 3.12 on macOS or Python 3.13 on Debian:

```bash
source source_me.sh && python3 -m pip install -r pip_requirements.txt
```

All website assets are local. Builds do not download assets or read `OTHER_REPOS/`.

## Build all designs

```bash
source source_me.sh && python3 build_sites.py
```

This strictly builds the landing page first, followed by all seven designs, into `output_site/`.
Do not run the root `mkdocs build` afterward: its clean step removes the child outputs.
A single design's build cleans only that design's output.

Preview the complete voting site:

```bash
source source_me.sh && python3 -m http.server 8000 --bind 127.0.0.1 --directory output_site
```

Open [the comparison homepage](http://127.0.0.1:8000/), then choose an original design or a D revision.
This static server previews the root mount; the browser check below also exercises the actual
GitHub Pages project prefix, including design-specific 404 pages.

## Preview one design

Run commands from this repository's root. Substitute `b`, `c`, or `d` for `a`:

```bash
source source_me.sh && python3 -m mkdocs serve --strict -f mkdocs_a.yml
```

Open [Design A](http://127.0.0.1:8000/nilbc-web/a/). The other configurations serve at
`/nilbc-web/b/`, `/nilbc-web/c/`, and `/nilbc-web/d/`.
For simultaneous previews, add a different `--dev-addr 127.0.0.1:8001` port to each command.

Build a design independently:

```bash
source source_me.sh && python3 -m mkdocs build --strict -f mkdocs_a.yml
```

Each design retains its own editing model. Edit the corresponding `design_*/` directory;
the original competition entries in `OTHER_REPOS/` remain untouched.

## Verify the integration

Node 22.12 or newer is needed only for browser verification:

```bash
npm ci
npx playwright install chromium --only-shell
npm test
```

`npm test` rebuilds all eight sites, then checks every generated HTML route at desktop and
phone widths, local links and assets, prefix isolation, mobile menus, image viewers,
and search in every design that provides them. Any failure must be resolved before publishing the artifact.
Results go to ignored `output_checks/designs_report.json`.

To capture all seven homepages at desktop and phone widths:

```bash
npm test -- --capture
```

Screenshots go to ignored `output_checks/screenshots/`; no original screenshots are overwritten.
If the machine uses a custom Playwright cache, set its standard `PLAYWRIGHT_BROWSERS_PATH`
variable when installing and running Chromium. On Linux, `--with-deps` also installs required
browser libraries.

The existing repository checks remain separate:

```bash
source source_me.sh && python3 -m pytest tests/
```

## GitHub Pages

[deploy-pages.yml](../.github/workflows/deploy-pages.yml) builds and publishes one combined artifact on a push
to `main` or a manual workflow run. Set the repository's Pages source to **GitHub Actions**.
This is a one-time setting in [Settings > Pages](https://github.com/vosslab/nilbc-web/settings/pages).
Every subsequent push to `main` builds, checks, and publishes all seven designs automatically;
no local combined build is required. Continue using `mkdocs serve -f mkdocs_a.yml` (or b, c, d)
for live local development. Local build and test commands do not publish anything.

If the setup check reports that Pages is not enabled, select **GitHub Actions** in that setting
and rerun the workflow. The workflow uses GitHub's built-in token; no personal token is needed.

The configured landing URL is `https://vosslab.github.io/nilbc-web/`.
Designs live at that URL followed by `a/`, `b/`, `c/`, or `d/`.
The revisions live at `d-alpha/`, `d-beta/`, and `d-gamma/` under that same URL.
If the deployment address changes, update `site_url` in all eight root configurations.
Keep each design's final path segment.

Publish the complete `output_site/` directory. Do not deploy a design's output on its own.
The entries retain their original demo content and dated event records. No voting form,
vote storage, or winner selection is included.

## Preview the D revisions

```bash
source source_me.sh && python3 -m mkdocs serve --strict -f mkdocs_d_alpha.yml
```

Open `http://127.0.0.1:8000/nilbc-web/d-alpha/`. For beta, use `mkdocs_d_beta.yml` and
`/nilbc-web/d-beta/`. Gamma uses `mkdocs_d_gamma.yml` and `/nilbc-web/d-gamma/`. All three share
`design_d_revised/`; beta and gamma inherit alpha independently and add their own stylesheets.
Original D stays independent.

### Edit photos, collections, and timeline

The shared `design_d_revised/data/photos.yml` is the photo manifest. Each photo has a stable
`id`, `theme`, caption/alt text and credit; a show photograph also has a `show` value matching
a key in `data/photo_shows.yml`. Keep that association structured; do not infer shows from
filenames or captions. Preserve source provenance and the completed-show-only selection boundary
in [DISCORD_ARCHIVE.md](DISCORD_ARCHIVE.md) before adding archive photographs. Upload timestamps
and file metadata are not capture dates: never add or imply a capture date from the upload.

The metadata indexer is an archive-review utility, not a build dependency. From the repository
root, this command reads the default external archive and writes `metadata.json` beside its
`downloads.json` catalog:

```bash
source source_me.sh && python3 devel/index_archive_metadata.py
```

Pass an archive directory as the optional positional argument to use a different local copy.
The full archive and its metadata index remain outside Git and deployment. The separate
`image_forward_review.json` and `train_review_batch_3.json` editorial ledgers also stay in the
external archive; consult the dated reports under `docs/active_plans/reports/` for the selected
evidence summary. Do not publish raw archive identifiers or private discussion text.

For public collection ordering, add a verified `event_date` to the corresponding
`photo_shows.yml` entry as a quoted ISO string (`'YYYY-MM'` when only month is verified,
`'YYYY-MM-DD'` only when the day is verified). The build sorts dated shows newest-first; within
each show, its `sequence` remains the explicit editorial/viewer order and must list every photo
in that album exactly once. The first sequence ID is the album cover. Undated archive material
comes after dated shows in stable manifest order; do not guess a date to move it forward.
Keep the display `date` label consistent with the verified `event_date`; maintainers are
responsible for that consistency. The build validates `event_date` syntax and calendar validity,
show references, and complete, duplicate-free sequences, but does not compare the display label
to the verified event date.

Refresh the homepage manually and briefly: choose the desired IDs in `homepage_photos` at the
bottom of `photos.yml`, in display order; keep them unique and associated with shows having a
verified `event_date`. The `/// featured-photos` block in `site_src/index.md` renders that
curated list. It does not automatically select the newest uploads. Album listings use
`/// show-gallery`; `/// collection | THEME` supplies a full, date-ordered theme page.
Dedicated trains, cities, screen-and-story, castles, and creatures pages use this collection
block. Collections are thumbnail-first; the full-image viewer is an optional enhancement, not
a reason to load full-size images for the grid. No external API or Discord login is used at
runtime.

The shared editable timeline lives at `site_src/about/timeline.md` and is sourced from public
research links in that page. Preserve the cited date precision, distinguish documented events
from interpretation, and leave the rebrand/identity chapter undated unless a public launch date
is verified. Do not turn a planned or approved identity into a fabricated launch date.

Alpha, beta, and gamma share the revised source and hooks. Alpha's `extra_css` loads the common
tokens, base, components, gallery, home, pages, timeline, and image-forward styles, then
`alpha-layout.css`. Beta inherits alpha's MkDocs settings but explicitly replaces the CSS list,
loading common styles, `beta.css`, `image-forward.css`, and `beta-layout.css`. Gamma likewise
sets its own list, including `photo-frames.css`, `image-forward.css`, `timeline.css`,
`gamma.css`, and `gamma-layout.css`. Keep variant-specific rules in the corresponding
stylesheet; later loaded rules can layer over earlier common rules. The data blocks and local
assets are built statically; there is no external API at runtime.

## Export the flyer

After the Node and Chromium setup above, run `npm run flyer`. The command reads the editable
SVG in `marketing/` and writes the PDF and PNG preview to `output/pdf/`. It checks font loading
and text margins. See [../marketing/README.md](../marketing/README.md) for editing and print details.
The website build does not depend on the flyer export.
