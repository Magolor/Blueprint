---
id: workflow-editor
title: Editor workflow
audience: editor
description: Maintain, validate, version, synchronize, and install Heaven Style.
---

# Edit Heaven Style

Edit only the canonical checkout declared by its repository. Preserve distinct contracts; remove duplicate instructions, generic tutorials, and repeated catalogs. Keep rules source-neutral. User-requested personal setup locators belong in `assets/instance/` with an authority limit; credentials and reference checkouts stay outside distribution.

## Structure

- `SKILL.md`: required reading, core decisions, and task routes.
- `references/rules/`: one owner per rule, aligned language topics with native mechanics.
- `references/tasks/`: distinct task procedures, without repeating the common work loop.
- `references/workflows/`: discovery, broad work, design outputs, and maintenance.
- `references/design/philosophy.md`: shared public mental model and internal ownership.
- `references/design/gui/`: visual rules and exact palettes.
- `references/examples/`: reusable comparisons; keep small examples with their rule.
- `references/failures/`: verified recurring blockers and bounded recovery.

For this skill, aim for an entry under 800 words, maps under 450, and focused pages under 900. These are review targets, not target-repository documentation rules. Split by reader decision into short named files. Keep vital principles and reading prerequisites in the entry. Nested code and design rules remain required within their task category. Do not replace that obligation with topic-only selection. Read both language trees for work spanning both; leave unrelated operational recovery conditional.

Frontmatter supplies stable IDs and concise search descriptions. The body is normative. Preserve IDs when moving files, update links and anchors, and generate `references/index.yaml`; never edit it manually. Add tasks only for stable repeated work that cannot fit an existing route. Wrapper skills, if needed, only link here.

## Evidence and verification

Inspect affected repository contracts, manifests, runtime pins, configuration, representative code/tests, and relevant primary specifications. Generalize only evidence that survives across repositories. Keep private names, incidental provenance, framework internals, and mutable setup facts out of rules.

Bump the fourth segment of `MAJOR.MINOR.PATCH.N[devK]` for ordinary edits unless the user waives it. Optional `devK` marks development; skill and product versions are independent.

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

Remove legacy version-suffixed installs only after their `SKILL.md` verifies identity. `scan.py` allows only declared standalone dependencies; keep exceptions such as YAML narrow. Report changed surfaces, version, evidence, verification, and waivers.
