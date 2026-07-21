---
id: gui-style
title: GUI style
enabled: true
default_exposed: false
order: 10
keywords: [gui, ui, frontend, desktop app, web app, app shell, dashboard, design system, theme, tokens, minimalism, materialism, react, vue, streamlit, pyside, nicegui, tailwind]
description: Use when designing, implementing, or reviewing graphical user interfaces, app shells, dashboards, desktop tools, or web frontends in any framework.
---

# GUI Style

## Core Rule

Heaven-style GUI work should feel like a quiet local workbench: minimal visible choices, precise surfaces, thin typography, clean icons, low-glare colors, and smooth but modest motion. This guide is framework-neutral. Apply it to React, Vue, Streamlit, PySide, NiceGUI, Tailwind, native desktop, or any other UI layer by mapping the tokens and rules to that platform's primitives.

This is not Google Material Design. "Materialism" here means the interface feels calmly physical: soft edges, subtle elevation, restrained panels, tactile state changes, and colors that stay close enough that the user can work for hours without visual fatigue.

GUI architecture follows the [service interface rule](../rules/project/interfaces.md): graphical surfaces are thin API clients. Prefer the zero-build Python/ASGI local-workbench stack for a minimal GUI and React with TypeScript plus Tauri v2 for a serious releasable desktop app.

## Philosophy

### Minimalism

Show the smallest number of buttons, labels, descriptions, and decorative elements that still makes the current task obvious.

- Prefer one clear primary path over several visible alternatives.
- Hide secondary actions behind icon buttons, menus, command palettes, context menus, inspectors, or progressive disclosure.
- Use one-line empty states and status text. Avoid tutorial copy inside the app chrome.
- Replace repeated text buttons with icon buttons when the icon is familiar and the control has an accessible label or tooltip.
- Collapse panels, filters, inspectors, and logs when they are not the user's immediate focus.
- Let data tables, lists, editors, canvases, and chat/workflow surfaces carry the screen; do not surround them with marketing copy.

### Materialism

Use calm material surfaces instead of visual effects.

- Corners are smooth and modest: normally `6px` to `8px`; use `12px` only for larger sheets, dialogs, or broad surfaces.
- Borders are thin: normally `1px`; use stronger borders for focus, active selection, or split boundaries.
- Shadows are rare and soft; panels can usually separate through background, border, and spacing alone.
- Motion is short and quiet: `120ms` to `220ms`, easing like `cubic-bezier(0.2, 0.8, 0.2, 1)`.
- Avoid glassmorphism, decorative gradients, glow effects, bouncy motion, heavy blur, thick outlines, and theatrical high contrast.
- Preserve accessibility contrast for text and controls, but avoid pure-black/pure-white dominance when a softer neutral works.

## Reference Signals

Use these examples for interaction feel, not for direct cloning:

- Attu Data Explorer: dense left navigation, nested object browser, tabbed detail surface, icon-first actions, subdued empty state, and a large primary workspace.
- Ollama desktop app: local-first chat surface, simple file-aware workflow, quiet app chrome, and desktop-tool restraint.
- oMLX: native desktop packaging, localized app expectations, and local-model workflow focus.
- Codex app: restrained panes, thread/workspace focus, low-copy controls, and compact agent/status surfaces.

## Layout

Start every GUI as the actual tool, not a landing page.

Prefer this shell model for workbench apps:

```text
App window
  left rail: global navigation, workspace switch, command entry
  optional browser panel: project, collection, files, objects, or modules
  main workspace: editor, table, canvas, chat, dashboard, or task surface
  optional inspector: selected object, run details, settings, logs, metadata
  status strip: local services, route, backend, sync, or job state
```

The shell should support dense repeated work:

- Use rails, side panels, split panes, tabs, trees, tables, lists, editors, and inspectors before cards.
- Cards are for repeated items, modal sheets, or contained tools. Do not put cards inside cards.
- Keep page sections unframed unless a real item or modal needs a frame.
- Use a shared toolbar for search, command entry, sync/run actions, panel toggles, and theme choice.
- Panel chrome should usually be icon-only; action menus can show icon plus label.
- Tabs are for durable workspace contexts. Segmented controls are for modes inside one context.
- Empty workspaces should be intentional and short: one line, one obvious action, no long explanation.
- Prefer stable dimensions for rails, toolbar controls, tables, boards, and tiles so hover states and dynamic labels do not shift layout.

