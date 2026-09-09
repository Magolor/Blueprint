---
name: gui-motion
description: Read before choosing GUI geometry or animation.
---

# Geometry and motion

## Summary

Use shared geometry and motion to explain cause, continuity, or feedback. Preserve the same information with reduced motion.

## Geometry And Motion

| Token | Value |
| --- | --- |
| Radius small | `6px` |
| Radius medium | `8px` |
| Radius large | `12px` |
| Border | `1px` |
| Focus boundary | Solid `2px` accent boundary with `2px` offset and a surface separator when needed |
| Fast feedback | `120ms` to `150ms` |
| Standard transition | `150ms cubic-bezier(0.2, 0.8, 0.2, 1)` |
| Panel transition | `210ms cubic-bezier(0.2, 0.8, 0.2, 1)` |

Use `6px` for compact controls and chips. Use `8px` for panels and popovers. Use `12px` for dialogs and sheets. Pill shapes belong to semantic chips, status, and genuinely circular actions, not generic controls. Use thin borders and nearby surface shifts before shadow. Reserve the one soft shadow for floating layers that overlap content.

### Motion Rules

- Animate to show causality, preserve spatial continuity, or confirm state. If the motion explains none of these, remove it.
- Keep only one focal movement active at a time. Do not combine panel motion, animated badges, pulsing status, and attention-seeking hover effects.
- Make entry emerge from its source and exit return toward it. Expansion and collapse preserve the user's spatial model without abrupt jumps.
- Use color, border, opacity, or a restrained `1px` movement for hover/press feedback. Avoid bounce, elastic overshoot, parallax, looping decoration, and large hover lifts.
- Do not delay task completion for choreography. Avoid staggered reveals in operational interfaces.
- Allow looping motion only for real ongoing progress, and keep it quiet. Stop it as soon as the state ends.
- Provide a reduced-motion path with the same information and continuity, using immediate state changes or short fades.

## Pattern and Anti-pattern

- **Pattern:** A drawer expands from its trigger; reduced motion reveals it immediately.
- **Anti-pattern:** A drawer bounces while badges and the primary action pulse.

Motion explains one transition without competing attention.
