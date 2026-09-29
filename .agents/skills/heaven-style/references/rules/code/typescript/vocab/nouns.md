---
name: typescript-vocab-nouns
description: Read when naming TypeScript providers, identities, configuration, schemas, or CLI options.
---

# Domain nouns

## Summary

Use one explicit noun per concept across SDKs, configuration, registries, and CLI commands. Prefer a domain name over generic kind/type/data labels. Keep names short and explain new terms in the owning vocabulary.

| Concept | Canonical convention |
| --- | --- |
| PostgreSQL provider identity | `postgres`; normalize accepted `postgresql`/`pg` aliases at the input boundary when supported. Keep the official product name PostgreSQL in prose and actual dependency/import/URL identifiers unchanged. |
| Configuration | `config` as the concept; `cfg` for a short binding or documented alias. Config is KV data/service, not mandatory caller construction of a settings class. |
| Path join | `pj` for the package-owned utility. |
| Provider selector | `provider`, or a specific qualifier such as `storageProvider`; CLI `--provider` or `--storage-provider`, not an unexplained `--kind`. |
| Data format | `format`, e.g. json/csv; do not call an output format a provider. |
| Entity/type identity | Explicit `entityType`/`typeId` in TypeScript, `entity_type`/`type_id` in Python when distinguishing a type/class from an instance. Preserve a declared identifier field when its context is already precise. |
| Object identity | `id` in an unambiguous owning object; `objectId`/`productId` or Python `object_id`/`product_id` where several identities could be confused. |
| Request | Raw caller intent that can omit defaults. |
| Spec | Declarative contract; distinguish unresolved input from a validated/resolved execution spec when both exist. |
| Plan | Ordered execution decision. |
| Metadata | Opaque extension data; never hide required domain fields here. |

A discriminator should name what it discriminates: `provider`, `format`, `operation`, `entityType`. Generic `kind` is discouraged when a more explicit concept exists. Preserve actual external protocol field names and narrow local closed unions when generic terminology is already exact; do not mechanically rename third-party contracts.

Do not resurrect KL/UKF lineage vocabulary in unrelated packages. `CM_*` may remain an established Python config singleton convention; it is not the universal name for a future TypeScript config system. Keep one package vocabulary, using native casing rather than different concepts between languages.

**Pattern:** CLI `--provider postgres` resolves the same canonical provider as the SDK/config value; accepted aliases normalize before resolution and serialization.

**Anti-pattern:** CLI calls it pg, config stores postgresql, and the registry expects postgres without one alias owner; or `--kind` ambiguously selects a provider in one command and a format in another.

## Specs, configs, plans, and lifecycles

- `*Request`: raw caller intent that may omit defaults.
- `*Spec`: validated/resolved declarative execution contract.
- `*Config`: runtime settings and defaults.
- `*Plan`: ordered execution decision.
- `*Client`: protocol/provider client without domain policy.
- `*Service`: application behavior with a clear boundary; not a generic dependency bucket.
- `*Engine`: stateful executor only when the domain already uses that term.
- `*Registry`: authoritative registration/resolution behavior for an open family.
- Use the table above for explicit identity, provider, and schema names.
- Prefer a specific domain discriminator such as `provider`, `format`, or `entityType`; avoid generic `kind` when the concept has a name.
- `metadata`: genuinely opaque extension data, never a hiding place for required fields.

Avoid vague `Manager`, `Helper`, `Utils`, `Data`, `Impl`, and `Base` suffixes unless they express a real role that cannot be named by the domain.