## Information Density

The interface should feel compact, not cramped.

- Default body text is `13px` to `14px`; panel labels can be `11px` to `12px`.
- Use `ui-monospace` fonts for paths, IDs, model names, status codes, table keys, and protocol labels.
- Letter spacing stays `0`; do not compress headings with negative tracking.
- Long names truncate with ellipsis in narrow rails and reveal the full value through title/tooltip or inspector detail.
- Prefer tables and lists for comparable operational data. Use cards only when item shape is heterogeneous or spatial grouping is meaningful.
- Group related controls by proximity and separators; avoid descriptive paragraphs next to every control.
- Write labels as nouns and actions as verbs. Keep button copy to one or two words when text is needed.

## Component Rules

- Use clean icon sets from the framework or app library; icons inherit current text color.
- Icon buttons need accessible labels and tooltips. Text labels are optional only when the icon is familiar.
- Use text buttons for clear commands such as `Run`, `Build`, `Sync`, `Open`, `Save`, and `Connect`.
- Use segmented controls for mutually exclusive modes.
- Use toggles or checkboxes for binary settings.
- Use sliders, steppers, or numeric inputs for numeric settings.
- Use menus for option sets and overflow actions.
- Use tabs for open workspaces, views, or durable contexts.
- Use chips, badges, and progress indicators only when they carry real state.
- Do not fake production metrics, live status, or completed work. Use honest states such as `scaffold`, `planned`, `offline`, `local`, `ready`, `loading`, `running`, and `failed`.
- Keep all interactive controls keyboard-focusable and screen-reader named.

## Component Unity

Every visible component must look like it belongs to the same interface, regardless of page, route, framework widget, browser default, or open-source component library.

- Buttons, dropdown lists, comboboxes, select menus, search bars, text inputs, textareas, tables, tabs, chips, dialogs, tooltips, context menus, date pickers, file pickers, pagination controls, scrollbars, and command palettes must consume the same theme tokens.
- Do not let default browser or library styles escape into the product. Native `select`, default dropdown menus, data-grid controls, and popover panels are common failure points; wrap, theme, or replace them before shipping.
- A third-party component is acceptable only when its background, border, radius, typography, icon color, shadow, hover, active, selected, disabled, focus, error, and empty states can be aligned with this guide.
- Prefer one component library per surface. If a project mixes libraries, add a local adapter layer that normalizes tokens, sizing, state classes, and accessibility labels.
- Dropdown and popover panels must match the invoking control: same font scale, radius family, border color, surface color, item height, icon treatment, hover color, selected state, and shadow policy.
- Search bars and text inputs share the same height, padding, border, placeholder color, focus ring, disabled state, and error treatment unless a dense table filter explicitly needs a compact variant.
- Tables use the same typography, row height rhythm, separator color, hover state, selected state, loading state, empty state, and inline action style as the rest of the shell.
- Component variants should be explicit and few: default, compact, danger, subtle, and primary are usually enough.

## Typography

Use system fonts first and keep the interface code-adjacent:

```css
font-family:
  Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont,
  "Segoe UI", sans-serif;
```

Use `SFMono-Regular`, `Menlo`, `Consolas`, `Liberation Mono`, or `ui-monospace` for technical labels.

| Role | Size | Weight | Line height |
| --- | ---: | ---: | ---: |
| App title | `14px` | `650` | `20px` |
| Panel heading | `12px` | `650` | `16px` |
| Body | `13px` | `450` | `19px` |
| Label | `11px` | `600` | `14px` |
| Mono/status | `11px` | `500` | `15px` |

Use larger headings only for real document pages, reports, or first-viewport website heroes. Tool surfaces, sidebars, dashboards, modals, and cards should use compact headings.

## Geometry And Motion

| Token | Value |
| --- | --- |
| Radius small | `6px` |
| Radius medium | `8px` |
| Radius large | `12px` |
| Border width | `1px` |
| Focus ring | `0 0 0 3px color-mix(in srgb, var(--accent) 22%, transparent)` |
| Fast motion | `150ms cubic-bezier(0.2, 0.8, 0.2, 1)` |
| Panel motion | `210ms cubic-bezier(0.2, 0.8, 0.2, 1)` |

