# Approved visual references

The club owner supplied and approved the NILBC branding and Matchstick identity below.
Preserve the supplied originals. Their placement in the starter does not constrain the
website's eventual file organization or visual composition.

## Asset inventory

| File | Role and provenance |
| --- | --- |
| [nilbc_banner.png](../ARTIFACTS/nilbc_banner.png) | Owner-supplied approved NILBC banner. |
| [NILBC_Logo_Presentation-yt-B7RhKU5QXYI.mp4](../ARTIFACTS/NILBC_Logo_Presentation-yt-B7RhKU5QXYI.mp4) | Owner-supplied presentation explaining the identity and showing Matchstick. |
| [NILBC_Logo_Presentation-yt-B7RhKU5QXYI.jpg](../ARTIFACTS/NILBC_Logo_Presentation-yt-B7RhKU5QXYI.jpg) | Supplied presentation thumbnail; contextual material. |
| [NILBC_Logo_Presentation-yt-B7RhKU5QXYI.en-orig.srt](../ARTIFACTS/NILBC_Logo_Presentation-yt-B7RhKU5QXYI.en-orig.srt) | Supplied captions; transcription may contain errors. |
| [NILBC_Logo_Presentation-yt-B7RhKU5QXYI.en.srt](../ARTIFACTS/NILBC_Logo_Presentation-yt-B7RhKU5QXYI.en.srt) | Alternate supplied English captions. |
| [matchstick_presentation_frame.png](../ARTIFACTS/matchstick_presentation_frame.png) | Full frame extracted unchanged at 00:04:19 from the supplied video. Character reference shown as a rendering, not a photograph of a physical model. |
| [nilbc_banner.png](../site_src/assets/nilbc_banner.png) | Byte-identical copy of the approved banner, included in the minimal public starter. |
| [matchstick_render_with_video_controls.png](../ARTIFACTS/matchstick_render_with_video_controls.png) | Full-body rendered mascot screenshot with video controls and captions visible. |
| [nilbc_circular_matchstick_logo.png](../ARTIFACTS/nilbc_circular_matchstick_logo.png) | Circular blue club logo with Matchstick and the full club name. |
| [matchstick_brick_model_illustration.png](../ARTIFACTS/matchstick_brick_model_illustration.png) | Full-body brick-model illustration with outlined construction details. |
| [matchstick_brick_model_render.png](../ARTIFACTS/matchstick_brick_model_render.png) | Full-body glossy brick-model rendering without video controls. |
| [matchstick_teacher_with_graduation_cap.png](../ARTIFACTS/matchstick_teacher_with_graduation_cap.png) | Matchstick wearing a graduation cap and holding a pointer beside a chalkboard. |
| [matchstick_teacher_chalkboard_presentation.png](../ARTIFACTS/matchstick_teacher_chalkboard_presentation.png) | Wider education-themed composition with Matchstick and presentation notes on a chalkboard. |

The presentation contains earlier proposals as well as the chosen identity. The owner-approved
banner and the owner's current mascot guidance take precedence over superseded proposals.
The additional owner-supplied screenshots show presentation artwork and rendered models;
they are not photographs of a physical model. Their descriptive filenames preserve the
original image bytes, including any slide text and video controls.

## Matchstick's recognizable features

Matchstick is NILBC's brick-built dragon mascot, not a generic cartoon dragon. Preserve:

- A glossy red body, head, feet, and tail, with recognizable brick construction and joints.
- Oversized eyes with a friendly, expressive, slightly goofy personality.
- Purple horns, back spikes, and tail accents.
- Blue wings and a cream/tan belly and lower jaw.
- A large head, short legs, small wings, and a curled tail.

Choose the mascot's prominence and presentation freely while keeping the established identity
recognizable. Illustrations or adaptations should retain the connection to the buildable model.

## Working digital palette

The owner supplied this provisional palette for design use on 2026-10-19. Wings use
**Dark Azure**, superseding the earlier Medium Azure suggestion. These are visual estimates
and supplied color references, not confirmed parts identifications or sampled image pixels.
Shading, lighting, and reflections change the rendered appearance. Confirm against the actual
parts list if exact LEGO color identification is needed.

