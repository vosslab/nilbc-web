# Gamma world card hit targets

## Cause and fix

Gamma's stretched-link selector matched both the route link and Material's generated
`.headerlink` permalink in each world-card heading. The resulting full-card pseudo-elements
overlapped. Gamma does not load `home.css`, which normally hides these permalinks in navigation
cards.

The route link alone now stretches across each world card, and the decorative permalink is
hidden within those cards. Heading permalinks elsewhere remain available.

## Verification

- Strict gamma build passed with output isolated to `output_checks/hit_fix`.
- A browser probe at 390 and 1440 pixels clicked the center of each of the five home world cards;
  each pointer action opened its matching route, including Trains.
- At both widths, keyboard focus landed on the real Trains route link and Enter opened the Trains
  page. The generated permalink was hidden and was not the focused target.
- The browser probe was run inline and was not added to the permanent test suite.
