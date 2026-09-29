---
name: ts-comment
description: Read before writing TypeScript implementation comments.
---

# TypeScript implementation comments

## Summary

Use line comments for implementation rationale and reserve TSDoc for public contracts.

## Comments

Use concise `//` comments for non-obvious invariants, ordering, deliberate transformations, and safety rationale. Use consecutive line comments for a short multi-line explanation.

Reserve `/** ... */` for the caller-facing contract on a public declaration. Do not use it for test/demo narration, build scripts, fixtures, private modules, or implementation notes. Prefer line comments over generic `/* ... */` when they convey the intent.

Keep public facts on the [API documentation](doc.md) owner. Comments must add meaning beyond names and types. Private helpers need comments only when their constraints are non-obvious.

Describe the current invariant, not the correction conversation. Do not mention the rejected implementation, the user's instruction, or why the code was changed unless historical compatibility is itself part of the maintained contract. Apply [correction integration](../../project/docs/edit.md).

## Pattern and Anti-pattern

- **Pattern:** `// Publish only after persistence succeeds.`
- **Anti-pattern:** `// Call persist.`

Explain the ordering constraint instead of narrating a call.
