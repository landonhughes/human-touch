# Yolo sports-ad comparison

Two fictional Yolo water-bottle ads built with **Hyperframes 0.8.84**. Both are 12-second, 1080 × 1080, 30 fps, silent H.264 MP4s.

| Hyperframes only | Hyperframes + Human Touch |
| --- | --- |
| [![Baseline](../without-skill/yolo-ad.gif)](../without-skill/yolo-ad.mp4) | [![Directed](../with-skill/yolo-ad.gif)](../with-skill/yolo-ad.mp4) |

The GIF previews above animate directly in GitHub. Click either for the full-resolution MP4, or use the [local gallery](../index.html) for video controls. GitHub README pages do not embed the local HTML video player.

## Shared brief

The user requested an ad with both skills and another without Human Touch, then selected **energetic sports ads**. Duration, square format, silent playback, colors and copy were production choices. Both use the same generated bottle image, fonts, words, and framework. The baseline was not instructed to be worse.

Copy: “GO ALL IN.” → “TAKE A BREATHER.” → “GO AGAIN.” with “Yolo”, “WATER BOTTLE”, and “MEET YOLO”. The bottle is fictional; no specifications or performance claims are implied.

## Direction

The baseline uses a centered product showcase, a rotating outline, a blue panel, sequential headline reveals, and continuous bottle drift.

Human Touch uses an asymmetric track-inspired layout and grounded product, with fast entrances followed by a still water-break beat. It keeps the energetic sports style while making the product, message, and closing action easy to follow.

Both were authored in the same agent session, not independent skill-disabled runs. This is a showcase of specific art-direction decisions, not a controlled benchmark. Hyperframes has its own design guidance in both versions.

## Editable projects

- [Baseline composition](without-skill/index.html), [brief](without-skill/BRIEF.md), [design](without-skill/design.md).
- [Human Touch composition](with-skill/index.html), [brief](with-skill/BRIEF.md), [design](with-skill/design.md).
- [Shared image-generation prompt](asset-prompt.json). The transparent bottle PNG was generated once with the built-in image tool and copied unchanged into both projects. Each project records its local media adoption in `.media/`.
- [Ad briefs in the prompt manifest](../prompts.json).

Text motion adapts Hyperframes' `line-by-line-slide` registry primitive, with `spring-pop-entrance` and seek-safe GSAP transform patterns. The registry source and lock hash are retained in the baseline project. The directed version adapts the same reveal mechanism with its own layout and timing.

## GitHub previews

The GIFs contain each full 12-second ad at 540 × 540 and 15 fps, with infinite looping. They are conversions of the existing Hyperframes MP4s; the source compositions were not changed.

```sh
ffmpeg -i yolo-ad.mp4 -filter_complex "fps=15,scale=540:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=128[p];[b][p]paletteuse=dither=bayer:bayer_scale=3" -loop 0 yolo-ad.gif
```

## Reproduce

Requires Node.js 22+, FFmpeg/FFprobe on PATH, and Hyperframes' Chrome renderer. The package scripts pin Hyperframes 0.8.84. Initial setup may download the CLI, browser, GSAP, and fonts; final MP4s play offline.

From either project directory:

```sh
npm run check
npm run dev
npm run render -- --quality delivery --fps 30 --output yolo-ad.mp4
```

Both projects have one continuous composition with three copy beats. The single-scene structure intentionally retains Hyperframes' advisory `nested_structure_needs_subcomposition` warning. There are no check errors. The directed text has explicitly allowed overlap for Oswald's font-metric boxes; inspected glyphs remain visibly separated.

Verification: Hyperframes runtime/layout/contrast checks passed; early, middle and closing frames were visually reviewed. FFprobe confirmed 360 frames, 30 fps, 1080 square and exactly 12 seconds for each output. No audio track is included. The posters are extracted from the actual encodes at 9 seconds.
