# Refinement test reconciliation

The initial full pytest run recorded 3 failures and 1,664 passes. Two failures were in this work's
scope:

- The temporary collection check expected plain divider text. Collection headings now include links,
  so the check compares visible heading text while retaining its label-order assertion.
- The human-guidance format check found one four-line bullet. The bullet is now three lines and
  retains the metadata review, visual assessment, design differentiation, and gamma-manager
  direction.

Targeted verification passed: `source source_me.sh && pytest -q tests/_temp/test_image_forward_collection.py tests/test_guidance_doc_format.py` (12 passed).

After those fixes, the updated full run recorded 1,667 passed and one failed in 7.71 seconds.
The remaining failure was `tests/test_podman_disk_budget.py`: Podman could not change permissions
under read-only `/run/user/1000/libpod`. A separate read-only check confirmed 35.72 GB against the
20 GB budget (one failure in 37.56 seconds). No cleanup was authorized or needed for this website
work; the host-runtime failure was left unchanged.
