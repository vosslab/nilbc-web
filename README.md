# nilbc-web

Four independent Northern Illinois Brick Club website proposals, preserved together for an
A/B/C/D design vote. A neutral landing page links to the complete designs, and one static
GitHub Pages deployment serves all four.

## Build and preview

```bash
source source_me.sh && python3 -m pip install -r pip_requirements.txt
source source_me.sh && python3 build_sites.py
source source_me.sh && python3 -m http.server 8000 --bind 127.0.0.1 --directory output_site
```

Open [the local comparison](http://127.0.0.1:8000/).

- [docs/INSTALL.md](docs/INSTALL.md): independent previews, browser checks, and deployment.
- [docs/DESIGNS.md](docs/DESIGNS.md): source mapping and preserved implementation boundaries.
- [docs/DESIGN_BRIEF.md](docs/DESIGN_BRIEF.md): the common assignment.
- [docs/ASSETS.md](docs/ASSETS.md): supplied artwork and individual design credits.

Each design has its own `mkdocs_a.yml`, `mkdocs_b.yml`, `mkdocs_c.yml`, or `mkdocs_d.yml`.
The original competition checkouts in `OTHER_REPOS/` are read-only references and are not
required for builds.

## License

Source code: [LICENSE.Apache-2.0](LICENSE.Apache-2.0).

Documentation and other non-code materials: [LICENSE.CC-BY-4.0](LICENSE.CC-BY-4.0).

Supplied club branding, outside photographs, and fonts retain their respective rights;
see the individual designs' credits.
