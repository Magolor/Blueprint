---
name: py-comment
description: Read before writing Python implementation comments.
---

# Python implementation comments

## Summary

Explain non-obvious implementation constraints with comments. Keep caller contracts in public docstrings.

## Comments

Use `#` for non-obvious implementation constraints, ordering, transformations, and rationale. Explain why the code needs the constraint; do not narrate obvious statements or duplicate public contract facts.

Keep caller-visible behavior on the [public docstring](doc.md). A private helper may have a short docstring when its name and annotations do not explain a meaningful boundary. Do not add full public-section boilerplate to tiny private helpers. Follow repository tooling and local comment conventions.

Describe the current invariant, not the correction conversation. Do not mention the rejected implementation, the user's instruction, or why the code was changed unless historical compatibility is itself part of the maintained contract. Apply [correction integration](../../project/docs/edit.md).

## Pattern and Anti-pattern

- **Pattern:** `# Publish only after persistence succeeds.`
- **Anti-pattern:** `# Call persist.`

Explain the ordering constraint instead of narrating a call.
