# Archive metadata parser fix

## Change

IPTC parsing now rejects incomplete dataset headers, truncated extended-length
fields, and payloads shorter than their declared length. `image_record` converts
malformed IPTC into an explicit per-image warning and leaves the IPTC section
empty, while preserving the record and other metadata.

## Evidence

- `source source_me.sh && python3 -m pytest tests/test_archive_metadata.py -q` —
  6 passed.
- Reindexed `/home/vosslab/nsh/niltc_archive_shows/metadata.json` with
  `devel/index_archive_metadata.py` — 1,336 records and 4 exact duplicate
  groups. The existing archive has no malformed IPTC records.
- Added rejection coverage for a truncated dataset header, a two-byte extended
  length with one length byte, and a payload shorter than its declared size.
  Added record-level coverage that confirms malformed IPTC produces a warning
  while EXIF metadata remains present.
