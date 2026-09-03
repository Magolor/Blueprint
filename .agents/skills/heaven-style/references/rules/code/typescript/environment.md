---
id: ts-environment
title: TypeScript environment and toolchain
enabled: true
blocking: true
order: 110
category: code-quality
keywords: [Bun, pnpm, packageManager, lockfile, TypeScript, tsconfig, Biome, Oxlint, ESLint, Prettier, Vitest, ESM, NodeNext, CI, dependency audit, workspace, packed consumer]
description: Use when creating or changing a TypeScript repository, package manager, runtime, lockfile, compiler configuration, scripts, linting, testing, dependency policy, workspace, package exports, or CI commands.
---

# TypeScript Environment and Toolchain

## Core rule

Repository metadata wins. Preserve a coherent existing package manager, lockfile, runtime, workspace, and release policy.

For greenfield work with no contrary evidence, use this priority:

```text
Bun = pnpm > other managers
```

This is a choice between two first-class defaults, not permission to keep both:

- Choose **Bun** for a compact Bun-native application, CLI, local service, or UI toolchain that benefits from one runtime, installer, script runner, and test runner.
- Choose **pnpm** for a Node-first published library or service, a larger workspace, native/optional dependency pressure, clean npm-package consumer fidelity, or alignment with a collaborating pnpm repository.
- Choose npm, Yarn, Deno, or another manager when an existing ecosystem, deployment target, contributor constraint, or repository policy provides stronger evidence.

After choosing, commit exactly one authoritative lockfile, pin the manager and local tools, use frozen installs, and keep runtime, compiler mode, emitted artifacts, package exports, and consumer tests aligned.

## Apply when

- Bootstrapping a TypeScript app, library, CLI, service, UI, or workspace.
- Changing `package.json`, a lockfile, workspace metadata, `tsconfig*.json`, formatter/linter/test config, scripts, CI, dependencies, runtime support, or exports.
- Choosing among Bun, pnpm, npm, Yarn, Deno, Node, or another runtime/manager.
- Diagnosing mixed lockfiles, global-tool dependence, ESM/CJS disagreement, or source-versus-package behavior.

## Manager and runtime policy

- Read `AGENTS.md`, `package.json#packageManager`, lockfiles, workspace configuration, runtime pins, CI, and release scripts before choosing commands.
- Do not migrate package managers inside unrelated feature work.
- Pin the selected manager through checked metadata and provision/verify it in CI. `packageManager` expresses policy but does not by itself prove the running binary.
- Use project-local dependencies and declared scripts. Standing gates must not fetch floating tools through `bunx`, `npx`, `pnpm dlx`, or a global install.
- Use the manager's frozen path in CI: `bun ci` or `bun install --frozen-lockfile` for Bun; `pnpm install --frozen-lockfile` for pnpm; the repository-declared equivalent for others.
- Declare supported runtime versions in checked metadata and keep the CI matrix aligned. Prefer supported LTS releases for Node production libraries/services unless product evidence requires another line.
- Bun may manage dependencies for Node-targeted code, but Bun success does not prove Node compatibility. Test every advertised runtime and the packed artifact.
- A migration updates the manager pin, lockfile, workspace settings, CI, caches, containers, docs, and release automation in one isolated change and removes the old lockfile.

## Minimal tool ownership

Tooling enforces contracts; it does not create architecture. Start with:

- TypeScript for semantic checking and declaration/build ownership;
- one formatter;
- one primary linter, with type-aware rules only when they protect demonstrated boundaries;
- one test runner or repository-defined test surface; and
- an aggregate checked script.

Valid compact profiles include Bun + Biome + Bun test, or pnpm + `tsc` + Vitest with Biome or an explicitly divided Oxlint/Prettier/ESLint stack. Do not make two tools own formatting or the same stylistic rules. Choose from repository needs rather than copying another workspace's lineup.

Pin direct tool versions or a deliberate accepted range according to repository release policy. Do not copy concrete versions from this skill.

## Compiler baseline

