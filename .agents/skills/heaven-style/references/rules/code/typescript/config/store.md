---
id: ts-config-store
title: TypeScript configuration persistence
description: Read for TypeScript configuration persistence.
blocking: true
---

# TypeScript configuration persistence

## Paths and edits

- Expose nested snapshots for people and ordinary consumers. Use structured paths for partial edits, audit entries, policy checks, and history.
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
- Validate before mutation. Persist before publication. Notify only after commit. A failed write must not leave optimistic process state visible.
- Define conflict, retry, atomicity, refresh, cache invalidation, migration, and cross-process consistency per backend. Never imply a distributed transaction that the backend cannot provide.
- Serialize same-key writes where promises can interleave. A process-local queue does not solve cross-process concurrency.
- Carry `AbortSignal` through remote reads, commits, refresh, and teardown; close watchers and connections quiescently.
- Use one contract suite for in-memory, file, database, Redis, and future backends. Test restart and cross-process behavior where the backend promises them.

## Bootstrap and runtime composition

- Pass the first backend into the configuration owner explicitly. Do not require the configuration system to read itself before it can open.
- A backend used during bootstrap must not depend on a later service that itself consumes configuration. Use a minimal adapter or postpone that integration.
- Keep durable config independent from dependency-injection containers, plugin contexts, event buses, and service instances. A composition root may consume a resolved spec to build live services.
- Ordinary config writes never import modules, execute callbacks, or activate plugins. Executable-definition lifecycle needs a separate authorized command.
- Keep scope, tenant, principal, and authorization metadata separate from value paths. Policy selects a view; it does not silently change a key's identity.
