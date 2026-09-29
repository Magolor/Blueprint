---
name: ts-verbs
description: Read before naming TypeScript API operations.
---

# TypeScript API vocabulary

## Summary

Use one operation name per meaning while preserving JavaScript protocols and observable contracts.

## Paired operation families

Choose the whole family by its data/lifecycle model, not one fashionable verb in isolation. Member methods belong to the natural domain owner. Canonical names and supported aliases share one implementation and observable contract; see [aliases](aliases.md). CLI commands use the same concepts as SDK methods.

| Model | Canonical family | Contract |
| --- | --- | --- |
| KV configuration/cache | `get`, `set`, `unset`, `setdef`, `clear` | Lookup by key; assign; remove key; assign only if absent; remove all contents. Preserve falsy values and meaningful null/None. `setdef` returns the existing or newly assigned value. |
| Rich rows/entities | `upsert`, `insert`, `remove`, `get` | Merge/create by identity; create only; remove member; exact identity lookup. `update` explicitly changes an existing member. |
| Rich selection | `retrieve`, `query`, `search` | Retrieval or structured selection can expose filters, projections, ranking, or other control beyond exact `get`. Use `search` for fuzzy/ranked discovery. Do not invent fetch/get/load synonyms for the same operation. |
| Resource access | `open`, `close`, `dispose`; `connect` when appropriate | Open/close access; connect a remote/session resource; dispose owned runtime resources. Document whether close allows reopening and whether disposal is final. |
| Resource existence | `create`, `destroy`, `drop` | Create an owned resource; destroy its lifecycle/existence; drop destructive schema/storage objects. Keep these distinct from closing a handle or removing one row. |
| Persistence | `load`, `dump` or `save`, `flush` | Read persisted state; write a file/artifact snapshot; flush buffered changes. These names promise persistence, usually filesystem I/O. They are not generic in-memory conversion verbs. |
| Setup | `setup`, `init`, `reset` | Setup is usually global/one-time; init prepares a project or routinely initialized scope. Expose reset when meaningful, commonly as an explicit setup option. Constructors still avoid hidden activation/I/O. |
| Representation | `encode`, `decode`; paired `from*`, `to*` | Encode/decode representations; construct/export a domain value with explicit format or source. Keep text, bytes, JSON-shaped data, and display distinct. |
| Discovery/collection | `list`, `register`, `add`, `rename`, `clear` | List members; make discoverable; add to an in-memory collection; rename identity/label under its documented contract; clear contents. |

### Single and multiple values

Prefer one versatile operation: `upsert(product)` and `upsert([product])`. Keep input cardinality, return shape, ordering, error behavior, and transaction semantics explicit. A single input can return one result and a collection can return a collection when overloads/types express that distinction. Do not silently conflate partial success with atomic success.

Do not introduce `batch_*`/`batch*` merely to accept a collection. A separate bulk operation is justified only by a materially different contract that the ordinary operation cannot express clearly, such as a streaming job or different transaction/result semantics. Internal batching for performance alone need not add a public verb.

### Persistence versus value conversion

`load` may reopen an object from a persisted registry, config store, or artifact; it does not mean arbitrary lookup from an in-memory map. Use `get` for that lookup. Paired format utilities may use their established language vocabulary (Python `loads_*`/`dumps_*` for text/bytes); document that format suffix and do not confuse those with unsuffixed persistence methods. `save`/`dump` are paired with `load`, and `flush` commits buffers. Immediate KV/entity writes use `set`/`upsert`, not a redundant save step.

## Canonical vocabulary

Use domain meaning first, with these defaults when the repository has no stronger established term:

| Concept | Preferred TypeScript vocabulary |
| --- | --- |
| Parse external text into a validated value | `parse*` |
| Encode/decode a wire or binary representation | `encode*` / `decode*` |
| Format a value for people or a textual protocol | `format*` |
| Export JSON-shaped data | `toJson`; `toJSON` is the JavaScript hook alias |
| Build from JSON-shaped data with validation | `fromJson`; `fromJSON` may alias it |
| Exact optional lookup | `get` |
| Exact lookup that fails when absent | `getOrThrow` or a domain-specific `require*` |
| Predicate/local optional lookup | `find` |
| Remote or network retrieval | `retrieve`; retain native `fetch` for the platform HTTP API |
| Reopen persisted/configured state | `load`; in-memory lookup uses `get` |
| Structured selection | `query` |
| Fuzzy/ranked discovery | `search` |
| Domain retrieval, including RAG | `retrieve` |
| Make discoverable through an open family/workspace | `register` |
| Create only / merge by key | `insert` / `upsert` |
| Change an existing durable value | `update` |
| Remove a domain member / clear all members | `remove` / `clear` |
| Owned KV removal / native Map or Set removal | `unset` / native `delete` |
| Resource lifecycle | `connect`, `start`, `stop`, `close`, `dispose` |