Keep these semantic checks enabled unless a concrete tool/target incompatibility is recorded:

```jsonc
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitOverride": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true,
    "verbatimModuleSyntax": true,
    "forceConsistentCasingInFileNames": true
  }
}
```

- Add only the host libraries the package supports; do not add DOM types to make accidental browser globals compile in server code.
- Use `import type`/`export type` where runtime-edge visibility matters.
- Keep typecheck and emit responsibilities explicit. A library often needs a no-emit check config plus a build config.
- Treat `skipLibCheck: true`, broad assertions, and lint suppressions as recorded compatibility debt, not silent defaults.

## Runtime and module modes

- **Bun-native app/tool:** use the compiler/module profile supported by Bun or the selected bundler; test the real entry path.
- **Unbundled Node library:** use modern Node ESM/`NodeNext`, emit JavaScript and declarations, write runtime-valid specifiers, and test supported Node releases.
- **Bundled app/browser package:** use the actual bundler/target profile and keep browser/shared code free of unsupported server-runtime imports.
- **Published source package:** document the required consumer tooling and validate a packed external consumer; do not assume Node executes TypeScript source.
- **Workspace:** import other packages by their public package names, declare workspace dependencies, and reject sibling source-path coupling unless it is an explicitly private source plane.

Never mix modes opportunistically within one package. Runtime, resolver, emit, exports, and consumer expectations must agree.

## Package boundaries and artifacts

- A package boundary is earned by independent consumption, runtime/dependency isolation, compatibility/release ownership, or extraction—not by a noun in an architecture diagram.
- Keep source-plane and artifact-plane checks distinct. Workspace aliases can prove source behavior while hiding broken exports, specifiers, declarations, optional peers, or packed files.
- Published packages need explicit `exports`, correct dependency classes, a controlled packed file set, and a clean tarball consumer smoke.
- Apps may bundle for distribution. Libraries should prefer transparent output until bundling solves a real consumer or artifact need.

## Dependency discipline

- Prefer platform capabilities and small maintained packages over dependency chains for trivial wrappers; do not reimplement security-sensitive protocols, parsers, or cryptography casually.
- Classify runtime, peer, optional, and development dependencies from the consumer contract.
- Review ownership, maintenance, license, transitive weight, install scripts, native support, and existing platform overlap before adding a dependency.
- Use the selected manager's allow/trust controls for lifecycle scripts. Default trust lists or package popularity do not replace project review.
- Keep credentials out of source, metadata, command history, and logs. Resolve required environment configuration at one application boundary.

## Verification ladder

Use repository script names when they differ.

For Bun:

```bash
rtk bun ci
rtk bun run check
```

For pnpm:

```bash
rtk pnpm install --frozen-lockfile
rtk pnpm run check
```

During iteration, run only the affected formatter, lint, typecheck, test, build, package, or consumer gate; finish with the repository aggregate when risk warrants it.

- Run build only when the repository produces an artifact.
- For published packages, pack and install the archive in a clean consumer.
- Test every advertised runtime and environment boundary.
- Keep essential flags in repository scripts so local and CI entry points do not drift.

## Avoid

- Mixed lockfiles or manager commands that do not match the lockfile.
- A manager/runtime migration bundled into product work.
- Floating tool downloads and global-tool assumptions.
- Permanent `skipLibCheck`, `@ts-ignore`, `any`, or broad lint suppression instead of a typed boundary.
- Overlapping formatters or linters with unclear ownership.
- Workspace-only source success presented as package-release evidence.
- Copying a large monorepo toolchain into a small package without matching pressure.

## Related rules

- [TypeScript types](types.md)
- [TypeScript utilities and platform APIs](util.md)
- [TypeScript API design and vocabulary](api.md)
- [TypeScript modules and package boundaries](modules.md)
- [TypeScript async, lifecycle, and errors](async.md)
- [TypeScript compatibility and migrations](compat.md)
- [Agent environment and commands](../../project/environment.md)
- [Formatting and lint](../../project/format.md)
- [Testing](../../project/test.md)
