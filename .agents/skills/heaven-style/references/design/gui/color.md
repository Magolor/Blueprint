---
name: gui-color
description: Read before applying theme tokens or building theme controls.
---

# Color application

## Summary

Apply semantic colors to their intended roles and verify contrast in the rendered interface. Keep theme controls consistent and accessible.

## Theme Application

Token names define attention roles. They do not guarantee that every possible pairing is useful or readable.

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

The default standard GUI control is a compact three-position slide switch: Light, Warm, and Dystopia (the Dark position), in that order. Use the `.theme-dystopia` palette for the third position rather than the separate GitHub Soft Dark theme. Use the Tabler sun, flame, and moon icons for these positions. Dystopia borrows Dark's moon only in this compact control because it occupies the dark-mode position. Give every icon a visible or programmatic label. The control must expose the selected state through text, shape, or position as well as color. It must support keyboard focus and arrow/Home/End navigation. It must avoid layout shifts or decorative motion when the mode changes.

An optional icon-labeled dropdown may expose the full six-mode palette: Light (Ollama White Grayscale), Colorful (Ollama White), Warm (Anthropic), Dark (GitHub Soft Dark), Utopia (cool light), and Dystopia (cool dark). Use this canonical mapping:

| Theme | Tabler icon | Bundled SVG |
| --- | --- | --- |
| Light | Sun | [`light.svg`](../../../assets/gui/theme-icons/light.svg) |
| Colorful | Palette | [`colorful.svg`](../../../assets/gui/theme-icons/colorful.svg) |
| Warm | Flame | [`warm.svg`](../../../assets/gui/theme-icons/warm.svg) |
| Dark | Moon | [`dark.svg`](../../../assets/gui/theme-icons/dark.svg) |
| Utopia | Atom | [`utopia.svg`](../../../assets/gui/theme-icons/utopia.svg) |
| Dystopia | Eye | [`dystopia.svg`](../../../assets/gui/theme-icons/dystopia.svg) |

Use these assets or the matching icons from the Tabler library. Keep the `24×24` view box, `2px` stroke, round line caps, round line joins, and equal optical size across the set. Reuse the same labels and icon family in both controls, subject to the compact-control Dystopia exception above. Keep the current mode visible after selection. Place the advanced menu near the common three-mode switch, with less visual prominence. A theme change is a user preference, not a new layout or component vocabulary. Preserve the same task state, density, and attention order in every mode.

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
- Verify filled accent controls before using `--accent-contrast` for normal-size text. The token name alone is not proof of contrast.
- Soft fills and borders may group content, but they are not the only boundary for focus, selection, or a control. Add structure, spacing, text, or a solid edge.
- Meet WCAG AA in the rendered composition: at least `4.5:1` for normal text, `3:1` for large text, and `3:1` for necessary control and focus boundaries. Preserve meaning at high zoom, reduced motion, and without color.
- Add a narrowly scoped accessibility role token when necessary rather than changing the canonical palette. Document its single role and keep it visually subordinate to the principal accent.

## Pattern and Anti-pattern

- **Pattern:** A failed row shows an error label and icon with the danger role.
- **Anti-pattern:** An unlabeled red row is the only indication of failure.

Color reinforces meaning; it does not carry the only signal.
