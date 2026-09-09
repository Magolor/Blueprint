---
name: task-sync-git
description: Read before milestone commits, remote synchronization, or completed-work cleanup.
---

# Repository synchronization

## Summary

Keep verified milestones available to collaborators and retire temporary Git state after integration. Follow the repository’s branch, history, and publication policy.

## Procedure

Inspect current branch, diff, worktrees, remotes, and integration evidence. Preserve other work and uncommitted changes. At a coherent milestone, run required checks and commit under the declared history policy. Avoid arbitrary time-based commits that capture incomplete shared contracts.

When push authority exists, fetch and inspect divergence, integrate according to policy, verify affected behavior, and push the intended refs. A non-fast-forward update needs explicit authority; do not infer it from a normal push request. Report local-only milestones when publication is outside scope.

Keep the smallest useful active branch set. Preserve protected and long-lived product branches. Before retiring a temporary branch or worktree, verify its owner is finished, its changes and evidence are integrated or recoverable, and it contains no unique commits or local work that must remain. An old timestamp alone is insufficient. Remove only authorized completed targets; never force removal to bypass unexplained changes. Remote deletion needs explicit authority.

## Acceptance

The milestone’s revision and checks are known, authorized remote refs match, and any retired state has verified integration or recovery evidence. Report remaining divergence, unsynced work, or skipped cleanup. This manual schedules no background automation.
