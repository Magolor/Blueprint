---
name: workflow-guide
description: Read after selecting a role to choose a multi-task workflow.
---

# Workflow guide

## Summary

A workflow joins distinct tasks into a complete outcome or delivery slice. The agent keeps its role while following the selected workflow. Procedures for only one task live inside that task’s folder.

## Select a workflow

| Outcome | Workflow |
| --- | --- |
| Add a supported capability | [Feature](feature.md) |
| Correct failing behavior | [Bugfix](bugfix.md) |
| Improve an existing capability | [Enhancement](enhance.md) |
| Change a user interface | [GUI](gui.md) |
| Create or align documentation | [Document](document.md) |
| Maintain this skill | [Self-edit](self.md) |
| Repeated independent review and fixes | [Extensive Review](review.md) |
| Simplify structure with preserved behavior | [Refactor](refactor.md) |

Use a direct [task](../tasks/README.md) for a question, single review, translation, or other bounded request when a full workflow adds no value. A workflow step is not automatically a new queue item, agent, branch, or document.

## Execution contract

Read the selected workflow’s inputs, sequence, acceptance, and stopping conditions. Complete [required reading](../rules/project/read.md) and each task’s manual before dependent work. Use one accepted scope and comparison revision. Keep live progress in the repository’s queue and linked plan, not in the reusable workflow file.

Compose workflows only for distinct needs: a Feature can use GUI for its interface and Document for affected guidance. Apply shared steps once to the same verified output; avoid recursive or duplicate review and sync loops. A conditional step needs its stated trigger. Translation, independent agents, external publication, and destructive cleanup remain subject to existing authority.

A slice finishes when its acceptance and required checks pass. Record unresolved blockers or an explicit owner waiver; a time or round limit does not establish correctness. Resume from the first incomplete condition.