Animate size, opacity, and transform only when the movement explains state. Collapsible panels should animate layout tracks or size constraints instead of unmounting abruptly. Always provide a reduced-motion fallback.

## Theme System

Maintain exactly three major themes unless the product has a real brand requirement. Each theme must define shell, semantic, inline-code, editor, and option-accent tokens together. Do not create a new theme by only changing background and accent colors.

| Mode | CSS class | Source | Intent |
| --- | --- | --- | --- |
| Light Mode | `.theme-light` | Ollama White | Local-first light workbench with neutral surfaces and a muted teal action color. |
| Dark Mode | `.theme-dark` | GitHub Soft Dark | Soft developer dark mode with GitHub-like syntax colors and low-glare panels. |
| Warm Mode | `.theme-anthropic` | Anthropic | Warm paper workbench with Anthropic-inspired slate, ivory, and clay tones. |

Every theme defines:

- Shell tokens: `--bg`, `--surface`, `--surface-2`, `--surface-3`, `--text`, `--muted`, `--subtle`, `--label`, `--border`, `--border-strong`, `--accent`, `--accent-contrast`, `--accent-2`, `--accent-soft`, `--danger`, `--danger-soft`, `--warning`, `--warning-soft`, `--success`, `--success-soft`, and `--shadow`.
- Inline code tokens: `--code-bg` and `--code-text`.
- Editor tokens: `--cm-bg`, `--cm-text`, `--cm-gutter-bg`, `--cm-gutter-text`, `--cm-active-line`, `--cm-selection`, `--cm-search-match`, `--cm-search-selected`, `--cm-token-class`, `--cm-token-property`, `--cm-token-enum`, `--cm-token-string`, `--cm-token-number`, and `--cm-token-variable`.
- Option accents: `--option-accent-0` through `--option-accent-9` for hashed repeated objects, series, labels, and category markers.

### Light Mode (Ollama White)

```css
.theme-light {
  --bg: #f6f6f5;
  --surface: #ffffff;
  --surface-2: #f1f1ef;
  --surface-3: #e9e9e6;
  --text: #171717;
  --muted: #6f6f6a;
  --subtle: #9a9a94;
  --label: #6f6f6a;
  --border: #deded9;
  --border-strong: #c8c8c1;
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

### Dark Mode (GitHub Soft Dark)

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

### Warm Mode (Anthropic)

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

## Framework Mapping

- CSS/Tailwind: keep these as CSS custom properties and map Tailwind theme values to them.
- React/Vue/Svelte: expose a small theme enum and one root class; components consume tokens only.
- Streamlit/NiceGUI: define the closest theme config first, then add component-level CSS only for gaps.
- PySide/Qt: map shell colors to palette roles and use style sheets only for spacing, radius, and token gaps.
- Native desktop: prefer platform controls where they match this density; override only color, spacing, and icon policy.
- Canvas/WebGL/custom views: keep surrounding chrome token-driven; use option accents only for stable categories or selected objects.

## Review Checklist

- The first screen is the usable tool, not a marketing or tutorial page.
- The visible button count is the minimum needed for the current task.
- Secondary controls are discoverable but not always visible.
- Text is short, factual, and placed only where it changes decisions.
- Icons are clean, consistent, keyboard reachable, and accessible.
- Buttons, dropdowns, search bars, input boxes, tables, popovers, and third-party widgets share the same component theme rather than showing library defaults.
- The palette uses the three-mode token contract and avoids one-off colors.
- Corners, borders, shadows, and motion are calm and consistent.
- Dense data uses lists, tables, trees, tabs, editors, or split panes instead of decorative cards.
- Empty, loading, running, failed, and offline states are honest and visually quiet.
- The interface remains readable on small screens and does not shift when labels, hover states, or status values change.

## Sources

- [Attu Data Explorer screenshot](https://github.com/zilliztech/attu/blob/main/.github/images/v3/19-collection-search.png)
- [Ollama desktop app announcement and screenshots](https://ollama.com/blog/new-app)
