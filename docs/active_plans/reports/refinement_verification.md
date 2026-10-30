# Page refinement verification handoff

Date: 2026-10-30. This report records final integration evidence and the remaining host-only
pytest failure.

## Scoped evidence accepted

- Metadata: [archive metadata report](refinement_metadata.md) accounts for all 1,336 images,
  four exact duplicate groups, 32 malformed-XMP warnings, and no EXIF `DateTimeOriginal` values.
  The [IPTC parser fix](refinement_metadata_fix.md) has six focused tests passing. Indexing
  retained every record; malformed IPTC is isolated as a warning.
- Alpha and beta: [variant report](refinement_alpha_beta.md) records strict builds, ten-route
  desktop/phone browser review, no horizontal overflow, and representative inspected captures.
- Shared content: [content report](refinement_content.md) records strict builds for all three
  revisions and generated-HTML assertions for navigation, photos, dates, shared calls to action,
  timeline links, and full-image access.
- Curation: [curation report](refinement_curation.md) records 73 distinct photos: 52 archive
  photos and 21 existing site photos. Seventeen records are trains. Two Arlington train images
  were added after show-context review; Purple Rain leads the curated homepage photo list.
  The report does not establish photographer, builder, ownership, or general redistribution rights.
- Gamma: [final refinement report](refinement_gamma.md) records the exhibition-floor direction,
  18 routes at five widths (90 checks), five interaction journeys, and zero browser page errors
  or local HTTP failures. Its earlier blocked specification attempt predates this final probe.
  Gamma specification and scoped quality reviews are accepted.

## Whole-repository checks

The initial full pytest run recorded 1,664 passes and three failures. The two scoped failures
were fixed, and the targeted rerun passed 12 tests. An intermediate full run recorded 1,667
passed and one failure in 7.71 seconds. The latest complete run recorded 1,671 passed and one
failure in 7.38 seconds. Its `tests/test_podman_disk_budget.py` failure came from Podman being
unable to change permissions under the sandbox's read-only `/run/user/1000/libpod`. A separate
read-only check outside the sandbox measured 35.72 GB against the 20 GB limit. No cleanup was
authorized or needed for this website task. The repository test result is not green. Details:
[test reconciliation](refinement_test_reconcile.md).

The final whole-site browser run passed 172 desktop/mobile page checks and 25 journeys across
designs A, B, C, D, D-alpha, D-beta, and D-gamma. It reported no browser errors or failures. Run:

```bash
node tests/playwright/designs_smoke.mjs --capture
```

The recorded results are in `output_checks/designs_report.json`. The Gamma card hit-area fix
was included in this run. Gamma's scoped route probe remains separate evidence.

The mobile drawer fix passed a fresh independent review across alpha, beta, and gamma. Real Enter
and Space presses each toggle once with `aria-expanded` in sync; pointer activation works, and the
desktop toggle is removed from the tab order. The Escape probe started with the drawer already
closed and retained focus; it does not establish that Escape closes an open drawer.

The final integration review found no remaining defects. The original A-D sites remain unchanged.
No commit or deployment occurred.

## Boundaries

The local archive, metadata index, image-forward review ledger, and train-candidate ledger live
outside Git at `/home/vosslab/nsh/niltc_archive_shows/`. Do not copy private discussion or the
full archive into the site or deployment. Upload timestamps and embedded metadata do not prove
capture dates. Rights and source identity remain unknown unless the individual provenance record
establishes them. No commit or deployment was performed.
