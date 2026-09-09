---
name: workflow-bugfix
description: Use when diagnosing and correcting a supported behavior failure.
---

# Bugfix

## Summary

Confirm the failure, fix its cause, and verify recovery without expanding the feature. Keep the expected behavior and affected users clear.

## Tasks

1. Use [triage](../tasks/triage.md) to establish the trigger, expected and actual behavior, supported environment, and cause. Distinguish baseline failures from new regressions.
2. [Address](../tasks/address.md) the confirmed issue at its owner. Keep the correction general for the supported contract and the change minimal. Add a meaningful regression check when applicable.
3. [Review](../tasks/review.md) the candidate and verify the original failure plus affected behavior. Repeat triage and fixes for material findings within the accepted scope.
4. [Sync](../tasks/sync/README.md) changed claims and devlog evidence; run required repository checks. Use [Document](document.md) when substantial prose changes need proofreading or translation.

## Acceptance and stopping

The original failure is resolved with evidence and no confirmed material regression remains. If evidence cannot establish the cause, report the gap without inventing a speculative fix. Diagnosis-only authority ends with diagnosis.
