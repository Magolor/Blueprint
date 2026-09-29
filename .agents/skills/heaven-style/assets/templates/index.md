---
name: template-index
description: Read when selecting a template for a document, PR, issue, skill, or report.
---

# Artifact templates

## Summary

Repository rules, formats, and templates take precedence. Otherwise use the
[authoring manual](../../references/tasks/docs/write.md) and the matching template
below. Select it from the requested outcome without requiring the user to name it.
For edits, read only the relevant template; do not reformat unrelated content.
If none fits, use the repository format and shared authoring guidance; do not
force an unrelated template or create a new specialization without a need.

## Use a template

Template titles are labels: replace them with the subject, or omit the duplicate
H1 in PR/issue bodies where the platform owns the title. Keep `## Summary` as the first body
section. File templates recommend a
`name` and scenario-focused `description` header; replace their example metadata
for the authored page. Omit file metadata in posted PRs, issues, and comments.
Retain core sections in order, translate their headings naturally,
and include conditional material only when its trigger applies. Remove prompts
and empty References sections; add subsections only for useful detail. The
repository owns metadata and lifecycle, not these examples.

## Templates

| Artifact | Template | Purpose |
| --- | --- | --- |
| Pull request | [PR](pr.md) | Explain behavior and verification; load [GUI](pr/gui.md), [benchmark](pr/bench.md), or [stack](pr/stack.md) guidance when applicable. |
| Issue | [Issue](issue.md) | Locate a problem or request and define its observable resolution. |
| Design | [Design](design.md) | Explain an idea, intuition, and architecture. |
| Skill | [Skill](skill.md) | Build a short SKILL.md with invocation triggers and task-specific references. |
| Decision record | [Decision](decision.md) | Record a choice, alternatives, consequences, and disposition. |
| Execution plan | [Plan](plan.md) | Turn an accepted design into slices, acceptance, and checks. |
| Review | [Review](review.md) | Record findings and verification limits. |
| Survey | [Survey](survey.md) | Compare evidence to support a decision. |
| General report | [Report](report.md) | Explain investigated results and implications. |
| User guide | [User](user.md) | Show safe use, outcomes, and recovery. |
| Developer guide | [Developer](developer.md) | Explain a supported integration to a newcomer. |
| Overview | [Overview](overview.md) | Introduce a small mental model and reading path. |
| Contract reference | [Contract](contract.md) | Specify invariants, semantics, and support status. |
| Architecture check | [Check](check.md) | State one boundary and how to assess it. |
| Source evidence | [Source](source.md) | Pin a reference snapshot and its authority limits. |
| Handoff | [Handoff](handoff.md) | Transfer verified context without creating another queue. |
| Development log | [Devlog](devlog.md) | Record concise change and verification evidence. |
| Runnable tutorial | [Tutorial](tutorial.md) | Reproduce an end-to-end outcome and clean up. |

Choose one artifact per need. A design explains an idea; a decision records a
choice; a plan organizes execution. They can link to existing owners without
requiring three new files. A user guide explains a feature; a tutorial reproduces
one outcome. A review judges a change; a survey compares options; a report records
other investigation. Use the compact devlog or handoff formats for progress.

Read the catalog only while selecting an authoring format. Routine code work
needs none of these templates. New authoring modes can add focused templates
later; this catalog does not yet define academic-paper or website/blog writing.
Templates add no validators, publication authority, or duplicate task/log systems.
