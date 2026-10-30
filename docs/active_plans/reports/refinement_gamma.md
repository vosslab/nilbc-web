# Gamma refinement: the exhibition floor

## Concept and implementation

Gamma is a club exhibition rendered as a bold visual index: black structure, fluorescent
wayfinding, orange poster lettering, numbered destinations and real club photography.
This supersedes the working-atlas implementation; the earlier concept proposals do not
constrain this refinement. No invented model, show, date, membership fact or synthetic
club photograph was added.

- Home pairs an oversized welcome poster with full-frame curated photographs, then presents
  five photographic worlds as a two-plus-three exhibit wall. The shared next-show ticket
  remains a distinct, full-width practical destination. Phone welcome is compact enough for
  the photographic lead to enter the initial 390 by 844 viewport.
- Worlds is a numbered index with real photographic routes and its existing optional filter.
  Collections become black contact sheets with bright show transitions and full-frame images.
- Shows is a date-led departures board, with venue details beside the date on desktop and
  below it on phones. Album navigation uses paired image/label strips; opened albums use
  asymmetric lead/detail sequences. Visiting retains its numbered walk-through and practical
  warnings; Logbook retains its readable chronological table.
- Join presents one shared membership email action followed by the existing membership facts.
  Standards becomes a ruled field manual with icon, heading and specifications in distinct
  columns, rather than a set of inherited cards.
- About keeps the club explanation and timeline route. Timeline uses illustrated chapters
  with a broad heading rail and alternating orange edges. Matchstick keeps the supplied parts
  diagram and recognizable mascot artwork. Credits uses compact source headings and retains
  the shared credits ledger.
- The numbered exhibition index is the primary desktop navigation, replacing redundant
  Material tabs. The Material header, mobile drawer, search, theme controls, skip link and
  footer remain. Three prominent exits offer work/show/membership journeys at each page end.
  Search results receive the same visual structure; the 404 offers clear route recovery.

## Cascade and scope

Runtime files owned by this work:

- [main.html](../../../design_d_revised/theme/main.html): gamma-only content wrapper and index;
  alpha/beta continue through their existing content and hero branches. Removed the duplicate
  gamma Join invitation and its inline DOM-reparenting JavaScript.
- [gamma_wayfinder.html](../../../design_d_revised/theme/gamma_wayfinder.html): semantic, static
  route links shared by gamma content and the 404.
- [404.html](../../../design_d_revised/theme/404.html): gamma recovery screen; the non-gamma
  branch retains Material's original `404 - Not found` content.
- [gamma.css](../../../design_d_revised/site_src/stylesheets/gamma.css) and
  [gamma-layout.css](../../../design_d_revised/site_src/stylesheets/gamma-layout.css): replace
  the previous gamma files. The selectors follow the actual `.md-typeset .nb-atlas` structure;
  none depend on the previous inverted `.nb-atlas .md-typeset` ancestry.
- [mkdocs_d_gamma.yml](../../../mkdocs_d_gamma.yml): gamma no longer loads the alpha/beta
  `base.css`, `home.css` or `pages.css`. Shared tokens, component structures, gallery/viewer,
  image-forward and timeline rules remain, followed by the two gamma owners.

No new dependency, framework, font, asset, animation or gamma JavaScript was introduced.
Source order and actual links work without JavaScript. The existing optional filters and
photo viewer continue to use shared behavior. Dark colors are role-based; orange/yellow
surfaces retain dark text in both themes. There is no forced motion; reduced-motion disables
shared transitions as well.

## Verification and evidence

Strict build command (passed repeatedly, latest final build recorded with browser probe):

```bash
source source_me.sh && python3 -m mkdocs build --strict -f mkdocs_d_gamma.yml \
  --site-dir output_checks/refinement_gamma/nilbc-web/d-gamma
```

The artifact is served with its real project prefix at
`http://127.0.0.1:8744/nilbc-web/d-gamma/`. Browser evidence and the one-shot probe live in
ignored `output_checks/refinement_gamma/`; the probe is not permanent test-suite code.

Rendered review covered Home, Worlds, Trains, Shows, Gallery, Visiting, Join, Standards,
About, Timeline, Matchstick, Credits and Logbook on desktop, with representative phone
captures. Review caught and corrected:

- A heading permalink that occupied an invisible extra line below the home poster.
- A narrow timeline heading rail that wrapped chapter names excessively.
- Inherited mosaic row-flex causing six pixels of Visiting overflow at 320 pixels; the shared
  gamma figure rule now explicitly owns both gallery and mosaic orientation.
- Low-contrast inherited collection divider links on the black contact-sheet background.
- The old duplicate Join CTA and JavaScript-dependent placement.

The final probe covers all 18 generated HTML routes at 320, 390, 768, 1440 and 2560 pixels,
one H1, five working index links and document overflow. It also exercises keyboard photo
opening, next/previous arrows, Escape/focus restoration, one shared Join CTA, mobile drawer,
search, dark mode, reduced motion and no-JavaScript original-image access/native show albums.
The initial viewer assertion compared the whole transient loading-status string; the probe
now compares the stable photo position and does not mistake image loading for navigation
failure. Final machine results: **18 routes, 90 width checks, five passing interaction journeys,
zero browser page errors or local HTTP failures**. Results are in `probe.json` and
`widths.json`. Commands: `node output_checks/refinement_gamma/probe.mjs` for the route and
capture pass; `node output_checks/refinement_gamma/probe.mjs --journeys` for the final
interaction pass using those width results. The final search probe types after the new
page loads; an earlier synthetic fill ran before Material initialized and produced no
results. Real typed search returned 13 result links for Matchstick.

Alpha and beta also passed isolated strict builds into `alpha_template_check` and
`beta_template_check`; assertions confirm their generated Home and 404 contain no gamma
wrapper/index and retain Material's original 404 text.

Representative captures: `home-1440.png`, `home-390.png`, `home-worlds-1440.png`,
`trains-1440.png`, `shows-390.png`, `standards-1440.png`, `timeline-1440.png`,
`gallery-390.png`, `home-dark-1440.png`, `standards-dark-390.png`, `search-390.png`,
and `404-1440.png`.

## Limits and handoff

This report records implementation evidence. The manager reports that independent visual
specification review accepted the design; independent quality/integration review follows. Whole-repository integration tests, actual Safari/Firefox, screen-reader testing,
automated WCAG conformance and physical touch-device testing are outside this scoped pass.
No commit, push or deployment was performed. Photo/date facts remain owned by the concurrent
shared-data work; rebuild after final curation and run the combined integration suite.
