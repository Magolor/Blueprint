---
name: template-developer
description: Read before writing a developer integration or extension guide.
---

# Developer guide

## Summary

Explain the engineering task, its place in the system, and the main contract
for a skilled engineer new to the repository.

## Context and contract

Introduce domain terms, caller, responsibility, and dependencies. Explain inputs,
outputs, invariants, lifecycle, and failures that matter to integration; link
the authoritative API for exact members.

## Integrate

Show the smallest supported use or extension path, expected result, and verification.
Explain public identifiers before relying on them. State important limits and
compatibility obligations.

## Design

Explain the relationships, ownership, and data flow needed to maintain or extend
the feature. Include concurrency, performance, or security only where consequential.
Link existing design and code-map owners rather than copying them.

## References

Link prerequisites, API contracts, decisions, and focused verification examples.
