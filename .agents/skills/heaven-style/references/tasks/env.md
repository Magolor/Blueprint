---
name: env
description: Read before machine maintenance or environment handoffs.
task_kind: env
status: active
---

# Env Task

## Summary

Maintain the requested machine environment through its setup owner without turning local choices into universal rules.

## Goal

Maintain a developer machine environment without turning machine-specific choices into universal Heaven-style rules. Use this task for host toolchains, shell environment policy, package-manager ownership, machine setup docs, command handoffs, and requested machine-maintenance execution.

## Routing

1. Read the repository or machine setup guide that owns the environment. Treat prose guidelines as planning context. Finalized scripts, assets, lockfiles, and checked-in configuration are stronger evidence.
2. Read [environment](../rules/project/environment.md) before choosing agent shell commands, Python/uv paths, or wrapper policy. Use [env](../failures/env.md) when commands fail because PATH, Python, uv, or activation is wrong.
3. Keep stable policy here. Keep environment owner references and recovery procedures in `assets/`. Track reviewed non-secret machine notes under `assets/instance/` when they are useful. For macOS setup maintenance, read [MacOS env](../../assets/MacOS-env.md). Generate or inspect an instance note only when the task needs host facts.
4. Identify the role for this turn before acting: a machine-maintainer agent may change the machine environment within the requested scope; a setup-pipeline, docs, or planning agent edits reproducible assets and hands commands to the user.

## Guardrails

- Machine-maintainer agents are allowed to run machine-changing environment operations when the user asks them to maintain, update, repair, or verify the machine environment. Stay inside the requested scope and prefer scripted, reproducible, logged operations over ad-hoc manual edits.
- Setup-pipeline, docs, and planning agents should not run machine-changing operations. They edit guidelines, scripts, assets, and plans, then give the user commands to run.
- Before mutating the environment, inspect the relevant setup docs/assets. Separate low-risk checks from mutating steps. State any high-risk operation such as database major upgrades, profile rewrites, destructive cleanup, or credential/auth changes.
- Keep global shell/profile changes minimal, reviewable, and reversible. Prefer repo-local `.envrc`, `.env.local`, lockfiles, and wrapper scripts for project state.
- Identify package-manager ownership from the selected setup. In the macOS setup pattern, Homebrew owns native CLIs/apps, uv owns project Python, Miniforge owns interactive Python, Bun/Corepack own JS package work, mise owns Node, rustup owns Rust, and Docker owns containers. Verify these owners before applying them to another machine.
- Never write raw secrets, tokens, serial numbers, UUIDs, private key paths, or transient live state into shared rules, OS-wide assets, or instance assets.
- Treat stateful Docker databases differently from stateless CLI tools. Image and major-version upgrades need a concrete reason, backup/dump plan, and rollback path.

## Workflow

1. Classify the request as machine maintenance, policy update, reproducible script edit, local instance note, or command handoff.
2. Inspect the relevant setup docs and assets before proposing changes. Prefer checked-in scripts over memory or live machine assumptions.
3. Put OS-wide procedures and owner references in `assets/`. Put reviewed non-secret host observations in `assets/instance/` or the machine setup repository. Keep sensitive or transient observations outside the distributed skill. Keep this task limited to durable decision rules.
4. For machine maintenance, run inventory/check commands first. Apply scoped changes. Verify with the smallest reliable checks. Record what changed and what remains pending.
5. For command handoffs, group commands by risk and order. Separate inventory/check commands from mutating update commands.
