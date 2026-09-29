---
name: ts-compat
description: Change TypeScript exports, runtime support, schemas, or compatibility promises.
---

# TypeScript Compatibility and Migrations

## Summary

Keep one live API for unreleased or fully owned code. Preserve logical features while replacing obsolete interfaces and updating every owned caller in the same change. Published packages, persisted data, wire protocols, and independently deployed consumers follow the repository's declared compatibility and release policy.

## One live version

Enforce one current owned API, configuration schema, and internal representation. Update owned callers together and delete obsolete paths; do not proactively preserve an old version. Supported canonical aliases belong to this same current API and share its implementation. They are not permission for parallel v1/v2 implementations.

Published support or an explicit user requirement can justify a bounded compatibility adapter at the external boundary, with a named consumer and removal condition. It does not create a second internal version or permit silent loss of persisted data.

## Principle

Intentional protocol/ergonomic aliases such as the [JSON conversion pair](vocab/verbs.md) share one supported implementation and are not migration shims. The following temporary-layer rules apply to obsolete APIs.

A compatibility layer is a temporary product contract, not courtesy boilerplate. It needs a named consumer, scope, removal condition, deadline or release boundary, tests through the old entry, and documentation that points to the canonical replacement.

## Compatibility surfaces

Review each surface separately. One successful typecheck does not prove the others:

- **Source/types:** imports, signatures, overloads, generic inference, and declarations.
- **Runtime/package:** built files, ESM/CJS behavior, package `exports`, side effects, and supported runtimes.
- **Wire/config:** serialized field names, optionality, defaults, error codes, and protocol behavior.
- **Persistence:** schema/data versions, migration order, restart/rollback posture, and old-reader/new-writer interaction.
- **Behavior:** timing, ordering, retries, errors, and lifecycle that consumers may rely on even when types are unchanged.

## Do

- For owned/unreleased changes, rename the canonical symbol and update imports, call sites, tests, examples, generated declarations, package exports, and docs together.
- Remove obsolete aliases, wrappers, and fallback paths in that scope. An old name alone does not justify a shim. Verify the retained capability through the current entry; drop tests that only preserve a retired interface while retaining behavioral regressions.
- For published compatibility, use semantic versioning and the target repository's support window. Keep the adapter at the public boundary; internal code uses only the canonical API.
- Mark a retained export with `@deprecated` only when a real consumer needs a migration window. Name the replacement and removal release/condition.
- Test source/type compatibility and runtime/package compatibility independently. Pack and install a clean consumer when package entry points change.
- Version wire, config, and persisted schemas when old and new deployments may overlap. Validate both versions at the boundary and normalize immediately to one internal representation.
- Make one-shot data migrations explicit, ordered, observable, and safe to retry or resume. Remove the compatibility reader after the supported migration window and evidence permit it.
- Record runtime-floor changes, module-format changes, and removed subpaths as public compatibility decisions rather than incidental toolchain cleanup.
- Keep current guides about the supported interface and useful decision history in its history owner. “Current” follows the accepted design and support policy, not an automatic dependency upgrade or deletion of stored data.

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

Delete `getProfile`. Update every owned caller. Keep no alias.

For a published package with a verified migration window:

```ts
/**
 * @deprecated Use `loadProfile`. Removed after the declared compatibility window.
 */
export function getProfile(id: ProfileId): Promise<Profile> {
  return loadProfile(id)
}
```

The package must name the consumer/window outside this comment. It must test the alias through packed output. New internal code must use only `loadProfile`.
