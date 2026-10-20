# Independent design integration

The four entries are complete alternatives for an A/B/C/D design vote. They remain separate
websites, with their own content, templates, styling, assets, and browser behavior. No winner
is selected and no visual or content synthesis is part of this integration.

## Source and configuration

| Design | Original entry | Imported source | Root configuration | Published suffix |
| --- | --- | --- | --- | --- |
| A | `OTHER_REPOS/nilbc-web-aella` | `design_a/` | [mkdocs_a.yml](../mkdocs_a.yml) | `/a/` |
| B | `OTHER_REPOS/nilbc-web-astra` | `design_b/` | [mkdocs_b.yml](../mkdocs_b.yml) | `/b/` |
| C | `OTHER_REPOS/nilbc-web-grok` | `design_c/` | [mkdocs_c.yml](../mkdocs_c.yml) | `/c/` |
| D | `OTHER_REPOS/nilbc-web-work` | `design_d/` | [mkdocs_d.yml](../mkdocs_d.yml) | `/d/` |

The current repository is the integration destination. `OTHER_REPOS/` is a read-only local
reference, ignored by Git, and is never needed to build the imported websites. The original
working trees include staged and unstaged work beyond their shared `f28ae35` starter commit;
imports therefore use their working files, not only their Git commits.

[design_imports.json](design_imports.json) records each original repository, commit, and SHA-256
digest of every imported runtime file. Its paths are relative to the corresponding `design_*`
directory. It is an import receipt, not a rule preventing future edits. Original entry-specific
audits and screenshots remain historical evidence in `OTHER_REPOS/`; they do not certify this
integrated build.

## Build boundaries

Each configuration owns a different `docs_dir`, theme directory, URL, and `site_dir`.
Only location settings are adapted from the original configurations. A's snippet search path
points to its own `site_src/`. D's hooks and photo manifest remain together under `design_d/`.
The website source and assets retain their imported bytes.

- A uses ordinary Markdown sections, a shared event snippet, and two templates in `overrides/`.
- B uses Markdown frontmatter and body text, page templates in `theme/`, and a gallery dialog.
- C uses Markdown with embedded HTML, `site_theme/`, and Material search.
- D uses Markdown blocks, Python hooks, a photo manifest, Material search, and light/dark themes.
  Its event selection depends on the build date, as in the original implementation.

These editing models are intentionally different. Routine edits stay inside the selected design.
For A, edit `site_src/includes/NEXT_SHOW.md` once for the homepage and Visit page. For B,
`site_src/shows.md` owns the calendar and `site_src/join.md` owns the shared contact address.
For C, edit its existing page markup. For D, retain its `///` block syntax, show records in
`site_src/shows/index.md`, and photo records in `data/photos.yml`.

All four currently use MkDocs 1.6.1 and Material 9.7.7. The shared requirements also declare A's
PyMdown extension and D's Markdown, Pillow, and PyYAML imports. Their compatible dependencies
can be installed together; their implementations do not share content or theme code.

## Combined output

[build_sites.py](../build_sites.py) builds the neutral homepage first, then A through D.
This order matters: MkDocs cleans its configured output directory before building. Building the
homepage last would remove the four child outputs. Any failed build stops the combined build
and prevents the workflow from uploading or deploying an incomplete artifact.

The result is `output_site/index.html` plus `output_site/a/` through `output_site/d/`.
For this GitHub Pages project, the public prefix is `/nilbc-web/`, so the actual demo addresses
are `/nilbc-web/a/`, `/nilbc-web/b/`, `/nilbc-web/c/`, and `/nilbc-web/d/`. A custom domain at the
site root can use `/a/` through `/d/` after updating all five configurations' `site_url` values.

The neutral landing page labels only A, B, C, and D. It adds no voting backend and changes
none of the entries' navigation or visual elements. One Pages workflow uploads and deploys
the entire output directory. Original per-entry deployment workflows are not imported.

See [INSTALL.md](INSTALL.md) for independent previews, the combined build, and deployment setup.
See [ASSETS.md](ASSETS.md) for brand provenance and the designs' individual credits.

## Verification on 2026-10-20

- All five strict builds pass. The integrated browser check passes 64 desktop/phone page
  checks and nine journeys, including local references, mobile menus, galleries, and search.
- Fresh builds of the read-only originals were compared with the imports: all 64 full-page
  screenshot pairs match exactly at 1440 and 390 pixels. All 16 paired interaction checks pass.
  Both pages were foregrounded for screenshots to avoid background-tab icon rasterization differences.
- All 162 imported file hashes match their originals. Original source hashes and Git working-tree
  status are unchanged. The comparison report and screenshots are in ignored `output_checks/parity/`.
- The normal repository suite passes 793 checks. A temporary scan including the new, unstaged
  files passes 1,211 checks; it makes no changes to the Git index.
- Verification is local Chromium evidence. The GitHub Actions deployment has not been run from
  this working tree. The workflow checks the combined build before uploading its Pages artifact.
