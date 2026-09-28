<div align="center">

# Human Touch

### Give generated visuals a point of view.

A composable art-direction and visual-QA skill for AI agents.

**Images · Websites · 3D · Pixel art · Motion**

[Explore the examples](#the-showcase) &nbsp; / &nbsp; [Install](#install) &nbsp; / &nbsp; [Read the skill](skills/human-touch/SKILL.md)

</div>

---

Human Touch works alongside your creative tools. It helps an agent make deliberate decisions about composition, materials, hierarchy, continuity, and pacing—while preserving the style you asked for.

## The showcase

**Eight briefs. Sixteen examples.** The left version uses the base workflow; the right adds Human Touch art direction. Click an image to inspect it. Click a Yolo poster to open its video.

These are illustrative comparisons, not a controlled benchmark. [Read the methodology](examples/README.md#how-these-were-made) · [See the exact prompts](examples/prompts.json) · [Open the local gallery](examples/index.html)

### 01 / Cookie shop

*Pink & black · website mockup*

<table>
<tr><th width="50%">Without Human Touch</th><th width="50%">With Human Touch</th></tr>
<tr><td><a href="examples/without-skill/cookie-website.png"><img src="examples/without-skill/cookie-website.png" alt="Cookie shop — without Human Touch" width="100%"></a></td><td><a href="examples/with-skill/cookie-website.png"><img src="examples/with-skill/cookie-website.png" alt="Cookie shop — with Human Touch" width="100%"></a></td></tr>
</table>

A bakery storefront, from a promotional layout to a focused shop page.

### 02 / Shoes

*Red & black · website mockup*

<table>
<tr><th width="50%">Without Human Touch</th><th width="50%">With Human Touch</th></tr>
<tr><td><a href="examples/without-skill/shoes-website.png"><img src="examples/without-skill/shoes-website.png" alt="Shoes — without Human Touch" width="100%"></a></td><td><a href="examples/with-skill/shoes-website.png"><img src="examples/with-skill/shoes-website.png" alt="Shoes — with Human Touch" width="100%"></a></td></tr>
</table>

Two ways to frame the product: dramatic campaign imagery and a grounded catalogue.

### 03 / A quiet sunset

*Calm colors · watercolor illustration*

<table>
<tr><th width="50%">Without Human Touch</th><th width="50%">With Human Touch</th></tr>
<tr><td><a href="examples/without-skill/watercolor-sunset.png"><img src="examples/without-skill/watercolor-sunset.png" alt="A quiet sunset — without Human Touch" width="100%"></a></td><td><a href="examples/with-skill/watercolor-sunset.png"><img src="examples/with-skill/watercolor-sunset.png" alt="A quiet sunset — with Human Touch" width="100%"></a></td></tr>
</table>

A change in palette, composition, and the treatment of paper and paint.

### 04 / The lion

*Character study · pixel art*

<table>
<tr><th width="50%">Without Human Touch</th><th width="50%">With Human Touch</th></tr>
<tr><td><a href="examples/without-skill/pixel-art-lion.png"><img src="examples/without-skill/pixel-art-lion.png" alt="The lion — without Human Touch" width="100%"></a></td><td><a href="examples/with-skill/pixel-art-lion.png"><img src="examples/with-skill/pixel-art-lion.png" alt="The lion — with Human Touch" width="100%"></a></td></tr>
</table>

A scenic portrait and a quieter, silhouette-led character study.

### 05 / Polar

*Cute app mascot · transparent illustration*

<table>
<tr><th width="50%">Without Human Touch</th><th width="50%">With Human Touch</th></tr>
<tr><td><a href="examples/without-skill/polar-mascot.png"><img src="examples/without-skill/polar-mascot.png" alt="Polar mascot — without Human Touch" width="100%"></a></td><td><a href="examples/with-skill/polar-mascot.png"><img src="examples/with-skill/polar-mascot.png" alt="Polar mascot — with Human Touch" width="100%"></a></td></tr>
</table>

Two friendly greetings for Polar: a softly shaded cartoon and a simpler outlined character with a restrained palette and relaxed expression. Both are transparent PNGs.

### 06 / Mellow

*Yellow bird · app icon*

<table>
<tr><th width="50%">Without Human Touch</th><th width="50%">With Human Touch</th></tr>
<tr><td><a href="examples/without-skill/mellow-icon.png"><img src="examples/without-skill/mellow-icon.png" alt="Mellow app icon — without Human Touch" width="100%"></a></td><td><a href="examples/with-skill/mellow-icon.png"><img src="examples/with-skill/mellow-icon.png" alt="Mellow app icon — with Human Touch" width="100%"></a></td></tr>
</table>

A fluffy yellow bird against a blue sky and a simpler graphic silhouette on plum. Two interpretations of a friendly app icon, with square artwork ready for platform masking.

### 07 / Yolo

*Energetic sports ad · Hyperframes · 12 seconds*

<table>
<tr><th width="50%">Without Human Touch</th><th width="50%">With Human Touch</th></tr>
<tr><td><a href="examples/without-skill/yolo-ad.mp4"><img src="examples/without-skill/yolo-ad-poster.png" alt="Yolo — without Human Touch" width="100%"></a></td><td><a href="examples/with-skill/yolo-ad.mp4"><img src="examples/with-skill/yolo-ad-poster.png" alt="Yolo — with Human Touch" width="100%"></a></td></tr>
</table>

The same bottle and copy, with different composition and motion direction.

[Watch baseline](examples/without-skill/yolo-ad.mp4) · [Watch Human Touch](examples/with-skill/yolo-ad.mp4) · [Editable Hyperframes projects](examples/yolo/README.md)

### 08 / Sword swing

*Final Fantasy–inspired · 8 frames per sheet*

<table>
<tr><th width="50%">Without Human Touch</th><th width="50%">With Human Touch</th></tr>
<tr><td><a href="examples/without-skill/sword-spritesheet.png"><img src="examples/without-skill/sword-spritesheet.png" alt="Sword swing — without Human Touch" width="100%"></a></td><td><a href="examples/with-skill/sword-spritesheet.png"><img src="examples/with-skill/sword-spritesheet.png" alt="Sword swing — with Human Touch" width="100%"></a></td></tr>
</table>

An original swordswoman in eight attack poses, arranged left to right in a 4 × 2 sheet.

Transparent PNGs. These are generated sprite-sheet studies; pixel-grid, registration, and loop cleanup may be needed before use in a game.

---

## Install

Give your agent this instruction:

```text
Install the Human Touch skill from
https://github.com/landonhughes/human-touch/tree/main/skills/human-touch
```

Then create as usual. [Implicit invocation](skills/human-touch/agents/openai.yaml) is enabled for visual work. You can also ask directly:

> Use human-touch to art-direct this image, website, model, or animation.

## Works with your tools

| Your workflow | Human Touch adds |
| --- | --- |
| Image generation & illustration | Composition, material coherence, visual hierarchy |
| Websites & UI | Clear reading order, useful content, intentional section rhythm |
| 3D modeling & rendering | Silhouette, proportions, material response, purpose-specific geometry checks |
| Pixel art & sprites | Readable clusters, palette discipline, grid and frame consistency |
| Animation & video | Motivated motion, continuity, pacing, and a purposeful ending |

The specialized tool handles creation. Human Touch provides an art-direction and review layer.

**Intentional style stays.** Cinematic light, neon, maximalism, glossy surfaces, surrealism, and expressive motion are all valid. The skill questions accidental choices; it does not impose a single house style.

<details>
<summary><strong>Explore the skill references</strong></summary>

- [Core workflow](skills/human-touch/SKILL.md)
- [Web design](skills/human-touch/references/web-design.md) · [UI design](skills/human-touch/references/ui-design.md) · [Typography](skills/human-touch/references/typography.md)
- [Photography](skills/human-touch/references/photography.md) · [Product mockups](skills/human-touch/references/product-mockups.md) · [Illustration](skills/human-touch/references/illustration.md)
- [3D modeling](skills/human-touch/references/3d-modeling.md) · [Pixel art](skills/human-touch/references/pixel-art.md)
- [Animation](skills/human-touch/references/animation.md) · [Video design](skills/human-touch/references/video-design.md)
- [AI-tell diagnostics](skills/human-touch/references/anti-ai-tells.md) · [Final review](skills/human-touch/references/final-review.md)

A rendered image does not validate an editable 3D model. Generated pixel-style artwork does not establish that a sprite is ready for a game engine. The references distinguish visual review from production checks.

</details>

<details>
<summary><strong>Repository guide</strong></summary>

| Path | Contents |
| --- | --- |
| `skills/human-touch/` | Installable skill, invocation metadata, specialist references |
| `examples/with-skill/` | Human Touch images, videos, and preview posters |
| `examples/without-skill/` | Baseline images, videos, and preview posters |
| `examples/yolo/` | Editable Hyperframes compositions and reproduction notes |
| `examples/prompts.json` | Exact prompts and production briefs |
| `examples/index.html` | Local comparison gallery with video playback |
| `plugin.json` | Plugin metadata |

</details>

---

<div align="center">

[Contribute](CONTRIBUTING.md) &nbsp; · &nbsp; [MIT License](LICENSE)

© 2026 Landon Hughes

</div>
