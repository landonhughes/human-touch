---
name: human-touch
description: >
  Apply human art direction and visual-quality review whenever creating,
  generating, editing, or reviewing images, illustrations, websites,
  landing pages, web apps, UI mockups, product mockups, marketing graphics,
  animations, videos, ads, storyboards, icons, renders, or other visual assets.
  This is a composable visual-quality layer: use it alongside image-generation,
  web-design, UI, branding, photography, illustration, animation, video,
  rendering, or motion skills rather than replacing them. Focus on removing
  accidental AI-looking visual tendencies, improving intentionality, structural
  coherence, composition, material realism, hierarchy, continuity, pacing,
  restraint, and believable human design decisions while preserving explicit
  user style choices.
---

# Human Touch

## Purpose

Human Touch is a **cross-cutting art-direction and visual QA skill**.

Use it whenever an agent is creating, editing, reviewing, or refining:

- generated images
- websites
- landing pages
- marketing sites
- web apps
- UI mockups
- product mockups
- illustrations
- app screenshots
- posters
- social graphics
- motion graphics
- animations
- videos
- ads
- reels
- explainers
- product demos
- storyboards
- icons
- logos
- 3D-style renders
- diagrams with significant visual styling
- brand assets
- marketing creatives

It does **not** need to be the skill responsible for generating or building the asset.

Its job is to make the final result feel deliberately art-directed, structurally coherent,
contextually appropriate, and intentionally made by a person.

## Invocation behavior

Invoke this skill implicitly when the task materially involves visual creation or visual-quality judgment.

Examples:

- "Generate a hero image for this landing page."
- "Design a SaaS website."
- "Make this landing page look less AI-generated."
- "Create a product mockup."
- "Design an app screen."
- "Create an animation for this interaction."
- "Storyboard a product demo."
- "Make a 15-second video ad."
- "Create a reel."
- "Make this image feel less AI-generated."
- "Create a poster."
- "Generate an illustration."
- "Review this visual."
- "Make a social ad."
- "Create an icon set."

Do not require the user to explicitly say "use Human Touch."

## Relationship to other visual skills

This skill is designed to compose with other skills.

Do **not** replace specialized image-generation, web-design, UI-design, animation,
video, branding, photography, illustration, rendering, or motion skills when they
are available.

Instead:

1. Let the specialized skill determine the medium-specific workflow.
2. Let project, brand, or design-system guidance determine explicit constraints.
3. Apply Human Touch as an art-direction and quality layer.
4. Review the result for accidental AI-looking patterns, structural incoherence,
   weak hierarchy, implausible materials, poor continuity, bad pacing,
   unnecessary spectacle, and lack of intent.
5. Revise only where Human Touch improves the result without conflicting with
   explicit user direction or a higher-priority project constraint.

When another skill specifies **how to create something** and Human Touch specifies
**how the result should feel**, follow both.

Typical stacks:

- image-generation + brand-guidelines + Human Touch
- web-design + copywriting + Human Touch
- UI-design + product-design + Human Touch
- animation + motion-system + Human Touch
- video-generation + storyboard + Human Touch

## Do not fight intentional style

The purpose of this skill is **not** to force everything to become plain,
photorealistic, minimal, understated, or documentary.

If the user or another specialized skill intentionally requests:

- cinematic lighting
- surrealism
- neon
- perfect symmetry
- glossy materials
- exaggerated depth of field
- maximalism
- fantasy
- stylization
- particles
- unusual composition
- hyperrealism
- retro-futurism
- glassmorphism
- highly polished advertising imagery
- aggressive motion
- experimental typography
- fast editing
- handheld camera
- unusual web layouts

those choices can be valid.

Evaluate whether they appear intentional, coherent, and well executed.

Do not remove a stylistic feature merely because it is also common in AI-generated work.

**Human Touch should remove accidental AI aesthetics, not intentional art direction.**

## Core principle

A human designer asks:

> Why is this element here?

Generated visuals often behave more like:

> What visually plausible thing could go here?

Every significant visual decision should have a reason.

Before creating or reviewing anything, identify:

1. What is the visual trying to communicate?
2. What should the viewer notice first?
3. What should the viewer notice second?
4. What should remain visually quiet?
5. Which decisions reinforce the brand, story, environment, or product?
6. Which details are required by the medium?
7. What can safely be removed?

If an element has no useful visual, functional, narrative, or stylistic role, remove it.

## Default art direction

Only when the user and other active skills provide no stronger visual direction,
default to:

**clean, restrained, realistic, thoughtful contemporary design with believable
materials, understandable lighting, clear hierarchy, subtle asymmetry,
contextual imperfections, minimal arbitrary decoration, and no accidental
stereotypical AI-image effects.**

Do not interpret:

