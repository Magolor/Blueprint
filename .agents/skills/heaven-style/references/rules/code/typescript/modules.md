---
id: ts-modules
title: TypeScript modules and packages
enabled: true
blocking: true
order: 60
category: code-quality
keywords: [TypeScript files, ESM, package exports, index.ts, barrel, workspace, subpath exports, moduleResolution, dynamic import, sideEffects]
description: Use when adding or reviewing TypeScript files, package boundaries, imports, exports, workspaces, barrels, optional integrations, build output, or published artifacts.
---

# TypeScript Modules and Packages

## Core rule

Organize by feature ownership and make runtime boundaries explicit. A package entry point declares the supported surface; it does not expose the source tree, trigger hidden registration, or make optional integrations eager.

## Apply when

- Adding, moving, or renaming `.ts`/`.tsx` files, feature folders, packages, workspaces, adapters, providers, registries, or generated code.
- Changing imports, aliases, `index.ts`, `package.json` `exports`, module resolution, bundling, declaration output, or publish configuration.
- Adding an optional/heavy SDK or a multi-package dependency.

## Feature locality

- Keep one feature's implementation, types, tests, and small helpers under its owning folder or package.
- Split by reason to change, not one file per function and not generic top-level buckets.
- Multiple implementations of one contract live as siblings under the owning family, such as `storage/sqlite.ts` and `storage/postgres.ts`.
- A shared helper package exists only for demonstrated cross-feature reuse. A package named `utils` is not a dumping ground.
- Keep pure, stateless helpers as functions/modules. Add a service/class/plugin only when it owns mutable state, lifecycle, registration, or replaceable behavior. Use [TypeScript API design](api.md) for helper extraction and public vocabulary, and [utilities](util.md) before creating a shared platform-helper module.

```text
src/search/
  index.ts
  service.ts
  query.ts
  registry.ts
  providers/
    local.ts
    remote.ts
  tests/
    service.test.ts
```

Do not create all illustrated files by default. Start with the smallest owning module and split when responsibilities or review cost become distinct.

## File names

- Follow an established repository convention. When none exists, use short `kebab-case.ts` names for modules and `PascalCase.tsx` only where a component convention requires it.
- Do not repeat parent-folder context: `search/providers/openai.ts`, not `search/providers/search-openai-provider-impl.ts`.
- Re-examine names with three or more semantic parts.
- Use role names such as `registry.ts`, `schema.ts`, `config.ts`, `errors.ts`, or `types.ts` only when the file actually owns that role.
- Do not declare `types.ts` to be type-only while exporting runtime functions/classes from it. Either keep it type-only or use a name that describes the runtime concept.
- Avoid vague `common.ts`, `misc.ts`, `helpers.ts`, `manager.ts`, and catch-all `utils.ts` when a domain owner exists.

## Entry modules and barrels

- `index.ts` is a small package/feature entry point: explicit exports, minimal compatibility wiring, and no business logic.
- Prefer named exports for library surfaces and refactorability; use default exports where the framework or local convention needs them.
- Barrels are public boundary tools, not a reason to re-export every internal file at every folder level.
- Keep barrels side-effect-free. Registration happens through an explicit function or one composition root, not because importing the root happens to execute provider modules.
- Avoid barrel-induced cycles. Import a local implementation from its owning file inside the package; consumers import through the supported entry point.

**Anti-pattern:**

```ts
// src/index.ts
export * from './internal/cache.ts'
export * from './providers/openai.ts' // importing root also registers provider
```

**Recommended pattern:**

```ts
// src/index.ts
export { Client } from './client.ts'
export type { ClientConfig, ClientResult } from './types.ts'
```

Expose an optional provider as a package subpath or explicit loader instead of importing it from the root.

## ESM and runtime-correct imports

- New code is ESM-first and declares `"type": "module"` explicitly.
- Use `import type`/`export type` for type-only dependencies and enable `verbatimModuleSyntax`.
- Match `module`, resolution, and import specifiers to the actual runtime/emitter; [TypeScript environment](environment.md) owns the Bun-app, bundled-package, and unbundled-Node profiles.
- Bun-run source may use runtime-supported `.ts` specifiers. Emitted unbundled Node ESM uses runtime-valid `.js` relative specifiers. Bundled published libraries validate runtime output and declarations against their target consumers.
- Do not rely on extensionless imports or workspace-only resolution if the published runtime cannot resolve them.
- Use the `node:` protocol for Node built-ins when Node APIs are part of the target contract.

Do not apply one module profile to browser, Bun, Node, workers, config scripts, and test globals if they need distinct environments. Use small derived `tsconfig` files.

## Workspaces and dependency boundaries

- Name logical roles before creating packages. A package boundary is earned by an independent consumer, runtime/dependency isolation, compatibility/release ownership, security/process separation, or an extraction/artifact contract. Otherwise keep a feature folder in the cohesive owner.
- Use package-manager workspaces for real packages; sibling packages depend on each other through `workspace:*` or the repository's pinned equivalent.
- Cross-package imports use package names/subpaths, never `../../other-package/src/...`.
- Each workspace declares the dependencies it imports. Do not depend on accidental root hoisting or phantom dependencies.
- TypeScript `paths` may map checked workspace sources for development, but it is not a package system and must not be the only reason an import resolves.
- Use package `imports` (`#name`) for private aliases when they improve a real deep path and the runtime supports them.
- Add project references only for a real graph/build need; keep references, workspaces, and package dependencies consistent through a generated or checked graph when the repo is large enough.

