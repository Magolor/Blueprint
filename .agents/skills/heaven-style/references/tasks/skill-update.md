---
id: skill-update
task_kind: skill-update
status: active
enabled: true
order: 40
keywords: [update heaven-style, maintain skill, refresh skill, update rules, update tasks, skill version]
triggers: [skill-update, update heaven-style, stabilize heaven-style, TAL-215, TAL-231]
description: Use when maintaining heaven-style Python or TypeScript rules, tasks, workflows, scripts, indexes, versions, evidence, or failure patterns.
related_rules: [overview, util, config, files, clean, error, sql, solid, extension, docs, review, environment, format, test, ts-architecture, ts-types, ts-modules, ts-async, ts-docs, ts-environment, interfaces]
---

# Skill Update Task

## Goal

Keep `heaven-style` aligned with repo-owned contracts, packaged reference assets, primary public tool documentation, the docs ecosystem, and recurring verified failure patterns without making normal coding slower or leaking source provenance.

## Architecture

- `SKILL.md` is the fast path. A small coding or review task should succeed from it plus one directly matched task/failure/rule file.
- `references/tasks/` contains stable active workflows only: `code`, `code-review`, `doc-sync`, `doc-trans`, `test-compress`, `code-explain`, `env`, `arch-design`, `manager`, and `skill-update`.
- `references/design/` contains framework-neutral design references for GUI, frontend, desktop, dashboard, and app-shell work.
- `references/tasks/arch-design.md` is the task entry point for architecture design and periodic architecture review.
- `references/rules/` contains project rules plus language-selected code criteria: `code/python/` for Python mechanics and `code/typescript/` for TypeScript architecture, types, modules, async/resources, API docs, and environment.
- `references/examples/code/` contains source-neutral smell comparisons that build reusable design intuition without creating repository-shaped rules.
- `references/rules/code/python/solid.md` owns Python SOLID diagnostics; `references/rules/code/typescript/architecture.md` owns their TypeScript translation, including open registries versus closed unions. Link rather than duplicating examples.
- `references/workflows/architect.md` is the design-only workflow route: docs organization, module designs, architecture reviews, refactor plans, goals updates, API standard tables, and step-by-step execution plans.
- `references/workflows/developer.md` is the expanded planning/refactor route during implementation.
- `references/workflows/editor.md` is the skill-maintenance route.
- `references/failures/` contains recurring blocker playbooks and subagent delegation prompts.
- `scripts/sync.py` refreshes `assets/heavenbase-reference`.
- `scripts/index.py` validates frontmatter, IDs, relations, and local links, then generates a compact deterministic `references/index.yaml` routing projection. Parse errors and broken graph edges fail closed.
- `scripts/install.py` is the one-shot updater: run sync, then index, then install the standard global copy at `~/.agents/skills/heaven-style`; `--all-harnesses` also installs the Claude Code plugin bridge without writing `~/.claude/skills/heaven-style`; `--mirror` copies into repos that intentionally embed the skill.
- `scripts/scan.py` checks skill Python scripts for banned stdlib utility imports. A maintenance script that must remain import-hermetic and usable without HeavenBase may use the exact audited `# heaven-style-scan: standalone-control-plane` marker; the scanner still parses it, and focused tests must prove the exception.

## Repo sync

- Edit heaven-style in **Blueprint** only. Blueprint `.agents/skills/heaven-style/` is canonical.
- After rule/task/script/index changes, run `rtk uv run python .agents/skills/heaven-style/scripts/install.py` from Blueprint for the global install.
- HeavenBase does not track an in-repo skill copy; it uses the standard global install. Use `--mirror <path>` only for repos that intentionally embed a copy.
- Do not edit any embedded in-repo copy directly unless applying an emergency hotfix; backport the same change to Blueprint immediately.

## Update Workflow

