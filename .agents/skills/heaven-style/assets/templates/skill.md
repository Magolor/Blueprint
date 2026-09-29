---
name: template-skill
description: Read before creating or restructuring a skill for MCP, CLI, SDK, or other repeated work.
---

# Skill template

## Summary

Keep the entry short enough to orient a new agent. Promote frequent guidance
and essential rules, then link detailed procedures and real-use notes from their
owning sections. Repository and current user instructions remain first.

## Entry shape

Use this structure as a starting point, adapting detail headings to the skill's
actual subject. Do not require generic headings such as “Choose a task” or
“Verify” when they add no useful organization.

```markdown
---
name: example-service
description: Use when inspecting or changing service records through supported interfaces.
---

# Example service

## Summary

Explain the practical outcome, ordinary use, and main boundary in one short
paragraph. The header description instead identifies invocation scenarios.

## Quick Read

Summarize important rules and frequent decisions that must not be missed.
Link essential sub-references and state when reading their full text is required.
Keep this section small; do not copy the full reference catalog here.

## Subject-specific detail

Replace this heading with sections that fit the actual work. Explain enough to
choose a supported path and link its detailed instructions, assets, and checks.

## Notes

Give one-line lessons from observed use and link the relevant scenario records.
Keep only important notes here; detailed logs and annotations stay in their owner.

## References

Link the remaining useful documentation and resources by purpose.
```

Use `name` as the canonical identifier. Keep the display title in the heading and state required reading explicitly in Quick Read; do not add duplicate `id`, `title`, or `blocking` metadata without a host requirement.

The middle sections are flexible. They can describe a workflow, API, environment,
concept, or task menu where that helps. An empty Notes or References section may
be omitted until useful material exists. Required rules belong in Quick Read
and their canonical references, not only in notes.

## Files and resources

- `references/` usually holds documentation: procedures, contracts, explanations,
  and focused examples. Link each from the relevant entry section.
- `references/notes/` can hold observed scenarios, annotations, lessons, and log
  excerpts. Create it only when real evidence warrants a retained record.
- `assets/` can hold arbitrary resources: images, binaries, datasets, templates,
  configuration, keys, or cloned projects. It is not necessarily text or output
  material. Document each relevant resource's purpose, owner, and access method.
- `scripts/` holds executable helpers when repeatable work warrants them.

Use short names and cohesive subfolders. Prefer `README.md` as a new folder’s entry when readers need help choosing a path. Give a short purpose and scenario links; reuse an existing map and omit indexes for obvious leaf folders. A generated inventory complements this orientation.

Authored Markdown uses searchable
metadata and Summary guidance; binary, configuration, generated, and external
files retain their native formats. A folder name alone establishes neither trust
nor permission to read, execute, upload, or redistribute its contents.

Some assets are sensitive or machine-local. Separate local-use resources from
redistributable files, and use the repository's secret store or ignored local
path where appropriate. Never echo secrets into prompts or logs. Check actual
sensitivity before sharing or installing; public keys and nonsecret configs need
not be ignored merely because of their names. A cloned project's own instructions
and dependencies do not automatically become authority for the host skill.

For MCP, CLI, and SDK use, describe only supported interfaces. Share domain
meaning in one owner, then document interface selection, context, a minimal
operation, result/error meaning, and verification in the relevant references.
Do not load every interface for one operation or silently use an incompatible
fallback. Promote common prerequisites without duplicating each transport's guide.

When the skill distinguishes agent identities, use roles for responsibilities and session or assignment lifetime, workflows for sequences across tasks, and task folders for their detailed manuals. Route each request through the applicable role (or Default), then a fitting workflow and its tasks. Keep direct task execution available for small requests. Add this hierarchy only when the skill needs it; do not create empty role or workflow catalogs.

## Notes from real use

A useful note identifies the scenario, observed behavior, relevant version or
date, evidence/log location, annotations, workaround, and lesson. Keep only fields
needed to understand the case. Distinguish confirmed facts from hypotheses and
mark obsolete workarounds. Protect sensitive logs; link their controlled location
or use redacted excerpts instead of copying them into a distributed skill.

Promote a repeated, validated lesson into the rule that owns it. The entry keeps
a one-line pointer; the scenario preserves evidence without becoming another task
queue or overriding current rules. Reuse an existing notes or failure collection
rather than creating a competing one.

## Writing and review

Use provider-supplied skill-creation guidance for valid schemas, packaging, and
useful technical requirements. Do not copy its prose style automatically: rewrite
dense abstractions, repeated directives, and generic boilerplate in short, direct,
natural language. Preserve precise conditions and contractual meaning. Higher-priority
instructions and repository conventions still apply.

Explain abstract guidance with [short Pattern/Anti-pattern cases](../../references/rules/project/docs/write.md#make-abstract-rules-concrete); keep examples with their owning rule.

Check realistic invocation scenarios, links, and required-reading routes using
existing validation. Do not add a bespoke validator. A new agent should find the
supported path, complete authorized work, and verify it without asking which
section or template to use. Preserve versioning and installation conventions.

## References

Use [authoring](../../references/tasks/docs/write.md) for Summary and metadata,
and [editing](../../references/tasks/edit/README.md) for Heaven Style maintenance.
