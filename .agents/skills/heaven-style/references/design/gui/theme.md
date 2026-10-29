---
name: gui-theme
description: Read before implementing or reviewing theme support.
---

# Themes

## Summary

Use six exact palettes for one consistent interface. Theme changes preserve layout, meaning, and attention order.

## Theme System

The six themes are alternate atmospheres for one interface, not separate designs. Layout, hierarchy, component meaning, spacing, and relative salience remain stable when the theme changes.

The palette below is design-system revision 10, which unifies the six presets across Dashboard, HeavenBase-2, and Heaven Style and records the split between the Ollama White Light frame and the Pantone Cloud Dancer Colorful frame. Durable Heaven Style interfaces support all six themes and keep every listed value exact unless a later explicit design-system revision changes the contract. A disposable static artifact may choose one canonical theme. It must not invent a seventh theme or partially recolor only the background and accent. The CSS classes in the palette pages are reference selectors; a host may apply the same tokens through scoped style variables.

Light uses a pure-white (`#ffffff`) canvas, soft gray borders (`#e5e5e5` and `#d4d4d4`), black primary actions, neutral supporting surfaces, and MUI semantic status colors; its chart accents are grayscale, and colored code syntax stays confined to code content. Green is reserved for semantic controls. Colorful starts from the Ollama White structure, replaces the white and gray neutral ramp with Pantone Cloud Dancer densities (`#f0eee9` canvas, `#fbfaf7`, `#eae7e0`, and `#dcd8cf` surfaces, `#dcd8cf` and `#b9b4a9` borders), uses MUI only for semantic status colors, and Classical Material Design 2 only for chart accents; the tuned muted blue remains the interaction accent. Utopia and Dystopia copy the DeepSeek Harness light and dark palettes; Warm follows Anthropic's paper and clay tones, and Dark follows GitHub Soft Dark. The declarations below own the exact values.

| Short name | Theme name | CSS class | Intent |
| --- | --- | --- | --- |
| Light | Ollama White Grayscale | `.theme-light` | Ollama White frame with MUI semantic status colors and a grayscale chart palette; scoped green semantic controls. |
| Colorful | Cloud Dancer Material | `.theme-color` | Pantone Cloud Dancer neutral ramp with MUI status and Material Design 2 chart accents. |
| Warm | Anthropic | `.theme-anthropic` | Anthropic paper surfaces with slate, ivory, and clay tones.  |
| Dark | GitHub Soft Dark | `.theme-dark` | Soft developer-dark surfaces with low glare and clear editor syntax. |
| Utopia | DeepSeek Harness light | `.theme-utopia` | DeepSeek Harness light palette: a white canvas, cool neutral-bluish layers, and deepseek-blue business state. |
| Dystopia | DeepSeek Harness dark | `.theme-dystopia` | DeepSeek Harness dark palette: low-glare neutral-bluish layers and deepseek-blue business state. |

Every theme maintains parity across:

- Shell tokens: `--bg`, `--surface`, `--surface-2`, `--surface-3`, `--text`, `--muted`, `--subtle`, `--label`, `--border`, `--border-strong`, `--accent`, `--accent-contrast`, `--accent-2`, `--accent-soft`, `--danger`, `--danger-soft`, `--warning`, `--warning-soft`, `--success`, `--success-soft`, and `--shadow`.
- Inline code tokens: `--code-bg` and `--code-text`.
- Editor tokens: `--cm-bg`, `--cm-text`, `--cm-gutter-bg`, `--cm-gutter-text`, `--cm-active-line`, `--cm-selection`, `--cm-search-match`, `--cm-search-selected`, `--cm-token-class`, `--cm-token-property`, `--cm-token-enum`, `--cm-token-string`, `--cm-token-number`, `--cm-token-variable`, and `--cm-token-comment`.
- Option accents: `--option-accent-0` through `--option-accent-9` for hashed repeated objects, series, labels, and category markers.
- Progress tokens: `--progress-fill` and `--progress-sheen` for a stable determinate track.

Raw hexadecimal colors belong only in these declarations or in documented domain visualizations. Elements consume semantic tokens. `--accent` is the principal interaction accent. `--accent-2` and option accents support stable identity or data categories. They must not compete with primary actions or encode selection or status alone.

## Exact palettes

Load the relevant declaration for a static artifact, or all six when implementing durable theme support: [Light](theme/light.md), [Colorful](theme/color.md), [Warm](theme/warm.md), [Dark](theme/dark.md), [Utopia](theme/utopia.md), [Dystopia](theme/dystopia.md). Use [color application](color.md) for the selector, contrast, and semantic roles.
