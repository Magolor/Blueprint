---
id: environment
title: Agent environment and commands
enabled: true
blocking: true
order: 95
category: project
keywords: [rtk, uv, Bun, package manager, lockfile, AGENTS.md, scripts/_env.bash, bash wrapper, python path, venv, sync-env.bash, package script, command prefix, coding agent]
description: Use when running shell commands, choosing the repository's Python or TypeScript environment, adding wrappers or package scripts, or diagnosing wrong-environment failures for coding agents.
---

# Agent environment and commands

## Core rule

Read repo `AGENTS.md`, runtime/package metadata, lockfile, and CI first. Preserve the repository's coherent environment. When the session provides `rtk`, prefix the **entire** agent shell command with it.

Python Heaven-lineage repos are `uv`-first: run work through repo Bash wrappers that source `scripts/_env.bash`. That normally means repo wrappers or `rtk uv run python`, not `rtk python`; bare PATH Python can resolve to broken system or Conda shims. Do not bypass wrappers with bare `python`, `pytest`, `black`, `flake8`, or ad-hoc `pip install` when the repo declares `scripts/*.bash`.

TypeScript repositories are metadata-first: use the checked-in package manager, one lockfile, pinned local tools, and declared package scripts. For a new repo with no contrary policy, use Bun and the detailed [TypeScript environment rule](../code/typescript/environment.md). Do not convert an existing pnpm/npm/Yarn project or introduce a second lockfile as incidental work.

For the Blueprint/HeavenBase Python scaffold, dependency source of truth is **`requirements*.txt`**, with `pyproject.toml` referencing those files. Its install priority when setup is unavoidable outside wrappers is **uv → pip (`requirements*.txt`) → pyproject (`pip install -e ".[dev]"`) → conda (`environment-*.yml`) → poetry (`poetry.lock`)**. This paragraph does not apply to a TypeScript package.

## Apply when

- Starting implementation, verification, release, sync, lint, test, benchmark, or docs-generation work.
- Adding or reviewing repo Bash wrappers or CI command examples.
- A coding agent chooses shell commands, Python/Bun/Node executables, package managers, or environment setup steps.
- Commands fail with missing modules, wrong interpreter/runtime, lockfile drift, or a missing tool.

## Do

- Read `AGENTS.md` for repo-specific wrapper names, extras, markers, demo paths, and release policy.
- Prefix the full agent shell command with `rtk` when available (`rtk bash ...`, `rtk uv ...`, `rtk uv run python ...`).
- For ad-hoc repo Python probes, use `rtk uv run python ...` or a Bash wrapper helper. Use `rtk python ...` only when deliberately testing PATH/system Python behavior.
- Prefer repo wrappers in this order when they exist (wrapper name comes from repo `AGENTS.md`; Blueprint and HeavenBase use `scripts/sync-env.bash`):
  1. `rtk bash scripts/sync-env.bash`
  2. `rtk bash scripts/flake.bash --ci` or `-a`
  3. `rtk bash scripts/test.bash`
  4. repo-specific wrappers such as `release.bash`, `benchmark.bash`, or `sync-readme.bash`
- Use direct `uv` only when no wrapper exists or the wrapper explicitly forwards extra args, for example `rtk uv build` or `rtk uv run <tool>`.
- Source `scripts/_env.bash` in new Bash wrappers and call `resolve_uv`, `run_python`, or `run_uv_python` instead of duplicating interpreter lookup.
- Honor repo Python preference env vars when hooks or CI need `uv` first: `REPO_PYTHON_PREFERENCE`, `HEAVENBASE_PYTHON_PREFERENCE`, or `BLUEPRINT_PYTHON_PREFERENCE` set to `uv-first`.
- Report the exact wrapper, `uv` path, and Python resolution used when env failures block progress.
- For TypeScript, use the scripts declared in `package.json`; in a Bun repo, prefer `rtk bun ci` for frozen installation and `rtk bun run <script>` for standing gates.
- Pin the TypeScript runtime and tool versions through repository metadata and CI. Use project-local tools; do not rely on global TypeScript, ESLint, Prettier, `ts-node`, or test runners.
- In a new Bun repo, commit only `bun.lock`, pin the executable Bun release in the repo/CI setup, and keep `packageManager` aligned. Use the repository's declared version manager only when Node compatibility is required.

## Avoid

- Bare `pytest`, `black`, `flake8`, `python -m pytest`, `rtk python ...`, or `pip install -e .` when repo wrappers or `uv run` are the intended repo environment.
- Conda activation or hand-maintained `requirements*.txt` as the primary setup path in `uv`-first repos.
- Hard-coded `python`/`uv` lookup ladders copied into every Bash script.
- Assuming `rtk` replaces repo wrappers; `rtk` wraps the outer command, it does not replace `bash scripts/test.bash`.
- Treating heaven-style skill-maintenance scripts as target-repo commands.
- Mixed JavaScript lockfiles, `bunx`/`npx` downloads in standing scripts or CI, global-tool assumptions, or a package-manager migration hidden inside feature work.

## Python command ladder

```text
AGENTS.md
  -> rtk (when session provides it)
    -> bash scripts/<wrapper>.bash
      -> scripts/_env.bash
        -> uv / uv.exe
          -> repo .venv or uv-managed env
```

For TypeScript:

```text
AGENTS.md + package.json + committed lockfile + CI runtime pin
  -> rtk (when session provides it)
    -> declared package manager
      -> repository package scripts
        -> local formatter / linter / typecheck / test / build
```

## Python `_env.bash` contract

Shared helpers in `scripts/_env.bash`:

- `resolve_uv` / `resolve_uv_optional` — prefer `uv` before `uv.exe`
- `resolve_python` / `run_python` — active venv, repo `.venv`, `uv run python`, then system Python
- `run_uv_python` — force `uv run python`

New repo wrappers should set `ROOT`, `cd` to it, `source "${ROOT}/scripts/_env.bash"`, then call helpers.

## Exceptions

- **Skill maintenance:** scripts under `.agents/skills/heaven-style/scripts/` may use bare `python` from a known-good shell; prefer `rtk uv run python` in agent sessions.
- **Python CI:** GitHub Actions may call `uv sync` and `bash scripts/...` directly without the agent-only `rtk` prefix.
- **Non-uv legacy repos:** follow that repo's `AGENTS.md`; do not force `uv` where the repo is not `uv`-first.
- **Existing TypeScript repos:** follow the coherent committed manager/runtime; Bun is the new-repo fallback, not an automatic migration mandate.

## Blueprint/Python example

**Anti-pattern:**

```bash
pytest tests -q
python -m black src
pip install -e ".[dev]"
```

**Recommended pattern:**

```bash
rtk bash scripts/sync-env.bash
rtk bash scripts/flake.bash --ci
rtk bash scripts/test.bash tests/test_config_manager.py -q
rtk uv build
```

HeavenBase also uses `scripts/sync-env.bash` and commonly adds:

```bash
rtk bash scripts/benchmark.bash
rtk bash scripts/release.bash
```

A new Bun-based TypeScript repo normally exposes one aggregate package script:

```bash
rtk bun ci
rtk bun run check
```

## Related rules

Also apply [format.md](format.md) for lint/format wrapper details, [test.md](test.md) for verification policy, [../code/typescript/environment.md](../code/typescript/environment.md) for Bun/compiler/package details, and [../../failures/env.md](../../failures/env.md) when commands still fail after the wrapper ladder is used.
