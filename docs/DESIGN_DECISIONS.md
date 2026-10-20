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
