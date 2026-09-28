# 3D Modeling

## Start with the asset's job

Apply this reference to meshes, sculpts, procedural models, materials, scenes,
and renders. Compose with available modeling or DCC tools; Human Touch supplies
art direction and review, not a replacement modeling engine.

Establish the intended use before choosing detail: a still render, game asset,
rigged character, product visualization, or printable object has different needs.
Inherit the requested style, scale, units, polygon budget, target engine, and
export format. Do not invent production constraints when the request is only
for a visual concept.

## Shape before surface

- Block out silhouette, proportions, and primary masses before adding bevels,
  panel lines, noise, or tiny surface details.
- Inspect relevant front, side, and three-quarter views. A convincing camera
  angle can hide flattened forms, intersections, or missing backs.
- Give connected parts credible attachment points and thickness. Intentional
  exaggeration is valid; accidental floating parts and fused joints are not.
- Judge silhouette at the intended viewing distance. Spend geometry where it
  changes the outline, deformation, or visible shading.

## Topology follows use

- For deformation, inspect edge flow around joints and test representative poses.
  Do not require all-quads topology for every asset.
- Check normals, unintended duplicate faces, intersections, and shading artifacts.
  Preserve intentional hard edges rather than smoothing every surface.
- For closed printable solids, check manifoldness, wall thickness, and disconnected
  shells; do not impose watertightness on legitimate open render or game meshes.
- Treat retopology, UV work, baking, and LODs as purpose-dependent steps, not
  mandatory embellishments for every model.

## Materials and presentation

Use material response that communicates construction: distinguish painted metal,
raw metal, fabric, skin, rubber, or clay through coherent roughness and texture
scale. Stylized flat materials and low-poly facets are valid visual languages.
Avoid universal gloss, oversized bevels, or random wear added to imply quality.
Wear belongs where use or exposure would cause it.

Where textures are used, inspect UV stretch, visible seams, texel density, and
baked artifacts at the target distance. Light the form so it can be understood;
keep contact shadows, reflections, and scale cues consistent with the scene.
Use a neutral inspection view alongside dramatic presentation when needed.

## Delivery and review

For an actual model deliverable, preserve an editable source and inspect the
requested export in the target viewer or re-import it when available. Check
units, axis orientation, pivot, transforms, material assignments, and referenced
textures as relevant. Do not apply transforms blindly to a rigged asset.

A render alone does not validate topology, rigging, printability, or export
compatibility. State which checks were possible. Do not represent a generated
picture of a 3D object as an editable 3D model.
