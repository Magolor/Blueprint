---
name: task-address
description: Read before fixing confirmed review findings or reported defects.
---

# Address issues

## Summary

Resolve confirmed issues through their owning contracts with the smallest coherent change. Preserve unrelated behavior and verify the actual failure path.

## Procedure

Use [triage](triage.md) when the finding is not yet confirmed. Establish expected behavior and existing fix authority. Read the [code task](code/README.md) for implementation or [compose docs](docs/README.md) for prose corrections.

Fix the cause at the appropriate boundary, updating affected owned callers together. Inspect sibling cases to determine whether the cause is shared before widening the edit. Prefer a general solution for supported inputs over a special case for the reported sample. Keep validation at meaningful boundaries and avoid speculative defensive scaffolding. Preserve supported contracts and explicit compatibility obligations.

Verify the reported case, relevant sibling behavior, and an unaffected neighboring path when scope leakage is plausible. A local color correction must not silently change every screen sharing the same style. A shared parser defect should be fixed in parsing rather than by recognizing the sample string. These are boundary examples, not a fixed test quota.

Run focused regression checks and required gates. Record the candidate revision, evidence, and finding disposition; return it to the reviewer for verification. Route changed claims to [sync](sync/README.md). Do not silently resolve a finding merely because its code changed.

## Acceptance

The confirmed failure is resolved with evidence, affected behavior remains supported, and the reviewer can verify the candidate. Unresolved items retain their severity and next condition. A review-only assignment reports findings without entering this task unless fixes are authorized.