1. Read this file, `SKILL.md`, `references/workflows/editor.md`, the compact generated `references/index.yaml`, and the changed script/task/rule/design/failure surfaces.
2. Read evidence for the affected language before changing rules. Use the target repository's `AGENTS.md`, manifests, runtime pins, lockfile, configuration, public contracts, representative implementation/tests, and current primary runtime/compiler/tool documentation. For work explicitly about HeavenBase, use the packaged `assets/heavenbase-reference/` surface rather than depending on an external local checkout.
3. Compare repo-owned docs, generated artifacts, prior review reports, and packaged reference assets when relevant. Extract repeated requirements, not one-off preferences.
4. Update `SKILL.md` only for daily notices, task routing, and default criteria needed for fast coding. Move detailed or situational guidance into task/rule/failure files.
5. Add or revise a task only when the workflow is stable, repeated, and cannot fit an existing task. Keep tasks non-overlapping.
6. Add or revise failure playbooks when the same blocker pattern appears repeatedly and needs a safe recovery path or subagent handoff.
7. Keep examples grounded in double-checked evidence for their language, but make distributed rules and Blueprint docs source-neutral. Do not record private/reference-repository names, absolute local checkout paths, machine-specific setup guides or observed versions, package-specific internals, or incidental implementation provenance. Preserve the generic pattern/anti-pattern and link primary public specifications when useful. For work explicitly about HeavenBase APIs/assets, use the owned names and [compat.md](../rules/code/python/compat.md) normally.
8. Keep the skill version on `MAJOR.MINOR.PATCH.N[devK]`; the current heaven-style train is `0.1.2`. Bump `N` (and optional `devK`) for ordinary skill-only edits unless the user explicitly requires version preservation; realign with `heavenbase.version.__version__` on HeavenBase-aligned releases.
9. Run `rtk uv run python scripts/install.py` from the Blueprint skill root to refresh the standard global install and `assets/heavenbase-reference/`. Use `--all-harnesses` when Claude Code should consume the generated plugin bridge too. When the skill is embedded in HeavenBase itself, `install.py` skips reference sync automatically; use `~/.agents/skills/heaven-style` for the reference clone. `install.py` must always leave the index current.
10. Run validation, including invalid fixtures for every new gate, and report changed surfaces, evidence sources, version changes, commands, and any waivers.

## Version Criteria

- Schema: `MAJOR.MINOR.PATCH.N[devK]` (for example `0.1.2.1`).
- `MAJOR.MINOR.PATCH` is the release train; heaven-style and HeavenBase share the `0.1.2` train on aligned releases.
- `N` is the very small frequent-updates fourth segment.
- Optional `devK` (`dev0`, `dev1`, …) marks in-development snapshots; omit for stabilized releases.
- The skill may lead HeavenBase between releases; skill frontmatter `version` and `src/heavenbase/version.py` must match on HeavenBase-aligned releases.
- Blueprint and HeavenBase-docs follow the same schema and stay aligned with HeavenBase when version bumps are intentional.

## Verification

From the Blueprint repo root:

```bash
rtk uv run python .agents/skills/heaven-style/scripts/install.py
rtk uv run python .agents/skills/heaven-style/scripts/index.py --check
rtk uv run python .agents/skills/heaven-style/scripts/scan.py .agents/skills/heaven-style/scripts
rtk uv run python -m py_compile .agents/skills/heaven-style/scripts/index.py .agents/skills/heaven-style/scripts/install.py .agents/skills/heaven-style/scripts/sync.py .agents/skills/heaven-style/scripts/scan.py
rtk bash scripts/flake.bash --ci --paths .agents/skills/heaven-style/scripts
```

These are Python commands because the skill-maintenance scripts are Python. Also run the target evidence repo's declared gates when rule examples or behavior depend on it; Python uses its wrappers, while TypeScript uses its checked package manager/scripts. See [../rules/project/environment.md](../rules/project/environment.md).

`index.py --check` must be hermetic and byte-deterministic: no network, configuration/database initialization, user-level writes, or volatile timestamps. Keep routing output succinct; full keywords, ordering, and relationship metadata remain in the owning frontmatter.
