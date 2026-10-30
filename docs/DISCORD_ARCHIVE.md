# Discord show archive

## Scope and ordered stages

The owner authorized read-only use of the existing NILTC bot for guild
`1014224389300043888`, exact category Archive Shows `1204459631016149082`.
No messages, permissions, credentials, or server configuration were changed.
The full collection was copied before organization and curation. This pass uses those
existing local copies, without redownloading images.

### Stage one: copy

Durable full archive: `/home/vosslab/nsh/niltc_archive_shows/`, outside this repository
and the deployment tree. Do not add that directory to Git or deploy it.

- 34 direct child text channels inventoried; no non-text children were returned.
- 8,167 messages paginated; every channel reached an empty terminal page.
- 1,336 unique image attachment IDs copied; zero download or image-decode failures.
- 2,039,029,563 received bytes preserved without local image edits.
- 401 Discord metadata byte counts differ from CDN response bytes. Responses decode;
  repeat and `download=1` / `format=original` requests returned the same bytes for a
  representative mismatch, with a Discord image-transform header. These are unchanged
  CDN-served sources, not a claim to recover pre-upload camera bytes. Both sizes and
  SHA-256 remain recorded. Five of the current 45 selections have this documented mismatch.

Local records: `channels.json`, `pagination.json`, `inventory.json`, `downloads.json`, and
`summary.json`. The catalog records uploader, timestamp, message and attachment IDs,
filename, source permalink, CDN URL, local path, sizes, and hash. Full catalogs contain
private identifiers and expiring URLs; keep them local. No raw discussion histories are
included in the repository, deployed site, or durable collection.

### Stage two: organize

Originals occupy 32 nonempty channel folders; two channels had no image attachments.
Attachment-ID filename prefixes avoid collisions. All 1,336 sources decode.
The 72 contact sheets in `contact_sheets.json` cover the collection in channel catalog order.
Duplicate visual content remains preserved as distinct source attachments in the full archive.

### Stage three: broad review

All 72 sheets were individually visually reviewed, covering all 32 nonempty folders and
1,336 tiles. Forty-six promising original frames were inspected in this pass, including
one already selected streetscape. Thirty-seven new photographs were admitted; eight earlier
selections remain, for **45 distinct archive photographs across seven shows**.

Very large originals produced misleading detail-only descriptions during inspection. An
uncropped, EXIF-oriented 1,400-pixel preview of each candidate was therefore inspected to
verify the full composition. Source originals remain untouched. Contact-sheet identifications
were corrected against these frames: for example, a presumed dragon was a giant spider,
and a supposed station was a drive-through coffee shop. Captions follow the verified frames.

The machine-readable review ledger is `ARTIFACTS/discord_archive_shows/review.json`.
It records all sheet paths and hashes, covered index ranges, folder-level findings,
individual candidate decisions, and exclusions. Coverage counts are calculated from the
local catalog, not estimated. Not all 1,336 originals received individual full-frame review;
all contact-sheet tiles did.

## Publication boundary

The owner's explicit correction is **completed club work photographed at shows only**.
Home/workbench photographs are excluded even if a model is finished. Also excluded:
setup/teardown, WIP track, planning diagrams, personal/visitor-focused photographs, private
notes, memes, promotional overlays, ambiguous photographs, and other LUG exhibits.

An Archive Shows channel name is not ownership evidence. Convention folders contain work
from multiple exhibitors; attractive models without a secure club connection stay unpublished.
Promotional cards do not prove that their inset model attended the advertised event.
Many early folders contain few or no suitable finished-exhibit photographs.

For the seven selected library shows, read-only REST checks corroborated contemporary photo
batches with post-show photo requests, club exhibit discussion, completion messages, and
host feedback. Exact context message IDs are retained in each provenance record; raw text is
not copied into the repo or site. The Northbrook skyscraper also visibly carries the club sign.
Each selected photograph shows a completed model/display, corroborated by that batch context,
not merely by category membership. Ambiguous candidates were withheld rather than filling a quota.

Specific rejected full-frame candidates include a soft whale close-up, a space scene dominated
by a puzzle backdrop, a crowded car view, a repeated Ela farm detail, a tightly cropped cattle
scene with an unfinished appearance, a cluttered shoe-brand display, an ambiguously framed
aircraft table, and a tower with unfinished-looking surroundings. The barn-raising photograph
is a completed farm vignette depicting construction, not a workbench progress photograph.

## Historical selection snapshot

The following selection counts describe the earlier review snapshot documented at that time.
They are historical evidence, not a claim about the current manifest or final acceptance.
For current editorial choices, use `design_d_revised/data/photos.yml` and
`design_d_revised/data/photo_shows.yml`; for updated review status, consult
`docs/active_plans/reports/`. Broader curation and final acceptance remain pending; this is
not a completed or deployed collection.

| Show | Date | Archive photos |
| --- | --- | ---: |
| Northbrook Public Library | October 2026 | 9 |
| Ela Area Public Library | September 2026 | 10 |
| Algonquin Area Public Library | May 2026 | 6 |
| Wheaton Public Library | April 2026 | 4 |
| Arlington Heights Memorial Library | December 2025 | 7 |
| Oswego Public Library | October 2025 | 5 |
| Barrington Area Library | September 2025 | 4 |
| Total | | 45 |

