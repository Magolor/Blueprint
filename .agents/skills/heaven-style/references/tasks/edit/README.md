---
name: workflow-editor
description: Read before editing, validating, synchronizing, or installing Heaven Style.
audience: editor
---

# Edit Heaven Style

## Summary

Edit only the canonical checkout declared by its repository. Preserve distinct contracts; remove duplicate instructions, generic tutorials, and repeated catalogs. Keep rules source-neutral. User-requested personal setup locators belong in `assets/instance/` with an authority limit; credentials and reference checkouts stay outside distribution.

For a new skill or substantial entry rewrite, use the [skill template](../../../assets/templates/skill.md). Its search description selects invocation scenarios; its Summary explains the outcome.

## Structure

- `SKILL.md`: role-first routing, required reading, and core decisions.
- `references/rules/`: one owner per rule, aligned language topics with native mechanics.
- `references/roles/`: agent identity, responsibility, and session or assignment lifecycle.
- `references/tasks/`: bounded procedures and their nested manuals; each task has an observable output.
- `references/workflows/`: sequences across tasks with entry conditions, acceptance, and stopping rules. A single-task procedure belongs under its task.
- `references/design/philosophy/`: shared public mental model and internal ownership.
- `references/design/gui/`: visual rules and exact palettes.
- `assets/`: arbitrary resources with explicit ownership and distribution limits; `assets/templates/` is this skill’s artifact-template collection.
- `references/examples/`: reusable comparisons; keep small examples with their rule.
- `references/failures/`: verified recurring blockers and bounded recovery.

Use the [reference guide’s navigation convention](../../README.md#navigation-convention): prefer `README.md` for new folder entries when orientation helps, and reuse established maps instead of duplicating them.

For this skill, aim for an entry under 800 words, maps under 450, and focused pages under 900. These are review targets, not target-repository documentation rules. Split by reader decision into short named files. Keep vital principles and reading prerequisites in the entry. Nested code and design rules remain required within their task category. Do not replace that obligation with topic-only selection. Read both language trees for work spanning both; leave unrelated operational recovery conditional.

Use the skill template’s Summary, Quick Read, flexible detail, Notes, and References structure when it fits. Keep real-use evidence in an existing notes/failure owner; elevate validated frequent lessons into the canonical rule. Provider skill-creation guides supply technical contracts, not a prose style to copy: simplify dense wording and boilerplate without losing meaning.

Frontmatter uses `name` as its sole stable identifier and `description` for search scenarios. The body is normative. The document heading owns its title. Required reading is stated in `SKILL.md` and linked reading guides, not a `blocking` metadata flag. Preserve names when moving files, update links and anchors, and generate `references/index.yaml`; never edit it manually. Add tasks only for stable repeated work that cannot fit an existing route. Wrapper skills, if needed, only link here.

## Evidence and verification

Inspect affected repository contracts, manifests, runtime pins, configuration, representative code/tests, and relevant primary specifications. Generalize only evidence that survives across repositories. Keep private names, incidental provenance, framework internals, and mutable setup facts out of rules.

Follow the canonical repository’s version and release policy, including any freeze. Use its declared prerelease format; do not infer a bump from an ordinary edit. Skill and product versions are independent unless that policy aligns them.

From the skill root, with the repository's Python environment:

```bash
rtk uv run python scripts/index.py
rtk uv run python scripts/index.py --check
rtk uv run python scripts/scan.py --stdlib-only --allow-import yaml scripts
rtk uv run python -m py_compile scripts/index.py scripts/install.py scripts/machine.py scripts/scan.py
rtk uv run python scripts/install.py
```

Use repository wrappers where declared. Run the owning repository's lint/tests and all required branch gates. For structural edits, compare reading sizes, audit retained contracts, and follow representative routes. New validators need valid and invalid fixtures that exercise the real gate. Index check mode must be deterministic, read-only, network-free, and free of runtime/config initialization.

## Installation

`install.py` indexes and installs to `~/.agents/skills/heaven-style` without network, reference-project, or target-package dependencies. `--all-harnesses` also refreshes the Claude Code plugin bridge without a duplicate plain Claude skill. `--mirror <path>` is only for an intentionally embedded copy; `--skip-global` limits that operation. Backport emergency mirror fixes to the canonical source.

`scan.py` allows only declared standalone dependencies; keep exceptions such as YAML narrow. Report changed surfaces, version, evidence, verification, and waivers.
