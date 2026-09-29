---
name: design-philosophy
description: Read before code or architecture work.
---

# Design philosophy

## Summary

Minimize the user’s mental model: expose few public concepts and keep cohesive domain behavior on familiar objects. Internal decomposition must not make users assemble the implementation themselves.

## Quick Read

Before code or architecture work, read **every page below**, alongside the complete applicable language and project rules. This index does not replace them.

| Principle | Required page |
| --- | --- |
| Small public OOP surface | [surface](surface.md) |
| Decoupled layers with one owner | [layers](layers.md) |
| Explicit composition and extension | [compose](compose.md) |
| Explicit state and honest behavior | [state](state.md) |
| Review the user cost | [review](review.md) |

## References

Use the [language rule map](../../rules/overview.md) for native mechanics and the [design task guide](../../tasks/design/guide.md) for design work.
