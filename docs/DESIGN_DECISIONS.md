# Design decisions

<!-- VENDORED HEADER: START -->
Record each durable decision about how this code and repository are shaped, once it is settled, with
the reasoning a later reader needs. Guidance Neil Voss states belongs in
[HUMAN_GUIDANCE.md](HUMAN_GUIDANCE.md), dated history in `docs/CHANGELOG.md`, open discussion in
`docs/active_plans/decisions/`. [PROPAGATED HEADER - ENTRIES BELOW ARE YOURS]
<!-- VENDORED HEADER: END -->

### Editorial album presentation

**Decision.** Photo-show YAML owns a complete explicit sequence; its first image also supplies
the photographic cover. Build validation rejects duplicate, omitted, or foreign album IDs.
Album figures use optional short captions without category, event, note, or credit stacks.
Full attribution remains in the viewer and linked credits page, including without JavaScript.

**Why.** The prior uniform metadata-heavy cards concealed the photographs. Sequences now move
from an establishing exhibit to complementary details, based on inspection of the existing
45 selected images rather than invented stories or maker attributions.

**Consequence.** Only the gallery Markdown opts out of the generic mascot banner. Alpha uses
a clean catalog grid; beta uses a large opening frame and paired details; gamma uses selected
offsets and handwritten captions. All album images remain contained rather than cropped;
phone offsets are removed. Other pages retain their existing figure treatment and captions.

**Owner.** `design_d_revised/data/photo_shows.yml`, `site_hooks/data_blocks.py`,
`site_src/shows/gallery.md`, and shared/variant gallery styles.

### Show albums without an eager wall

**Decision.** Publish 45 reviewed archive photographs across seven library shows in the shared
D revisions. Use native expandable albums, lazy local thumbnails, and an uncropped viewer with
group-local navigation. Keep the homepage preview at three photographs.

**Why.** The owner rejected the eight-photo scope. Broad archive review supports much richer
coverage, but only completed club exhibits at shows qualify; attractive unrelated or ambiguous
images do not become eligible to meet a quota.

**Consequence.** Source hashes, unchanged selected originals, and all-sheet review evidence stay
in ARTIFACTS. The full archive stays external. Album labels live in YAML; counts are calculated.
No-JavaScript visitors retain native albums and direct image links. Original A/B/C/D and the
three revised variants' existing mascot, group image, and visual character are preserved.

**Owner.** [DISCORD_ARCHIVE.md](DISCORD_ARCHIVE.md),
`design_d_revised/data/photos.yml`, `design_d_revised/data/photo_shows.yml`, and
`design_d_revised/site_hooks/data_blocks.py`.

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

The castle photograph replacement was initially blocked on a verified club image. The
2026-10-28 Archive Shows collection resolves that gap with the Ela Area castle scene.

### Archive-first exhibit photography

**Decision.** Preserve the complete category image collection outside Git and deployment,
then curate finished club exhibit photographs for the shared D revisions. Keep selected
originals and exact provenance in ARTIFACTS, with local metadata-free WebP derivatives.

**Why.** The owner requires copy, organization, and assessment in that order. Category membership
alone is not evidence that a photo depicts club work; show context and full-image review matter.

**Consequence.** All revisions get a real Castles card and recent railway/city photographs.
Their existing restrained, balanced, and playful treatments remain distinct. Uploader credit
is explicit, private discussion stays unpublished, and full collection size does not inflate Git.

**Owner.** [DISCORD_ARCHIVE.md](DISCORD_ARCHIVE.md) and `design_d_revised/data/photos.yml`.

### Placement-specific archive curation

**Decision.** Use eight reviewed archive selections: the original three plus spacecraft, a
white dog, space-suited characters, a market stall, and a boating scene. Put a three-image
preview after the homepage club portrait and six complementary details on Visiting a show.

**Why.** The weaker Screen/story and Creatures cards needed clearer subjects; coherent local
show batches provide stronger evidence than broad but ambiguous external-show coverage.

**Consequence.** Captions describe visible builds and source-supported show dates, not inferred
franchises or makers. Homepage focal positions differ from gallery positions; the dog keeps
its complete frame on desktop and a face-focused crop on phones. Viewer images remain uncropped.
Alpha stays plain, beta retains selected paper notes, and gamma retains its existing playful
frames. All source originals and hashes stay preserved, with no private discussions published.

**Owner.** `design_d_revised/data/photos.yml`, revised home/gallery styles, and
[DISCORD_ARCHIVE.md](DISCORD_ARCHIVE.md).
