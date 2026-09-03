---
id: failure-env
title: Environment and PATH failures
enabled: true
order: 10
keywords: [wrong runtime, Bun, Node, package manager, wrong python, uv, command not found, PATH, module not found, lockfile, venv]
description: Use when commands fail because the wrong TypeScript/JavaScript runtime, package manager, shell, Python/uv environment, dependency install, or PATH is active.
---

# Environment and PATH Failures

Load [../rules/project/environment.md](../rules/project/environment.md) first for the normal `rtk` plus repository-owned runtime/package-manager/wrapper command ladder.

## Pattern

Commands fail with `program not found`, unresolved packages, lockfile/runtime mismatch, a wrong Bun/Node/Python executable, `ModuleNotFoundError`, broken shims, or repo scripts/wrappers using the wrong environment.

## Response

1. Verify the required repo environment from `AGENTS.md`, manifest, committed lockfile, runtime pin, and CI before blaming code.
2. For TypeScript, use the checked-in manager and package scripts. Inspect the active manager/runtime and run the smallest frozen-install or declared gate; do not introduce another lockfile or global tool to bypass the failure.

```bash
rtk bun --version
rtk bun ci
rtk bun run typecheck

rtk pnpm --version
rtk pnpm install --frozen-lockfile
rtk pnpm run typecheck
```

Run only the branch declared by the repository. Bun and pnpm are co-preferred for greenfield selection, but neither is a repair tool for another coherent package-manager contract.

3. For Python, prefer repo wrappers over bare tools: use the sync, test, and lint wrappers named in `AGENTS.md`. In uv-managed repositories, prefer `uv run` over an unrelated ad-hoc environment.
4. Inspect active executables only when declared scripts still fail: the package manager/runtime for TypeScript, or `rtk where uv`, `rtk where python`, `rtk where python3` (plus repo `.venv`) for Python. Use the platform's normal executable lookup command when `where` is unavailable.
5. Run the smallest Python environment check through the repo wrapper ladder:

```bash
rtk bash scripts/sync-env.bash --check
rtk uv run python -c "import package_name; print('ok')"
```

6. If `rtk python` fails but `rtk uv run python` works, treat it as PATH/system-Python drift rather than a repo failure. Keep using wrappers or `rtk uv run python` for repo work.
7. If shell activation fails, call the repo helper path instead of changing global PATH. Bash wrappers may resolve Python through an active virtualenv, repo `.venv`, `uv run python`, then system Python; use the exact order declared by the target repository.
8. Retry the original command only after the declared runtime, install state, and command entry point are proven.

## Do Not

- Do not treat missing dependencies as code regressions until the intended environment is confirmed.
- Do not bypass TypeScript package scripts with global `tsc`, ESLint, Prettier, `bunx`, or `npx`, or bypass Python wrappers with bare `pytest`, `black`, `flake8`, or `python -m ...` when declared entry points exist.
- Do not edit global shell profiles unless the user explicitly asks.
- Do not hide the chosen runtime, package manager/interpreter, lockfile, or resolved path in the final report.
