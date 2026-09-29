---
name: workflow-read
description: Read before code, architecture, GUI, or documentation work.
---

# Required reading

## Summary

Complete the required document bodies for the task before dependent work. Categories are cumulative; an index is not a substitute.

## Reading procedure

The task categories and complete directory sets in [SKILL.md](../../../SKILL.md#quick-read) define the reading prerequisite. These sets are cumulative when categories overlap. Language selection limits which language mechanics apply; it does not allow selecting only familiar topics within that language.

1. Select or retain the [role](../../roles/README.md), choose a fitting [workflow](../../workflows/README.md) or direct task, and identify the task category, target language, repository policy, and architecture/documentation owners.
2. Enumerate every Markdown file recursively in each required directory. Include newly added files, nested rules, examples, formats, and other details; do not stop at the map’s top-level links.
3. Read the full file bodies in manageable batches. A filename list, keyword search, index description, or truncated output is not complete reading. Continue from omitted content when output is truncated.
4. Check the inventory against what was read before coding, judging a review, explaining code, or proposing architecture. If a required file is missing or unreadable, disclose the gap and obtain the missing source or an explicit reading waiver before dependent work.
5. Apply relevant conditions after reading. A database rule does not require a database, and a translation rule does not authorize translation. Keep native language conventions and repository precedence.

For example, from the skill root, enumerate a Python code task with:

```bash
rtk rg --files references/rules/code/python references/rules/project -g '*.md'
```

Use the TypeScript tree instead for TypeScript; include both when the task spans them. Code also requires the [design philosophy](../../design/philosophy/README.md). Architecture adds all design manuals and code-design comparisons. GUI adds the whole GUI tree. See the entry for the exact directories.

Do not reread unchanged content already available in the current task. After context loss or a skill update, recover the prerequisite material before continuing. Keep any durable resume evidence in the repository’s existing task authority rather than creating another reading tracker.

Failure playbooks, machine observations, external sources, and unrelated task procedures remain conditional. Required reading grants no additional editing, publication, or external-action authority.
