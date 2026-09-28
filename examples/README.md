# Human Touch examples

Thirteen briefs, each with a baseline and a version art-directed with [Human Touch](../skills/human-touch/SKILL.md). Click any preview to inspect the original.

| Brief | Without the skill | With Human Touch |
| --- | --- | --- |
| Cookie website · pink and black | ![Baseline cookie website](without-skill/cookie-website.png) | ![Human Touch cookie website](with-skill/cookie-website.png) |
| Shoes website · red and black | ![Baseline shoes website](without-skill/shoes-website.png) | ![Human Touch shoes website](with-skill/shoes-website.png) |
| Calm watercolor sunset | ![Baseline watercolor sunset](without-skill/watercolor-sunset.png) | ![Human Touch watercolor sunset](with-skill/watercolor-sunset.png) |
| House closing · stock photography | ![Baseline house closing](without-skill/house-closing.png) | ![Human Touch house closing](with-skill/house-closing-natural.png) |
| Coastal character · Oxenfree-inspired | ![Baseline coastal character](without-skill/coastal-character.png) | ![Human Touch coastal character](with-skill/coastal-character.png) |
| Pixel-art lion | ![Baseline pixel-art lion](without-skill/pixel-art-lion.png) | ![Human Touch pixel-art lion](with-skill/pixel-art-lion.png) |
| Polar app mascot | ![Baseline Polar mascot](without-skill/polar-mascot.png) | ![Human Touch Polar mascot](with-skill/polar-mascot.png) |
| Mobile game UI pack | ![Baseline mobile game UI](without-skill/mobile-game-ui.png) | ![Human Touch mobile game UI](with-skill/mobile-game-ui.png) |
| Oversoul · Steam capsule art | ![Baseline Oversoul capsule](without-skill/oversoul-capsule.png) | ![Human Touch Oversoul capsule](with-skill/oversoul-capsule.png) |
| Mellow app icon | ![Baseline Mellow app icon](without-skill/mellow-icon.png) | ![Human Touch Mellow app icon](with-skill/mellow-icon-3d-sky.png) |
| RealBeef Meatsticks logo | ![Baseline RealBeef logo](without-skill/realbeef-logo.png) | ![Human Touch RealBeef logo](with-skill/realbeef-logo.png) |
| Yolo sports ad · 12 seconds | [![Yolo baseline animation](without-skill/yolo-ad.gif)](without-skill/yolo-ad.mp4) | [![Yolo Human Touch animation](with-skill/yolo-ad.gif)](with-skill/yolo-ad.mp4) |
| Sword swing · 8 frames | ![Baseline sword-swing sprites](without-skill/sword-spritesheet.png) | ![Human Touch sword-swing sprites](with-skill/sword-spritesheet.png) |

## What changes

- **Cookie website:** a promotional layout becomes a focused shop page with one primary action, simpler navigation, and a visible flavor selection.

- **Shoes website:** a dramatic floating sneaker becomes a grounded product photograph, with restrained typography and clear category navigation.

- **Watercolor:** a brighter, centered sunset becomes a muted coastal study with an off-center sun, quieter sky, and visible paper margins.

- **House closing:** a real estate agent and married couple in a bright home. The baseline shows the signing; Human Touch directs a shared glance after signing, a simple key handoff, natural skin and fabric texture, and consistent window light.

- **Coastal character:** the same original traveler, outfit, radio, and dusk setting, with the directed version emphasizing a relaxed weight shift, an off-center composition, and open shoreline. Both preserve the requested painterly 2D game-art direction.

- **Pixel-art lion:** a scenic sunset portrait becomes an isolated full-body lion, emphasizing the silhouette, separated paws, a grounded shadow, and quieter surroundings.

- **Polar mascot:** a softly shaded cartoon bear and an outlined illustration with simpler shapes, an ivory-and-blue palette, and a quieter smile. Both wave hello on transparent backgrounds.

- **Mobile game UI:** the same twelve groups of controls and green/cream/gold theme. The baseline uses leafy ornaments and layered edges; Human Touch directs consistent outlines, simpler surfaces, visible state distinctions, and emphasis on the primary action.

- **Oversoul:** the same goggle-wearing hero, palm-fired electricity, mountain setting, and Celeste-inspired pixel-art brief. Human Touch directs a bold title on quiet sky, a separated airborne silhouette, deliberate lightning paths, and controlled pixel clusters.

- **Mellow app icon:** a fluffy yellow bird against a blue sky and a matte 3D yellow bird against a blue sky. The directed prompt emphasizes a calm pose, coherent volume, matte materials, soft lighting, and readability at small sizes.

- **RealBeef Meatsticks:** a detailed bull illustration and a simpler cattle mark with bold red lettering. Human Touch directs the shape language, hierarchy, spacing, and restrained palette.

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

