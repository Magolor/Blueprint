---
id: ts-api
title: TypeScript API design and vocabulary
enabled: true
blocking: true
order: 30
category: code-quality
keywords: [TypeScript public API, method names, class versus function, API vocabulary, get fetch load query search, helper cleanliness, guard clause, nullish coalescing]
description: Use when designing TypeScript public classes/functions, naming methods, choosing class versus function, shaping fluent or collection APIs, or reviewing code readability and helper cost.
---

# TypeScript API Design and Vocabulary

## Core rule

Expose the shortest domain-shaped TypeScript surface. Put identity, mutable state, invariants, and lifecycle on an owning object; use a typed function for a stateless transform. Follow JavaScript and TypeScript platform vocabulary where it is already strong, and use one domain verb per concept rather than translating Python spellings mechanically.

An API should be easy to describe in one sentence and easy to discover through imports, types, and autocomplete. New classes, helpers, flags, factories, overloads, aliases, and fluent steps must remove more caller complexity than they add.

## Apply when

- Code adds or changes exported functions, classes, methods, constructors, builders, stores, clients, registries, collections, specs, configs, plans, or engines.
- A design chooses class versus function, constructor versus async factory, overload versus options object, or platform protocol versus custom accessor.
- Code introduces alternate verbs such as `get`, `fetch`, `load`, `find`, `query`, `search`, `retrieve`, `save`, or `register`.
- Local code becomes nested, fallback-heavy, wrapper-heavy, or difficult to read.

## Public front door

- Prefer one supported import and one obvious flow for each task.
- Use a class when it owns identity, mutable state, invariants, replaceable behavior, registration, or resource lifetime.
- Use a function for parsing, normalization, compilation, projection, formatting, and other stateless transforms.
- Keep constructors synchronous and free of I/O or registration. Use `create`, `connect`, `start`, or a framework lifecycle hook when setup can fail asynchronously.
- Use an options object when several parameters are optional, share a lifecycle, or are likely to evolve. Keep a short positional signature when order and meaning are unambiguous.
- Prefer structural interfaces and composition. Add inheritance only for a real substitutable runtime contract.
- Public examples import through package entry points, not source files, registry internals, or helper factories.

## Canonical vocabulary

Use domain meaning first, with these defaults when the repository has no stronger established term:

| Concept | Preferred TypeScript vocabulary |
| --- | --- |
| Parse external text into a validated value | `parse*` |
| Encode/decode a wire or binary representation | `encode*` / `decode*` |
| Format a value for people or a textual protocol | `format*` |
| Deliberate `JSON.stringify` projection hook | `toJSON` |
| Build from validated JSON-shaped data | `fromJSON` or a schema's `parse` |
| Exact optional lookup | `get` |
| Exact lookup that fails when absent | `getOrThrow` or a domain-specific `require*` |
| Predicate/local optional lookup | `find` |
| Remote or network retrieval | `fetch` |
| Reopen persisted/configured state | `load` |
| Structured selection | `query` |
| Fuzzy/ranked discovery | `search` |
| Domain retrieval, including RAG | `retrieve` |
| Make discoverable through an open family/workspace | `register` |
| Create only / merge by key | `insert` / `upsert` |
| Change an existing durable value | `update` |
| Remove a domain member / clear all members | `remove` / `clear` |
| Map/set/key-value removal | `delete` |
| Resource lifecycle | `connect`, `start`, `stop`, `close`, `dispose` |

Do not add synonyms such as `getUser`, `fetchUser`, and `loadUser` unless they have observably different contracts. Document absence, network failure, cache behavior, and ownership where the type alone cannot distinguish them.

`toJSON` has JavaScript runtime meaning: `JSON.stringify` calls it. Use it only when that implicit projection is intentional and returns JSON-shaped data. Prefer an explicit domain name such as `toRecord`, `toView`, or `encodeMessage` when implicit serialization would hide policy.

For collection-like objects, prefer JavaScript protocols and platform expectations before custom accessors: `Iterable`, `AsyncIterable`, `Symbol.iterator`, `length`/`size`, `get`, `set`, `delete`, and readonly arrays/maps where appropriate. Do not imitate Python dunder names.

## Specs, configs, plans, and lifecycles

- `*Request`: raw caller intent that may omit defaults.
- `*Spec`: validated/resolved declarative execution contract.
- `*Config`: runtime settings and defaults.
- `*Plan`: ordered execution decision.
- `*Client`: protocol/provider client without domain policy.
- `*Service`: application behavior with a clear boundary; not a generic dependency bucket.
- `*Engine`: stateful executor only when the domain already uses that term.
- `*Registry`: authoritative registration/resolution behavior for an open family.
- `id`/`*Id`: stable object identity; use branded types when confusing IDs would be dangerous.
- `kind` or `type`: discriminant chosen consistently with the wire/domain vocabulary.
- `metadata`: genuinely opaque extension data, never a hiding place for required fields.

Avoid vague `Manager`, `Helper`, `Utils`, `Data`, `Impl`, and `Base` suffixes unless they express a real role that cannot be named by the domain.

## Language shape and helper cleanliness

- Prefer guard clauses and direct returns over deep nesting.
- Use `??` for missing-value defaults; do not use `||` when `0`, `false`, or `''` are valid caller values.
- Use optional chaining when absence is expected and stopping the access chain is the intended behavior.
- Use `map`, `filter`, `flatMap`, `some`, `every`, and `find` for one clear collection operation. Prefer a readable `for...of` loop when a long chain, `reduce`, mutation, early exit, async sequencing, or multiple branches would obscure intent.
- Keep a specialized one-liner local. Extract a helper when its name and type contract clarify a meaningful transform, policy, validation, observability, or repeated use.
- Do not create wrapper classes/functions merely to rename a constructor, object spread, property access, or direct platform call.

**Anti-pattern:**

```ts
function getTimeout(options: RunOptions): number {
  return options.timeoutMs || 30_000
}
```

**Recommended pattern:**

```ts
const timeoutMs = options.timeoutMs ?? defaults.timeoutMs
```

If timeout resolution becomes a validated policy shared by several entry points, promote that complete policy to the configuration owner rather than preserving the one-line wrapper.

## Review checks

- Can a caller explain the happy path in one sentence?
- Does each class own real state, invariants, lifecycle, or replaceable behavior?
- Is a stateless transform needlessly hidden behind an object or factory?
- Do method names distinguish exact lookup, remote fetch, persisted load, query, and search?
- Does `toJSON` intentionally participate in implicit JSON serialization?
- Are defaults nullish-aware and control flow readable?
- Does every helper repay its navigation and abstraction cost?

## Related rules

Also apply [architecture.md](architecture.md) for ownership and SOLID boundaries, [types.md](types.md) for names and public contracts, [util.md](util.md) for platform/helper ownership, [modules.md](modules.md) for entry points and locality, [async.md](async.md) for async factories and lifecycle, [docs.md](docs.md) for public semantics, and [compat.md](compat.md) for aliases or renamed APIs.
