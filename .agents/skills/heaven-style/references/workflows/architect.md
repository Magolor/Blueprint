---
id: workflow-architect
title: Architect workflow
audience: architect
description: Select architecture discovery and design deliverables.
---

# Architecture work

## Summary

The architect defines component responsibilities and the smallest usable public
contract. Give implementers a compact object protocol and an accepted plan.
The manager coordinates assignments, reviews, and integration.

## Establish the design

Use this route for design and documentation before implementation. Read the [design philosophy](../design/philosophy.md). Start from the repository mental model, goals, status, constraints, and reasons for change, then narrow to affected boundaries. One file or ticket is insufficient evidence for a system-wide conclusion.

Use [architecture checks](../tasks/design.md) for change pressure, smells, dependency direction, and feedback gates. Before any architecture task, complete [required reading](read.md), including the full target-language and project rules, every design workflow below, and all code-design comparisons. The table selects output shape, not which guidance may be skipped. Keep an accepted design distinct from shipped behavior.

| Deliverable | Read |
| --- | --- |
| Current-state brief or unfamiliar repository | [Discovery](design/inspect.md) |
| Module, extension, or API contract | [Module design](design/module.md) |
| Refactor or ordered execution | [Plan](design/plan.md) |
| Periodic health review | [Review](design/review.md) |
| Goals or linked tracker alignment | [Goals](design/goals.md) |
| Documentation hierarchy or cleanup | [Docs](design/docs.md) |

Before handoff, make public contracts, ownership, non-goals, migration, verification, feedback points, and risk explicit. Each slice must be understandable and testable by another engineer or agent. Match documentation and issue updates to the accepted scope.

## Acceptance and handoff

Each component has one [compact protocol](design/module.md#component-protocol)
with attributes, method signatures, and short implementation obligations.
Keep the public class count small. Separate internal responsibilities without
making callers assemble private objects. A class must earn its public role.

Start with a short [plan brief](design/plan.md#plan-brief). Expand confirmed
scope into execution details. Hand off the linked files through the
[file-based procedure](dispatch.md), not only through chat.

Report evidence, artifacts, decisions/findings, verification expectations, waivers, and handoff. Route implementation to [code](../tasks/code.md), newcomer explanation to [explain](../tasks/explain.md), shipped-doc sync to [docs](../tasks/docs.md), and coordination to [manager](../tasks/manager.md).
