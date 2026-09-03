---
id: gui-style
title: GUI style
enabled: true
default_exposed: false
order: 10
keywords: [gui, ux, frontend, desktop app, web app, app shell, dashboard, design system, visual hierarchy, attention, theme, color, tokens, minimalism, component unity, spacing, density, motion, animation, progressive disclosure, accessibility, maintenance, refactor, migration, copy, demo, prototype, temporary html]
description: Use when defining, creating, maintaining, refactoring, transferring, demonstrating, or reviewing GUI/UX design in any framework, including existing interfaces, app shells, dashboards, desktop tools, demos, and temporary HTML.
---

# GUI Style

## Contents

1. [Design Philosophy](#design-philosophy)
2. [Work Modes](#work-modes)
3. [Attention And Hierarchy](#attention-and-hierarchy)
4. [Composition And Disclosure](#composition-and-disclosure)
5. [Elements And Unity](#elements-and-unity)
6. [Typography, Spacing, And Density](#typography-spacing-and-density)
7. [Geometry And Motion](#geometry-and-motion)
8. [Theme System](#theme-system)
9. [Maintenance And Review](#maintenance-and-review)

## Scope And Precedence

Use this reference for new interfaces and for work on interfaces that already exist: maintenance, focused fixes, refactors, cross-project transfers, demos, disposable HTML, and design reviews. Repository policy and tested product behavior come first. Unless a redesign is explicitly authorized, preserve task flow, information meaning, keyboard semantics, user state, and honest runtime behavior while improving the visual system around them.

This is a framework-neutral visual and interaction contract. Map it to the platform already in use. Architecture and toolchain choices belong to the [service interface rule](../rules/project/interfaces.md); this guide does not require a particular framework.

## Design Philosophy

Heaven-style UI is a quiet workbench: focused, compact, precise, and calm enough for prolonged use. It gives the task more visual weight than the chrome. It feels physical through alignment, spacing, restrained surfaces, and responsive state—not through decoration.

Minimalism means minimizing decision cost and irrelevant salience. It does not mean maximizing empty space, hiding useful context, or reducing a capable tool to a sparse landing page. Complexity may remain when the work requires it; competition for attention may not.

Every persistent element must earn attention by doing at least one of four jobs:

1. advance the current task;
2. explain current state or consequence;
3. prevent a likely mistake;
4. preserve orientation or continuity.

Remove, merge, demote, or disclose an element that does none of these.

### Non-Negotiable Principles

- **One view-level focus.** Establish one dominant task or object for the current view. Supporting panels may have actions, but they stay visually neutral until that panel becomes the active task.
- **Earned visibility.** Keep frequent actions, current scope, selection, and consequential state visible. Put infrequent options where they become relevant.
- **Stable orientation.** Preserve spatial position, selection, scroll, edits, and familiar control locations across state changes.
- **Recognition before recall.** Make available actions and current state inferable from the interface; do not depend on remembered shortcuts, hidden gestures, or tooltip-only instructions.
- **Unified meaning.** The same semantic role uses the same appearance, placement logic, copy pattern, interaction, and state language everywhere.
- **One principal interaction accent.** Reserve the theme accent for the active task, current selection, or primary action. Secondary and option accents may identify stable categories but never compete with the task or encode state alone.
- **Motion with meaning.** Animate only to explain cause, continuity, or feedback. Motion is never ambient decoration or a recurring demand for attention.
- **Convergent maintenance.** Every change should reduce one-off styling and move the product closer to its canonical tokens, components, spacing, and behavior.

### Design Brief

Before substantial UI work, define six compact decisions. Keep them proportional to the change:

1. **Primary goal:** what the user must accomplish in this view.
2. **Attention target:** what should be noticed first, next, and only on demand.
3. **Hierarchy:** what is primary, supporting, and tertiary.
4. **Disclosure:** what appears immediately and where optional complexity lives.
5. **System fit:** which existing layout, component, token, spacing, and motion patterns the change reuses.
6. **Continuity:** how the design preserves orientation across wide, constrained, narrow, loading, empty, and error states.

For a small repair, use the questions as an internal check. For a review, connect each recommendation to visible evidence, its effect on attention or comprehension, and the smallest coherent correction.

## Work Modes

| Mode | Required behavior |
| --- | --- |
| Maintain or refactor | Preserve the user's mental model and spatial memory. Compare before and after at the same state and size; remove drift instead of adding a parallel style. |
| Transfer between projects | Transfer hierarchy, semantic roles, component families, spacing rhythm, and state behavior—not raw markup or incidental styling. Translate each role into the target system. |
| Build a new interface | Define the task, attention order, information architecture, and disclosure model before choosing decorative treatment. Establish the shared system before page-level exceptions. |
| Build a demo | Make the demonstrated task clear and genuinely usable. Use realistic, explicitly illustrative content and keep the same visual language expected of a durable surface. |
| Build temporary HTML | Use one canonical theme, the shared geometry and spacing, semantic structure, and the smallest coherent element family. Disposable does not mean visually unrelated. |
| Review an interface | Judge task clarity, attention, hierarchy, unity, spatial rhythm, theme use, motion, continuity, and access before pixel polish. |

## Attention And Hierarchy

Treat attention as a finite budget. Persistent accent, high contrast, large type, elevation, badges, and motion all spend that budget. Do not stack several of them on ordinary controls.

Use visual signals in this order, escalating only when the earlier signals are insufficient:

1. position and reading order;
2. grouping, alignment, and spacing;
3. typography and size;
4. surface or border contrast;
5. accent color;
6. motion.

The hierarchy must remain understandable without color. Position, type, spacing, and structure establish persistent importance; semantic color and motion communicate temporary consequence.

### Salience Rules

- Give the view one dominant task surface and normally one filled primary action. Panel-level actions remain neutral until their panel is active.
- Reserve persistent accent for the current selection, active mode, direct task progress, or the action that advances the task.
- Allow urgency to override the normal hierarchy only when the user must act. Remove the urgent treatment as soon as the condition clears.
- Avoid simultaneous badges, bright accents, shadows, and animation. A notification that is always loud stops communicating priority.
- Keep global controls, appearance, help, and assistants visually quieter than the current work.
- Preserve stable control locations. Do not move common actions because content, labels, status, or hover state changes.

### Information Levels

- **Primary:** the current object, task surface, result, and action that advances the task.
- **Supporting:** navigation, filters, selection context, and frequent task aids.
- **Tertiary:** metadata, uncommon settings, logs, appearance, help, and advanced detail.

Organize a view into roughly three to five meaningful groups when that improves scanning; this is a cognitive-load heuristic, not a visual quota. A group exists because its contents share a decision or task, not because the page needs another container.

## Composition And Disclosure

Start with the actual tool, not a landing page. For dense workbench applications, this is a useful archetype rather than a universal shell:

```text
App window
  global navigation rail
  optional scoped browser or project panel
  primary workspace: editor, table, canvas, form, chat, or task surface
  optional inspector: selection, settings, logs, or metadata
  optional status strip: service, route, sync, or job state
```

- Prefer rails, side panels, split panes, tabs, trees, tables, lists, editors, and inspectors before cards.
- Establish groups through alignment, spacing, and panel boundaries before adding another framed container.
- Use a shared toolbar for search, commands, run/sync actions, and panel toggles. Keep appearance and other tertiary controls out of the primary action cluster.
- Keep dimensions stable so selection, hover, asynchronous status, and translated labels do not shift the layout.
- Empty states should name what is empty and, when recovery is possible, offer one obvious next action.

### Progressive Disclosure

Choose the smallest surface that preserves context:

| Surface | Use for |
| --- | --- |
| Inline | A short local consequence, explanation, validation message, or one-step choice. |
| Inspector or drawer | Supporting detail that benefits from comparison with the current selection or workspace. |
| Dedicated view | Complex editing, configuration, history, or work that needs its own navigation and recovery. |
| Modal or sheet | A short blocking decision or high-consequence confirmation. Never use it as routine navigation. |
| Menu or popover | Compact options and infrequent peer actions. Never hide the only path to continue or recover. |

Disclosure must preserve selection, edits, scroll, and task context. Closing a layer returns attention to the point that opened it. Familiar tooltips may clarify compact controls; required instructions, state, and recovery remain visible without them.

### Responsive Behavior

Breakpoints follow task failure, not device labels. Define how the interface changes when the primary workspace no longer has enough room:

- Wide: browser, workspace, and optional inspector may coexist.
- Constrained: preserve the workspace and at most one supporting pane; collapse the other behind an explicit control.
- Narrow or touch: show one hierarchy level at a time, using a drawer, sheet, or route for navigation and inspection. Preserve selection and edits across transitions.
- Horizontal scrolling is acceptable only for intrinsically wide content such as data grids, timelines, or code. Ordinary forms and navigation must reflow.
- Verify the sizes the product claims to support and verify at `200%` zoom. Dense desktop controls may use a `24px` minimum target when spacing is limited; touch-oriented surfaces should approach `40px` to `44px` without making the visual chrome heavy.

## Elements And Unity

Unity means semantic consistency, not forced uniformity. Identical meanings use the same component family and behavior. A compact, touch, data-dense, or domain-specific variant is acceptable only when it is named, intentional, and still recognizably part of the same system.

Use this order when a need appears: reuse an existing element, adapt an existing named variant, extend the shared family, then invent a new element only when the semantics are genuinely new.

### Element Families

- Controls with the same role share height, padding, radius, typography, icon treatment, and state behavior across every view.
- Inputs, search fields, and compact filters belong to one field family. Dropdown panels and popovers visibly belong to their trigger.
- Tabs represent open or durable contexts. Segmented controls switch modes inside one context. Do not style the two as interchangeable pills.
- Tables and lists share row rhythm, separators, selection, empty states, and inline-action placement with the surrounding shell.
- Cards represent repeated objects or truly contained tools. They do not replace normal page structure and are never nested by default.
- Third-party widgets must disappear into the product language. If their type, surfaces, geometry, icons, states, or motion remain visibly foreign, they are not yet integrated.
- Keep variants few and semantic: default, compact, primary, subtle, and danger are usually enough. Retire a variant when its distinct need disappears.

### Control Language

- Use short text buttons for explicit commands such as `Run`, `Build`, `Sync`, `Open`, `Save`, and `Connect`.
- Use icon-only controls for familiar repeated actions, with one icon family, consistent optical size and stroke, a clear name, and discoverable explanation.
- Use toggles or checkboxes for binary settings, segmented controls for exclusive modes, numeric controls for quantities, menus for overflow, and tabs for durable workspaces.
- Keep destructive actions distinct but visually subordinate until the destructive path is intentionally entered. Prefer undo when reversal is safe; reserve confirmation for consequential actions.

### States

Every interactive family defines the relevant default, hover, active, focus, selected, disabled, loading, empty, and error states. Forms also distinguish read-only, required, invalid, and help states.

- State changes preserve layout and do not move neighboring controls.
- Selection, status, and validation use a structural or textual cue in addition to color.
- The same state uses the same color role, icon, wording, and placement throughout the product.
- Feedback appears beside the object or action it belongs to. Temporary feedback does not become a competing permanent panel.
- Empty, offline, local, loading, running, interrupted, failed, and completed states are honest and visually proportionate.
- Focus, names, reading order, and state remain perceivable through keyboard and assistive access without changing the visual hierarchy.

## Typography, Spacing, And Density

Typography and space establish hierarchy before color does. Use the platform's system sans-serif family or a product-approved equivalent; reserve monospace for paths, identifiers, code, protocol values, and compact technical status.

| Role | Size | Weight | Line height |
| --- | ---: | ---: | ---: |
| App title | `14px` | `650` | `20px` |
| Panel heading | `12px` | `650` | `16px` |
| Body | `13px` | `450` | `19px` |
| Label | `11px` | `600` | `14px` |
| Mono/status | `11px` | `500` | `15px` |

- Use larger display headings only for real document pages, reports, or presentation surfaces—not routine workbench chrome.
- Keep letter spacing neutral. Use weight and spacing, not compressed tracking or many type sizes, to create hierarchy.
- Write labels as nouns and actions as verbs. Keep commands short, specific, and consistent.
- Truncate only when the full value remains available through a stable detail surface. Place explanations and recovery near the decision they affect.

### Spacing Rhythm

Use only the shared scale: `4px`, `8px`, `12px`, `16px`, `24px`, `32px`, and `48px`.

| Relationship | Normal spacing |
| --- | ---: |
| Icon to label, tightly paired metadata | `4px` to `8px` |
| Inside compact controls and rows | `8px` to `12px` |
| Between items in one group | `8px` to `12px` |
| Between related groups | `16px` to `24px` |
| Between major task regions | `24px` to `32px`, or a clear panel boundary |
| Rare document/presentation break | `48px` |

Keep spacing tightest within a semantic group, larger between groups, and largest between task regions. Space clarifies ownership; it does not exist to make a dense tool look artificially empty.

- Align headings, labels, fields, toolbars, and content to shared axes. Repeated one- or two-pixel optical corrections belong to the component, not each page.
- Use `12px` to `16px` panel insets by default. A dense table may reach the panel edge when its header and row geometry provide the structure.
- Target a `32px` default desktop control family. A named compact variant may be smaller for repeated data operations; touch surfaces enlarge the hit region toward `40px` to `44px` without making every visible control heavy.
- Keep density consistent inside a task region. Do not mix airy cards, tiny table controls, and oversized marketing headings in one operational view.

## Geometry And Motion

| Token | Value |
| --- | --- |
| Radius small | `6px` |
| Radius medium | `8px` |
| Radius large | `12px` |
| Border | `1px` |
| Focus boundary | Solid `2px` accent boundary with `2px` offset and a surface separator when needed |
| Fast feedback | `120ms` to `150ms` |
| Standard transition | `150ms cubic-bezier(0.2, 0.8, 0.2, 1)` |
| Panel transition | `210ms cubic-bezier(0.2, 0.8, 0.2, 1)` |

Use `6px` for compact controls and chips, `8px` for panels and popovers, and `12px` for dialogs and sheets. Pill shapes belong to semantic chips, status, and genuinely circular actions—not generic controls. Use thin borders and nearby surface shifts before shadow; reserve the one soft shadow for floating layers that truly overlap content.

### Motion Rules

- Animate to show causality, preserve spatial continuity, or confirm state. If the motion explains none of these, remove it.
- Keep only one focal movement active at a time. Do not combine panel motion, animated badges, pulsing status, and attention-seeking hover effects.
- Make entry emerge from its source and exit return toward it. Expansion and collapse preserve the user's spatial model without abrupt jumps.
- Use color, border, opacity, or a restrained `1px` movement for hover/press feedback. Avoid bounce, elastic overshoot, parallax, looping decoration, and large hover lifts.
- Do not delay task completion for choreography. Avoid staggered reveals in operational interfaces.
- Allow looping motion only for real ongoing progress, and keep it quiet. Stop it as soon as the state ends.
- Provide a reduced-motion path with the same information and continuity, using immediate state changes or short fades.

## Theme System

The six themes are alternate atmospheres for one interface, not separate designs. Layout, hierarchy, component meaning, spacing, and relative salience remain stable when the theme changes.

The palette below is a compatibility contract. Durable Heaven-style interfaces support all six themes and keep every listed value exact unless an explicit design-system version changes the contract. A disposable static artifact may choose one canonical theme; it must not invent a seventh theme or partially recolor only the background and accent.

Light is anchored to the current official Ollama surfaces: the logo and primary calls to action are black, the canvas is white, and supporting surfaces use neutral grays. Colorful keeps that same white Ollama canvas while allowing the established colorful accent set for products that need it. Ollama's published web styles do not define a chromatic brand color. This contract retains green only for explicitly semantic or existing colored controls in Light, and scopes the broader accent set to Colorful; neither is a shell or logo color. The [official Ollama logo](https://github.com/ollama/ollama/blob/main/docs/logo.svg), [official documentation styles](https://github.com/ollama/ollama/blob/main/docs/styling.css), and [official app base styles](https://github.com/ollama/ollama/blob/main/app/ui/app/src/index.css) are the source evidence. Utopia and Dystopia use the [official DeepSeek Harness design tokens](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/client/ui-theme/src/styles/design-platform.css); the exact DeepSeek logo ink is documented separately by the [official DeepSeek logo](https://github.com/deepseek-ai/DeepSeek-LLM/blob/main/images/logo.svg).

| Short name | Theme name | CSS class | Intent |
| --- | --- | --- | --- |
| Light | Ollama White Grayscale | `.theme-light` | Default white, black, and neutral-gray workbench with scoped green semantic controls. |
| Colorful | Ollama White | `.theme-color` | White workbench with the established colorful accent set. The selector name remains for compatibility. |
| Warm | Anthropic | `.theme-anthropic` | Warm paper surfaces with slate, ivory, and clay tones. The selector name remains for compatibility. |
| Dark | GitHub Soft Dark | `.theme-dark` | Soft developer-dark surfaces with low glare and clear editor syntax. |
| Utopia | DeepSeek Light | `.theme-utopia` | DeepSeek Light surfaces with neutral-bluish layers and blue business state. |
| Dystopia | DeepSeek Dark | `.theme-dystopia` | DeepSeek Dark surfaces with neutral-bluish layers and blue business state. |

Every theme maintains parity across:

- Shell tokens: `--bg`, `--surface`, `--surface-2`, `--surface-3`, `--text`, `--muted`, `--subtle`, `--label`, `--border`, `--border-strong`, `--accent`, `--accent-contrast`, `--accent-2`, `--accent-soft`, `--danger`, `--danger-soft`, `--warning`, `--warning-soft`, `--success`, `--success-soft`, and `--shadow`.
- Inline code tokens: `--code-bg` and `--code-text`.
- Editor tokens: `--cm-bg`, `--cm-text`, `--cm-gutter-bg`, `--cm-gutter-text`, `--cm-active-line`, `--cm-selection`, `--cm-search-match`, `--cm-search-selected`, `--cm-token-class`, `--cm-token-property`, `--cm-token-enum`, `--cm-token-string`, `--cm-token-number`, and `--cm-token-variable`.
- Option accents: `--option-accent-0` through `--option-accent-9` for hashed repeated objects, series, labels, and category markers.

Raw hexadecimal colors belong only in these declarations or in documented domain visualizations. Elements consume semantic tokens. `--accent` is the principal interaction accent; `--accent-2` and option accents support stable identity or data categories and must not compete with primary actions or encode selection or status alone.

### Light

```css
.theme-light {
  --bg: #ffffff;
  --surface: #fafafa;
  --surface-2: #f5f5f5;
  --surface-3: #e5e5e5;
  --text: #171717;
  --muted: #737373;
  --subtle: #a3a3a3;
  --label: #525252;
  --border: #e5e5e5;
  --border-strong: #d4d4d4;
  --accent: #000000;
  --accent-contrast: #ffffff;
  --accent-2: #16a34a;
  --accent-soft: #f5f5f5;
  --danger: #b54545;
  --danger-soft: #f6e3e1;
  --warning: #a06419;
  --warning-soft: #f4eadc;
  --success: #16a34a;
  --success-soft: #dcfce7;
  --shadow: 0 12px 34px rgba(22, 22, 19, 0.08);
  --code-bg: #fafafa;
  --code-text: #171717;
  --cm-bg: #ffffff;
  --cm-text: #24292f;
  --cm-gutter-bg: #f6f8fa;
  --cm-gutter-text: #6e7781;
  --cm-active-line: #f6f8fa;
  --cm-selection: rgba(9, 105, 218, 0.18);
  --cm-search-match: rgba(191, 135, 0, 0.24);
  --cm-search-selected: rgba(191, 135, 0, 0.36);
  --cm-token-class: #8250df;
  --cm-token-property: #0969da;
  --cm-token-enum: #953800;
  --cm-token-string: #0a7f47;
  --cm-token-number: #0550ae;
  --cm-token-variable: #cf222e;
  --option-accent-0: #000000;
  --option-accent-1: #8f5d20;
  --option-accent-2: #6f64bf;
  --option-accent-3: #b65772;
  --option-accent-4: #4279b8;
  --option-accent-5: #16a34a;
  --option-accent-6: #aa5b3f;
  --option-accent-7: #737373;
  --option-accent-8: #9458a7;
  --option-accent-9: #4d7f91;
}
```

### Color

```css
.theme-color {
  --bg: #ffffff;
  --surface: #ffffff;
  --surface-2: #fafafa;
  --surface-3: #e5e5e5;
  --text: #171717;
  --muted: #737373;
  --subtle: #a3a3a3;
  --label: #525252;
  --border: #e5e5e5;
  --border-strong: #d4d4d4;
  --accent: #2f6f68;
  --accent-contrast: #ffffff;
  --accent-2: #7f5636;
  --accent-soft: #e2efec;
  --danger: #b54545;
  --danger-soft: #f6e3e1;
  --warning: #a06419;
  --warning-soft: #f4eadc;
  --success: #2f7652;
  --success-soft: #e1efe7;
  --shadow: 0 12px 34px rgba(22, 22, 19, 0.08);
  --code-bg: #ffffff;
  --code-text: #24292f;
  --cm-bg: #ffffff;
  --cm-text: #24292f;
  --cm-gutter-bg: #f6f8fa;
  --cm-gutter-text: #6e7781;
  --cm-active-line: #f6f8fa;
  --cm-selection: rgba(9, 105, 218, 0.18);
  --cm-search-match: rgba(191, 135, 0, 0.24);
  --cm-search-selected: rgba(191, 135, 0, 0.36);
  --cm-token-class: #8250df;
  --cm-token-property: #0969da;
  --cm-token-enum: #953800;
  --cm-token-string: #0a7f47;
  --cm-token-number: #0550ae;
  --cm-token-variable: #cf222e;
  --option-accent-0: #2f6f68;
  --option-accent-1: #8f5d20;
  --option-accent-2: #6f64bf;
  --option-accent-3: #b65772;
  --option-accent-4: #4279b8;
  --option-accent-5: #347854;
  --option-accent-6: #aa5b3f;
  --option-accent-7: #737373;
  --option-accent-8: #9458a7;
  --option-accent-9: #4d7f91;
}
```

### Dark

```css
.theme-dark {
  --bg: #0d1117;
  --surface: #161b22;
  --surface-2: #21262d;
  --surface-3: #30363d;
  --text: #e6edf3;
  --muted: #8b949e;
  --subtle: #6e7681;
  --label: #8b949e;
  --border: #30363d;
  --border-strong: #484f58;
  --accent: #58a6ff;
  --accent-contrast: #0d1117;
  --accent-2: #d29922;
  --accent-soft: #0f2744;
  --danger: #f85149;
  --danger-soft: #3a1518;
  --warning: #d29922;
  --warning-soft: #332412;
  --success: #3fb950;
  --success-soft: #102c1a;
  --shadow: 0 18px 42px rgba(1, 4, 9, 0.3);
  --code-bg: #161b22;
  --code-text: #c9d1d9;
  --cm-bg: #161b22;
  --cm-text: #c9d1d9;
  --cm-gutter-bg: #0d1117;
  --cm-gutter-text: #6e7681;
  --cm-active-line: rgba(88, 166, 255, 0.08);
  --cm-selection: rgba(56, 139, 253, 0.28);
  --cm-search-match: rgba(187, 128, 9, 0.34);
  --cm-search-selected: rgba(187, 128, 9, 0.48);
  --cm-token-class: #d2a8ff;
  --cm-token-property: #79c0ff;
  --cm-token-enum: #ffa657;
  --cm-token-string: #a5d6ff;
  --cm-token-number: #79c0ff;
  --cm-token-variable: #ff7b72;
  --option-accent-0: #58a6ff;
  --option-accent-1: #d29922;
  --option-accent-2: #d2a8ff;
  --option-accent-3: #ff7b9c;
  --option-accent-4: #79c0ff;
  --option-accent-5: #3fb950;
  --option-accent-6: #ffa657;
  --option-accent-7: #8b949e;
  --option-accent-8: #b083f0;
  --option-accent-9: #56d4dd;
}
```

### Warm

```css
.theme-anthropic {
  --bg: #f0eee6;
  --surface: #faf9f5;
  --surface-2: #e8e6dc;
  --surface-3: #d1cfc5;
  --text: #141413;
  --muted: #3d3d3a;
  --subtle: #87867f;
  --label: #5e5d59;
  --border: #1414131a;
  --border-strong: #14141333;
  --accent: #c6613f;
  --accent-contrast: #ffffff;
  --accent-2: #d97757;
  --accent-soft: #f1ded6;
  --danger: #c25b4e;
  --danger-soft: #f3ded8;
  --warning: #d9853b;
  --warning-soft: #f4e5d3;
  --success: #059669;
  --success-soft: #deeee5;
  --shadow: 0 16px 38px rgba(20, 20, 19, 0.1);
  --code-bg: #ecebe4;
  --code-text: #141413;
  --cm-bg: #faf9f5;
  --cm-text: #141413;
  --cm-gutter-bg: #f0eee6;
  --cm-gutter-text: #5e5d59;
  --cm-active-line: rgba(198, 97, 63, 0.1);
  --cm-selection: rgba(198, 97, 63, 0.22);
  --cm-search-match: rgba(217, 133, 59, 0.28);
  --cm-search-selected: rgba(217, 133, 59, 0.4);
  --cm-token-class: #c6613f;
  --cm-token-property: #5563c1;
  --cm-token-enum: #d97757;
  --cm-token-string: #059669;
  --cm-token-number: #d9853b;
  --cm-token-variable: #c25b4e;
  --option-accent-0: #c6613f;
  --option-accent-1: #d97757;
  --option-accent-2: #5563c1;
  --option-accent-3: #c25b4e;
  --option-accent-4: #4f7a99;
  --option-accent-5: #059669;
  --option-accent-6: #d9853b;
  --option-accent-7: #5e5d59;
  --option-accent-8: #9561a8;
  --option-accent-9: #4d8372;
}
```

### Utopia

```css
.theme-utopia {
  --bg: #ffffff;
  --surface: #ffffff;
  --surface-2: #f5f6f7;
  --surface-3: #e9ecf2;
  --text: #0f1115;
  --muted: #61666b;
  --subtle: #adb2b8;
  --label: #61666b;
  --border: rgba(0, 0, 0, 0.04);
  --border-strong: rgba(0, 0, 0, 0.12);
  --accent: #4176e6;
  --accent-contrast: #ffffff;
  --accent-2: #4d6bfe;
  --accent-soft: #edf3fe;
  --danger: #ec1313;
  --danger-soft: #fef2f2;
  --warning: #f59e0b;
  --warning-soft: #fef5e7;
  --success: #22c55e;
  --success-soft: #e6faed;
  --shadow: 0 0 1px 0 rgba(0, 0, 0, 0.2), 0 0 4px 0 rgba(0, 0, 0, 0.02), 0 12px 32px 0 rgba(0, 0, 0, 0.08);
  --code-bg: #f9fafb;
  --code-text: #0f1115;
  --cm-bg: #ffffff;
  --cm-text: #0f1115;
  --cm-gutter-bg: #f5f6f7;
  --cm-gutter-text: #81858c;
  --cm-active-line: #f1f3f5;
  --cm-selection: rgba(65, 118, 230, 0.18);
  --cm-search-match: rgba(245, 158, 11, 0.24);
  --cm-search-selected: rgba(245, 158, 11, 0.36);
  --cm-token-class: #4868b2;
  --cm-token-property: #4176e6;
  --cm-token-enum: #dd8629;
  --cm-token-string: #22c55e;
  --cm-token-number: #5686fe;
  --cm-token-variable: #ec1313;
  --option-accent-0: #4176e6;
  --option-accent-1: #4d6bfe;
  --option-accent-2: #5686fe;
  --option-accent-3: #679efe;
  --option-accent-4: #4868b2;
  --option-accent-5: #22c55e;
  --option-accent-6: #f59e0b;
  --option-accent-7: #ec1313;
  --option-accent-8: #61666b;
  --option-accent-9: #adb2b8;
}
```

### Dystopia

```css
.theme-dystopia {
  --bg: #151517;
  --surface: #232324;
  --surface-2: #2c2c2e;
  --surface-3: #353638;
  --text: #f9fafb;
  --muted: #cfd3d6;
  --subtle: #adb2b8;
  --label: #cfd3d6;
  --border: rgba(255, 255, 255, 0.06);
  --border-strong: rgba(255, 255, 255, 0.16);
  --accent: #5686fe;
  --accent-contrast: #0f1115;
  --accent-2: #4d6bfe;
  --accent-soft: #34415b;
  --danger: #f25a5a;
  --danger-soft: #570c0c;
  --warning: #f59e0b;
  --warning-soft: #27241f;
  --success: #22c55e;
  --success-soft: #233c2c;
  --shadow: 0 0 1px 0 rgba(0, 0, 0, 0.2), 0 0 4px 0 rgba(0, 0, 0, 0.02), 0 12px 32px 0 rgba(0, 0, 0, 0.08);
  --code-bg: #1b1b1c;
  --code-text: #e9ecf2;
  --cm-bg: #1b1b1c;
  --cm-text: #e9ecf2;
  --cm-gutter-bg: #151517;
  --cm-gutter-text: #81858c;
  --cm-active-line: rgba(86, 134, 254, 0.1);
  --cm-selection: rgba(86, 134, 254, 0.28);
  --cm-search-match: rgba(245, 158, 11, 0.34);
  --cm-search-selected: rgba(245, 158, 11, 0.48);
  --cm-token-class: #b7c8fe;
  --cm-token-property: #679efe;
  --cm-token-enum: #f7ad31;
  --cm-token-string: #4ed17e;
  --cm-token-number: #679efe;
  --cm-token-variable: #f25a5a;
  --option-accent-0: #5686fe;
  --option-accent-1: #4d6bfe;
  --option-accent-2: #679efe;
  --option-accent-3: #b7c8fe;
  --option-accent-4: #4868b2;
  --option-accent-5: #22c55e;
  --option-accent-6: #f59e0b;
  --option-accent-7: #f25a5a;
  --option-accent-8: #cfd3d6;
  --option-accent-9: #adb2b8;
}
```

## Theme Application

Token names define attention roles; they do not guarantee that every possible pairing is useful or readable.

| Role | Use |
| --- | --- |
| `--bg` | Outer application frame and the quietest continuous field. |
| `--surface` | Primary work surfaces, forms, tables, editors, and dialogs. |
| `--surface-2` | Supporting panels, grouped controls, hover regions, and secondary layers. |
| `--surface-3` | Pressed, strongly separated, or selectively emphasized neutral regions. |
| `--text` | Meaningful body text, labels, values, and task-critical information. |
| `--muted` | Meaningful secondary information that still needs comfortable reading. |
| `--subtle` | Dispensable metadata and decorative de-emphasis only. |
| `--accent` / `--accent-soft` | Current task, primary action, active mode, and selection; soft fill carries area, solid accent carries the focal edge or control. |
| Semantic hue / soft pair | Consequence and status. Use hue as one cue, not the only cue. |
| Option accents | Stable category identity in repeated objects or data, with deterministic mapping. |

### Theme Controls

The default standard GUI control is a compact three-position slide switch: Light, Warm, and Dystopia (the Dark position), in that order. Use the `.theme-dystopia` DeepSeek Dark atmosphere for the third position rather than the separate GitHub Soft Dark theme. Give each position a stable icon (sun, warm spark, and moon) plus a visible or programmatic label. The control must expose the selected state through text, shape, or position as well as color, support keyboard focus and arrow/Home/End navigation, and avoid layout shifts or decorative motion when the mode changes.

An optional icon-labeled dropdown may expose the full six-mode palette: Light (Ollama White Grayscale), Colorful (Ollama White), Warm (Anthropic), Dark (GitHub Soft Dark), Utopia (DeepSeek Light), and Dystopia (DeepSeek Dark). Reuse the same labels and icon family in both controls, keep the current mode visible after selection, and place the advanced menu near—but visually quieter than—the common three-mode switch. A theme change is a user preference, not a new layout or component vocabulary; preserve the same task state, density, and attention order in every mode.

### Color Attention Rules

- Let neutral surfaces and text carry most of the interface. Accent marks the current path through it.
- Keep one filled accent action or focal accent cluster per view. Multiple selected items may use accent-soft, but they must not all read as calls to action.
- Use semantic colors only when the semantic state is present. Never use danger, warning, or success as decoration or brand color.
- Keep option-accent assignments stable across themes and sessions. Pair them with labels, shape, or position so color is not the only identifier.
- Preserve the same attention order in all six modes. A theme change must not make tertiary chrome more prominent than the task.
- Keep code/editor colors inside technical content; they do not become general interface accents.

### Contrast And Perception

- Use `--text` for meaningful small text. Use `--muted` only when the rendered pairing remains comfortably readable.
- Never use `--subtle` for labels, placeholders that act as labels, instructions, state, or the only discoverable affordance.
- Prefer `--text` on semantic soft fills and use the semantic hue in an icon, edge, or marker when colored text would be weak.
- Verify filled accent controls before using `--accent-contrast` for normal-size text; the token name alone is not proof of contrast.
- Soft fills and borders may group content, but they are not the only boundary for focus, selection, or a control. Add structure, spacing, text, or a solid edge.
- Meet WCAG AA in the rendered composition: at least `4.5:1` for normal text, `3:1` for large text, and `3:1` for necessary control and focus boundaries. Preserve meaning at high zoom, reduced motion, and without color.
- Add a narrowly scoped accessibility role token when necessary rather than changing the canonical palette. Document its single role and keep it visually subordinate to the principal accent.

## Maintenance And Review

Maintenance is design work. Its goal is not to freeze every pixel; it is to preserve the user's mental model while steadily reducing visual drift.

### Maintenance Order

1. Capture the relevant current views, themes, widths, and states before changing them.
2. Name the task, attention order, and user state that must remain stable.
3. Reuse the canonical layout, element family, token, spacing, and motion pattern.
4. Repair an existing shared pattern before adding a local exception.
5. Compare the same states before and after. Check what became louder, quieter, denser, or displaced—not only what looks polished in isolation.
6. Remove superseded one-off values and variants. Record any necessary exception with its reason and review condition.

When transferring an interface between projects, map semantic roles and relationships: task surface to task surface, browser to browser, selection to selection, and supporting detail to the appropriate disclosure layer. Preserve the target product's system; do not transplant incidental dimensions or framework defaults.

### Rendered Review Matrix

Review only the states the product claims to support, but review them consistently:

- all six themes for durable surfaces;
- wide, constrained, narrow, and `200%` zoom layouts;
- default, hover, focus, selected, disabled, loading, empty, offline, success, and failure states as relevant;
- opening and closing panels, menus, dialogs, inspectors, and assistants;
- reduced motion, long or translated labels, slow content, and preserved selection or edits;
- third-party element boundaries, actual contrast, and the hierarchy without color.

### Final Questions

- **Task:** Is the current task or object unmistakable, with one dominant action path?
- **Attention:** Does every persistent element earn its salience, and are global/tertiary controls quieter than the work?
- **Hierarchy:** Can the reading order and importance be understood through position, type, and spacing before color?
- **Disclosure:** Is complexity revealed at the moment and in the layer where it helps, without losing context?
- **Unity:** Do identical meanings use the same element family, geometry, copy, state, and motion?
- **Color:** Are all six modes complete, equally calm, and free of one-off color or competing accents?
- **Spacing:** Is spacing tight within groups, larger between groups, and largest between task regions?
- **Motion:** Does every animation explain cause, continuity, or feedback, with no recurring attention capture?
- **Maintenance:** Did the change reduce drift and retire obsolete exceptions rather than add another style island?
- **Access:** Are focus, state, contrast, hit regions, reading order, and reduced motion clear without weakening the visual hierarchy?
