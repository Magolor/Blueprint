---
id: env
task_kind: env
status: active
enabled: true
order: 36
keywords: [maintain env, update env, repair env, system env, machine maintenance, setup maintenance, Homebrew, Brewfile, uv, conda, mise, rustup, docker]
triggers: [env, update env, maintain environment, repair environment, system maintenance, machine maintenance, refresh machine tools, setup maintenance]
description: Use when maintaining a developer machine environment, updating setup plans, performing scoped machine maintenance, or preparing safe local environment commands.
related_rules: [overview, environment, docs, review]
---

# Env Task

## Goal

Maintain a developer machine environment without turning machine-specific choices into universal Heaven-style rules. Use this task for host toolchains, shell environment policy, package-manager ownership, machine setup docs, command handoffs, and requested machine-maintenance execution.

## Routing

1. Read the repo or machine setup guide that owns the environment. Treat prose guidelines as planning context; finalized scripts, assets, lockfiles, and checked-in configuration are stronger evidence.
2. Read [../rules/project/environment.md](../rules/project/environment.md) before choosing agent shell commands, Python/uv paths, or wrapper policy. Use [../failures/env.md](../failures/env.md) when commands fail because PATH, Python, uv, or activation is wrong.
3. Keep stable policy here, OS-wide operation playbooks in `assets/`, and ignored single-machine facts in `assets/instance/*.local.md`. For macOS setup maintenance, read [../../assets/MacOS-env.md](../../assets/MacOS-env.md). Generate or inspect a local instance note only when the task needs host facts.
4. Identify the role for this turn before acting: a machine-maintainer agent may change the machine environment within the requested scope; a setup-pipeline, docs, or planning agent edits reproducible assets and hands commands to the user.

## Guardrails

- Machine-maintainer agents are allowed to run machine-changing environment operations when the user asks them to maintain, update, repair, or verify the machine environment. Stay inside the requested scope and prefer scripted, reproducible, logged operations over ad-hoc manual edits.
- Setup-pipeline, docs, and planning agents should not run machine-changing operations. They edit guidelines, scripts, assets, and plans, then give the user commands to run.
- Before mutating the environment, inspect the relevant setup docs/assets, separate low-risk checks from mutating steps, and state any high-risk operation such as database major upgrades, profile rewrites, destructive cleanup, or credential/auth changes.
- Keep global shell/profile changes minimal, reviewable, and reversible. Prefer repo-local `.envrc`, `.env.local`, lockfiles, and wrapper scripts for project state.
- Keep package-manager ownership clear: Homebrew owns native CLIs/apps, uv owns project Python, Miniforge owns interactive Python, Bun/Corepack own JS package work, rustup owns Rust, and Docker owns containers.
- Never write raw secrets, tokens, serial numbers, UUIDs, private key paths, or transient live state into shared rules, OS-wide assets, or instance assets.
- Treat stateful Docker databases differently from stateless CLI tools. Image and major-version upgrades need a concrete reason, backup/dump plan, and rollback path.

## Workflow

1. Classify the request as machine maintenance, policy update, reproducible script edit, local instance note, or command handoff.
2. Inspect the relevant setup docs and assets before proposing changes. Prefer checked-in scripts over memory or live machine assumptions.
3. Put commands that apply across one OS family in `assets/`; put commands that name one host, account, or private path in an ignored `assets/instance/*.local.md` file. Keep this task limited to durable decision rules.
4. For machine maintenance, run inventory/check commands first, then apply scoped changes, then verify with the smallest reliable checks. Record what changed and what remains pending.
5. For command handoffs, group commands by risk and order. Separate inventory/check commands from mutating update commands.