- professional as cinematic
- premium as glowing
- modern as gradient
- creative as busy
- futuristic as holographic
- minimal as empty
- beautiful as perfect

These are defaults, not prohibitions.

## Operating workflow

### 1. Determine governing creative direction

Identify any explicit:

- user style request
- brand system
- design system
- medium-specific skill
- reference visual
- product context

These take precedence over Human Touch defaults.

### 2. Define the visual opinion

Choose one dominant visual character appropriate to the task.

Examples:

- understated
- playful
- utilitarian
- nostalgic
- technical
- elegant
- awkward
- handmade
- editorial
- documentary
- youthful
- institutional
- premium
- domestic
- theatrical
- surreal

Do not blend every fashionable aesthetic without a reason.

### 3. Build from purpose

Determine:

- subject
- context
- hierarchy
- materials
- lighting
- composition
- camera or rendering approach
- level of polish
- intended emotional character

before adding decoration.

### 4. Keep the visual vocabulary controlled

Use a deliberate set of:

- materials
- type styles
- shape language
- effects
- lighting behaviors
- motion behaviors
- textures
- colors

Consistency is usually more convincing than abundance.

### 5. Preserve quiet areas

Not every region needs detail.

Allow:

- empty space
- flat backgrounds
- ordinary surfaces
- simple clothing
- muted regions
- neutral lighting
- visual breathing room
- asymmetry where appropriate

### 6. Verify causal coherence

A visual should make sense as a constructed scene, object, interface, website,
video sequence, or motion system.

Check:

- object connections
- anatomy
- perspective
- scale
- gravity
- contact points
- light direction
- shadows
- reflections
- material behavior
- fabric behavior
- architecture
- UI state
- responsive behavior
- interaction logic
- animation cause and effect
- continuity across shots
- visual pacing

### 7. Run a subtraction pass

Ask what can be removed without harming the concept.

Common candidates:

- arbitrary particles
- extra cards
- secondary icons
- gratuitous gradients
- unnecessary props
- random labels
- duplicated textures
- unnecessary motion
- dramatic lighting added only for spectacle
- website sections that repeat the same idea
- video shots that do not advance the sequence

Do not remove intentionally requested stylistic elements just because they are decorative.

### 8. Run an AI-tell pass

Read `references/anti-ai-tells.md`.

Treat AI tells as diagnostic signals, not automatic bans.

If a tell is clearly intentional and supports the requested direction, keep it.

If it appears accidental, generic, structurally incoherent, or visually unmotivated,
revise it.

### 9. Run the appropriate specialist reference

Use the relevant file:

- Photography → `references/photography.md`
- Product mockups → `references/product-mockups.md`
- UI/app mockups → `references/ui-design.md`
- Websites/landing pages → `references/web-design.md`
- Illustration → `references/illustration.md`
- Animation/motion → `references/animation.md`
- Video/storyboards → `references/video-design.md`
- Typography → `references/typography.md`

### 10. Run final QA

Read `references/final-review.md` before accepting important visual work.

## Human-first prompt construction

For generative visual work, build prompts in this order:

1. **Subject** — What exactly exists?
2. **Context** — Where is it and why?
3. **Composition** — How is it framed?
4. **Materials** — What are objects physically made from?
5. **Lighting** — Where does light actually come from?
6. **Camera/rendering method** — What medium or visual system is appropriate?
7. **Art direction** — What dominant visual character should the work have?
8. **Style-preservation constraints** — Which intentional choices must remain?
9. **AI-tell constraints** — Which accidental generated-image tendencies should be avoided?

Specificity should come from the scene, concept, and design decisions rather than
simply adding more decoration.

## Humanization revision

When an existing visual feels accidentally generated, preserve the core concept and
intentional style while considering:

- reducing excessive generic polish
- removing meaningless micro-detail
- simplifying unmotivated lighting
- eliminating accidental symmetry
- removing arbitrary decorative objects
- correcting geometry and anatomy
- improving object connections
- improving material behavior
- replacing generic beauty with context-specific choices
- introducing plausible irregularity where appropriate
- clarifying hierarchy
- improving shot continuity
- improving website section rhythm
- removing elements that exist only because the generator tends to add them

Do not flatten intentional maximalism, surrealism, fantasy, cinematic treatment,
or stylization.

## Taste hierarchy

When tradeoffs are necessary, prioritize:

1. user intent
2. project and brand constraints
3. clarity
4. structural coherence
5. intentionality
6. usability
7. visual hierarchy
8. realism appropriate to the chosen medium
9. continuity
10. consistency
11. restraint appropriate to the chosen style
12. personality
13. beauty
14. spectacle

Spectacle is not bad. **Unmotivated spectacle is.**

## Success criterion

The target is not:

> This is an impressive AI image, website, or video.

The target is:

> This looks intentionally art-directed, and every major visual choice feels deliberate.
