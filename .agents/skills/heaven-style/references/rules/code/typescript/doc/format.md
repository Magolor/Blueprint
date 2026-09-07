---
id: ts-doc-format
title: TypeScript TSDoc semantics and tags
description: Read for TypeScript tsdoc semantics and tags.
blocking: true
---

# TypeScript TSDoc semantics and tags

## What types do not explain

Document these when relevant:

- whether absence, `undefined`, and `null` differ;
- whether input is copied, frozen, retained, or mutated;
- whether returned collections are snapshots or live views;
- whether results preserve input order;
- units and inclusive/exclusive bounds;
- configuration precedence and when defaults resolve;
- lifecycle and whether `close`/disposal reaches quiescence;
- whether a nonzero process exit is a result or an exception;
- retry/idempotency and at-most/at-least/exactly-once behavior;
- callback ordering, short-circuiting, and error containment;
- capability/fallback honesty;
- supported literal values when a generated reference is not already authoritative.

Do not narrate implementation steps that callers cannot observe.

## Tags

- Use `@param` for non-obvious parameter semantics or when the repository's API generator requires every parameter.
- Use `@returns` when the result semantics are not obvious from the type.
- Use `@throws` for synchronous or rejected errors that form part of the public contract; state the condition, not every internal exception.
- Use `@example` for a short realistic path when it reduces misuse.
- Use `@remarks`/`@internal`/`@public` only when supported by the chosen documentation tool.
- Use `@deprecated` only when the repository's stable compatibility policy requires a deprecation window. Unreleased/internal break-and-fix changes remove the old API and update call sites.

Use TSDoc tags and prose on TypeScript user-facing APIs; keep Python `Args:`, `Returns:`, and `Raises:` sections on the Python surface.