Do not add synonyms such as `getUser`, `fetchUser`, and `loadUser` unless they have observably different contracts. Document absence, network failure, cache behavior, and ownership where the type alone cannot distinguish them.

Use aligned `from*` / `to*` families: `fromJson` / `toJson`, `fromDict` / `toDict`, and `fromSchema` for schema construction. Treat acronyms as words; naming consistency takes precedence over uppercase acronym spelling. Official docs and owned callers recommend `fromJson` / `toJson`.

`toJSON` is the JavaScript hook called by `JSON.stringify`; `fromJSON` is an ecosystem spelling, not a JavaScript runtime hook. When exposing the uppercase spellings, make each pair share one implementation with identical validation, values, errors, and ownership. The implementation may live under either spelling. These intentional protocol/ergonomic aliases are supported API, not temporary migration shims. Do not deprecate them or give them a removal deadline merely because the preferred spelling differs.

Illustrative class members (the row schema and data owner are package-defined):

```ts
static fromJson(data: unknown): Row {
  return new Row(RowSchema.parse(data))
}

static fromJSON(data: unknown): Row {
  return this.fromJson(data)
}

toJson(): RowData {
  return { ...this.data }
}

toJSON(): RowData {
  return this.toJson()
}
```

`fromJson` / `fromJSON` agree with each other, as do `toJson` / `toJSON`; construction and export remain opposite operations. The hook must not change projection based on the key argument supplied by `JSON.stringify`. Enable implicit serialization only when intentional; use `toDict`, `toView`, or `encodeMessage` for a different projection contract. JSON text parsing/stringifying remains distinct from JSON-shaped data conversion.

For collection-like objects, prefer JavaScript protocols and platform expectations before custom accessors. Use `Iterable`, `AsyncIterable`, `Symbol.iterator`, `length`/`size`, and readonly arrays/maps where appropriate. Native Map/Set retain `delete`; an owned KV service uses the canonical get/set/unset/setdef family and may expose a documented delete alias. Do not imitate Python dunder names.

## Value operations

Use `fromSchema` when input defines a type/schema rather than one instance. Use an explicit `clone` or domain-named copy operation for a detached value with updates. Prefer `toString` for intentional JavaScript string conversion and `toView` for a UI/API projection; document ownership and loss of information.

Reserve `save(path)` for an owned file/artifact when that is the domain term. Registry or immediately durable row/config writes use their actual registration or mutation verb. Distinguish `clear` (contents) from `drop` (destructive schema/storage removal). Prefer `upsert(value)` and `upsert(values)` on the same owner; add a separate batch verb only for the materially different contract described above.

## Representation pairs

| Representation | Canonical pair | Distinction |
| --- | --- | --- |
| Mapping/object fields | `fromDict` / `toDict` | Aligned with Python from_dict/to_dict; existing fromRecord/toRecord may be explicit equivalent aliases. A dictionary can contain values that are not JSON-compatible. |
| JSON-shaped data | `fromJson` / `toJson` | Validate JSON-compatible representation; equivalent fromJSON/toJSON aliases preserve the accepted JavaScript interface. |
| Textual representation | `fromString` / `toString` when a reversible format is defined | toString alone may be display-only; never imply it is lossless without a contract. Do not add toStr merely for acronym symmetry. |
| Wire or binary data | `encode` / `decode`, with a format suffix when needed | Define encoding, byte/text shape, validation, and loss explicitly. |
| Schema | `fromSchema` / `toSchema` when supported | Constructs/exports a type or schema, not one instance. |
| File | `load` / `dump` or `save`; `fromFile`/`fromPath` for explicit construction sources | These perform persistence I/O; get remains lookup. |

Use the repository's existing schema/parser internally without exposing a second competing public factory. Native JSON.parse/stringify remain native utilities; the entity owns its fromJson/toJson contract.

Prefer explicit setup reset policy: `setup(reset=True)` in Python or `setup({ reset: true })` in TypeScript. Reset remains a member operation when the object has a useful independent reset lifecycle; the option does not justify hidden constructor setup.
