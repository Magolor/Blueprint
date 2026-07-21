---
id: workflow-editor
title: Editor workflow
enabled: true
audience: editor
keywords: [maintain heaven-style, edit skill, install skill, update rules, update tasks, update failures, update skill version]
description: Use when maintaining this heaven-style skill, changing rules/tasks/failures/workflows, regenerating indexes, syncing reference assets, or aligning versions.
---

# Editor Workflow

## When to use

Use this surface only when maintaining the `heaven-style` skill itself: editing `SKILL.md`, rules, design references, workflows, task playbooks, failure playbooks, scripts, assets, generated index metadata, or packaged artifacts.

## Skill maintenance workflow

1. Edit the smallest relevant surface:
   - `SKILL.md` for the default fast coding path, task routing, and high-level criteria.
   - `references/tasks/code.md` for implementation workflow details.
   - `references/tasks/code-review.md` for review workflow, artifact, and Linear follow-up details.
   - `references/tasks/doc-sync.md` for docs/Mintlify/sibling-doc workflow details.
   - `references/tasks/doc-trans.md` for line-aligned Chinese MDX translation workflow details.
   - `references/tasks/test-compress.md` for pytest suite compression, marker policy, and low-value test pruning.
   - `references/tasks/code-explain.md` for newcomer-oriented explanation workflow details.
   - `references/tasks/env.md` for system environment maintenance policy and local instance handoff rules.
   - `references/tasks/arch-design.md` for architecture design and periodic architecture review workflow details.
   - `references/tasks/manager.md` for GitHub/Linear status and orchestration workflow details.
   - `references/tasks/skill-update.md` for skill architecture, script contracts, and version alignment.
   - `references/failures/` for recurring blocker triage and subagent delegation playbooks.
   - `references/workflows/architect.md` for doc organization, module designs, refactor plans, goals updates, API standard tables, and pre-implementation execution plans.
   - `references/workflows/developer.md` for large refactors, public API design, and full-rule reading during implementation.
   - `references/workflows/editor.md` for skill maintenance.
   - `references/rules/code/python/` for Python mechanics and `references/rules/code/typescript/` for TypeScript architecture/mechanics; `references/rules/project/` owns cross-language repository, service-interface, verification, and release rules and routes to the matched language surface.
   - `references/examples/code/` for source-neutral good-smell/bad-smell comparisons that support multiple rules without becoming rules themselves.
   - `references/design/` for framework-neutral GUI, frontend, dashboard, desktop, and app-shell design references.
2. Keep `references/tasks/` minimal. Default active tasks are `code.md`, `code-review.md`, `doc-sync.md`, `doc-trans.md`, `test-compress.md`, `code-explain.md`, `env.md`, `arch-design.md`, `manager.md`, and `skill-update.md`; add another task only for a stable, repeated workflow that cannot fit them.
3. Use trigger-oriented YAML frontmatter. Use `description` and `keywords` for discovery; the Markdown body is normative.
4. Keep brief examples inside their owning rule. Put reusable cross-rule smell comparisons in `references/examples/code/`, then link them directly from the relevant rule and `SKILL.md` route.
5. Keep distributed skill text and Blueprint docs source-neutral: no private/reference-repository names, absolute local checkout paths, machine-specific setup sources or observed versions, or borrowed package/framework internals. Retain only generic patterns/anti-patterns, public primary references, and explicitly owned HeavenBase API/asset/version/docs workflows.
6. Run `rtk uv run python scripts/install.py` from the Blueprint skill root after reference, design, or script changes to refresh the standard global install at `~/.agents/skills/heaven-style`. Use `rtk uv run python scripts/install.py --all-harnesses` when local Claude Code support should be refreshed too; it installs a Claude plugin bridge and does not write `~/.claude/skills/heaven-style`. Skill-maintenance scripts under `.agents/skills/heaven-style/scripts/` may use bare `python` only from a known-good shell; prefer `rtk uv run python` in agent sessions. Target-repo work follows its `AGENTS.md` and checked toolchain: `uv` for Heaven-lineage Python, the existing manager for TypeScript, and Bun only as the new-repo fallback. Prefix agent commands with `rtk` when available. When maintaining an embedded in-repo copy, use `rtk uv run python scripts/install.py --skip-sync` (or rely on the embedded auto-skip) and refresh the global install for reference assets.
7. Run `rtk uv run python scripts/index.py --check` after install to confirm the compact routing projection is structurally valid and byte-current. The check must stay hermetic and fail on malformed frontmatter, duplicate IDs, broken relations, or local links.
8. HeavenBase does not track an in-repo skill copy; it consumes the standard global install. Use `rtk uv run python scripts/install.py --mirror <path> --skip-global` only for repos that intentionally embed a copy.

## Commands

From `.agents/skills/heaven-style/`:

```bash
rtk uv run python scripts/install.py
rtk uv run python scripts/install.py --skip-sync
rtk uv run python scripts/sync.py
rtk uv run python scripts/index.py
rtk uv run python scripts/index.py --check
rtk uv run python scripts/scan.py scripts
```

From the Blueprint repo root after skill edits:

```bash
rtk uv run python .agents/skills/heaven-style/scripts/install.py
rtk uv run python .agents/skills/heaven-style/scripts/install.py --mirror <embedded-skill-path> --skip-global
```

## Self-compliance

The skill must follow its own code-quality rules. Its maintenance scripts are Python, so Python-only checks below do not become target-repo TypeScript rules:

- Scripts use HeavenBase utilities where feasible. Hermetic validation/control-plane scripts may use the scanner's explicit standalone marker when importing HeavenBase would initialize unrelated runtime state; that exception needs a focused test.
- Scripts pass `scripts/scan.py`.
- Scripts pass repo `flake.bash --ci` (includes `.agents/skills/heaven-style/scripts`) and `py_compile`.
- Skill scripts use one-line docstrings; full Google-style docstrings apply to library public APIs.
- `index.yaml` is a compact deterministic routing projection, not a frontmatter dump and never hand-edited. Full descriptions/keywords/relations stay in owning files.
- Task playbooks are few, active, and non-overlapping.
- Failure playbooks are operational, narrow, and safe around secrets and local machine state.
- Skill version follows `MAJOR.MINOR.PATCH.N[devK]` on the current heaven-style train (`0.1.2`); frontmatter `version` matches `src/heavenbase/version.py` on HeavenBase-aligned releases. Preserve the exact version only when the user records an explicit no-bump waiver.

## Install behavior

- `install.py` runs `sync.py`, then `index.py`, so a normal install leaves reference assets and `references/index.yaml` current. Use `--skip-sync` when avoiding network/reference refresh.
- The standard user install path is `~/.agents/skills/heaven-style`; legacy `heaven-style-<version>` installs are removed only after their `SKILL.md` verifies that they are the same skill.
- `--all-harnesses` installs the common Agent Skill plus a Claude Code plugin bridge. It never writes `~/.claude/skills/heaven-style`; use `--backup-claude-skill` only when an existing verified plain Claude skill must be moved aside to avoid duplicate discovery in Cursor, OpenCode, and Kilo.
- When embedded in the HeavenBase repository, `install.py` skips reference sync automatically to avoid a maintenance loop; use `~/.agents/skills/heaven-style` for `assets/heavenbase-reference/`.
- `sync.py` refreshes `assets/heavenbase-reference` in global or sibling skill checkouts only.
- `index.py` validates rules, examples, design references, workflows, tasks, failures, and local links, then indexes only concise navigation fields plus scripts/assets.
- `scan.py` checks banned stdlib imports for covered utility concerns.
