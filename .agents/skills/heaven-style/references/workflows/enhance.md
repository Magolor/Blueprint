---
name: workflow-enhance
description: Use when improving an existing feature’s usability, efficiency, or capability.
---

# Enhancement

## Summary

Improve an existing user path against a clear baseline. Preserve supported behavior outside the accepted change.

## Tasks

1. Inspect the current experience or metric and state the intended improvement. Use [design](../tasks/design/README.md) for changed boundaries or consequential tradeoffs. Assess suggestions as candidates under [judgment](../rules/project/work.md#interpret-intent-and-exercise-judgment); a new reference or dependency does not require a redesign.
2. [Implement](../tasks/code/README.md) the smallest coherent improvement. For efficiency work, capture comparable baseline and candidate measurements under the same stated conditions.
3. [Review](../tasks/review.md), [triage](../tasks/triage.md), and [address](../tasks/address.md) material findings. Assess the user benefit and recurring maintenance cost, not just changed line counts.
4. Run [Document](document.md) for changed guidance and [sync](../tasks/sync/README.md) the verified result. Efficiency PRs use the [benchmark comparison](../../assets/templates/pr/bench.md).

## Acceptance and stopping

Evidence shows the intended improvement, supported contracts remain intact, and required gates pass. An inconclusive benchmark is not an efficiency claim. Reassess scope if the proposed improvement adds more complexity than its demonstrated benefit.

An investigation can finish with an evidence-backed recommendation to keep the current design. State that disposition explicitly; do not claim the proposed enhancement was implemented. A request for a specific implemented outcome remains incomplete unless that outcome is met or the user changes it.
