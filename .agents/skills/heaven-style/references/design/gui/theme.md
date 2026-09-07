---
id: gui-theme
title: Themes
description: Read for themes.
---

# Themes

## Theme System

The six themes are alternate atmospheres for one interface, not separate designs. Layout, hierarchy, component meaning, spacing, and relative salience remain stable when the theme changes.

The palette below is a compatibility contract. Durable Heaven Style interfaces support all six themes and keep every listed value exact unless an explicit design-system version changes the contract. A disposable static artifact may choose one canonical theme. It must not invent a seventh theme or partially recolor only the background and accent.

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

Raw hexadecimal colors belong only in these declarations or in documented domain visualizations. Elements consume semantic tokens. `--accent` is the principal interaction accent. `--accent-2` and option accents support stable identity or data categories. They must not compete with primary actions or encode selection or status alone.

## Exact palettes

Load the relevant declaration for a static artifact, or all six when implementing durable theme support: [Light](theme/light.md), [Colorful](theme/color.md), [Warm](theme/warm.md), [Dark](theme/dark.md), [Utopia](theme/utopia.md), [Dystopia](theme/dystopia.md). Use [color application](color.md) for the selector, contrast, and semantic roles.
