---
name: template-pr
description: Read before drafting or substantially revising a pull request body.
---

# PR body

## Summary

Summarize the affected feature, reason for change, and observable outcome.
Explain the system responsibility before naming internal symbols. Keep the
summary about this PR, even when it belongs to a larger effort.

## Changes

Explain the trigger, cause, and before/after behavior to the depth needed for
review. For new functionality, show what becomes possible. Link the canonical
user guide, design, or investigation for extensive usage and implementation detail.

## Evidence

State checks actually run, results, and material gaps. Read and include the
applicable evidence below; omit unrelated subsections:

- GUI-related PR: [screenshots](pr/gui.md).
- Efficiency-related change or claim: [benchmark comparison](pr/bench.md).
- Dependent or stacked PR: [stack context](pr/stack.md), placed after Changes.

Include risks, compatibility, or rollout details only when consequential; link
their canonical owner. Unavailable evidence remains an explicit gap, not a pass.

## References

Link relevant issues, tasks, and canonical docs. Use closing keywords only for
issues this PR resolves. Keep essential context in the body, not only behind links.
