# Gallery count correction

Removed the stale show and photograph totals from the shared D revision gallery metadata and intro. The intro now explains how visitors browse albums and open full-frame photos, without depending on a changing count.

## Verification

- Strict alpha build passed to `output_checks/refinement_count_fix/d-alpha/`.
- The rendered gallery contains the new album and viewer guidance and no stale totals.
- `git diff --check` passed.
- Current D revision source has no other gallery count copy. Other repository matches describe documented historical snapshots and were left intact.

## Limits

Only the alpha variant was built; beta and gamma share this source page. No browser or visual review was run.
