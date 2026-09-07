---
id: gui-element
title: Elements and states
description: Read for elements and states.
---

# Elements and states

## Elements And Unity

Unity means semantic consistency, not forced uniformity. Identical meanings use the same component family and behavior. A compact, touch, data-dense, or domain-specific variant is acceptable only when it is named, intentional, and still recognizably part of the same system.

When a need appears, first reuse an existing element. If that is insufficient, adapt an existing named variant. Then extend the shared family if needed. Invent a new element only when the semantics are new.

### Element Families

- Controls with the same role share height, padding, radius, typography, icon treatment, and state behavior across every view.
- Inputs, search fields, and compact filters belong to one field family. Dropdown panels and popovers visibly belong to their trigger.
- Tabs represent open or durable contexts. Segmented controls switch modes inside one context. Do not style the two as interchangeable pills.
- Tables and lists share row rhythm, separators, selection, empty states, and inline-action placement with the surrounding shell.
- Cards represent repeated objects or truly contained tools. They do not replace normal page structure and are never nested by default.
- Integrate third-party widgets into the product language. If their type, surfaces, geometry, icons, states, or motion remain visibly foreign, they are not yet integrated.
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
