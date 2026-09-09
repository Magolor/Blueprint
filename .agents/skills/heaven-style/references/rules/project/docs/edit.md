---
name: project-docs-edit
description: Read before applying a correction or changed decision to existing documentation.
---

# Integrate documentation corrections

## Summary

A correction updates the current explanation; it does not become the page’s subject. First identify the page’s audience, purpose, and main outcome. Apply the accepted behavior consistently across affected claims, code, examples, and projections. Scale the visible edit to its importance in that document.

## Current documentation

Current user guides, overviews, and demos describe the supported behavior in context. Remove the obsolete claim and incidental references to it. Do not add correction warnings, user-instruction reminders, rejected alternatives, or “previously/now” narration. Introduce the replacement only where it helps the reader’s task; do not insert an isolated explanation simply because it was the latest request.

## History and support

Record the changed decision and necessary rationale in the development log. Use an existing decision record only for a consequential architectural choice. PRs, investigations, and explicitly historical records can explain the change; current feature documentation does not inherit their emphasis. Do not invent compatibility or migration guidance. Retain it only when an explicit repository support contract or user request requires it, in its appropriate owner.

## Pattern and Anti-pattern

- **Pattern:** A demo’s query API changes. Update the call and its expected result; keep the demo about the workflow it teaches.
- **Anti-pattern:** Add a new section explaining the rejected API and the instruction to stop using it.

A small implementation detail should not take over a user-facing demonstration.

- **Pattern:** In a configuration guide, describe the accepted default where readers choose configuration.
- **Anti-pattern:** Open the guide with “Important: we used A before; always use B instead.”

After editing, reread the whole page without the correction request. Its summary, order, and emphasis should still serve the overall subject. Keep general Pattern/Anti-pattern teaching only when the contrast independently helps readers, not to memorialize a correction.

