---
name: template-source
description: Read before recording an external source snapshot as evidence.
---

# Source evidence

## Summary

Explain the question this source helps answer and its authority limit.

## Snapshot

Record the locator, inspected revision/release or content digest, date, and
relevant paths. For consumed local edits, record the actual content or hashes;
a dirty worktree's HEAD alone does not identify the evidence.

## Findings and limits

Summarize relevant observations with source locations. Distinguish source claims,
verified behavior, and inference. State conflicts, freshness limits, and valid
uses. Reference checkouts do not become build or runtime dependencies.

## References

Link primary evidence and the consuming design, decision, or survey. Include
retrieval steps only when needed to reproduce the evidence.
