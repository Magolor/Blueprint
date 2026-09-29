---
name: workflow-feature
description: Use when delivering a new supported capability across design, code, review, and docs.
---

# Feature

## Summary

Deliver a usable capability from the accepted user outcome through verified code and current documentation. Keep one complete slice small enough to assess.

## Tasks

1. Establish the user path, inputs, observable result, constraints, and non-goals. Use [design](../tasks/design/README.md) when public contracts, architecture, or ordered work need a decision or plan.
2. [Implement](../tasks/code/README.md) the accepted slice and verify relevant happy, edge, and failure paths. Use [GUI](gui.md) for interface-specific work.
3. [Review](../tasks/review.md), [triage](../tasks/triage.md), and [address](../tasks/address.md) confirmed issues. Use [Extensive Review](review.md) when requested or justified by substantial scope.
4. Run [Document](document.md) for affected claims, then [sync](../tasks/sync/README.md) the accepted result and closeout evidence. Run repository gates on the assembled candidate.

## Acceptance and stopping

The supported user path works, required checks pass, current docs match, and material findings are resolved or explicitly waived. Stop dependent implementation for an unresolved consequential contract; continue independent accepted work. A proposed feature is not shipped behavior.
