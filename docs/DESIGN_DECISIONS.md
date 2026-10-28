# Design decisions

<!-- VENDORED HEADER: START -->
Record each durable decision about how this code and repository are shaped, once it is settled, with
the reasoning a later reader needs. Guidance Neil Voss states belongs in
[HUMAN_GUIDANCE.md](HUMAN_GUIDANCE.md), dated history in `docs/CHANGELOG.md`, open discussion in
`docs/active_plans/decisions/`. [PROPAGATED HEADER - ENTRIES BELOW ARE YOURS]
<!-- VENDORED HEADER: END -->

### Temporary Graphify Cargo reconciliation

**Decision.** Reconcile exact Cargo aliases with their AST package twins before
reclustering; verify the resulting IDs against Graphify's loaded graph before writing.

**Why.** Graphify 0.9.80 compares normalized candidate counts with raw JSON counts,
and its original-link export otherwise drops links still pointing to removed aliases.

**Consequence.** Preserve all link records and the active shrinkage guard. Keep the
correction in one removable function; already reconciled upstream output is a no-op.

**Owner.** `normalize_cargo_twins` in
[devel/graphify_prune_tests.py](../devel/graphify_prune_tests.py)
and [devel/graphify_map_repo.py](../devel/graphify_map_repo.py).

Write each decision as a level-three heading with these four fields. `Owner` names the
authoritative code or contract document, rather than a person.

```markdown
### <decision title>

**Decision.** <the durable direction>

**Why.** <the reason it was chosen>

**Consequence.** <the constraint a future change preserves>

**Owner.** <the authoritative code or contract doc>
```

### Minimal replaceable starter

**Decision.** Start with one MkDocs configuration, a default Material homepage, and a local
copy of the approved banner. Keep source presentation materials separate from public content.

**Why.** A working build provides immediate feedback without prescribing the eventual website.

**Consequence.** Every file, dependency, directory, and implementation choice remains open
to the designer. The initial font setting avoids a remote font dependency for the starter.

**Owner.** [DESIGN_BRIEF.md](DESIGN_BRIEF.md) and [mkdocs.yml](../mkdocs.yml).

### Mascot source and palette

**Decision.** Bundle the unmodified presentation frame at 00:04:19 as a full-body Matchstick
reference. Record the owner's working palette, including Dark Azure wings, as provisional.

**Why.** The supplied presentation establishes the character's brick-built identity; lighting
in its rendering cannot confirm actual part colors.

**Consequence.** Treat the rendering as a reference, not a physical-model photograph. Preserve
the recognizable model when adapting it, and confirm part colors from a parts list if needed.

**Owner.** [ASSETS.md](ASSETS.md).

### Four independent voting demos

**Decision.** Import each completed entry under its own `design_*` directory and build it with
`mkdocs_a.yml`, `mkdocs_b.yml`, `mkdocs_c.yml`, or `mkdocs_d.yml`. Keep the root configuration
for a neutral comparison homepage. Build that homepage first, then all four child sites.

**Why.** The competition compares independent designs. Combining their features or theme
architectures would change the entries, and sharing an output directory would overwrite them.

**Consequence.** Preserve each design's source and behavior. Adapt only paths required for
relocation. Keep OTHER_REPOS read-only and deploy one artifact containing all four outputs.

**Owner.** [DESIGNS.md](DESIGNS.md), [build_sites.py](../build_sites.py), and the five MkDocs configs.

### Shared D revisions

**Decision.** Preserve A-D and share revised D content across alpha, beta, and gamma.
Alpha retains the conservative layout. Beta and gamma inherit alpha's configuration separately,
adding a final stylesheet for photographic emphasis or the exhibition/poster collage.

**Why.** The owner expanded the initial texture comparison on 2026-10-27 into three levels
of visual experimentation. Shared wording keeps the club's comparison focused on presentation.

**Consequence.** Content fixes reach all revisions. Style overrides live in their variant;
no duplicated content tree or new JavaScript framework is needed. Phone layouts simplify
rotations and overlaps. Existing theme, search, gallery, and reduced-motion behavior remains.

**Owner.** `design_d_revised/` and the three `mkdocs_d_*.yml` revision configurations.

### Editable evergreen flyer

**Decision.** Keep one self-contained SVG master with live text, embedded fonts and logo,
and a vector QR code. Export a US Letter PDF from that SVG with the existing browser tooling.

**Why.** Kerbear requested printable marketing material and Joel suggested blue type on white.
Neil approved a flyer. The existing browser supports the embedded fonts; this machine's
`inkscape` command is a stub, so it cannot provide a native export.

**Consequence.** The SVG owns the wording and layout. PDF and preview files are generated in
`output/pdf/`, independently of the website build. Omit dates and dues. The QR code points to
`https://niltc.org/`, with the old name explained on the page.

**Owner.** [../marketing/README.md](../marketing/README.md) and
`tests/playwright/export_flyer.mjs`.

### Selected photo treatments

**Decision.** Keep original photographs and full-image links. Add stable photo identifiers
and optional editorial notes to the shared figure output. Alpha keeps simple borders;
beta and gamma share paper frames and locally hosted Kalam handwriting for selected pictures.
Gamma adds wood-style frames and a soft edge mask to a few gallery images.

**Why.** The owner requested a personal scrapbook feel without treating every photograph alike.
Captions remain selectable text, and frame effects are CSS rather than baked into originals.

**Consequence.** Shared photo notes live in the manifest. Variant styles choose presentation;
photo credits and descriptive captions remain visible. Asset derivatives retain their source credits.

**Owner.** `design_d_revised/data/photos.yml`, `site_hooks/data_blocks.py`, and variant stylesheets.

## 2026-10-27 review refinements

Gamma's existing 44em mobile breakpoint now reduces category photo stages from 11rem to
7rem, retaining stacked cards, full copy, and colored frames. Desktop photo heights stay
unchanged. The comparison page leads with beta and invites feedback on individual details.

The castle photograph replacement is blocked on a verified club image. The shared manifest,
original design assets, and earlier Instagram-source records contain no suitable photograph;
the club's castle page contains module diagrams. Keep the current diagram until a suitable
source is available rather than substitute an unrelated build.
