# Blueprint Agent Guide

## Purpose and authority

The `python` branch is the maintained Python compatibility starter. It contains one small SDK and one CLI package.

Use this authority order:

1. Current user instructions and this guide.
2. Shipped code, tests, package artifacts, and CI.
3. `README.en.md` and `docs/README.md`.
4. Current plans and reports.

`pyproject.toml` owns package metadata and direct dependencies. `uv.lock` owns the resolved environment.

## Work loop

1. Run `rtk uv run python scripts/docs.py tasks --ready` for non-trivial work.
2. Claim an existing task before you create one.
3. Keep resumable state only in `docs/tasks.yaml`.
4. Use one linked plan for architectural or multi-slice work.
5. Preserve unrelated changes and other worktrees.
6. Run focused checks during implementation.
7. Run `rtk bash scripts/check.bash full` before closeout.
8. Update canonical docs and `docs/DEVLOG.md`.
9. Remove completed or canceled queue rows.

The queue supports `draft`, `ready`, `active`, `blocked`, and `postponed`. Record cancellation during closeout, then remove the row.

## Python architecture

- Keep one cohesive package until a real boundary earns another distribution.
- Use `blueprint.__init__` as the only public SDK facade.
- Use `blueprint.cli` as a thin adapter over the SDK.
- Keep imports inert. Constructors perform no I/O.
- Validate external mappings at one boundary.
- Use direct functions for stateless behavior. Do not invent a template-domain object.
- Add no GUI, service, database, plugin, or framework without a concrete requirement.

## Commands

Prefix local agent commands with `rtk`.

```bash
rtk uv sync --all-extras --frozen
rtk bash scripts/check.bash fast
rtk bash scripts/check.bash full
rtk uv build
```

## Branch and skill contract

`python` is the compatibility line. `typescript` is active and is the hosted default. These are the only long-lived branches.

Product files can differ. The `.agents/skills/heaven-style/` tree must be byte-identical on every configured product branch. The default branch set is `python typescript`.

Edit Heaven Style only in Blueprint. Synchronize its exact tree to both branches. Run both branch gates after a skill change. Then reinstall it with:

```bash
rtk uv run python .agents/skills/heaven-style/scripts/install.py
```

Do not create duplicate harness-specific skill copies.

An external push, package publication, deployment, default-branch change, or remote deletion needs explicit user authority.
