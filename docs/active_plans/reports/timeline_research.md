# Club history timeline research

## Scope

A selective, photo-led history for `design_d_revised/site_src/about/timeline.md`, not an
exhaustive show log. Evidence was checked against the public NILTC history and show list,
venue listings, existing local Discord archive provenance, and the selected photo credits.
No private messages, personal identifiers, or message quotations are published.

## Verified narrative facts

| Timeline point | Evidence and qualification |
| --- | --- |
| Late summer 2001 | NILTC's own history says a few enthusiasts from Illinois and Wisconsin met, discussed enlarging a local train display, selected a logo, agreed building parameters, and prepared for a first show the following March. The public source does not identify that first show's exact date. |
| Early 2002 | NILTC says five members presented a 17-by-22-foot layout at the NMRA High Wheeler Show at Harper College in Palatine. It reports three members joined after the show. |
| Later 2002 | NILTC says the regional Train Collectors Association invited it to the national show in St. Charles, Illinois, and reports two additional members joined after that show. No exact event date is given on the history page. |
| 2003 | NILTC's retrospective says its 30-by-30-foot layout stood inside a 40-by-40-foot tent at Illinois Railway Museum's Day Out With Thomas in Union, and reports 48,000 guests across two weekends. The page calls this its largest show attendance "to date"; without a dated comparison, that wording is not presented as a current record or as attendance at the layout alone. |
| 2010 onward | The public show log documents Arlington Heights Memorial Library in September 2010 and multiple library venues in 2011. This is a documented stretch, not a claim that the club's first library exhibition occurred in 2010. |
| December 2016 | NILTC's history page labels the group photograph Cantigny, December 2016. The source credits used in this site identify the image as NILTC / niltc.org; no individual photographer is claimed. |
| 2025-2026 | The public show log lists Oswego Public Library in October 2025 and Ela Area Public Library in September 2026. Existing local archive records and published derivative credits identify the selected images with those show entries. Uploader names are not presented as photographers or builders. |
| October 2026 | The public show log lists Northbrook Public Library on October 17-18, 2026. The library event listing independently confirms the exhibit and describes spaceships, cities, castles, planes, horses, dragons, and more. |
| New name | The owner-approved identity uses Northern Illinois Brick Club and Matchstick. No public evidence establishes a launch date for NILBC or Matchstick, so this transition is deliberately undated. |

## Photo provenance and constraints

- Four local photo pairs are used: Cantigny 2016, Oswego 2025, Ela Area 2026, and Northbrook 2026.
- Each figure links its existing thumbnail to the existing larger local WebP; all eight paths were verified in the repository.
- Existing credits provide the provenance basis. Discord archive uploader labels, where present, are not treated as photographer, builder, or capture-date evidence.
- No date is inferred from an upload URL, filename, or asset identifier. Dates on the recent show photos are event dates supported by the show log and local archive record, not asserted camera capture dates.
- No source licenses or new redistribution permissions were inferred. Existing site photo credits remain linked for details.

## Public sources

1. [NILTC club history and Cantigny photo captions](https://niltc.org/about) - founding, 2002 exhibits, 2003 IRM event, historical Cantigny context and labeled group photo.
2. [NILTC past shows](https://niltc.org/past-shows) - dated venue continuity through 2026, including Northbrook, Ela Area, and Oswego; the 2022 Cantigny listing calls its event the 20th Annual LEGO Christmas Show, which does not establish uninterrupted years at Cantigny.
3. [Northbrook Public Library exhibit listing](https://visit.northbrook.info/event/14127359) - independent confirmation of October 17, 2026 exhibit and the range of displayed themes.
4. [NILTC collaborative castle display proposal](https://niltc.org/castle) - an undated proposal describing modular collaborative building, cross-genre themes, and the club's wish to show it is not only a train club. It does not date the pictured castles or establish that selected models follow the proposal.

## Integration guidance

- Include `design_d_revised/site_src/stylesheets/timeline.css` in alpha and beta after their existing layout stylesheets so the shared semantic `.nb-timeline*` structure has a coherent baseline.
- Keep timeline content and these class hooks shared and editable in Markdown. Gamma should override the hooks (for example `.nb-timeline-entry`, `.nb-timeline-origin`, `.nb-timeline-castle`, `.nb-timeline-photo`, `.nb-timeline-photo-pair`, and `.nb-timeline-note`) rather than rewriting content; the base sheet defines structure, readable responsive photos, focus visibility, and native disclosure styling.
- Include the timeline page in all variants' About navigation using the existing route `about/timeline/` (MkDocs page URL). Do not add a new route or embed the timeline into the homepage.
- Preview/build only with an isolated temporary site directory; do not overwrite shared combined output as part of this task.

## Remaining uncertainty

The public history provides only year/season precision for founding and early milestones. The 2003 attendance number is solely the club's retrospective report. The show log and local archive associate selected photos with event dates, but the photos do not establish their own capture dates, makers, or individual builders. NILBC/Matchstick launch timing remains unknown.