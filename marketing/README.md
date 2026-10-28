# Printable club flyer

[nilbc_club_flyer.svg](nilbc_club_flyer.svg) is the editable master. It contains live text,
the approved circular logo, embedded fonts, and a vector QR code for `https://niltc.org/`.
The flyer is an evergreen introduction for public-show visitors and prospective adult members.

## Edit and export

Edit the SVG text and grouped artwork in a vector editor or text editor. For vector editors
that ignore embedded web fonts, install Barlow Condensed Bold and DM Sans Regular/Bold from
`design_b/site_src/assets/fonts/`. The browser export uses the embedded copies.

After the Node and Chromium setup in [../docs/INSTALL.md](../docs/INSTALL.md), run:

```bash
npm run flyer
```

The exporter reads the master and writes `output/pdf/nilbc_club_flyer.pdf` and a PNG preview.
It checks loaded fonts and text bounds. Inspect the PDF after changing the artwork; a successful
export alone does not prove a good layout. The PDF and preview are ignored generated outputs.

Print the PDF at actual size on US Letter paper. The artwork stays inside half-inch margins.
There is no bleed. Colors are RGB for ordinary office and home printing; check a paper proof
before printing a batch. The blue type remains readable in grayscale.

## Sources and editing notes

- The embedded logo is the approved `ARTIFACTS/nilbc_circular_matchstick_logo.png`, unchanged.
  The logo is raster artwork; type, rules, accents, and the QR code are vectors.
- Barlow Condensed and DM Sans come from Design B. Their SIL Open Font License files remain
  beside the original font files. The editable SVG embeds those same font bytes.
- The headline comes from B and was specifically requested for the revisions and flyer.
- The club's [membership page](https://niltc.org/membership) and
  [public website](https://niltc.org/) confirmed the adult membership age, email, and URL on
  2026-10-26. The flyer explains the former NILTC name and does not promise free admission.
- The QR code contains `https://niltc.org/`. If the destination changes, replace its vector
  artwork as well as the printed URL and hyperlink, then decode the exported PDF image to check it.
- The SVG uses a 612 by 792 viewBox with an 8.5 by 11 inch viewport. The SVG creator references
  on project delivery and viewBox/viewport sizing informed the editable, print-sized source.

The humanizer pass replaced generic introductory copy with concrete examples of members' builds.
"Many interests. One club." remains unchanged. Font licenses and artwork provenance are described
in [../docs/ASSETS.md](../docs/ASSETS.md).
