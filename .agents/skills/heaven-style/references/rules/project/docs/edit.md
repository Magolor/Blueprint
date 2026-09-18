---
name: project-docs-edit
description: Read before applying a correction or changed decision to existing documentation.
---

# Integrate documentation corrections

## Summary

A correction updates the current explanation; it does not become the page’s subject. First identify the page’s audience, purpose, and main outcome. Apply the accepted behavior consistently across affected claims, code, examples, and projections. Scale the visible edit to its importance in that document.

## Current documentation

Current user guides, overviews, demos, API documentation, docstrings, and comments describe the supported behavior in context. Remove the obsolete claim and incidental references to it. Write the accepted behavior as the current design, even when it resulted from a correction, a missed requirement, or a changed decision. Do not add apologies, correction warnings, user-instruction reminders, defenses of the new choice, rejected alternatives, or “previously/now” narration.

Explain rationale only when readers need the current constraint to use, maintain, or review the system. State that constraint directly instead of retelling the conversation that revealed it. A historical comparison belongs only in an artifact whose purpose is migration, decision rationale, investigation, or change history.

## Preserve purpose and emphasis

Scale an edit to its importance in the artifact. When a minor change affects one claim, example, or review detail, update that location and any directly dependent text. Do not rewrite the summary, add a prominent section, reorganize the page, or substantially expand a PR body unless the change alters the artifact's primary outcome, reader path, review risk, or acceptance evidence.

Introduce the replacement only where it helps the reader's task. Reread the artifact without the latest request in mind: its title, opening, section order, and amount of detail should still emphasize its main subject. A complete diff does not require every small implementation correction to receive equal narrative weight.

## History and support

Record the changed decision and necessary rationale in the development log. Use an existing decision record only for a consequential architectural choice. PRs, investigations, and explicitly historical records can explain the change; current feature documentation does not inherit their emphasis. Do not invent compatibility or migration guidance. Retain it only when an explicit repository support contract or user request requires it, in its appropriate owner.

## Pattern and Anti-pattern

- **Pattern:** A demo’s query API changes. Update the call and its expected result; keep the demo about the workflow it teaches.
- **Anti-pattern:** Add a new section explaining the rejected API and the instruction to stop using it.

A small implementation detail should not take over a user-facing demonstration.

- **Pattern:** In a configuration guide, describe the accepted default where readers choose configuration.
- **Anti-pattern:** Open the guide with “Important: we used A before; always use B instead.”

- **Pattern:** A small validation fix in a larger PR gets one accurate line under Changes and its test under Evidence.
- **Anti-pattern:** Rewrite the PR summary and add a rationale section that makes the validation detail appear to be the PR's main outcome.

After editing, reread the whole artifact without the correction request. Its summary, order, and emphasis should still serve the overall subject. Keep general Pattern/Anti-pattern teaching only when the contrast independently helps readers, not to memorialize a correction.
