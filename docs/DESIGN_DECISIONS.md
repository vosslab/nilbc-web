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

### Verified event dates and curated homepage photographs

**Decision.** Represent verified event dates as quoted ISO `YYYY-MM` or `YYYY-MM-DD`,
at the precision the evidence supports. Order dated events newest first with an explicit,
stable tie-break; keep undated entries last. A photograph's show reference supplies its
public event date without duplicating date metadata. Maintain the homepage preview as an
explicit root `homepage_photos` list of curated IDs; the `featured-photos` hook validates
ID uniqueness and that each photo resolves to a show with a verified date.

**Why.** Explicit source-supported chronology avoids false precision from IDs or upload order,
while a small curated homepage set can be refreshed deliberately without dumping the catalog.

**Consequence.** Never infer event dates from identifiers or upload timestamps. Preserve album
sequence independently from chronology; do not publish undated event dates as verified. The
homepage list remains handpicked and validation prevents duplicate or undated selections.

**Owner.** Shared photo/show data, `featured-photos` hook, and root MkDocs homepage configuration.

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

### Gamma working atlas

**Decision.** Gamma uses a task-changing working-atlas composition across the shared D revision
pages: real club builds are inspection windows, with a route index and practical handoff for
visitors. Keep variant presentation in gamma's configuration, template branch, and final CSS.

**Why.** A coherent experiential distinction should extend beyond headline lettering or photo
frames while leaving facts, photo provenance, and editing in shared Markdown/data.

**Consequence.** Gamma can use route-scoped composition but must preserve Material navigation,
search, theme controls, the shared viewer, accessible focus, responsive reflow, and reduced-motion
meaning. Alpha/beta keep the existing template branch.

**Owner.** `mkdocs_d_gamma.yml`, `design_d_revised/theme/main.html`,
`design_d_revised/site_src/stylesheets/gamma.css`, and `gamma-layout.css`.

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

### Visitor-first shared content

**Decision.** Keep the homepage welcome and curated show photos adjacent while leaving
composition to each variant. Give all five creation themes a representative linked photo,
and link collection show/date headings to their show albums while captions identify the build.
Use one shared email call to action on Join and one About timeline as the history detail source.

**Why.** Visitors can act, see real exhibits, and choose a building interest without reading
repeated history or show metadata before reaching practical information.

**Consequence.** Keep category links and section IDs stable, preserve direct full-image links
without JavaScript, and use `album_caption` with `caption` as its fallback. The variants may
arrange shared content differently.

**Owner.** `design_d_revised/site_src/index.md`, `creations/index.md`, `join/index.md`,
`shows/index.md`, `about/index.md`, and `site_hooks/data_blocks.py`.

## 2026-10-30 page refinements

**Decision.** Treat alpha, beta, and gamma as distinct whole-site directions: a restrained
club catalog, an editorial photo-led presentation, and a numbered exhibition floor. Keep facts
and Markdown shared; let each variant own layout and styling. Gamma's manager chose its concept
exploration process. Any coverage matrix is illustrative, not a required structure or quota.

**Why.** Visitors need clear club and show information across all variants, while the design
exercise asks each revision to make a coherent visual choice across home and interior pages.

**Consequence.** Content and structured photo records remain common. The refinement checkpoint
has 73 unique photos (52 archive selections and 21 existing site photos), including 17 train
records and two newly selected Arlington train views. Purple Rain leads the homepage selection.
Uploader credits do not claim an unverified photographer, builder, ownership, or redistribution
right. See [DISCORD_ARCHIVE.md](DISCORD_ARCHIVE.md) and the dated refinement reports for evidence.
Gamma specification, scoped quality reviews, the mobile drawer fix, and final whole-site browser
suite are accepted. The latest full pytest run recorded 1,671 passes and one sandbox-only Podman
failure; an outside-sandbox read-only check confirmed storage above the 20 GB budget.

**Owner.** `.hermes/plans/refinement-execution.md`, the three D revision stylesheets, shared
`design_d_revised/data/`, and [refinement verification](active_plans/reports/refinement_verification.md).

### Presentation polish and photo catalog

**Decision.** Keep Alpha compact and traditional; give Beta a horizontal magazine opening
  and Nunito headings; give Gamma a full-width poster opening and staggered photo strip.
  Featured captions describe the subject, with the linked show label supplying venue/date.
**Why.** The earlier Beta opening left a large empty column, and Beta and Gamma shared too
  much composition. Repository photo evidence was difficult to browse in raw manifests.
**Consequence.** A generated repository catalog organizes all selected photos by theme and
  show. It records actual dimensions, sizes, hashes, crop focus, and explicit date uncertainty.
  Existing manifests remain authoritative; image files are linked rather than copied.
  The full private archive is still external and is not a website build dependency.
**Owner.** [build_photo_catalog.py](../devel/build_photo_catalog.py),
  [README.md](photos/README.md), and the variant layout stylesheets in
  `design_d_revised/site_src/stylesheets/`.

### Thumbnail previews invite visits

**Decision.** Revised galleries use static thumbnails instead of a full-image viewer, with
prominent show invitations. The train selection grows to 23 with six reviewed archive views.
Original D's Rail yards card now opens a dedicated page using the same train selection.

**Why.** The owner wants a teaser for visiting club shows. Original D still linked to a
section, and the revised photo interactions emphasized image browsing rather than attendance.

**Consequence.** Original D reuses shared thumbnails at build time without duplicate source
files. Larger existing derivatives remain available for editorial use and repository review;
new train previews use 480-pixel thumbnails and at most 720-pixel larger derivatives. Show
and capture-date precision, credits, and unchanged archive originals remain preserved.

**Owner.** [train_teasers.py](../design_d/site_hooks/train_teasers.py), the shared photo manifest,
and `design_d_revised/site_hooks/data_blocks.py`.

### Compact train preview grids

**Decision.** Train thumbnails have a maximum 480-pixel edge. Revised collections keep their
verified chronological ordering, but use a continuous grid with show links in the captions.

**Why.** Thumbnail browsing should convey variety quickly. Full-width show headings previously
left large blank rows for shows with only one selected image.

**Consequence.** All 23 train thumbnails total 805,046 bytes. Browser checks verify that train
pages load only thumbnails, retain descriptive alternatives, and reach shows with JavaScript
both enabled and disabled. Preserved originals keep their original hashes.

**Owner.** The shared photo manifest and `design_d_revised/site_hooks/data_blocks.py`.

### Club photo captions

**Decision.** Public photo captions describe builds and locations without source credits or
  original-image links. Navigation uses local pages instead of the former club website.
**Why.** The owner supplied club photography for a replacement website and wants visitors
  to explore shows, rather than photo provenance.
**Consequence.** Existing repository records remain preserved; public source lists are removed.
**Owner.** `design_d_revised/site_hooks/data_blocks.py` and each design's page content.

### Concise photo captions

**Decision.** Captions name the subject and retain useful location or date context. Obvious
visual details belong in descriptive image alternatives rather than repeated caption prose.

**Why.** The owner wants confident, concise labels, including Prince's Purple Rain railcar.

**Consequence.** Original and revised D use shorter captions in galleries and the generated
repository catalog; image alternatives retain their accessibility detail.

**Owner.** `design_d/data/photos.yml` and `design_d_revised/data/photos.yml`.
