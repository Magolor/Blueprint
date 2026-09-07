---
id: ts-files-package
title: TypeScript packages
description: Read for TypeScript packages.
blocking: true
---

# TypeScript packages

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