The archive selections cover 15 city/landscape scenes, 9 castle/market scenes, 9 creatures
and characters, 7 screen/story/aircraft scenes, and 5 railway views. At this historical checkpoint, the shared photo manifest contained 66 photographs in total:
these 45 archive selections plus 21 pre-existing website photographs. Repeated use of a
photograph in an album, theme, or preview did not increase that unique count. Matchstick
artwork was separate, not counted as show photography. This snapshot total is not the current
manifest count; read the current manifest/report instead.

## Current refinement checkpoint

The 2026-10-30 manifest contains 73 distinct photos: 52 archive selections across the same seven
dated shows and 21 existing site photographs. Seventeen manifest records have the train theme.
Two Arlington train selections were added after full-frame review and match to already selected
post-show photo batches with corroborating show-context references. Their records support the
event and club-exhibition context, not an individual builder identity. Purple Rain leads the
manual three-photo homepage sequence. See
[refinement_curation.md](active_plans/reports/refinement_curation.md) for the selection evidence
and [refinement_verification.md](active_plans/reports/refinement_verification.md) for the
integration status. This is a current review checkpoint, not a claim of final acceptance or
deployment.

The completed-show selection rule continues to exclude candidates whose show context is not
corroborated, even when the image is visually strong. Uploader attribution is not photographer,
builder, ownership, or a general redistribution license. Source and rights remain unknown where
the individual provenance record does not establish them.

Uploaders are Kerbear, Andertoons, and Jason C. Uploader does not mean photographer or builder.
Use is owner-requested for the demo, not a new external redistribution license. Existing club
website photographs and their credits remain intact.

The exact source manifest is `ARTIFACTS/discord_archive_shows/provenance.json`. Each record
includes original filename, source channel/message/attachment IDs, source permalink, local
archive path, received and advertised sizes, SHA-256, preserved repository original,
processing, rights limitations, context references, and derivative hashes/dimensions/sizes.
Expiring CDN URLs and uploader account IDs are omitted from the selected manifest.

## Image processing and weight

Selected unchanged originals are preserved under `ARTIFACTS/discord_archive_shows/` only.
They total 95,200,225 bytes; they are not deployed. Public WebP derivatives live under
`design_d_revised/site_src/assets/photos/` and total 13,277,066 bytes, including
2,755,140 bytes of thumbnails across all 45 archive selections.

For the 37 new photographs: apply EXIF orientation, convert to RGB, resize with Lanczos to
longest edges 1,600 and 640 pixels, then WebP quality 82 and 78 respectively, method 6.
The earlier eight retain their 1,600/720-pixel quality-82 derivatives. No source crop,
synthetic fill, background removal, or source-byte modification. Derivatives omit EXIF.
The album thumbnails contain the full frame; theme/homepage thumbnails may crop through CSS.
The full-image viewer always opens the uncropped optimized frame, never an external CDN URL.

## Website and editing contract

Dalpha, Dbeta, and Dgamma share the photo data and gallery source. Original A/B/C/D and
Matchstick remain unchanged; image-forward revisions and curation are still being reviewed.

- `design_d_revised/data/photos.yml`: captions, alternative text, theme, structured `show` key,
  credit, source URLs, and the manually curated `homepage_photos` ID list. Each show photo's
  `show` must match a key in `photo_shows.yml`; do not infer association from text or filenames.
- `design_d_revised/data/photo_shows.yml`: show labels/descriptions and the explicit editorial
  `sequence`, plus `event_date` when verified. Quote `event_date` as ISO `'YYYY-MM'` for verified
  month-only precision, or `'YYYY-MM-DD'` only for a verified day. Never infer capture dates
  from Discord upload times or file metadata. Dated collections sort newest-first by event date;
  each show's sequence controls its internal order. Undated archive entries come last.
- `site_src/index.md`: the `/// featured-photos` block renders `homepage_photos` in list order.
  To refresh the homepage, edit that short ID list manually; it does not auto-pick recent uploads.
- `site_src/shows/gallery.md`: `/// show-gallery` renders the show albums. The dedicated trains,
  cities, screen-and-story, castles, and creatures pages use `/// collection | THEME` for complete,
  newest-first, thumbnail-first views; opening a full-size image/viewer is optional.
- `site_src/about/timeline.md`: one shared editable timeline, grounded in the public sources
  cited there. Preserve source-level date precision; leave the identity/rebrand chapter undated
  unless a public launch date is verified. No upload timestamp establishes a photo's capture
  date. Avoid implying an unverified launch event.
- Alpha, beta, and gamma share source and hooks. Alpha loads common CSS then `alpha-layout.css`;
  beta and gamma inherit MkDocs settings but define their own CSS lists, layering their variant
  styles over common styles. Gamma includes `photo-frames.css`; beta includes `beta.css`; each
  has its own layout stylesheet. Static data blocks and local assets need no external API at
  runtime.
- Full-image viewing is an enhancement; collection grids remain local-thumbnail-first. No
  Discord login or image API is needed to build or view the site.

## Verification and historical passes

The first two passes selected three and then eight photographs. Their narrower scope was
superseded by the owner's explicit request for substantial archive-wide review and coverage.
Their originals, hashes, credits, and authorized layout changes were preserved.

Execution results and screenshots from the earlier broad-review pass are documented in
[archive_broad_review.md](active_plans/reports/archive_broad_review.md).
That dated report is a historical checkpoint, not final acceptance evidence. Check the latest
report in `docs/active_plans/reports/` for ongoing work. Build and browsing require neither
Discord credentials nor network images. No final acceptance or deployment is claimed here.
