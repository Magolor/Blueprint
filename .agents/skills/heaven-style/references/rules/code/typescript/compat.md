---
id: ts-compat
title: TypeScript compatibility and migrations
enabled: true
blocking: true
order: 100
category: code-quality
keywords: [TypeScript compatibility, semver, deprecation, package export rename, migration, alias, v1 v2, schema version, declaration compatibility]
description: Use when TypeScript code renames exports or package subpaths, changes config/wire/persistence schemas, adds deprecations or aliases, or changes supported runtimes and consumers.
---

# TypeScript Compatibility and Migrations

## Core rule

Keep one live API for unreleased or fully owned code and update every owned call site in the same change. Published packages, persisted data, wire protocols, and independently deployed consumers follow the repository's declared compatibility and release policy.

A compatibility layer is a temporary product contract, not courtesy boilerplate. It needs a named consumer, scope, removal condition, deadline or release boundary, tests through the old entry, and documentation that points to the canonical replacement.

## Apply when

- Renaming an export, function, method, package subpath, option, event, config key, or wire field.
- Changing ESM/CJS output, runtime support, declaration shape, package `exports`, persistence schemas, or protocol versions.
- Adding `@deprecated`, aliases, adapters, `v1`/`v2` modules, dual readers/writers, or migration scripts.

## Compatibility surfaces

Review each surface separately; one green typecheck does not prove the others:

- **Source/types:** imports, signatures, overloads, generic inference, and declarations.
- **Runtime/package:** built files, ESM/CJS behavior, package `exports`, side effects, and supported runtimes.
- **Wire/config:** serialized field names, optionality, defaults, error codes, and protocol behavior.
- **Persistence:** schema/data versions, migration order, restart/rollback posture, and old-reader/new-writer interaction.
- **Behavior:** timing, ordering, retries, errors, and lifecycle that consumers may rely on even when types are unchanged.

## Do

- For owned/unreleased changes, rename the canonical symbol and update imports, call sites, tests, examples, generated declarations, package exports, and docs together.
- For published compatibility, use semantic versioning and the target repository's support window. Keep the adapter at the public boundary; internal code uses only the canonical API.
- Mark a retained export with `@deprecated` only when a real consumer needs a migration window. Name the replacement and removal release/condition.
- Test source/type compatibility and runtime/package compatibility independently. Pack and install a clean consumer when package entry points change.
- Version wire, config, and persisted schemas when old and new deployments may overlap. Validate both versions at the boundary and normalize immediately to one internal representation.
- Make one-shot data migrations explicit, ordered, observable, and safe to retry or resume. Remove the compatibility reader after the supported migration window and evidence permit it.
- Record runtime-floor changes, module-format changes, and removed subpaths as public compatibility decisions rather than incidental toolchain cleanup.

## Avoid

- Permanent re-export aliases, wrapper functions, or parallel `v1`/`v2` trees without an active support contract.
- Letting internal code continue to call the deprecated entry.
- Silent dual-read or dual-write behavior with no version, telemetry, owner, or removal condition.
- Assuming structural assignability means runtime, wire, or behavioral compatibility.
- Keeping CommonJS, an older runtime, or a second package shape without a named consumer and test matrix.
- A deprecation warning or log on every hot-path call when documentation/type tooling provides the intended migration channel.
- One broad compatibility flag that changes unrelated API, storage, and protocol behavior.

## Example

For an unreleased package, prefer a clean break-and-fix change:

```ts
export function loadProfile(id: ProfileId): Promise<Profile> {
  // ...
}
```

Delete `getProfile`, update every owned caller, and keep no alias.

For a published package with a verified migration window:

```ts
/**
 * @deprecated Use `loadProfile`. Removed after the declared compatibility window.
 */
export function getProfile(id: ProfileId): Promise<Profile> {
  return loadProfile(id)
}
```

The package must name the consumer/window outside this comment, test the alias through packed output, and keep new internal code on `loadProfile` only.

## Review checks

- Which exact consumers and compatibility surfaces require preservation?
- Is the canonical API used everywhere inside the repository?
- Does every shim have an owner, removal condition, and focused test?
- Are package declarations, runtime files, exports, and clean-consumer behavior all verified?
- Do wire/config/data versions normalize to one current internal model?
- Can the migration resume after partial failure without corrupting newer state?

## Related rules

Also apply [api.md](api.md) for the canonical replacement, [modules.md](modules.md) for package exports and packed consumers, [types.md](types.md) for source/declaration contracts, [config.md](config.md) for config versions, [sql.md](sql.md) for data migrations, [docs.md](docs.md) for deprecation semantics, and [environment.md](environment.md) for supported runtime changes.
