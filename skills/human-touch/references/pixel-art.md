# Pixel Art

## Establish the pixel grammar

Choose or inherit the intended use, logical canvas size, display scale, palette,
outline treatment, lighting direction, and perspective. A game sprite, tileset,
portrait, and decorative pixel illustration need different levels of precision.

Preserve intentional styles: chunky low-resolution sprites, detailed scenes,
isometric views, selective outlines, and deliberate dithering can all work.
Human Touch should not turn every request into the same retro-console aesthetic.

## Silhouette and clusters first

- Make the subject and pose readable at native size before adding texture.
- Group pixels into deliberate connected shapes that describe volume or material.
  Remove isolated noise unless a single pixel earns its place as a highlight,
  eye, or other essential accent.
- Give important features room to separate. Avoid merged paws, eyes lost in an
  outline, tangencies, and inconsistent limb lengths.
- Use intentional stair-step rhythms on curves and diagonals. Correct accidental
  bumps without making every contour mechanically identical.
- Keep a consistent apparent pixel grid. Mixed pixel sizes need a deliberate
  compositional reason, not accidental resizing or generated texture drift.

## Color and shading

Use a compact palette appropriate to the brief, with distinguishable value steps.
Choose ramps that support the subject; hue shifts can add depth without adding
many near-duplicate colors. Keep the focal feature distinct from its surroundings.

Place shadows according to one readable light source. Avoid accidental pillow
shading, glossy highlights on every surface, or smooth gradients masquerading as
pixel shading. Use dithering only where it earns space through a tone transition
or material effect; blanket checkerboards can obscure the silhouette.

## Scaling and tooling

For strict sprites or game assets, work on a real logical pixel grid and inspect
at native size and integer magnification. Use nearest-neighbor scaling and avoid
resampling blur, fractional transforms, JPEG compression, or unintended edge
antialiasing. Deliberately hand-placed antialiasing is a valid pixel-art technique.

Generated raster images may approximate pixel art without honoring a true grid
or exact palette. For a visual illustration, review that limitation honestly.
For an engine-ready asset, verify the logical dimensions, colors, alpha edges,
and grid, or redraw/clean up with appropriate pixel tools. Do not call a large
pixel-style image a verified low-resolution sprite without checking it.

## Animation and tiles, when requested

Keep registration, proportions, palette, and light direction stable across
frames. Check planted feet and avoid unmotivated outline shimmer. Use timing and
holds that support the action; more frames do not automatically improve motion.
Inspect tile edges in a repeated arrangement, not just as isolated squares.

## Final review

Check silhouette, anatomy appropriate to the style, cluster readability, edge
rhythm, palette discipline, light direction, and quiet areas. Judge at the actual
viewing scale as well as enlarged. Preserve personality rather than filling every
unused pixel or mechanically enforcing symmetry.
