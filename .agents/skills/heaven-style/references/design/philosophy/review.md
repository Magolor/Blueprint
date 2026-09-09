---
name: design-philosophy-review
description: Read before you review added concepts and architectural boundaries.
---

# Review the user cost

## Summary

Judge a structural change by the user flow, policy ownership, and supported behavior. Added public surface needs a concrete benefit.

## Principle

For each structural change, verify the shortest user flow, the owner of each policy, dependency direction, extension parity where promised, and lifecycle effects. Compare the number of concepts the caller must understand before and after. Require a concrete reason for added public surface.

Pair mandatory boundaries with focused behavioral tests, import checks, or concrete review criteria. Record current behavior, intended changes, and explicit non-goals in their canonical documentation owners.

## Pattern and Anti-pattern

These are illustrative pseudocode, not a required API or package layout.

```text
Pattern:      Before: create project -> export
              After:  create project -> export; storage policy has one owner
Anti-pattern: After:  configure five managers -> wire them -> export
              Reason: "more extensible"
```

Compare actual caller steps and ownership. More classes or layers do not establish a benefit.

```text
Pattern:      verify two promised adapters follow the same lifecycle
Anti-pattern: approve extension parity because the diagram has matching boxes
```

Use focused behavior checks or concrete review evidence for claimed boundaries.

## References

Keep language-specific [API and SOLID rules](../../rules/overview.md), [extension contracts](../../rules/project/extension.md), and [interface boundaries](../../rules/project/interfaces.md) authoritative for their detailed mechanics.
