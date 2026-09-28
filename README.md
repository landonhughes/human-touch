# Human Touch

**Composable human art direction and visual QA for AI agents.**

Human Touch is a reusable skill that layers on top of image generation, web design, UI design, branding, animation, video, illustration, photography, and other visual workflows.

Its purpose is not to replace specialized creative skills. It acts as an art-direction and QA layer that helps generated work feel deliberate rather than default-generated.

## Install

Use the skill folder:

```text
https://github.com/landonhughes/human-touch/tree/main/skills/human-touch
```

Example:

> Install the Human Touch skill from https://github.com/landonhughes/human-touch/tree/main/skills/human-touch

## Implicit invocation

The skill is configured for implicit invocation through:

```text
skills/human-touch/agents/openai.yaml
```

It is intended to activate automatically for visual-generation, website,
UI, mockup, illustration, animation, video, storyboarding, and visual-review tasks.

Users can still invoke it explicitly:

> Use human-touch to review this generated image.

## Composable by design

Example stacks:

```text
image-generation
+ brand-guidelines
+ human-touch
```

```text
web-design
+ copywriting
+ human-touch
```

```text
video-generation
+ storyboard
+ human-touch
```

The specialized skill handles creation. Human Touch handles art direction,
coherence, continuity, and visual QA.

## Important principle

Human Touch does not ban cinematic lighting, neon, particles, symmetry,
glassmorphism, maximalism, glossy materials, surrealism, expressive motion,
or unusual layouts.

It distinguishes between:

- **intentional art direction**
- **accidental AI-generation habits**

The goal is to remove the latter without flattening the former.

## Structure

```text
human-touch/
├── plugin.json
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── .gitignore
├── .github/
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       └── improvement.md
└── skills/
    └── human-touch/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        └── references/
            ├── anti-ai-tells.md
            ├── animation.md
            ├── final-review.md
            ├── illustration.md
            ├── photography.md
            ├── product-mockups.md
            ├── typography.md
            ├── ui-design.md
            ├── video-design.md
            └── web-design.md
```

## License

MIT © 2026 Landon Hughes
