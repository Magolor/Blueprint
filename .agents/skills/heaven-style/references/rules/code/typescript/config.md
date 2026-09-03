---
id: ts-config
title: TypeScript configuration and control state
enabled: true
blocking: true
order: 50
category: code-quality
keywords: [TypeScript config, JSON, YAML, override, resolved spec, config path, revision, CAS, secret reference, scope, config backend]
description: Use when TypeScript code reads, resolves, edits, persists, watches, versions, scopes, authorizes, or exposes configuration through JSON, YAML, files, memory, databases, Redis, or another backend.
---

# TypeScript Configuration and Control State

## Core rule

Treat configuration as validated durable data, not ambient process state. Keep the logical model independent from JSON/YAML syntax, physical storage, and live dependency-injection or plugin runtimes.

## Apply when

- Reading JSON/YAML, environment values, CLI options, settings forms, or database rows.
- Adding defaults, overrides, scopes, secret references, revisions, watchers, or config backends.
- Choosing nested documents versus flat keys, memory versus remote storage, or raw config versus runtime specs.

## Logical model and boundaries

- Accept decoded input as `unknown`; validate it into JSON-shaped data before persistence or resolution.
- Admit only `null`, booleans, strings, finite numbers, arrays, and plain string-keyed objects. Reject `undefined`, `NaN`, infinities, `bigint`, symbols, functions, class instances, cycles, and lossy coercions.
- Detach values at ownership changes and publish readonly snapshots. TypeScript `readonly` does not freeze shared backing objects.
- Keep JSON/YAML as import, export, wire, or file formats. A backend may use a document, rows, a key/value store, or another physical representation.
- Keep secrets out of inspectable config. Persist a secret reference plus safe presence metadata; resolve the value only at the authorized runtime boundary.

```ts
type JsonValue =
  | null
  | boolean
  | number
  | string
  | readonly JsonValue[]
  | { readonly [key: string]: JsonValue }
```

Do not use `Record<string, any>` as a configuration contract. A `Map` may be an internal index, but it is neither JSON nor a public serialization model.

## Layers and resolution

- Keep raw layers separate and ordered; do not mutate a lower-precedence layer to apply an override.
- Resolve defaults, aliases, environment observations, policy, and caller overrides once at the owning boundary.
- Execution receives one complete, detached, readonly spec. Do not scatter defaulting or environment reads through runtime code.
- Preserve enough layer provenance to explain whether a value was inherited, overridden, redacted, or rejected.
- Define precedence once. Adding a layer is an architecture decision because it changes every resolved value.

## Paths and edits

- Expose nested snapshots for people and ordinary consumers; use structured paths for partial edits, audit entries, policy checks, and history.
- Represent a path as validated segments such as `readonly string[]`, not a dot-delimited string. Delimiter characters may be valid keys.
- Distinguish `set`, `unset`, missing, and `null`. Do not overload `undefined` as a durable tombstone.
- Treat arrays as atomic unless the domain gives elements stable identities. Index-based patches become ambiguous after insertion or reordering.
- Do not require all backends to persist flattened entries. The logical mutation contract and physical storage layout are separate decisions.

```ts
type ConfigOp =
  | { readonly kind: 'set'; readonly path: readonly string[]; readonly value: JsonValue }
  | { readonly kind: 'unset'; readonly path: readonly string[] }
```

## Backend and consistency contract

- Make the backend seam async even when the first implementation is in memory.
- Read immutable snapshots carrying an opaque or monotonic revision. Commit validated change sets with an optional expected revision so stale writers can fail explicitly.
- Validate before mutation, persist before publication, and notify only after commit. A failed write must not leave optimistic process state visible.
- Define conflict, retry, atomicity, refresh, cache invalidation, migration, and cross-process consistency per backend. Never imply a distributed transaction that the backend cannot provide.
- Serialize same-key writes where promises can interleave. A process-local queue does not solve cross-process concurrency.
- Carry `AbortSignal` through remote reads, commits, refresh, and teardown; close watchers and connections quiescently.
- Use one contract suite for in-memory, file, database, Redis, and future backends. Test restart and cross-process behavior where the backend promises them.

## Bootstrap and runtime composition

- Pass the first backend into the configuration owner explicitly. Do not require the configuration system to read itself before it can open.
- A backend used during bootstrap must not depend on a later service that itself consumes configuration; use a minimal adapter or postpone that integration.
- Keep durable config independent from dependency-injection containers, plugin contexts, event buses, and service instances. A composition root may consume a resolved spec to build live services.
- Ordinary config writes never import modules, execute callbacks, or activate plugins. Executable-definition lifecycle needs a separate authorized command.
- Keep scope, tenant, principal, and authorization metadata separate from value paths. Policy selects a view; it does not silently change a key's identity.

## Fitness checks

- Invalid JSON-shaped values fail before persistence.
- Override resolution is deterministic and does not mutate any input layer.
- `unset` differs from `null`, arrays follow the declared policy, and delimiter-bearing keys round-trip.
- A stale expected revision fails without publication.
- A persistence failure leaves the previous snapshot visible.
- Every backend passes the same contract suite; remote backends also prove cancellation, restart, and stated cross-process semantics.
- Importing configuration modules performs no environment read, I/O, registration, or service construction.

## Related rules

Also apply [types.md](types.md) for `unknown`, JSON types, readonly ownership, and resolved specs; [util.md](util.md) for environment, files, and writable-path ownership; [architecture.md](architecture.md) for composition and durable authority; [async.md](async.md) for cancellation and commit ordering; [modules.md](modules.md) for side-effect-free entry points; [compat.md](compat.md) for schema versions and migration windows; and [docs.md](docs.md) for precedence, redaction, revision, and lifecycle semantics.
