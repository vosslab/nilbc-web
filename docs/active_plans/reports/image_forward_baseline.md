# Image-forward execution baseline

## Scope and timing

This is an initial execution snapshot, not final acceptance. The user authorized implementation
and later added timeline work. This delegate edits only this report and
[image-forward-execution.md](../../../.hermes/plans/image-forward-execution.md), with ignored command
receipts under `output_checks/baseline/`. No runtime files, test definitions, host resources, Git
index, commits, pushes or deployments were changed by this delegate. Changelog and human-guidance
updates remain the manager's responsibility because those files are outside this delegate's scope.

Workspace: `/home/vosslab/nsh/nilbc-web`.
Branch: `main`. HEAD: `0d999af547c2d5fb65a74faa68378787c1d848b0`.

| Measurement | Actual value |
| --- | --- |
| Initial inspection | 2026-10-30T13:40:29-05:00 |
| Pre-command Git snapshot | 2026-10-30T13:40:43.433231049-05:00 |
| Command start | 2026-10-30T13:40:43.450389967-05:00 |
| Command end | 2026-10-30T13:41:28.931063867-05:00 |
| Post-command Git snapshot | 2026-10-30T13:41:28.932379428-05:00 |
| Pytest-reported duration | 44.62s |
| Pytest exit code | 1 |
| Actual result | 2 failed, 1616 passed |

## Command and decisive output

Executed from the repository root with stdout/stderr saved to `output_checks/baseline/pytest.log`:

```bash
source source_me.sh && python3 -m pytest tests/ -q
```

Decisive output, copied from the completed run:

```text
E     AttributeError: module 'revised_blocks' has no attribute 'collection_html'
tests/_temp/test_image_forward_collection.py:15: AttributeError

E    AssertionError: Podman disk usage is 35.54 GB; the budget is 20.00 GB. Inspect `podman system df -v` and deliberately remove stale Podman resources.
E    assert 35536877883 <= 20000000000
tests/test_podman_disk_budget.py:40: AssertionError

FAILED tests/_temp/test_image_forward_collection.py::test_collection_uses_real_count_and_album_order
FAILED tests/test_podman_disk_budget.py::test_podman_disk_usage_stays_under_20_gb
2 failed, 1616 passed in 44.62s
```

The shell receipt wrapper exited successfully after recording the failing pytest exit; that wrapper
success does not mean pytest passed.

## Failure classification

- **Active implementation RED, not historical baseline:** the temporary collection test was
  collected during parallel implementation and called a function absent from its imported module.
  The approved plan explicitly expects this initial missing-function RED. The hook changed during
  this run, so this result is neither an immutable pre-change failure nor a verdict on the later
  implementation. The owner must supply its GREEN receipt; manager must rerun integrated checks.
- **Known host-budget class, currently reproduced:** the mandatory Podman check measured
  35,536,877,883 bytes against 20,000,000,000 bytes. Its source measures machine-wide active-connection
  storage, not website behavior. [archive_broad_review.md](archive_broad_review.md) historically
  recorded 35.23 GB against the same budget; the current measured value is 35.54 GB. The mandatory
  gate is genuinely failing, not skipped or waived. No cleanup was attempted under this scope.
- No other failures were reported by this invocation. This does not prove browser, visual,
  provenance, or build acceptance.

## Worktree evidence

Before pytest, `git status --short` reported:

```text
 M docs/CHANGELOG.md
 M docs/HUMAN_GUIDANCE.md
?? .hermes/
?? docs/active_plans/IMAGE_FORWARD_D_REVISIONS.md
```

These documents and plans predate execution and were preserved. Before-run tracked diff:
`2 files changed, 20 insertions(+)` (12 changelog and 8 human-guidance lines).

After pytest, before writing this report and the ledger, status reported:

```text
 M design_d_revised/site_hooks/data_blocks.py
 M docs/CHANGELOG.md
 M docs/HUMAN_GUIDANCE.md
?? .hermes/
?? docs/active_plans/IMAGE_FORWARD_D_REVISIONS.md
```

After-run tracked diff: `3 files changed, 60 insertions(+), 3 deletions(-)`. The hook diff had
43 changed lines. Other agents own runtime changes. Ignored temporary tests are not represented
in ordinary short status; the pytest trace proves the new collection probe participated. The
before/after snapshots establish concurrent source changes, not an isolated reproducible checkout.

## Historical browser caution

Read [editorial_gallery.md](editorial_gallery.md), its commands table, and the search journey in
`tests/playwright/designs_smoke.mjs` (lines 179-186 at inspection). The journey opens original C's
search, searches for Bensenville, and opens the first Material result. The historical report records
original C search timeouts in the final suite and an unchanged retry, alongside an isolated diagnostic
that found results. [archive_broad_review.md](archive_broad_review.md) also records an earlier timeout
followed by an unchanged passing retry. This supports historical flakiness, not any current outcome.

Neither `npm test -- --capture` nor a website build was run by this delegate: the explicit concurrent
build prohibition supersedes the plan's broader A1 baseline command list for this assignment.
Current browser/search/build acceptance remains pending for coordinated sequential verification.

## Receipt locations

All paths below are repository-relative, ignored local output artifacts, not promised committed links:

- `output_checks/baseline/pytest.log`: complete 52-line pytest output and failure traces.
- `output_checks/baseline/pytest_timing.txt`: start/end timestamps and actual pytest exit code.
- `output_checks/baseline/git_before.txt`: branch, HEAD, short status and diff stat before command.
- `output_checks/baseline/git_after.txt`: timestamp, short status and diff stat after command.

All four receipts were read after execution. `git check-ignore output_checks/baseline/pytest.log`
confirmed the output location is ignored. No historical reports were overwritten. The manager owns
fresh reviews, gamma selection/implementation dispatch, final checks and subsequent ledger updates.
