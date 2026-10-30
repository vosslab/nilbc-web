# Photo refinement and curation

Date: 2026-10-30. No commit or deployment.

## Decisions

Reviewed the six train candidates from the local metadata and image-forward ledgers against their original frames. A candidate entered the public set only when its completed rail exhibit and its show context were both supported. Two Arlington images meet that bar: their message IDs are the same post-show photo batches as already selected Arlington photographs, whose provenance records point to the corroborating show-context messages. Those references establish the event and club exhibition context; they do not identify a builder.

| Attachment | Decision | Evidence |
| --- | --- | --- |
| `1450178339338715288` | Selected as `arlington_multitrack_2025` | Full frame shows a blue-and-orange Metra engine, black-and-red steam-style engine, passenger coaches, tank cars, freight cars, and completed parallel tracks. Message `1450178341452644392` matches the already selected Arlington dinosaurs batch. |
| `1449994464465653761` | Selected as `arlington_cnrail_8744_2025` | Full frame shows blue CN Rail 8744 on finished track with additional rail equipment and parallel tracks. Message `1449994471168020511` matches the already selected Arlington Santa batch. |
| `1470117005997641900` | Excluded for now | The CB&Q hopper and neighboring cars are visually strong, but the local metadata reports no event date and the available candidate record does not provide corroborating show-context references. A Schaumburg channel label and upload the next day do not establish eligible club-show provenance. SHA-256: `7aab9e7f27d81fd0d4b61de04d916c66222ae36179a0044a78f6fa66137b0296`. |
| `1446832997285363722` | Excluded for now | The North Pole tank car is a finished, distinctive subject, but the named Aurora channel has no corroborated event date in the metadata; its 2025-12-06 upload predates the 2026-03-21 channel label. The upload and depicted holiday wording cannot resolve that conflict. SHA-256: `aaa359c32e52e4943a002ae948d661cc82fb6b3a1a4d6b345fa76436a50523b5`. |
| `1437887990293856327` | Excluded | Promotional poster for a future Arlington show. Its inset train image is not evidence that the model was photographed at the completed show. SHA-256: `3a45ddc4283983f3b1a9374918b3c1b96febc746cfad5ff6114dcee540bebbb2`. |
| `1437887990675280074` | Excluded | Promotional poster for a future Arlington show, with a different inset train. It is not a show photograph. SHA-256: `892e6e523af307febc0fcd0f17cb68fcc80ac651d31f3d11c1234508fd8ce179`. |

The Arlington event display label and `2025-12` event precision come from the existing verified show record. No Discord upload timestamp was presented as a capture date; the two new source images have no embedded capture-date metadata. The uploader credit is retained without a photographer or builder claim.

## Published selection

- Added the two Arlington train images to the shared photo manifest and explicit show sequence. The Arlington album now has 9 images; sequence coverage remains complete and duplicate-free.
- The shared manifest now contains 73 distinct photos: 52 archive show photos across seven dated shows and 21 pre-existing site photos. The train theme has 17 records.
- Put `northbrook_purple_train_2026` first in the three-photo homepage selection, followed by the Northbrook streetscape and Ela castle. This keeps the homepage compact and gives its lead a train subject; other featured themes remain present in the full collections.
- Updated the Purple Rain railcar caption and alt text to name the visible piano shape, lettering, and musician. Added focal positions for the streetscape, Purple Rain railcar, and both new train photos. Direct review confirmed the existing castle, spacecraft, and dog focal points for the castle, screen-and-story, and creatures themes, respectively.
- Updated the Arlington show description to reflect its winter, castle, dinosaur, and rail subjects.

## Originals and derivatives

Both source originals were copied unchanged from `/home/vosslab/nsh/niltc_archive_shows/` and matched the local metadata SHA-256. Public derivatives apply EXIF orientation, convert to RGB WebP, resize without upscaling to 640 and 1,600 pixels on the long edge, use quality 78/82 and method 6, and omit metadata. The full-size originals remain in the non-deployed `ARTIFACTS` archive.

| File | Dimensions | SHA-256 |
| --- | ---: | --- |
| `ARTIFACTS/discord_archive_shows/arlington_multitrack_2025.jpg` | 4032 × 3024 | `6457594e4fec094a4d8073299839415f38b0892047c50f757fe37b8e18cc8308` |
| `design_d_revised/site_src/assets/photos/arlington_multitrack_2025_thumb.webp` | 640 × 480 | `c27b133bc875631d90f5ff722822048a564e196a206734de6e93fdbb93fb8843` |
| `design_d_revised/site_src/assets/photos/arlington_multitrack_2025.webp` | 1600 × 1200 | `251e2ccb7aa93a4cd113bf65021f274c4bd965551da05a206123df1c733c421d` |
| `ARTIFACTS/discord_archive_shows/arlington_cnrail_8744_2025.jpg` | 5712 × 4284 | `45411376a4aa79f44f673e902b5aa7c18a119a487039a480d4f138f72aeb7cff` |
| `design_d_revised/site_src/assets/photos/arlington_cnrail_8744_2025_thumb.webp` | 640 × 480 | `67cb6103aebb3adb2ce5f565dc8cc878e5803e64259ca159539d782ec29d17c6` |
| `design_d_revised/site_src/assets/photos/arlington_cnrail_8744_2025.webp` | 1600 × 1200 | `adf9814ffa00963788c3b2b58354c967d8cc8a67ae540e369b7f1c87bd920257` |

## Checks and limits

A focused Python assertion pass parsed both YAML manifests, confirmed 73 unique photo IDs, checked every photo-to-show reference and every show's exact sequence coverage, matched both preserved original hashes, and decoded all four WebP derivatives to verify dimensions and absence of EXIF. `git diff --check` passed for the manifests and provenance/review ledgers.

No full site build, browser review, complete archive rehash, or repository test suite was run for this curation pass. Source ownership beyond the corroborated show context and general external redistribution rights remain unverified.
