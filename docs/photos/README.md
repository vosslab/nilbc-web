# Photo catalog

Generated from the shared site manifests. Edit the manifests, then regenerate; do not edit these sheets.

79 selected photo records. Browse the theme contact sheets below or [shows.md](shows.md).

| Theme | Photos |
| --- | --- |
| [Rail yards](trains.md) | 23 |
| [Cities and landmarks](city.md) | 22 |
| [Screen and story](screen.md) | 10 |
| [Creatures and characters](creatures.md) | 12 |
| [The club](club.md) | 3 |
| [Castles](castle.md) | 9 |

## Metadata and editing

- [inventory.yml](inventory.yml): dimensions, byte sizes, SHA-256 hashes, dates, categories, and crop focus.
- [photos.yml](../../design_d_revised/data/photos.yml): captions, alt text, categories, credits, and homepage picks.
- [photo_shows.yml](../../design_d_revised/data/photo_shows.yml): verified event dates and album order.
- [provenance.json](../../ARTIFACTS/discord_archive_shows/provenance.json): original source and processing evidence.
- [review.md](review.md): folder-by-folder review coverage for the full archive.
- [review.json](../../ARTIFACTS/discord_archive_shows/review.json): source review evidence.

## Selection boundaries

This catalog covers the selected website photographs, not all 1,336 archive records.
The full archive and its metadata index stay outside Git. No new photo rights are implied;
uploader credit does not identify the photographer or builder. Event dates are not capture dates.
Existing site photos without preserved archive originals retain their original source credits.
See [DISCORD_ARCHIVE.md](../DISCORD_ARCHIVE.md) for the evidence and permitted demo-use scope.

## Regenerate

```bash
source source_me.sh && python3 devel/build_photo_catalog.py
source source_me.sh && python3 devel/build_photo_catalog.py --check
```

The catalog links to existing image files and adds no duplicate image copies.
It lives in repository documentation and is not included in the club website.
