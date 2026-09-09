---
name: gui-style
description: Read before designing, maintaining, or reviewing a GUI.
default_exposed: false
---

# GUI style

## Summary

Build a quiet, compact workbench that preserves task context and makes consequential state visible.

## Quick Read

Use this contract for new interfaces, maintenance, refactors, transfers, demos, temporary HTML, and reviews. Repository policy and tested product behavior come first. Unless redesign is authorized, preserve task flow, meaning, keyboard semantics, user state, and honest runtime behavior.

Build a quiet, compact workbench for prolonged use. Give the task more weight than surrounding controls. Minimalism reduces decision cost; it does not require empty space or hide useful context.

- Give each view one dominant task. Supporting actions stay neutral until their panel becomes active.
- A persistent element must advance the task, explain state or consequence, prevent a likely mistake, or preserve orientation. Otherwise remove, merge, demote, or disclose it.
- Keep frequent actions, scope, selection, and consequential state visible. Reveal infrequent complexity where relevant.
- Preserve spatial position, selection, scroll, edits, and familiar controls. Make actions and recovery recognizable without remembered gestures or tooltip-only instructions.
- Use one component and state language for the same meaning. Reserve the principal accent for the active task; categories must not compete or encode state alone.
- Motion explains cause, continuity, or feedback. Maintenance converges on canonical tokens and components.

## Required GUI reading

Read every page below and all six palette files before GUI work. This table organizes the material; it does not make the rules optional. Code and architecture tasks also complete [their required reading](../../rules/project/read.md).

| Decision | Read |
| --- | --- |
| Substantial work or mode-specific constraints | [Brief](brief.md), [work modes](work.md) |
| Salience and reading order | [Attention](attention.md) |
| Panels, disclosure, responsive behavior | [Layout](layout.md) |
| Controls, variants, and states | [Elements](element.md) |
| Type, spacing, density | [Space](space.md) |
| Geometry and animation | [Motion](motion.md) |
| Colors or theme controls | [Theme](theme.md), [color](color.md) |
| Framework, host, or package choice | [Tech stack](techstack.md) |
| Before/after verification | [Review](review.md) |

Durable interfaces support all six exact palettes. Static disposable artifacts may choose one canonical theme. A new theme or palette change needs an explicit design-system version.
