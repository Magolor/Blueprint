---
name: code
description: Read before implementing features, fixes, or refactors.
task_kind: code
status: active
---

# Code

## Summary

Implement the authorized behavior through required reading, focused checks, review, and synchronized closeout.

## Procedure

Before even a small local change, complete [required reading](../../rules/project/read.md): the full applicable language tree and shared project rules, including nested pages. Then inspect repository policy and nearby code. Read [broad implementation](slices.md) only for ordered slices or unresolved shared boundaries.

1. Establish the requested behavior, public/data impact, compatibility constraints, acceptance conditions, and non-goals. Read a named issue, plan, or prior review before changing it.
2. Resolve uncertain contracts before implementation. Claim a queue task for resumable, multi-slice, blocked, or independently delegated work; keep detail in one linked plan.
3. Implement and update owned callers. Validate behavior with focused happy, edge, failure, and lifecycle checks where relevant. For a claimed user or agent workflow, exercise a representative path through the supported entry when the task requires it: a CLI command, SDK import, installed artifact, or real tool invocation. A build proves buildability; mocks alone do not establish a working external integration. Report unavailable required evidence.
4. Review the current diff, preserving other work. Fix confirmed defects and rerun affected checks.
5. Run repository closeout gates. Update affected user/engineering docs, examples, generated artifacts, declared sibling projections, development log, and task state. Record incomplete checks or explicit waivers.

Use [special work contracts](../../rules/project/work.md) for experiments, integrations, consumer projects, or permission boundaries. Report changed behavior, verification, and material risks. A local change does not authorize publication.
