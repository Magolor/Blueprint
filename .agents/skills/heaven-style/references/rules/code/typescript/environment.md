---
id: ts-environment
title: TypeScript environment and toolchain
enabled: true
blocking: true
order: 260
category: code-quality
keywords: [Bun, bun.lock, packageManager, TypeScript, tsconfig, Biome, ESLint, ESM, NodeNext, CI, dependency audit, trustedDependencies]
description: Use when creating or changing a TypeScript repository, package metadata, lockfile, compiler configuration, scripts, linting, testing, dependency policy, runtime selection, or CI commands.
---

# TypeScript Environment and Toolchain

## Core rule

Repository metadata wins. Preserve an existing coherent package manager, lockfile, runtime, and workspace policy. For a new Heaven-style TypeScript repository with no contrary requirement, use Bun for dependency management, scripts, tests, and the application runtime; use strict TypeScript, native ESM, project-local tools, one committed lockfile, and deterministic CI installs.

Tooling exists to enforce contracts, not to create a second architecture. Keep the default stack small: TypeScript for semantic checks, Biome for fast formatting and baseline linting, and Bun's test runner. Add type-aware `typescript-eslint` only when its rules protect a demonstrated boundary, especially async/lifecycle correctness or a published library.

## Apply when

- Bootstrapping a TypeScript app, library, CLI, service, or workspace.
- Changing `package.json`, `bun.lock`, `tsconfig*.json`, formatter/linter config, scripts, CI, dependencies, runtime selection, or package exports.
- Choosing between Bun, Node.js, pnpm, npm, or Yarn in an existing or new repository.
- Diagnosing install drift, mixed lockfiles, global-tool dependence, ESM/CJS disagreement, or source-versus-package behavior.

## Package-manager and runtime policy

- Read `AGENTS.md`, `package.json#packageManager`, the committed lockfile, workspace metadata, CI, and release scripts before choosing commands.
- Preserve a coherent existing toolchain. Do not convert a pnpm/npm/Yarn project to Bun as an incidental feature change.
- In a new repository, pin an exact Bun release in `packageManager`, commit the text lockfile `bun.lock`, and use `bun ci` in CI or other frozen-install gates.
- Pin the executable Bun runtime in the repository's supported runtime file and CI setup as well. `packageManager` declares intent but does not by itself provision or verify the running Bun binary; make CI fail on version drift when the setup cannot guarantee it.
- Keep exactly one authoritative package-manager lockfile. A migration removes the old lockfile and updates CI, containers, docs, release automation, and contributor commands in the same reviewed change.
- Use project-local dependencies and package scripts. Global TypeScript, ESLint, Prettier, `ts-node`, or test runners are not part of a reproducible build.
- Use `bun run <script>` for standing commands. Do not use `bunx` in package scripts or CI to fetch an unpinned tool at execution time.
- Use Bun as the runtime only when the target deployment supports it. If the product or published package targets Node.js, test the supported Node versions and package boundary even when Bun manages dependencies locally.
- Declare supported runtime versions in `engines` or the repository's equivalent checked metadata, and keep the CI matrix aligned. Prose-only runtime support is not a release contract.
- When Node.js is required locally, follow the repository's checked runtime file or declared version manager; do not install a second unmanaged system Node to satisfy one repository.

**Anti-pattern:**

```json
{
  "scripts": {
    "lint": "bunx eslint .",
    "test": "ts-node ./scripts/test.ts"
  }
}
```

with `bun.lock`, `package-lock.json`, and an unpinned global compiler all present.

**Recommended pattern:**

```json
{
  "type": "module",
  "packageManager": "bun@<exact-reviewed-version>",
  "scripts": {
    "format": "biome format --write .",
    "format:check": "biome format .",
    "lint": "biome lint .",
    "typecheck": "tsc --noEmit",
    "test": "bun test",
    "check": "bun run format:check && bun run lint && bun run typecheck && bun run test"
  },
  "devDependencies": {
    "@biomejs/biome": "<exact-reviewed-version>",
    "@types/bun": "<exact-reviewed-version>",
    "typescript": "<exact-reviewed-version>"
  }
}
```

Resolve placeholders to reviewed exact versions when scaffolding; do not copy a stale version from this skill.

## Compiler baseline

For Bun-run applications and bundled packages, start with this semantic profile and narrow it only for an evidenced tool or target constraint:

```jsonc
{
  "compilerOptions": {
    "lib": ["ESNext"],
    "target": "ESNext",
    "module": "Preserve",
    "moduleResolution": "bundler",
    "moduleDetection": "force",
    "types": ["bun"],
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "isolatedModules": true,
    "noEmit": true,
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitOverride": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true,
    "forceConsistentCasingInFileNames": true,
    "skipLibCheck": false
  }
}
```

