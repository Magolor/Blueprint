---
name: ts-modules
description: Organize TypeScript files, ESM entries, workspaces, and published packages.
---

# TypeScript Modules and Packages

## Summary

Organize by feature ownership. Make runtime boundaries explicit. A package entry point declares the supported surface; it does not expose the source tree, trigger hidden registration, or make optional integrations eager.

## Feature locality

- Keep one feature's implementation, types, tests, and small helpers under its owning folder or package.
- Split by reason to change, not one file per function and not generic top-level buckets.
- Multiple implementations of one contract live as siblings under the owning family, such as `storage/sqlite.ts` and `storage/postgres.ts`.
- A shared helper package exists only for demonstrated cross-feature reuse. A package named `utils` is not a dumping ground.
- Keep independent stateless utilities as functions/modules. Domain objects own their member operations, including pure construction and conversion; do not move those methods into helper modules merely because they are stateless. Add a class for a real domain concept, behavior, invariants, state, or lifecycle. Use [TypeScript API design](api.md) for helper extraction and public vocabulary, and [utilities](util.md) before creating a shared platform-helper module.

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
- Avoid barrel-induced cycles. Inside the package, import a local implementation from its owning file. Consumers import through the supported entry point.

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
- Match `module`, resolution, and import specifiers to the actual runtime/emitter; [TypeScript environment](env.md) owns the Bun-app, bundled-package, and unbundled-Node profiles.
- Bun-run source may use runtime-supported `.ts` specifiers. Emitted unbundled Node ESM uses runtime-valid `.js` relative specifiers. Bundled published libraries validate runtime output and declarations against their target consumers.
- Do not rely on extensionless imports or workspace-only resolution if the published runtime cannot resolve them.
- Use the `node:` protocol for Node built-ins when Node APIs are part of the target contract.

Do not apply one module profile to browser, Bun, Node, workers, config scripts, and test globals if they need distinct environments. Use small derived `tsconfig` files.

For workspace or published output, read [packages](files/package.md); for optional SDKs, [optional integrations](files/optional.md); for generated/vendor code or cycles, [module checks](files/check.md).
