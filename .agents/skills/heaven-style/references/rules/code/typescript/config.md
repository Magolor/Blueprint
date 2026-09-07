---
id: ts-config
title: TypeScript configuration and control state
blocking: true
description: Define validated TypeScript configuration, layers, defaults, and persistence.
---

# TypeScript Configuration and Control State

## Core rule

Treat configuration as validated durable data, not ambient process state. Keep the logical model independent from JSON/YAML syntax, physical storage, and live dependency-injection or plugin runtimes.

## Logical model and boundaries

- Accept decoded input as `unknown`. Validate it into JSON-shaped data before persistence or resolution.
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

- Keep raw layers separate and ordered. Do not mutate a lower-precedence layer to apply an override.
- Resolve defaults, aliases, environment observations, policy, and caller overrides once at the owning boundary.
- Execution receives one complete, detached, readonly spec. Do not scatter defaulting or environment reads through runtime code.
- Preserve enough layer provenance to explain whether a value was inherited, overridden, redacted, or rejected.
- Define precedence once. Adding a layer is an architecture decision because it changes every resolved value.

## Fitness checks

- Invalid JSON-shaped values fail before persistence.
- Override resolution is deterministic and does not mutate any input layer.
- `unset` differs from `null`, arrays follow the declared policy, and delimiter-bearing keys round-trip.
- A stale expected revision fails without publication.
- A persistence failure leaves the previous snapshot visible.
- Every backend passes the same contract suite; remote backends also prove cancellation, restart, and stated cross-process semantics.
- Importing configuration modules performs no environment read, I/O, registration, or service construction.

For edits, revisions, backends, bootstrap, and runtime publication, read [configuration persistence](config/store.md).

For configurable integrations, keep preset, provider, and backend distinct: a preset is named provider configuration; the provider owns route/default policy; the backend owns concrete driver/runtime execution. For model providers, keep model, gateway, and request parameters explicit. For databases, distinguish engine family, dialect/driver, and connection arguments. Do not add these layers when direct configuration is sufficient.
