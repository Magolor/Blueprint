---
name: gui-attention
description: Read before choosing GUI attention and information hierarchy.
---

# Attention

## Summary

Establish task importance through position, grouping, and typography before adding color or motion.

## Attention And Hierarchy

Treat attention as a finite budget. Persistent accent, high contrast, large type, elevation, badges, and motion all spend that budget. Do not stack several of them on ordinary controls.

Use visual signals in this order, escalating only when the earlier signals are insufficient:

1. position and reading order;
2. grouping, alignment, and spacing;
3. typography and size;
4. surface or border contrast;
5. accent color;
6. motion.

The hierarchy must remain understandable without color. Position, type, spacing, and structure establish persistent importance. Semantic color and motion communicate temporary consequence.

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

Organize a view into roughly three to five meaningful groups when that improves scanning. This is a cognitive-load heuristic, not a visual quota. A group exists because its contents share a decision or task, not because the page needs another container.

## Pattern and Anti-pattern

- **Pattern:** One filled Run action; neutral appearance control.
- **Anti-pattern:** Run, appearance, and help all pulse in bright accent.

Persistent emphasis follows the task rather than competing controls.
