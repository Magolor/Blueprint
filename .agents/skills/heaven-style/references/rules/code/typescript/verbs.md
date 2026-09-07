---
id: ts-verbs
title: TypeScript API vocabulary
description: Read for TypeScript api vocabulary.
blocking: true
---

# TypeScript API vocabulary

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

For collection-like objects, prefer JavaScript protocols and platform expectations before custom accessors. Use `Iterable`, `AsyncIterable`, `Symbol.iterator`, `length`/`size`, `get`, `set`, `delete`, and readonly arrays/maps where appropriate. Do not imitate Python dunder names.

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

## Value and batch operations

Use `fromSchema` when input defines a type/schema rather than one instance. Use an explicit `clone` or domain-named copy operation for a detached value with updates. Prefer `toString` for intentional JavaScript string conversion and `toView` for a UI/API projection; document ownership and loss of information.

Reserve `save(path)` for an owned file/artifact when that is the domain term. Registry or immediately durable row/config writes use their actual registration or mutation verb. Distinguish `clear` (contents) from `drop` (destructive schema/storage removal). Use `batchUpsert`, `batchGet`, or an established domain equivalent only when batching changes I/O, transactions, routing, or performance beyond a plain loop.
