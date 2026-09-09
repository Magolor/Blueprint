---
name: workflow-architect
description: Select architecture discovery and design deliverables.
audience: architect
---

# Architecture work

## Summary

The architect defines component responsibilities and the smallest usable public
contract. Give implementers a compact object protocol and an accepted plan.
The manager coordinates assignments, reviews, and integration.

## Establish the design

Use this route for design and documentation before implementation. Read the [design philosophy](../../design/philosophy/README.md). Start from the repository mental model, goals, status, constraints, and reasons for change, then narrow to affected boundaries. One file or ticket is insufficient evidence for a system-wide conclusion.

Use [architecture checks](README.md) for change pressure, smells, dependency direction, and feedback gates. Before any architecture task, complete [required reading](../../rules/project/read.md), including the full target-language and project rules, every design manual below, and all code-design comparisons. The table selects output shape, not which guidance may be skipped. Keep an accepted design distinct from shipped behavior.

| Deliverable | Read |
| --- | --- |
| Idea, intuition, and architectural shape | [Design template](../../../assets/templates/design.md) |
| Choice and rationale | [Decision template](../../../assets/templates/decision.md) |
| Current-state brief or unfamiliar repository | [Discovery](inspect.md) |
| Module, extension, or API contract | [Module design](module.md) |
| Refactor or ordered execution | [Plan](plan.md) |
| Periodic health review | [Review](review.md) |
| Goals or linked tracker alignment | [Goals](goals.md) |
| Documentation hierarchy or cleanup | [Docs](docs.md) |

Before handoff, make public contracts, ownership, non-goals, migration, verification, feedback points, and risk explicit. Each slice must be understandable and testable by another engineer or agent. Match documentation and issue updates to the accepted scope.

## Make the decision concrete

Apply [independent judgment](../../rules/project/work.md#interpret-intent-and-exercise-judgment) to the proposed mechanism. State the user scenario, the smallest public contract that serves it, and the decisive tradeoff against the relevant alternative. Inspect existing owners before adding a class, wrapper, registry, or configuration layer. Keep a useful utility usable on its own when its contract does not require the larger system.

Unify responsibilities that share semantics; retain differences justified by lifecycle or workload. Demonstrate that supplied examples fit the mechanism without hard-coding their incidental details. A new dependency or reference design may justify no further change. Recommend that outcome when it best meets the goal.

Return a choice and its reasons, not only a catalog of possibilities. Record any consequential unresolved assumption and the next authorized action. Do not replace a short reviewable decision with a full implementation before its scope is settled.

## Acceptance and handoff

Each component has one [compact protocol](module.md#component-protocol)
with attributes, method signatures, and short implementation obligations.
Keep the public class count small. Separate internal responsibilities without
making callers assemble private objects. A class must earn its public role.

Start with a short [plan brief](plan.md#plan-brief). Expand confirmed
scope into execution details. Hand off the linked files through the
[file-based procedure](../coordinate/handoff.md), not only through chat.

Report evidence, artifacts, decisions/findings, verification expectations, waivers, and handoff. Route implementation to [code](../code/README.md), newcomer explanation to [explain](../explain.md), shipped-doc sync to [docs](../docs/README.md), and coordination to [manager](../coordinate/README.md).
