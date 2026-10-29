---
name: gui-theme
description: Read before implementing or reviewing theme support.
---

# Themes

## Summary

Use six exact palettes for one consistent interface. Theme changes preserve layout, meaning, and attention order.

## Theme System

The six themes are alternate atmospheres for one interface, not separate designs. Layout, hierarchy, component meaning, spacing, and relative salience remain stable when the theme changes.

The palette below is design-system revision 6, which unifies the six presets across Dashboard, HeavenBase-2, and Heaven Style. Durable Heaven Style interfaces support all six themes and keep every listed value exact unless a later explicit design-system revision changes the contract. A disposable static artifact may choose one canonical theme. It must not invent a seventh theme or partially recolor only the background and accent. The CSS classes in the palette pages are reference selectors; a host may apply the same tokens through scoped style variables.

Light uses a pure-white (`#ffffff`) canvas, pure-black (`#000000`) borders, black primary actions, neutral supporting surfaces, and colored code syntax confined to code content. Green is reserved for semantic controls. Colorful keeps that complete Ollama white frame—canvas, borders, text, labels, muted text, and code surfaces—and changes only the interaction and semantic colors: the Material interaction and status accents and the Material Design 2 chart colors. Utopia and Dystopia use cool neutral layers and blue interaction accents. The declarations below own the exact values.

| Short name | Theme name | CSS class | Intent |
| --- | --- | --- | --- |
| Light | Ollama White Grayscale | `.theme-light` | Pure-white canvas with pure-black borders, black actions, and neutral-gray supporting surfaces, plus scoped green semantic controls. |
| Colorful | Ollama White | `.theme-color` | Ollama White frame with pure-black borders and only Material interaction, semantic, and chart accents changed. |
| Warm | Anthropic | `.theme-anthropic` | Warm paper surfaces with slate, ivory, and clay tones.  |
| Dark | GitHub Soft Dark | `.theme-dark` | Soft developer-dark surfaces with low glare and clear editor syntax. |
| Utopia | Cool light | `.theme-utopia` | Cool light surfaces with neutral-bluish layers and blue business state. |
| Dystopia | Cool dark | `.theme-dystopia` | Cool dark surfaces with neutral-bluish layers and blue business state. |

Every theme maintains parity across:

- Shell tokens: `--bg`, `--surface`, `--surface-2`, `--surface-3`, `--text`, `--muted`, `--subtle`, `--label`, `--border`, `--border-strong`, `--accent`, `--accent-contrast`, `--accent-2`, `--accent-soft`, `--danger`, `--danger-soft`, `--warning`, `--warning-soft`, `--success`, `--success-soft`, and `--shadow`.
- Inline code tokens: `--code-bg` and `--code-text`.
- Editor tokens: `--cm-bg`, `--cm-text`, `--cm-gutter-bg`, `--cm-gutter-text`, `--cm-active-line`, `--cm-selection`, `--cm-search-match`, `--cm-search-selected`, `--cm-token-class`, `--cm-token-property`, `--cm-token-enum`, `--cm-token-string`, `--cm-token-number`, `--cm-token-variable`, and `--cm-token-comment`.
- Option accents: `--option-accent-0` through `--option-accent-9` for hashed repeated objects, series, labels, and category markers.
- Progress tokens: `--progress-fill` and `--progress-sheen` for a stable determinate track.

Raw hexadecimal colors belong only in these declarations or in documented domain visualizations. Elements consume semantic tokens. `--accent` is the principal interaction accent. `--accent-2` and option accents support stable identity or data categories. They must not compete with primary actions or encode selection or status alone.

## Exact palettes

Load the relevant declaration for a static artifact, or all six when implementing durable theme support: [Light](theme/light.md), [Colorful](theme/color.md), [Warm](theme/warm.md), [Dark](theme/dark.md), [Utopia](theme/utopia.md), [Dystopia](theme/dystopia.md). Use [color application](color.md) for the selector, contrast, and semantic roles.