- Treat this as a starting contract, not a universal file to paste over existing configurations.
- Keep `skipLibCheck: false` when practical. A temporary `true` needs a recorded incompatible declaration, owner, and removal condition; it trades verification speed/compatibility for less dependency-boundary checking.
- Do not add DOM libraries to a server project just to make an accidental browser global type-check. Add only the host libraries actually supported.
- Use `import type` and `export type` under `verbatimModuleSyntax` so runtime edges remain visible.
- Do not enable emission in the typecheck config. Use a separate build config when the product genuinely emits JavaScript or declarations.

## App, Bun library, and Node library modes

- **Bun app or bundled package:** `module: "Preserve"` plus `moduleResolution: "bundler"`; execute TypeScript through Bun or the chosen bundler.
- **Published source package for Bun-aware consumers:** declare explicit `exports`, test from a packed artifact, and document that consumers must understand the shipped source format. Do not assume every Node tool can execute `.ts`.
- **Unbundled Node.js library:** use a separate build config with `module` and `moduleResolution` set to `NodeNext`, emit JavaScript and declarations, write Node-compatible relative specifiers, and validate the declared supported Node releases.
- **Browser package:** build against its actual browser targets and bundler; do not import Bun- or Node-only modules into shared browser paths.
- **Workspace:** keep packages narrowly owned, use explicit workspace dependencies, and run both per-package boundary checks and the root gate. A workspace is not permission for arbitrary cross-package source imports.

Never mix compiler modes opportunistically within one package. The runtime, resolver, emitted artifact, `exports` map, and consumer test must agree.

## Formatting and linting

- Use one formatter. Prefer Biome for a new lightweight repository.
- Use Biome's recommended baseline lint set, then add only rules the team will keep green.
- Add `typescript-eslint` with typed linting when rules need the type graph, such as unhandled promises, unsafe operations, or API/lifecycle correctness. If added, let Biome format and divide lint ownership explicitly; disable overlapping stylistic rules.
- Lint source, tests, scripts, and checked configuration files. If a file cannot be checked, make the exclusion narrow and explain the risk.
- Keep suppressions local, reasoned, and removable. A bare `eslint-disable`, `@ts-ignore`, or broad generated-directory exclusion is a defect unless the repository documents why it is safe.

## Dependency discipline

- Prefer platform capabilities and small, maintained packages over dependency chains for trivial helpers. Do not reimplement security-sensitive protocols, parsers, or cryptography to avoid one dependency.
- Classify runtime versus development dependencies correctly; do not make consumers install test/build tools.
- Review package ownership, release activity, license, transitive weight, install scripts, and existing platform overlap before adding a dependency.
- Bun does not run arbitrary dependency lifecycle scripts by default, but when `trustedDependencies` is absent it does trust a built-in list for npm-sourced packages. Inspect `bun pm default-trusted` and `bun pm untrusted`. If the project declares `trustedDependencies`, remember that it replaces rather than extends Bun's default list; include only reviewed exact packages whose install scripts are necessary, or use an empty list when none are needed.
- Run the repo's audit command and inspect direct-dependency release notes during updates. Prefer targeted updates over unreviewed whole-tree churn.
- Keep credentials out of source, metadata, command history, and logs. Validate required environment variables once at the application boundary and pass resolved config inward.
- Registry/linker choices and release-age policies are repository decisions, not universal defaults. Record them only when CI/deployment evidence requires them.

## Verification ladder

Use repository script names when they differ. In an `rtk` agent session, prefer the aggregate gate when it exists:

```bash
rtk bun ci
rtk bun run check
```

During iteration, run only the affected individual gates before the aggregate closeout:

```bash
rtk bun run format:check
rtk bun run lint
rtk bun run typecheck
rtk bun run test
rtk bun run build
```

- Run `build` only when the repository produces a build artifact.
- For published packages, pack the package and run a clean consumer smoke test against the tarball. Importing `src/` from the same workspace does not validate `exports`, declarations, files, or runtime compatibility.
- CI performs a frozen install and the same authoritative scripts contributors run. Do not hide essential flags only in CI YAML.
- Test every supported runtime that affects the public contract; Bun passing does not prove Node compatibility.

## Avoid

- Mixed lockfiles, floating tool downloads, global-tool assumptions, or `npm install` in a Bun-locked repository.
- A broad toolchain migration bundled into unrelated product work.
- `skipLibCheck`, `@ts-ignore`, `any`, or lint suppression as a permanent substitute for a typed boundary.
- Formatting through both Biome and Prettier, or overlapping stylistic ownership between Biome and ESLint.
- A build pipeline for a Bun application that can run source directly, unless deployment or distribution needs an artifact.
- Publishing package source without testing the packed consumer contract.
- Assuming Bun's built-in trusted list or package popularity replaces project-specific review of necessary lifecycle scripts.

## Related rules

- [TypeScript types](types.md)
- [TypeScript modules and package boundaries](modules.md)
- [TypeScript async, lifecycle, and errors](async.md)
- [Agent environment and commands](../../project/environment.md)
- [Formatting and lint](../../project/format.md)
- [Testing](../../project/test.md)
