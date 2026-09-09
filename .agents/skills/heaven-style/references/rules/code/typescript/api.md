---
name: ts-api
description: Choose TypeScript public objects, functions, options, and entry points.
---

# TypeScript API Design and Vocabulary

## Summary

Keep the public mental model and class count small. Expose the shortest TypeScript API that matches the domain. Put identity, mutable state, invariants, and lifecycle on an owning object. Prefer object member methods, including static factories and pure conversions, whenever the operation has a natural domain owner. Use a typed function for an independent stateless transform without such an owner. Preserve JavaScript protocols through native mechanics and aligned aliases; domain naming consistency owns the recommended API. Use one domain verb per concept. Do not translate Python spellings mechanically.

## Principle

An API should be easy to describe in one sentence and easy to discover through imports, types, and autocomplete. New classes, helpers, flags, factories, overloads, aliases, and fluent steps must remove more caller complexity than they add.

## Public front door

- Prefer one supported import and one obvious flow for each task.
- Prefer member methods as much as the domain permits. A method or static factory on an existing domain owner takes precedence over a parallel free-function API, even when its implementation is stateless.
- Use a class when it owns identity, mutable state, invariants, replaceable behavior, registration, or resource lifetime.
- Put entity construction, parsing, normalization, projection, and formatting on the entity when they describe that entity: `Entity.fromJson(data)`, `entity.toJson()`. Purity alone is not a reason to move a domain operation to a free function. Keep genuinely independent algorithms and shared utilities as functions.
- Keep constructors synchronous and free of I/O or registration. Use `create`, `connect`, `start`, or a framework lifecycle hook when setup can fail asynchronously.
- Prefer named choices through an options object: `ws.query(expr, { limit, includeDeleted: false })`. TypeScript has no Python-style keyword arguments. Keep a natural primary operand positional; avoid positional booleans and limits whose meanings must be memorized. Use no numeric argument-count threshold.
- Prefer structural interfaces and composition. Add inheritance only for a real substitutable runtime contract.
- Public examples import through package entry points, not source files, registry internals, or helper factories.

For operation names use [vocabulary](vocab/verbs.md); for guards, defaults, and extraction use [flow](flow.md).

## OOP patterns and anti-patterns

Read [owning-object examples](api/example.md) for construction, workspace mutation, public mental-model size, and the independent-utility exception. For every public API change, describe the happy path in one short sentence: construct or load the domain object, then call its operation. A new top-level function, factory, or wrapper must justify the additional concept the caller must learn.
