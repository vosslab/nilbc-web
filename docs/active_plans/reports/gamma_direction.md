# Gamma direction: the working atlas

## Selection and rationale

Use concept A, **The Club, in Motion**, as the basis: a club site feels like an active
workbench where real builds, shows, and ways to participate are laid out for inspection.
This creates spatial variety without turning the five interests into a miniature theme
park. Concept B's field notes offer one compatible idea: fast, clear wayfinding for dense
collections. Do not combine their visual motifs wholesale. Gamma's interpretation is the
**working atlas**: the page is an editorial instrument that moves between a live build
surface, a route index, and a practical handoff. It is not a pile of ruled cards or an
illustrated floor plan.

The creative departure from both proposals is to make page composition change by task.
The homepage opens like a cutaway work table: the real show photographs act as inspection
windows, while interest routes form an irregular index beneath. Event pages use a strong
calendar rail; joining becomes a clear three-part handoff; dense collections become compact
contact sheets interrupted only by real show transitions. Structural framing, asymmetric
columns, broad color fields, and changing scale—not just type, lines, or collage—carry the
identity through inner pages. The idea remains legible when motion is off and when images
fail. Never imply the site depicts a literal current club room or invent dates, people, or
build details.

## Scope

Owned runtime files:

- `mkdocs_d_gamma.yml`: gamma flag and final stylesheet registration after shared
  `image-forward.css` and `timeline.css`.
- `design_d_revised/site_src/stylesheets/gamma.css` and
  `design_d_revised/site_src/stylesheets/gamma-layout.css`: complete gamma composition,
  Material navigation/footer states, responsive/dark/reduced-motion styling, and route
  treatments using existing rendered classes.
- `design_d_revised/theme/main.html`: add only a gamma-conditional wrapper around Material
  content; retain the existing alpha/beta output and mascot/announcement behavior.
- `design_d_revised/site_src/javascripts/gamma.js` only if a nonessential progressive
  enhancement proves useful; no JavaScript is required for navigation or content.

Reports: `docs/active_plans/reports/gamma_direction.md` and
`docs/active_plans/reports/gamma_implementation.md`. Temporary probes and screenshots stay
under ignored `output_checks/`.

Explicitly out of scope: shared Markdown, `data_blocks.py`, alpha/beta configs/styles,
photo manifests/assets, timeline source/CSS, shared tests/smoke, original designs, commits,
pushes, and deployment. Consume the existing homepage, collection, show, ticket, gallery,
world, and timeline classes; do not duplicate shared copy or hardcode photo dates/counts.

## Acceptance

- Gamma is clearly distinct on Home, shows/gallery/visiting/logbook, Join/Standards,
  About/timeline/Matchstick/credits, and all five dense collections; it is not a CSS skin
  limited to the homepage.
- Native Material menu, search, theme toggle, skip link, links, and image viewer remain
  functional. Focus, keyboard, reduced motion, dark theme, narrow screens, and wide screens
  retain legibility and meaning.
- Exact gamma output builds strictly to `output_checks/gamma_build`; alpha/beta template
  and config files remain unchanged by this implementation.
- RED/GREEN probes exercise gamma scoping, routes, collection viewer, and mobile overflow.
  Inspect generated screenshots with vision at 390, 1440, and 2560 pixels, plus phone
  inner-page captures; correct visible defects before claiming visual completion.
