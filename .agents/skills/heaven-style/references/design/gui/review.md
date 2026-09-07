---
id: gui-review
title: GUI review
description: Read for GUI review.
---

# GUI review

## Maintenance And Review

Maintenance is design work. Preserve the user's mental model while steadily reducing visual drift. Do not treat every pixel as fixed.

### Maintenance Order

1. Capture the relevant current views, themes, widths, and states before changing them.
2. Name the task, attention order, and user state that must remain stable.
3. Reuse the canonical layout, element family, token, spacing, and motion pattern.
4. Repair an existing shared pattern before adding a local exception.
5. Compare the same states before and after. Check what became louder, quieter, denser, or displaced—not only what looks polished in isolation.
6. Remove superseded one-off values and variants. Record any necessary exception with its reason and review condition.

When transferring an interface between projects, map semantic roles and relationships: task surface to task surface, browser to browser, selection to selection, and supporting detail to the appropriate disclosure layer. Preserve the target product's system. Do not transplant incidental dimensions or framework defaults.

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