| Feature | Working color name | Digital reference |
| --- | --- | --- |
| Body, head, feet, tail | Red | `#C91A09` |
| Belly and lower jaw | Tan | `#E4CD9E` |
| Wings | Dark Azure | `#078BC9` |
| Horns, spikes, tail accents | Medium Lavender | `#AC78BA` |
| Eyes | White | `#FFFFFF` |
| Pupils | Black | `#05131D` |

These references describe Matchstick. They do not mandate the site's backgrounds, typography,
or complete palette. Choose accessible color combinations for actual interface elements.

## Sources and credits

The original files came from the club owner. Artist attribution and a source parts list were
not supplied. Keep that provenance with derivatives and distinguish new work from supplied
brand assets. Do not infer an external asset's license from the repository's general licenses.

For new photography or other external assets, record the source, credit, and permitted use.
The [existing club website](https://niltc.org/) contains public club material to investigate.

## Imported design assets

The four designs retain their own asset files and public credits, without image processing,
font substitution, deduplication, or changes to their visual treatments during integration.
The original artwork above remains in ARTIFACTS. Import hashes are recorded in
[design_imports.json](design_imports.json).

- A: [CREDITS.md](../design_a/site_src/CREDITS.md). Its Matchstick derivative removes slide
  debris from the supplied render while retaining the character. Club photographs retain
  their downloaded bytes.
- B: [credits.md](../design_b/site_src/credits.md). Its circular logo and photographs retain
  their downloaded bytes. Barlow Condensed and DM Sans license files accompany the fonts.
- C: [sources.md](../design_c/site_src/sources.md). Its cropped Matchstick render, club
  photographs, and locally served Syne and Newsreader fonts retain their original entry credits.
- D: [credits.md](../design_d/site_src/about/credits.md) and
  [photos.yml](../design_d/data/photos.yml). Its processed mascot images, WebP photographs,
  and Fredoka/Nunito font files retain the original entry's derivatives and license texts.

This import does not establish new redistribution rights. Original per-entry asset-generation
utilities remain in the read-only competition checkouts; the imported demos build directly from
their supplied assets and do not require those utilities or a network connection.

## D revisions and flyer

D&alpha; and D&beta; share the copied assets and photo manifest in `design_d_revised/`.
The guitar photograph featured on their homepage is D's existing `club_group_2026.webp`,
derived from the same club photograph used by A, B, and C. Existing credits remain with it.

The [flyer master](../marketing/nilbc_club_flyer.svg) embeds the unchanged approved circular
logo from ARTIFACTS and B's Barlow Condensed Bold and DM Sans Regular/Bold font bytes.
The source fonts and SIL Open Font License files remain in `design_b/site_src/assets/fonts/`.
Its QR code is new vector artwork encoding `https://niltc.org/`. The SVG is editable; the PDF
and raster previews are generated outputs. See [../marketing/README.md](../marketing/README.md).

### Selected photo treatments, 2026-10-27

Kalam Bold and `OFL_KALAM.txt` were downloaded unchanged from the Google Fonts `ofl/kalam`
directory. The font is loaded locally only by beta and gamma's shared photo-frame stylesheet.
The frames, feathered edge, and captions are CSS/live text; original photographs are unchanged.

`frog_cutout.webp` derives from the existing `frog.webp`, whose source is
`https://niltc.org/wp-content/uploads/2017/02/frog.jpg`. That URL indicates an archive upload
folder, not a verified creation date or builder. The owner confirmed that older archive photographs are appropriate alongside more recent
Instagram images. Public captions describe the models without a special age warning.

The cutout was made with the installed rembg CLI, `isnet-general-use`, followed by alpha-mask
cleanup and trimming in ImageMagick. No model parts were generated. The original photo stays
unchanged and is still the gallery-link destination. The failed u2net frog and Unikitty
experiments are not published. Build/deploy needs neither rembg nor its model weights.