## Published package surface

- Non-publishable apps and workspace roots set `"private": true`.
- Published packages expose only supported entry points through `exports` and restrict packed files with `files`.
- Put the `types` condition before runtime conditions.
- Prefer ESM-only output. Add a CommonJS branch only when a real consumer contract requires it and both outputs are built, typechecked, and tested.
- Do not export `./src/*` from a stable package unless source distribution is an intentional documented contract.
- Do not declare `"sideEffects": false` until tests prove intentional registration/style/polyfill side effects remain reachable.

```json
{
  "type": "module",
  "files": ["dist"],
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "default": "./dist/index.js"
    }
  }
}
```

Before release:

1. Build declarations and runtime artifacts from a clean checkout.
2. Inspect the packed file list (`bun pm pack --dry-run` or the repository's equivalent).
3. Install the archive into a temporary strict consumer.
4. Import every public entry/subpath and exercise one runtime smoke path.
5. Run a package manifest validator such as `publint` when the repository publishes npm packages.

Source-plane tests and workspace aliases cannot prove the artifact plane is usable. Keep both signals when the repository publishes packages.

## Optional integrations

- Lazy loading controls evaluation, not installation ownership. Model the SDK deliberately as an optional peer (`peerDependencies` plus optional `peerDependenciesMeta`), an `optionalDependency`, or a separate integration package according to who installs/owns it; do not leave a dynamically imported package undeclared.
- Keep optional/heavy SDK imports inside the selected adapter's `create`/`connect` path:

```ts
export async function createVectorBackend(config: VectorConfig): Promise<VectorBackend> {
  let sdk: typeof import('@vendor/vector-sdk')
  try {
    sdk = await import('@vendor/vector-sdk')
  } catch (cause: unknown) {
    if (isMissingPackage(cause, '@vendor/vector-sdk')) {
      throw new MissingIntegrationError('vector', { cause })
    }
    throw new IntegrationLoadError('vector integration failed to load', { cause })
  }
  return new VendorVectorBackend(sdk, config)
}
```

`isMissingPackage` must narrowly prove that the requested top-level package—not one of its transitive imports—is missing. Otherwise preserve the actual evaluation/load failure; do not relabel syntax, initialization, or transitive dependency errors as “please install the integration.” Omitting the catch is preferable when the repository has no trustworthy classifier.

- Do not catch provider connection errors and later return empty success. Either fail creation or preserve a sanitized inspectable health error and make every operation fail contextually.
- Test that importing the package root does not load optional provider modules.
- For published packages, test packed consumers both without the optional SDK (base import works and selected integration fails actionably) and with it (the integration smoke path works).
- Expose optional packages/subpaths explicitly so bundlers and users can keep them out of the base graph.

## Generated and vendored code

- Keep generated output under a clearly owned path and regenerate it through one command; never hand-edit it.
- Provide a check mode that fails when committed generated output is stale.
- Keep generated output out of lint/typecheck only when the generator is the source of truth and the built consumer still validates it.
- Vendored code preserves upstream style and lives behind a manifest/sync procedure. Local modifications are logged and rechecked during upgrades.
- Do not copy a vendor's internal module layout into first-party code merely for symmetry.

## Cycles and architecture gates

- Cross-layer/package runtime cycles and cycles whose behavior depends on initialization order are blocking findings.
- A local runtime cycle is acceptable only when its owner documents why it is intrinsic, the runtime path is deterministic, and a focused fitness test proves initialization/import behavior. Otherwise break it; do not normalize cycles with broad lint exemptions.
- Type-only cycles still deserve review because they often reveal misplaced ownership, but they are not automatically defects.
- Multi-package repositories should check dependency constraints, unused exports/dependencies, and package manifests with a project-local gate.
- Owned config and script files must not fall outside every typecheck/lint graph. Give them a dedicated checked project or an explicit justified exception.

## Review checks

- Can one feature be understood and changed mostly inside one folder/package?
- Does an entry module expose only the intended surface without side effects?
- Are runtime import specifiers valid outside the source workspace?
- Can any package import a sibling's source tree or an undeclared dependency?
- Are optional SDKs absent from the root import graph?
- Does `types.ts` match its claimed role?
- Is published output constrained, packed, and tested as a consumer?
- Are generated/vendor files owned by an explicit workflow?
- Are scripts/configs covered by static gates?
- Did each package earn an independent boundary, or did the folder diagram create package-per-noun overhead?
- If the family is internal-only, is its implementation list confined to one composition root? If the family promises independent extensions, do bundled and external items use the same declared discovery/registration path, with catalog/lifecycle machinery only where that promise requires it?

## Related rules

Also apply [architecture.md](architecture.md) for dependency direction and composition roots, [api.md](api.md) for public entry vocabulary, [util.md](util.md) for platform/resource boundaries, [types.md](types.md) for import/type contracts, [async.md](async.md) for lazy integration errors and lifecycle, [docs.md](docs.md) for exported surfaces, [compat.md](compat.md) for renamed subpaths/module formats, and [environment.md](environment.md) for module profiles, package manager, and publish gates.