The Mellow pair shares the yellow-bird app-icon brief, square full-bleed format, and no-text constraint. Both use the built-in image tool. The baseline retains its first output. The directed version was initially flat; after the user clarified that it should remain 3D, it was edited using that image as a reference, then edited again to add the requested blue sky and soft clouds. Human Touch guides the rounded forms, connected anatomy, matte material, soft studio lighting, and restrained composition. The initial prompt and both edit prompts are recorded in prompts.json; reference images are available at commits 1c762c3 (flat) and 150530f (3D on plum). This is a same-session prompt comparison, not an isolated skill-disabled test. These are raster icon concepts, not editable 3D models or platform-specific icon bundles.

The RealBeef logos share the company name, square presentation, and warm-white background brief. Each was generated separately with the built-in image tool, with its first output retained. The directed prompt adds Human Touch typography and illustration guidance. Both spell the brand correctly; the directed version renders the descriptor in uppercase. These are same-session prompt comparisons and raster concepts, not finished vector identities. Slight tonal variation remains in the generated artwork; one-color print separations and small packaging applications have not been validated.

The coastal character pair references Oxenfree as a visual style, with an original character rather than an extracted game asset. Each graphic was generated separately with the built-in image tool; both first outputs were retained. The directed prompt adds Human Touch illustration guidance about posture, composition, palette, and atmospheric depth. These are standalone raster illustrations, not rigs or layered animation assets. Like the other image pairs, this is a same-session prompt comparison.

The mobile-game UI pair uses the same cozy adventure theme and twelve-group control brief. Each was created in one built-in image-generation call, with its first result retained. Human Touch adds UI guidance on hierarchy, state distinctions, spacing, and a consistent visual family. These are opaque raster presentation sheets, not sliced sprites, editable vectors, or working widgets. Slider values are visual approximations; touch-target sizes, contrast compliance, nine-slice scaling, and runtime behavior have not been validated.

The Oversoul capsule pair uses an original hero and Celeste as a style reference. Each was generated in one built-in image-generation call; both first outputs were retained without retouching. The directed prompt adds Human Touch pixel-art and illustration guidance. This is a same-session prompt comparison, not an isolated skill-disabled run. Both are wide capsule-art concepts; exact pixel-grid compliance is not verified. Steam’s [header capsule specification](https://partner.steamgames.com/doc/store/assets/standard) is 920 × 430; these native generated images need final sizing before upload.

The house-closing pair shares the three-adult cast, home setting, closing paperwork, pen, keys, and landscape format. The baseline retains its first built-in image-generation output. The directed image was generated once, then edited using that output as a reference after a request for greater realism. The edit adds natural skin variation, less arranged hair, subtler expressions, and more ordinary photographic lighting. The original directed image is preserved in commit a83f9a9. Human Touch adds photography guidance on expressions, eye lines, hand placement, material behavior, and window light. These depict fictional people and a fictional transaction, not a photographed event. They are same-session prompt comparisons, not independent skill-disabled runs.

## Files and reproduction

- Two house-closing PNGs: 1536 × 1024, opaque AI-generated stock-style photographs.
- Two Oversoul capsule PNGs: baseline 1832 × 858; Human Touch 1834 × 858, opaque wide artwork.
- Two mobile-game UI PNGs: 1254 × 1254, twelve groups of controls per presentation sheet.
- Two coastal character PNGs: 1254 × 1254, standalone 2D illustrations.
- Two RealBeef logo PNGs: 1254 × 1254, opaque square presentations.
- Two Mellow app-icon PNGs: 1254 × 1254, opaque square artwork with no baked-in rounded corners.
- Two Polar mascot PNGs: 1254 × 1254, with alpha transparency.
- Two Yolo GIF previews: 540 × 540, 15 fps, full 12-second ads, looping for playback directly in GitHub.
- Two Yolo MP4 ads: H.264, 1080 × 1080, 30 fps, 12 seconds each; poster images are extracted from the videos.
- [Yolo source projects](yolo/README.md): editable HTML, briefs, design notes, and pinned rendering commands.
- Two sword-swing PNGs: 1774 × 887, eight poses each, arranged in four columns and two rows, with alpha transparency.
- Six website and watercolor PNGs: 1536 × 1024.
- Two square lion PNGs: 1254 × 1254. These are generated pixel-style illustrations, not verified 128 × 128 game sprites. The directed prompt requests a coarse logical grid, but the output retains finer detail and some soft color variation; strict grid and palette compliance are not claimed.
- [Browser gallery](index.html): open locally; no build or network dependencies.
- [Generation prompts](prompts.json): exact image-generation prompts.

Visual review covered palette, readable mockup text, composition, and lion silhouette and anatomy. File checks covered decoding, dimensions and local gallery links. Responsive layout and checkout behavior cannot be validated from static website mockups.
