---
name: template-pr-stack
description: Read when a pull request depends on another unmerged pull request.
---

# Stacked PRs

## Summary

Use this guidance only when a PR depends on another unmerged PR or belongs to
an ordered stack. Make its own change understandable without reading the stack.

## Describe the slice

After Changes, include a short Stack section identifying the root plan or PR,
immediate dependency, actual base branch, and this PR's purpose. Link the next
slice when known. Distinguish its own diff and verified behavior from inherited
changes and the stack's eventual target. A plan-only PR must say so.

Keep one ordered stack map in the root PR or canonical plan:

| Order | PR | Purpose | Depends on | PR state |
| --- | --- | --- | --- | --- |

Fill the table from current evidence; remove it from child bodies and link the
owner. This map describes integration order, not another live task queue.
State merge prerequisites and any remaining temporary contract. Link full target
protocols rather than pasting them into each PR. Use closing keywords only in
the slice that resolves the issue.

After a rebase, merge, or retarget, refresh dependency links, scope, and verification
claims. Separate checks for this slice from checks for the assembled stack.
