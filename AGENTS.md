# Blueprint Agent Guide

## Purpose and authority

The `typescript` branch is the active Blueprint product line. It is a strict starter for a small Node SDK and CLI package.

Use this authority order:

1. Current user instructions and this guide.
2. Shipped code, tests, package artifacts, and CI.
3. `README.en.md` and `docs/README.md`.
4. Current plans and reports.

`package.json` owns direct dependencies and commands. `pnpm-lock.yaml` owns resolved dependency state. Use pnpm only.

## Work loop

1. Run `rtk pnpm tasks --ready` for non-trivial work.
2. Claim an existing task before you create one.
3. Keep resumable state only in `docs/tasks.yaml`.
4. Use one linked plan for architectural or multi-slice work.
5. Preserve unrelated changes and other worktrees.
6. Run focused checks during implementation.
7. Run `rtk pnpm check` before closeout.
8. Update canonical docs and `docs/DEVLOG.md`.
9. Remove completed or canceled queue rows.

The queue supports `draft`, `ready`, `active`, `blocked`, and `postponed`. Record cancellation during closeout, then remove the row.

## TypeScript architecture

- Keep one cohesive native ESM package until a real boundary earns another package.
- Use `src/index.ts` as the only public SDK boundary.
- Use `src/cli.ts` as a thin adapter over the SDK.
- Validate external values from `unknown`.
- Use direct functions for stateless behavior. Do not invent a template-domain object.
- Keep strict compiler options enabled.
- Add no framework, GUI, service, database, plugin, or workspace without a concrete requirement.

## Commands

Prefix local agent commands with `rtk`.

```bash
rtk pnpm install --frozen-lockfile
rtk pnpm check:fast
rtk pnpm check
rtk pnpm build
rtk pnpm package:check
```

`pnpm check` is the complete code, documentation, and package gate.

## Branch and skill contract

`typescript` is active and is the hosted default. `python` is the compatibility line. These are the only long-lived branches.

Product files can differ. The `.agents/skills/heaven-style/` tree must be byte-identical on every configured product branch. The default branch set is `python typescript`.

Edit Heaven Style only in Blueprint. Synchronize its exact tree to both branches. Run both branch gates after a skill change. Then reinstall it with:

```bash
rtk python3 .agents/skills/heaven-style/scripts/install.py
```

Do not create duplicate harness-specific skill copies.

An external push, package publication, deployment, default-branch change, or remote deletion needs explicit user authority.
