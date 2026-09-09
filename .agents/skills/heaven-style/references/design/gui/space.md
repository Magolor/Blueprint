---
name: gui-space
description: Read before setting GUI typography, spacing, or density.
---

# Typography and spacing

## Summary

Use typography and shared spacing to make groups and task regions clear without artificial emptiness.

## Typography, Spacing, And Density

Typography and space establish hierarchy before color does. Use the platform's system sans-serif family or a product-approved equivalent. Reserve monospace for paths, identifiers, code, protocol values, and compact technical status.

| Role | Size | Weight | Line height |
| --- | ---: | ---: | ---: |
| App title | `14px` | `650` | `20px` |
| Panel heading | `12px` | `650` | `16px` |
| Body | `13px` | `450` | `19px` |
| Label | `11px` | `600` | `14px` |
| Mono/status | `11px` | `500` | `15px` |

- Use larger display headings only for real document pages, reports, or presentation surfaces—not routine workbench chrome.
- Keep letter spacing neutral. Use weight and spacing, not compressed tracking or many type sizes, to create hierarchy.
- Write labels as nouns and actions as verbs. Keep commands short, specific, and consistent.
- Truncate only when the full value remains available through a stable detail surface. Place explanations and recovery near the decision they affect.

### Spacing Rhythm

Use only the shared scale: `4px`, `8px`, `12px`, `16px`, `24px`, `32px`, and `48px`.

| Relationship | Normal spacing |
| --- | ---: |
| Icon to label, tightly paired metadata | `4px` to `8px` |
| Inside compact controls and rows | `8px` to `12px` |
| Between items in one group | `8px` to `12px` |
| Between related groups | `16px` to `24px` |
| Between major task regions | `24px` to `32px`, or a clear panel boundary |
| Rare document/presentation break | `48px` |

Keep spacing tightest within a semantic group, larger between groups, and largest between task regions. Space clarifies ownership. It does not exist to make a dense tool look artificially empty.

- Align headings, labels, fields, toolbars, and content to shared axes. Repeated one- or two-pixel optical corrections belong to the component, not each page.
- Use `12px` to `16px` panel insets by default. A dense table may reach the panel edge when its header and row geometry provide the structure.
- Target a `32px` default desktop control family. A named compact variant may be smaller for repeated data operations; touch surfaces enlarge the hit region toward `40px` to `44px` without making every visible control heavy.
- Keep density consistent inside a task region. Do not mix airy cards, tiny table controls, and oversized marketing headings in one operational view.

## Pattern and Anti-pattern

- **Pattern:** Related fields share a tight gap; the next task group has a larger gap.
- **Anti-pattern:** Every field and unrelated task region has the same large gap.

Spacing communicates relationships rather than decoration.
