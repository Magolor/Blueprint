---
name: references
description: Read when locating Heaven Style roles, workflows, tasks, or rules.
---

# Reference guide

## Summary

Select the agent’s role, follow a fitting workflow, and use the task manuals for each step. This guide explains where guidance lives; the generated YAML index supports exact lookup. Neither replaces required reading.

## Where to look

| Need | Entry and purpose |
| --- | --- |
| Agent identity and session or assignment lifecycle | [Roles](roles/README.md): Default, Manager, Worker, Teacher. |
| A complete outcome spanning tasks | [Workflows](workflows/README.md): ordered tasks, acceptance, and stopping rules. |
| One bounded result | [Tasks](tasks/README.md): procedures and nested task-specific manuals. |
| Reading prerequisites | [Required reading](rules/project/read.md), governed by SKILL.md. |
| Code and project standards | [Rule map](rules/overview.md) pairs language topics; `rules/project/` owns shared contracts, including [language](rules/project/language.md). |
| Public mental model or visual design | [Philosophy](design/philosophy/README.md) and [GUI style](design/gui/style.md). |
| Concrete design comparisons | [Capabilities](examples/code/capability.md) and [GUI ownership](examples/code/gui.md). |
| A verified recurring blocker | Conditional [authentication](failures/auth.md), [environment](failures/env.md), [Git](failures/git.md), [Linear](failures/linear.md), or [proxy](failures/proxy.md) recovery. |
| Artifact structure or other resources | [Templates](../assets/templates/index.md) and [assets](../assets/REFERENCE.md). |

## Navigation convention

Use `README.md` for new folder entries where readers need orientation. State the folder’s purpose and link the main choices. Reuse an established map such as `overview.md` or `index.md`; do not duplicate it for naming symmetry. Small, obvious leaf folders need no index.

Keep role contracts under `roles/`, cross-task sequences under `workflows/`, and single-task detail under its owning `tasks/<task>/` folder. Shared rules remain in `rules/`; linking them does not make them a workflow. Exact inventories belong in [index.yaml](index.yaml). A folder entry introduces its children and never makes required rules optional.
