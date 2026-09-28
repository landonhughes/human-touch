# Sword-swing animations

Updated 16-frame GIFs combine eight original poses with eight new generated in-between poses. Both use identical timing and foot alignment.

| Without Human Touch | With Human Touch |
| --- | --- |
| ![Baseline sword swing](../without-skill/sword-swing-smooth.gif) | ![Human Touch sword swing](../with-skill/sword-swing-smooth.gif) |

The GIFs are 576 × 512 with transparent backgrounds and loop every 1.26 seconds. The shorter holds and extra poses add motion between the original keyframes. Generated proportions and sword angles still vary; these remain animation studies.

Only the updated GIFs are retained from this revision. The new poses were created with the built-in image tool using the corresponding original sheet as reference, then sliced and interleaved with the original frames. No ghosted optical-flow blends are included. Exact prompts and animation metadata are recorded in [prompts.json](../prompts.json).

Original materials remain available: [baseline sheet](../without-skill/sword-spritesheet.png), [Human Touch sheet](../with-skill/sword-spritesheet.png), [baseline frames](../without-skill/sword-frames/), and [Human Touch frames](../with-skill/sword-frames/). The existing slicing script reproduces the original eight-frame preview, not the updated 16-frame GIFs.
