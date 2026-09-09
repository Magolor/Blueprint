---
name: task-sync
description: Read before aligning canonical documentation, branch copies, or installed skills.
---

# Synchronize

## Summary

Update declared projections from their canonical owner and verify that they agree. Synchronization follows existing relationships and authority; similar filenames alone do not establish a copy contract.

## Procedure

Identify the authoritative change, affected readers, declared projections, and current revisions. Use [documentation sync](../../rules/project/docs/sync.md) to update false claims and generated navigation with proportional edits. Compose changed content through [docs](../docs/README.md); translate only through the authorized [translation task](../translate.md).

For “keep everything current”, enumerate the task's actual projections: source, examples, generated output, installed package or skill, running service, and integrated branch as applicable. Use the accepted design and supported version. Do not infer a dependency upgrade or a copy relationship from the word “latest”.

Verify the destination, not only the source edit. For an installed artifact, inspect its revision or content and exercise the relevant entry when required. For a generated page, run its owner and freshness check. For a running application, establish which build or configuration it uses before claiming the change is visible.

Use [repository sync](git.md) for branches, remotes, and completed worktrees. For skill mirrors and installation, follow [skill maintenance](../edit/README.md#installation). Keep credentials and local-only resources out of distribution.

## Acceptance

Declared in-scope projections match their owner and pass applicable checks. Report stale or blocked projections and their owner. Record substantial closeout in the existing devlog; do not create a second queue or history surface.

Distinguish edited, verified, committed, integrated, installed, and published states when they affect the outcome. A current README beside a stale demo or an old installed copy is incomplete synchronization if those surfaces belong to the task.
