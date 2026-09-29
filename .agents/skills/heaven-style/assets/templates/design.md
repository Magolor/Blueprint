---
name: template-design
description: Read before explaining a new idea, intuition, or architecture.
---

# Design

## Summary

Summarize the idea, its intuition, and the architectural outcome. Identify its
status using repository conventions; an idea can stand before implementation
is authorized.

## Motivation

Explain the reader's problem or tension and the system context. State why a
different mental model would help.

## Idea and architecture

Explain the insight through a small scenario, then describe the smallest public
model, responsibilities, relationships, and essential flow. Use a diagram or
conceptual protocol when it clarifies the idea. Link detailed contracts instead
of enumerating signatures, file edits, or algorithms.

## Tradeoffs and boundaries

Explain invariants, alternatives, costs, and non-goals. Discuss lifecycle,
failure, state ownership, and extension boundaries where they affect the idea.
State assumptions and unresolved questions, including evidence that could
change the design. Do not turn this section into an execution checklist.

## References

Link the architecture, evidence, and any decision record. A separate plan owns
implementation slices, acceptance, migration, and rollout when those are needed.
