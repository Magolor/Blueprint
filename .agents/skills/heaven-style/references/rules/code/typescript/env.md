---
name: ts-environment
description: Choose TypeScript package managers, runtime profiles, and verification tools.
---

# TypeScript Environment and Toolchain

## Summary

Repository metadata wins. Preserve a coherent existing package manager, lockfile, runtime, workspace, and release policy.

## Principle

For greenfield work with no contrary evidence, use this priority:

```text
Bun = pnpm > other managers
```

This is a choice between two first-class defaults, not permission to keep both:

- Choose **Bun** for a compact Bun-native application, CLI, local service, or UI toolchain that benefits from one runtime, installer, script runner, and test runner.
- Choose **pnpm** for a Node-first published library or service, a larger workspace, native/optional dependency pressure, clean npm-package consumer fidelity, or alignment with a collaborating pnpm repository.
- Choose npm, Yarn, Deno, or another manager when an existing ecosystem, deployment target, contributor constraint, or repository policy provides stronger evidence.

After choosing, commit exactly one authoritative lockfile. Pin the manager and local tools. Use frozen installs. Keep runtime, compiler mode, emitted artifacts, package exports, and consumer tests aligned.

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

Tooling enforces contracts. It does not create architecture. Start with:

- TypeScript for semantic checking and declaration/build ownership;
- one formatter;
- one primary linter, with type-aware rules only when they protect demonstrated boundaries;
- one test runner or repository-defined test surface; and
- an aggregate checked script.

Valid compact profiles include Bun + Biome + Bun test, or pnpm + `tsc` + Vitest with Biome or an explicitly divided Oxlint/Prettier/ESLint stack. Do not make two tools own formatting or the same stylistic rules. Choose from repository needs rather than copying another workspace's lineup.

Pin direct tool versions or a deliberate accepted range according to repository release policy. Do not copy concrete versions from this skill.

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
- [TypeScript modules and package boundaries](files.md)
- [TypeScript async, lifecycle, and errors](async.md)
- [TypeScript compatibility and migrations](compat.md)
- [Agent environment and commands](../../project/environment.md)
- [Formatting and lint](../../project/format.md)
- [Testing](../../project/test.md)
When changing tsconfig or module mode, read [compiler profiles](env/compiler.md). For dependency, CI, or artifact changes, read [checks](env/check.md).
