# NILBC website design comparison

Explore the Northern Illinois Brick Club website proposals and three revisions of Design D.
Members can compare the complete sites on a phone or computer, using the same visitor tasks
to decide which best represents our club.

**[Open the comparison homepage](https://vosslab.github.io/nilbc-web/)**

<!-- screenshots:begin (managed by screenshot-docs) -->
<!-- screenshots:end -->

## D revisions

D&alpha;, D&beta;, and D&gamma; share tight copy, photographs, and light/dark controls.
All use "Many interests. One club." and remove the Christmas lights.

| Design | Direction | Explore the website |
| --- | --- | --- |
| D&alpha; | Conservative: familiar layout and faint banner studs | [Open D&alpha;](https://vosslab.github.io/nilbc-web/d-alpha/) |
| D&beta; | Middle ground: larger photographs and solid backgrounds | [Open D&beta;](https://vosslab.github.io/nilbc-web/d-beta/) |
| D&gamma; | Creative chaos: poster lettering, brick tiles, and a photo collage | [Open D&gamma;](https://vosslab.github.io/nilbc-web/d-gamma/) |

Compare them in the same color mode before trying the other mode.

The revised homepage features the club's brick-built guitars. Joining information is clearer,
and the wording received a light editing pass. The
[wording review](docs/active_plans/reports/D_REVISIONS_WORDING.md) shows the changes from D.
These links become available after the updated site is published.

## Original proposals

Each design started with the same brief and approved club artwork. Each is a complete website
with its own layout, navigation, and presentation. The letters identify the entries, not a ranking.

| Design | Explore the website |
| --- | --- |
| A | [Open Design A](https://vosslab.github.io/nilbc-web/a/) |
| B | [Open Design B](https://vosslab.github.io/nilbc-web/b/) |
| C | [Open Design C](https://vosslab.github.io/nilbc-web/c/) |
| D | [Open Design D](https://vosslab.github.io/nilbc-web/d/) |

These are replacement website designs for club review. Event dates and other demo content
may need updating. This comparison does not collect votes.

## Try the same tasks

You only need a web browser. Open the comparison homepage, choose a design, and explore it.
Use your browser's Back button or reopen the comparison homepage to try the next one.

- **Plan a visit:** Find a show and the information a family would need to attend.
- **Discover our builds:** Browse creations and see whether the site welcomes builders across
  themes while keeping trains part of the club.
- **Imagine joining:** Find how a prospective member can get involved or contact the club.
- **Try your phone:** Open the menu, read the pages, and explore the photos on a smaller screen.

Give each design the same tasks. Consider readability, ease of finding information, and how
well the photos, club identity, and Matchstick represent us.

## Make your feedback useful

Keep a note of your preferred design letter, what worked well, and anything that got in your way.
Include the page and whether you used a phone or computer when describing a problem.

For example, explain what helped you find the joining information or where you expected to
find the next show. Specific observations help the club understand your preference.

## Printable club flyer

The flyer uses blue lettering on white and the "Many interests. One club." slogan.
Its QR code links to the current club website. The editable master and export instructions
are in [marketing/README.md](marketing/README.md). Run `npm run flyer` to produce a one-page
US Letter PDF and preview in `output/pdf/`.

## Background and local previews

- [docs/DESIGN_BRIEF.md](docs/DESIGN_BRIEF.md): the shared assignment and club goals.
- [docs/ASSETS.md](docs/ASSETS.md): approved branding, Matchstick references, and asset credits.
- [docs/INSTALL.md](docs/INSTALL.md): optional local setup, live previews, and automatic publishing.
- [docs/DESIGNS.md](docs/DESIGNS.md): technical details about the original designs and shared D revision.

Each design has its own `mkdocs_a.yml`, `mkdocs_b.yml`, `mkdocs_c.yml`, or `mkdocs_d.yml`.
Developers can use `mkdocs serve -f mkdocs_a.yml` (or b, c, d) for live previews after setup.
The revisions use `mkdocs_d_alpha.yml` and `mkdocs_d_beta.yml`.
GitHub Actions builds and publishes the combined site on pushes to `main`. The original
competition checkouts in `OTHER_REPOS/` remain unchanged and are not needed to build the sites.

## License

Source code: [LICENSE.Apache-2.0](LICENSE.Apache-2.0).

Documentation and other non-code materials: [LICENSE.CC-BY-4.0](LICENSE.CC-BY-4.0).

Supplied club branding, outside photographs, and fonts retain their respective rights;
see the individual designs' credits.
