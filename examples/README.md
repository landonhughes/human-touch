# Human Touch examples

Eight briefs, each with a baseline and a version art-directed with [Human Touch](../skills/human-touch/SKILL.md). Click any preview to inspect the original.

| Brief | Without the skill | With Human Touch |
| --- | --- | --- |
| Cookie website · pink and black | ![Baseline cookie website](without-skill/cookie-website.png) | ![Human Touch cookie website](with-skill/cookie-website.png) |
| Shoes website · red and black | ![Baseline shoes website](without-skill/shoes-website.png) | ![Human Touch shoes website](with-skill/shoes-website.png) |
| Calm watercolor sunset | ![Baseline watercolor sunset](without-skill/watercolor-sunset.png) | ![Human Touch watercolor sunset](with-skill/watercolor-sunset.png) |
| Pixel-art lion | ![Baseline pixel-art lion](without-skill/pixel-art-lion.png) | ![Human Touch pixel-art lion](with-skill/pixel-art-lion.png) |
| Polar app mascot | ![Baseline Polar mascot](without-skill/polar-mascot.png) | ![Human Touch Polar mascot](with-skill/polar-mascot.png) |
| Mellow app icon | ![Baseline Mellow app icon](without-skill/mellow-icon.png) | ![Human Touch Mellow app icon](with-skill/mellow-icon.png) |
| Yolo sports ad · 12 seconds | [![Yolo baseline poster](without-skill/yolo-ad-poster.png)](without-skill/yolo-ad.mp4) | [![Yolo Human Touch poster](with-skill/yolo-ad-poster.png)](with-skill/yolo-ad.mp4) |
| Sword swing · 8 frames | ![Baseline sword-swing sprites](without-skill/sword-spritesheet.png) | ![Human Touch sword-swing sprites](with-skill/sword-spritesheet.png) |

## What changes

- **Cookie website:** a promotional layout becomes a focused shop page with one primary action, simpler navigation, and a visible flavor selection.
- **Shoes website:** a dramatic floating sneaker becomes a grounded product photograph, with restrained typography and clear category navigation.
- **Watercolor:** a brighter, centered sunset becomes a muted coastal study with an off-center sun, quieter sky, and visible paper margins.

- **Pixel-art lion:** a scenic sunset portrait becomes an isolated full-body lion, emphasizing the silhouette, separated paws, a grounded shadow, and quieter surroundings.

- **Polar mascot:** a softly shaded cartoon bear and an outlined illustration with simpler shapes, an ivory-and-blue palette, and a quieter smile. Both wave hello on transparent backgrounds.

- **Mellow app icon:** a fluffy yellow bird against a blue sky and a simpler yellow silhouette on plum. The directed prompt emphasizes a calm pose, clear shape language, and readability at small sizes.

- **Yolo sports ad:** the same bottle and copy in two energetic 12-second ads. The baseline uses a centered showcase and continuous movement; Human Touch adds track-inspired composition, a held water-break beat, and a larger product reveal. [Source and reproduction](yolo/README.md).

- **Sword swing:** eight poses per transparent sheet in a 4 × 2 arrangement, with the directed version adding explicit silhouette, anatomy, palette, and action-continuity guidance.

## How these were made

Created September 28, 2026. These are illustrative examples, not a controlled benchmark or a guarantee of improvement.

The eight original still-image PNGs were created with the built-in image-generation tool, one call per image. Baselines use the original brief plus a format instruction; the Human Touch prompts add specific art direction drawn from the skill. No baseline was instructed to look worse. For these original eight stills, every first output was retained, with no regeneration or retouching. Exact prompts are in [prompts.json](prompts.json). The tool did not expose a model version or seed.

These examples were created in the same session, not independent skill-disabled agent runs. The prompts demonstrate the effect of explicitly adding skill-derived direction, rather than isolating all possible context effects.

The website examples are static visual mockups, not functioning stores. Names, products, copy, and service claims are fictional concept content. The watercolor images simulate hand-painted work; they are AI-generated images, not physical paintings.

The Yolo pair uses Hyperframes 0.8.84 for both compositions and one shared bottle image generated with the built-in image tool. Human Touch guides only the directed composition. Both were authored in the same session; this demonstrates art-direction choices rather than an isolated skill ablation. Both videos are intentionally silent and make no product-performance claims.

The sword sheets were generated separately with the same character brief and eight-frame layout, adding Human Touch guidance only to the directed prompt. Earlier 64-frame attempts were superseded when the user clarified eight frames per version; only the final eight-frame sheets are included. Both are generated pixel-style studies with transparent backgrounds, not validated game-ready animation assets. Registration, exact pixel grids, and loop continuity may need cleanup. The character is original and the style references classic 16-bit Final Fantasy combat art.

The Polar mascots use the same app name, waving pose, square format, and transparent-background brief. The directed prompt adds Human Touch illustration guidance about shape language, palette, anatomy, and restraint. Both were generated separately with the built-in image tool in this same session; each first output was retained without retouching. This is a prompt-direction comparison, not an isolated skill-disabled test.

The Mellow pair shares the yellow-bird app-icon brief, square full-bleed format, and no-text constraint. Both were generated with the built-in image tool, one call per version, with each first result retained. Human Touch adds explicit silhouette, palette, and simplification guidance only to the directed prompt. This is a same-session prompt comparison, not an isolated skill-disabled test. The directed output retains slight color variation rather than perfectly flat vector fills. These are raster icon concepts, not platform-specific icon bundles.

## Files and reproduction

- Two Mellow app-icon PNGs: 1254 × 1254, opaque square artwork with no baked-in rounded corners.
- Two Polar mascot PNGs: 1254 × 1254, with alpha transparency.
- Two Yolo MP4 ads: H.264, 1080 × 1080, 30 fps, 12 seconds each; poster images are extracted from the videos.
- [Yolo source projects](yolo/README.md): editable HTML, briefs, design notes, and pinned rendering commands.
- Two sword-swing PNGs: 1774 × 887, eight poses each, arranged in four columns and two rows, with alpha transparency.
- Six website and watercolor PNGs: 1536 × 1024.
- Two square lion PNGs: 1254 × 1254. These are generated pixel-style illustrations, not verified 128 × 128 game sprites. The directed prompt requests a coarse logical grid, but the output retains finer detail and some soft color variation; strict grid and palette compliance are not claimed.
- [Browser gallery](index.html): open locally; no build or network dependencies.
- [Generation prompts](prompts.json): exact image-generation prompts.

Visual review covered palette, readable mockup text, composition, and lion silhouette and anatomy. File checks covered decoding, dimensions and local gallery links. Responsive layout and checkout behavior cannot be validated from static website mockups.
