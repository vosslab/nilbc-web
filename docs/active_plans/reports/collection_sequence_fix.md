# Collection sequence validation

## Scope

`collection_photos` now validates each show sequence against the exact set of photos associated with that show, including the empty-set case. IDs must be strings, unique, and known; an empty show must have an empty sequence. `show_gallery_html` uses the same validator. Validation errors name the show ID. The chronology fixture now associates every synthetic sequence entry with its actual show. Editorial sequence order and explicit `event_date` ordering remain unchanged; archive photos still follow the show sections.

## Verification

- RED: `source source_me.sh && python3 -m pytest tests/_temp/test_image_forward_collection.py -q` — 2 failed, 8 passed. The empty-show sequence containing a valid photo associated with another show was accepted; the synthetic chronology fixture also failed exact-set validation because one photo lacked its matching show record.
- GREEN: `source source_me.sh && python3 -m pytest tests/_temp/test_image_forward_collection.py -q` — 10 passed. This includes valid foreign-photo, unknown-ID, and duplicate-ID rejection for the empty show.
- `source source_me.sh && python3 -m py_compile design_d_revised/site_hooks/data_blocks.py tests/_temp/test_image_forward_collection.py` — passed.
- `git diff --check -- design_d_revised/site_hooks/data_blocks.py tests/_temp/test_image_forward_collection.py docs/active_plans/reports/collection_sequence_fix.md` — passed.

The final implementation/tests are limited to the hook and its temporary test module; this report is the requested additional artifact.
