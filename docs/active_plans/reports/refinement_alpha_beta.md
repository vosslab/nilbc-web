# Alpha and beta refinement report

Date: 2026-10-30

## Direction

Alpha is a compact, familiar club site: restrained Nunito typography, short neutral
section headers, quiet square surfaces, clear photo grids, and subdued member, visitor,
reference, timeline, and gallery components. It removes the shared stud decoration,
card tilt, and oversized section banners.

Beta carries an editorial photo-led rhythm beyond the homepage. It gives interior page
titles large photo or mascot headers, opens show galleries as photo essays, spaces
collections and albums generously, alternates timeline photography with narrative,
and treats show, build-standard, membership, and logbook material as field guides.
Both variants use the current shared Markdown and real club photographs; the layouts
do not invent page copy or facts.

## Implementation

- `alpha-layout.css` and `beta-layout.css` define whole-site variant treatments;
  `beta.css` retains beta's homepage and collection composition.
- `mkdocs_d_alpha.yml` sets `extra.revision: alpha`; beta sets `extra.revision: beta`
  while inheriting the other alpha extras.
- No additional hooks, dependencies, frameworks, or copied page content were added.

## Verification

Strict builds completed using the required environment and isolated output directories:

```text
source source_me.sh && python3 -m mkdocs build --strict -f mkdocs_d_alpha.yml -d output_checks/refinement-alpha
source source_me.sh && python3 -m mkdocs build --strict -f mkdocs_d_beta.yml -d output_checks/refinement-beta
```

Playwright opened home, shows, visiting, gallery, logbook, standards, trains, about,
timeline, and credits at 1440px and 390px. Every route had `scrollWidth <= innerWidth`.
Screenshots from representative home, gallery, logbook, and timeline pages are in
`output_checks/refinement_visuals/` at both widths. Desktop and phone pages were visually
inspected; the beta gallery remained readable as a single-column photo essay on phone.

## Limits

The builds show the upstream Material for MkDocs warning about possible MkDocs 2.0
compatibility changes; that is existing dependency guidance, unrelated to these styles.
The full repository browser suite, keyboard journeys, dark-scheme contrast review, and
fresh independent quality review were not run as part of this variant work.
