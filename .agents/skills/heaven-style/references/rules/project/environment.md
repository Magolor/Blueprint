---
id: environment
title: Agent environment and commands
enabled: true
blocking: true
order: 410
category: project
keywords: [rtk, Bun, pnpm, uv, package manager, lockfile, AGENTS.md, CLAUDE.md, agent harness, package script, bash wrapper, python path, venv, frozen install, coding agent]
description: Use when configuring repository agent instructions, running shell commands, choosing a repository environment, adding package scripts or wrappers, or diagnosing wrong-runtime and wrong-environment failures.
---

# Agent Environment and Commands

## Core rule

Read repository policy, runtime/package metadata, lockfiles, wrappers, and CI first. Preserve the coherent environment already declared. When the session provides `rtk`, prefix the entire agent shell command with it.

TypeScript repositories are metadata-first: use the checked manager, one lockfile, project-local tools, and declared scripts. For greenfield selection, Bun and pnpm are co-preferred; apply the detailed [TypeScript environment rule](../code/typescript/environment.md).

Python repositories use their declared wrapper or environment owner. Prefer repo wrappers and `uv run` in an uv-managed repository; do not force uv, a requirements layout, or one packaging backend onto a coherent repository that chose another system.

## Agent harness bridge

Keep one repository-owned agent policy. When an agent harness does not read that policy file directly, add the smallest checked-in bridge that the harness supports instead of copying shared instructions.

For Claude Code, prefer a root `CLAUDE.md` whose sole content is `@AGENTS.md` when `AGENTS.md` is the canonical policy and no Claude-only instruction is required. Claude Code resolves the relative import from `CLAUDE.md` and loads the imported policy as project context. This import is more portable than a symbolic link. Add harness-specific text only for a verified harness-only need, and keep shared rules in the canonical policy. See [Claude Code project memory](https://code.claude.com/docs/en/memory#agents-md).

## Apply when

- Starting implementation, verification, release, sync, lint, test, benchmark, build, or docs generation.
- Adding or reviewing package scripts, Bash wrappers, or CI command examples.
- Choosing a TypeScript/Python executable, manager, virtual environment, or tool invocation.
- Diagnosing missing modules, wrong runtimes, lockfile drift, or global-tool leakage.

## Command ladder

```text
AGENTS.md + manifests + lockfile + CI/runtime pins
  -> rtk (when the agent session provides it)
    -> repository manager or wrapper
      -> checked package script / local tool
```

## Do

- Use the repository's script names, extras, markers, and release policy.
- Prefix the full agent command with `rtk` when available; `rtk` wraps the command and does not replace the repository entry point.
- For TypeScript, run the checked manager's scripts and frozen install path. Never mix Bun and pnpm commands merely because both are preferred greenfield options.
- For Python, use a declared wrapper, active project environment, or `uv run`/equivalent before PATH Python. Use bare/system Python only for deliberate environment diagnosis or a standalone script that documents that contract.
- Use project-local formatter, linter, compiler, test, build, and generator dependencies.
- Keep one aggregate check script when the repository has several standing gates, while retaining targeted scripts for iteration.
- Source a shared environment helper in repeated Bash wrappers rather than copying interpreter lookup ladders.
- Report the exact command, resolved runtime, and failure boundary when environment problems block progress.

## Avoid

- Bare `pytest`, formatter, compiler, or test-runner commands when a repository wrapper/script owns the invocation.
- `pip install`, `npm install`, `bun install`, or `pnpm install` that disagrees with the checked environment or lockfile.
- Conda, uv, mise, Corepack, Homebrew, or another host manager forced onto a repository without policy evidence.
- Hard-coded interpreter lookup copied into every wrapper.
- Floating `bunx`, `npx`, or `pnpm dlx` in standing scripts or CI.
- A package-manager or environment migration hidden inside feature work.
- Treating skill-maintenance commands as target-repository policy.

## Examples

Bun repository:

```bash
rtk bun ci
rtk bun run check
```

Pnpm repository:

```bash
rtk pnpm install --frozen-lockfile
rtk pnpm run check
```

Uv-managed Python repository:

```bash
rtk uv sync
rtk uv run pytest tests/test_area.py -q
```

Wrapper-owned Python repository:

```bash
rtk bash scripts/sync-env.bash
rtk bash scripts/flake.bash --ci
rtk bash scripts/test.bash tests/test_area.py -q
```

These are patterns, not required filenames. The target repository remains authoritative.

## Exceptions

- CI does not need the agent-only `rtk` prefix.
- Standalone skill-maintenance scripts may use a known-good Python directly when they intentionally avoid target-repository dependencies.
- Legacy repositories keep their coherent manager/runtime until migration is explicitly in scope.

## Related rules

Apply [format](format.md), [tests](test.md), [TypeScript environment](../code/typescript/environment.md), and [environment failure recovery](../../failures/env.md) as needed.
