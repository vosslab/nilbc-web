# Archive metadata and candidate review

## Metadata extraction

Ran the local indexer against the preserved collection at
`/home/vosslab/nsh/niltc_archive_shows/`. It read all 1,336 rows from `downloads.json` and
wrote `metadata.json` atomically beside that source catalog. Each record keeps channel,
attachment and message IDs, original filename/path, catalog SHA-256, upload timestamp, media
type, advertised/received byte sizes, size-match status, and download/decode status. It records
format, encoded and orientation-adjusted dimensions, aspect ratio, selected EXIF, IPTC, and XMP
fields, capture date, and extraction warnings. Signed CDN URLs and uploader identifiers are not
copied into the output.

- 1,336 image records; all have decoded format and dimensions.
- 947 JPEG, 361 PNG, 15 MPO, 9 GIF, and 4 WebP files.
- Four exact SHA-256 duplicate groups; all eight attachment/path references are retained.
- No EXIF `DateTimeOriginal` values were found. XMP `CreateDate`, IPTC creation fields, and
  other embedded date values remain under their source metadata namespaces and do not become
  capture dates. Upload timestamps stay separate. Event dates are null; show/channel labels
  were not converted into event dates by this extraction.
- Seventeen records have at least one extracted descriptive metadata field. Thirty-two records
  have malformed XMP, recorded as warnings; 15 MPO files are flagged as an uncommon decoded
  format. Neither condition drops the image record.
- Exact duplicates are grouped by the SHA-256 already recorded in the archive download catalog;
  this pass did not rehash the 2 GB collection.

The utility reads image headers and metadata without pixel-transposing or rewriting the
preserved image files. EXIF orientation is applied to reported dimensions only. Metadata is
descriptive and was not treated as proof of ownership, capture date, or exhibit date.

## Visual candidates

The separate `image_forward_review.json` ledger now records a subject, theme, overview, detail,
crop guidance, and placement suitability for reviewed items across trains, city, castle, screen,
and creatures. Theme values match the shared photo manifest. It preserves existing review entries
and adds four full-frame-reviewed selections already in the website archive plus four pending
train candidates from the earlier batch-3 review. Pending train rows remain `candidate`; they are
not public selections.

Five full frames were inspected during this pass: Northbrook's purple rail vehicle, the Ela Area
Japanese storefront street, castle, spacecraft display, and white caped dog. The four pending
train additions use the earlier full-frame reviews in `train_review_batch_3.json`, which were
cross-checked against their contact-sheet review entries:

- CB&Q 189011 hopper with textured load: strong freight detail; wide crop should preserve wheels
  and adjacent rail cars.
- North Pole Railroad tank car: distinctive rolling stock; keep the full tank and wheels.
- Arlington blue CN Rail #8744: focused locomotive view; check against other #8744 images before
  adding a duplicate subject.
- Arlington multitrack display: useful collection overview; use a wide crop with both locomotives.

The record names and exact attachment references are in the external ledger. These are visual
recommendations only: the added train candidates still need provenance and show-eligibility
review before any public selection. Cropping guidance is editorial; no image was processed or
published during this pass.

## Commands and evidence

Commands run from the repository root:

```bash
source source_me.sh && python3 -m pytest tests/test_archive_metadata.py -q
source source_me.sh && python3 devel/index_archive_metadata.py
```

The focused tests passed (4 tests). The indexer reported `Indexed 1336 images; 4 exact duplicate
groups.` Candidate visuals were checked from local full-size archive images, without network
requests or private message retrieval. The prior batch-3 review supplies the contact-sheet and
full-frame evidence for its four train candidates. This review does not establish author
identity, license, or exact camera/show dates, and it does not authorize publication.
