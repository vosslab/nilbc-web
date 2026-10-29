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

## Published selection

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
and characters, 7 screen/story/aircraft scenes, and 5 railway views. The shared photo manifest
contains **66 photographs in total**: these 45 archive selections plus 21 pre-existing website
photographs. Repeated use of a photograph in an album, theme, or preview does not increase
this unique count. Matchstick artwork is separate, not counted as show photography.

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

Dalpha, Dbeta, and Dgamma share the complete gallery and photo data. Original A/B/C/D,
Matchstick, the guitar group image, and the existing variant treatments remain unchanged.

- `design_d_revised/data/photos.yml`: captions, alternative text, theme, show key, credit,
  and source URLs. Existing `focus` values apply to cropped theme/preview placements.
- `design_d_revised/data/photo_shows.yml`: album order, venue label, month/year, description.
  Album counts are calculated from the photos, not hand-maintained.
- `shows/gallery.md`: show navigation and seven native expandable albums. Only the newest
  album starts open. All thumbnails are local and lazy; larger images load on demand.
- `creations/index.md`: expanded theme galleries and a link to browsing by show.
- The homepage retains five category cards and a three-photo preview, not the full collection.
- The viewer supports Previous/Next, arrow keys, Escape, close button, focus return,
  loading/error feedback, and a direct-image link. It stays within the current album/theme.
- Without JavaScript, native albums and direct full-image links still work.
- Captions link back to their show album, including direct hash links that expand the album.

## Verification and historical passes

The first two passes selected three and then eight photographs. Their narrower scope was
superseded by the owner's explicit request for substantial archive-wide review and coverage.
Their originals, hashes, credits, and authorized layout changes were preserved.

Current execution results and screenshots are documented in
[archive_broad_review.md](active_plans/reports/archive_broad_review.md).
Build and browsing require neither Discord credentials nor network images.
