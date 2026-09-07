---
id: gui-layout
title: Layout and disclosure
description: Read for layout and disclosure.
---

# Layout and disclosure

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

Disclosure must preserve selection, edits, scroll, and task context. Closing a layer returns attention to the point that opened it. Familiar tooltips may clarify compact controls. Required instructions, state, and recovery remain visible without them.

### Responsive Behavior

Breakpoints follow task failure, not device labels. Define how the interface changes when the primary workspace no longer has enough room:

- Wide: browser, workspace, and optional inspector may coexist.
- Constrained: preserve the workspace and at most one supporting pane. Collapse the other behind an explicit control.
- Narrow or touch: show one hierarchy level at a time, using a drawer, sheet, or route for navigation and inspection. Preserve selection and edits across transitions.
- Horizontal scrolling is acceptable only for intrinsically wide content such as data grids, timelines, or code. Ordinary forms and navigation must reflow.
- Verify the sizes the product claims to support. Also verify at `200%` zoom. Dense desktop controls may use a `24px` minimum target when spacing is limited. Touch-oriented surfaces should approach `40px` to `44px` without making the surrounding controls visually heavy.
