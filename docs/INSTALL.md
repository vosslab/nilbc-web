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

## Export the flyer

After the Node and Chromium setup above, run `npm run flyer`. The command reads the editable
SVG in `marketing/` and writes the PDF and PNG preview to `output/pdf/`. It checks font loading
and text margins. See [../marketing/README.md](../marketing/README.md) for editing and print details.
The website build does not depend on the flyer export.
