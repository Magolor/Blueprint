---
id: failure-linear-pressure
title: Linear issue and comment pressure failures
description: Resolve Linear issue limits and repetitive status comments.
---

# Linear Issue and Comment Pressure Failures

## Pattern

Linear work gets blocked because a project has too many issues, issue creation fails, or one continuous issue has accumulated too many routine progress comments.

## Response

1. Confirm the Linear team, project, issue, and intended update before changing anything.
2. If issue creation is blocked by project pressure, remove `Done`, `Duplicated`, `Outdated` issues from that Linear project first. Preserve issue history. Do not delete issues or alter active/backlog issues without explicit approval.
3. Retry the blocked issue creation or project update after the `Done`, `Duplicated`, `Outdated` issue cleanup.
4. If one issue has too many comments, summarize routine progress, verification, and next-step comments into one rolling status comment.
5. Edit the rolling status comment for future routine updates. Add separate comments only for distinct decisions, blockers, handoffs, or explicit user-requested updates.
6. Report which project or issue was cleaned, whether issue creation now works, and which comment is the maintained rolling status comment.

## Do Not

- Do not create more routine comments while fixing comment pressure.
- Do not remove active, backlog, blocked, or in-review issues just to make space.
- Do not mark issues `Done` unless the user, or the reviewer, or the manager explicitly grants that authority for the current run.
- Do not hide cleanup actions. Agents should report Linear project membership changes and comment compression.
