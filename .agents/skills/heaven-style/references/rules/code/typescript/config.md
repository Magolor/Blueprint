---
name: ts-config
description: Define validated TypeScript configuration, layers, defaults, and persistence.
---

# TypeScript Configuration and Control State

## Summary

Configuration is a key/value dictionary of validated data. Keep changeable defaults in the owning config service or external resources whenever practical; do not freeze environment values or tunables into module constants or function defaults. Keep the logical model independent from JSON/YAML syntax, physical storage, and live dependency-injection or plugin runtimes.

## Logical model and boundaries

- Use a string-keyed dictionary as the logical root; typed specs are resolved execution views, not replacements for KV configuration. A small package may use an existing config helper plus a defaults resource; it need not add a service framework or persistence backend.
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

## Defaults and omission

Keep protocol markers, mathematical identities, and fixed sentinels in code. Provider/model choices, timeouts, lengths, temperatures, paths, retries, and similar tunables belong to config/default resources. Import environment overrides at the declared configuration boundary; avoid module-level `const` snapshots of environment variables.

Illustrative entry boundary: `cfg` is the package-owned typed KV service, already initialized from external defaults; `_embed` consumes validated values.

```ts
interface EmbedOptions {
  readonly model?: string
  readonly maxLen?: number
  readonly temperature?: number
}

function embed(text: string, options: EmbedOptions = {}): Promise<readonly number[]> {
  const model = options.model === undefined
    ? cfg.get('embed.model', 'text-embedding-3-small') : options.model
  const maxLen = options.maxLen === undefined
    ? cfg.get('embed.maxLen', 2048) : options.maxLen
  const temperature = options.temperature === undefined
    ? cfg.get('embed.temperature', 0.0) : options.temperature
  return _embed(text, { model, maxLen, temperature })
}
```

Lookup fallbacks are acceptable because configuration can override them; prefer externalizing changeable fallback values as well. Validate explicit overrides and resolved constraints before execution. Do not replace this pattern with hard-coded parameter defaults or a required caller-created config class.

Use `undefined` for omission and `null` for an intentional empty value when the API allows it. For a nullable override, use `value === undefined ? cfg.get(key) : value`; `??` would also replace `null`. Preserve `0`, `false`, and `''`. API omission is not persisted data: durable config rejects `undefined`, and removal uses `unset`. Under `exactOptionalPropertyTypes`, `field?: T` allows omission; add `| undefined` only if explicit undefined is part of the caller contract.

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

## Static package resources

Most substantial static/changeable content belongs in resources: default/bootstrap configuration, built-in instance definitions, prompt templates, and seed data. In a modular package system, keep these with the owning package under `resources/` or its established `assets/` folder; no global resource bucket or forced rename is required. Bundle and verify them with the installed/packed package. Keep runtime writable state separate.

This is an ownership preference, not an unconditional ban on every literal, schema declaration, or tiny fixed format marker in code. Preserve language-specific import/resource loading controls. Config data stays KV; typed validation and resolved execution specs can remain code-owned.
