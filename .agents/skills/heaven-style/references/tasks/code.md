---
id: code
task_kind: code
status: active
description: Implement features, fixes, refactors, experiments, or integrations.
---

# Code

Before even a small local change, complete [required reading](../workflows/read.md): the full applicable language tree and shared project rules, including nested pages. Then inspect repository policy and nearby code. Read [broad implementation](../workflows/developer.md) only for ordered slices or unresolved shared boundaries.

1. Establish the requested behavior, public/data impact, compatibility constraints, acceptance conditions, and non-goals. Read a named issue, plan, or prior review before changing it.
2. Resolve uncertain contracts before implementation. Claim a queue task for resumable, multi-slice, blocked, or independently delegated work; keep detail in one linked plan.
3. Implement and update owned callers. Validate behavior with focused happy, edge, failure, and lifecycle checks where relevant. Use a probe or demo for user-facing or integration-heavy paths when useful or required.
4. Review the current diff, preserving other work. Fix confirmed defects and rerun affected checks.
5. Run repository closeout gates. Update affected user/engineering docs, examples, generated artifacts, declared sibling projections, development log, and task state. Record incomplete checks or explicit waivers.

Use [special work contracts](../workflows/work.md) for experiments, integrations, consumer projects, or permission boundaries. Report changed behavior, verification, and material risks. A local change does not authorize publication.
