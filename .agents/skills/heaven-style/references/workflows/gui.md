---
name: workflow-gui
description: Use when designing, implementing, and verifying a GUI change.
---

# GUI

## Summary

Deliver the intended interaction with visible behavior and reviewable visual evidence. Keep the interface focused on the user’s task.

## Tasks

1. Use [design](../tasks/design/README.md) to establish the user flow, relevant states, layout, and acceptance. Complete the full [GUI reading](../design/gui/style.md) and applicable code or architecture prerequisites.
2. [Implement](../tasks/code/README.md) the accepted flow. Check relevant empty, loading, success, failure, keyboard, accessibility, and viewport behavior through the repository’s supported tools.
3. [Review](../tasks/review.md) the running interface and candidate. [Triage](../tasks/triage.md) and [address](../tasks/address.md) confirmed issues; screenshots alone do not prove interaction behavior.
4. Run [Document](document.md) for user-facing changes, capture actual screenshots for the [GUI PR body](../../assets/templates/pr/gui.md), and [sync](../tasks/sync/README.md) verified output.

## Acceptance and stopping

The intended flow works, relevant states and checks pass, and visual evidence shows the actual candidate. Disclose unavailable runtime or screenshot evidence; do not substitute a mockup for a captured implementation.
