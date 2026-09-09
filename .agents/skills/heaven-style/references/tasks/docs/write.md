---
name: project-docs-author
description: Read before creating or revising PRs, issues, comments, docs, or reports.
---

# Author artifacts

## Summary

Use this manual when creating or substantively editing PRs, issues, comments,
docs, or reports. User instructions and repository rules take precedence;
apply Heaven Style wherever they do not conflict.

## Start autonomously

1. Read the target repository's authoring policy, existing template, language,
   glossary, and affected canonical document. Use its established format first.
2. Choose the matching [template](../../../assets/templates/index.md). Read only
   that template and its applicable conditional guidance. For an edit, preserve
   the existing structure unless the task calls for a rewrite.
3. Infer routine language, headings, and detail choices from these owners and
   the intended reader. Proceed within the authorized task; do not ask for
   template approval. Resolve missing facts from evidence; state remaining gaps.

## Language and titles

Use the project's language for titles, bodies, and comments. If undeclared,
follow its maintained audience-facing docs; otherwise default to English.
Translate naturally and preserve identifiers and command syntax. Add translations
only when required or requested.

Use the project's PR title convention. The fallback is `type(scope): outcome`,
with optional scope and types such as `feat`, `bugfix`, `refactor`, `ui`, `docs`,
`test`, `perf`, `build`, `ci`, or `chore`; use `fix` when repository tooling expects
it. Name the final outcome and revise the body when scope changes. Issues may
use the same convention or a direct problem/question title.

## Required opening Summary

Every authored document starts its body with an explicit `## Summary` section
after YAML, the title, and any required language switcher. PR and issue bodies
also start with `## Summary`; their platform title needs no duplicate H1.
Use the natural equivalent heading in another language. Existing repository,
generated, and parser-owned formats take precedence. Short conversational
comments need an opening conclusion, not document headings.

Write one short paragraph, normally one to three sentences. Below 200 English
words is a soft recommendation; Chinese uses comparable natural brevity without
a numeric limit. Explain the reader's outcome and important boundary. The YAML
description is for finding the page and never replaces this summary.

## Searchable YAML

For new or substantially revised Markdown files, recommend a skill-style YAML
header with at least `name` and `description`, unless the repository's format
specifies otherwise. Use `name` as the single canonical identifier; do not duplicate it in `id` or repeat the document heading in a `title` field unless a repository consumer requires those fields. Keep required-reading instructions in the body and its entry route. Use a short stable name and a description that says **when
to read or invoke this material**, with the task, scenario, or trigger words a
reader would search for. Do not summarize the argument, contents, or philosophy.

```yaml
name: authoring
description: Read before creating documents, PRs, issues, skills, or reports.
```

A description such as “This document contains rules and norms for documentation”
does not identify a useful trigger. Put its substantive explanation in Summary.
Optional structured fields such as `project`, `tags`, or other useful context may
extend document headers under repository policy; no fixed taxonomy is required.
For actual skills, follow the host's supported schema and put extra fields in
`metadata` when required. Preserve stable identifier values and metadata consumers during a coordinated schema migration. Do not
replace translation sidecars or add a validator. This recommendation does not
require an unrelated corpus rewrite.

PRs, issues, and comments entered in a platform UI need no YAML. A Markdown file
storing their reusable template has its own searchable header; omit that template
metadata from the posted body. Generated files follow their generator's schema.

## Explain the reader's outcome

Explain capability, when it helps, and the consequential boundary. In PRs, issues,
and change reports, locate the feature and system responsibility, then explain
the trigger, cause, and before/after behavior. Current guides and demos follow
[correction integration](../../rules/project/docs/edit.md): describe accepted behavior in context, with emphasis proportional to the page’s purpose. Treat an unfamiliar developer as a skilled engineer
new to this repository. Introduce a symbol through its purpose; do not open with
an unexplained function name or internal inventory.

For example: “Quoted spaces split one CLI argument into several values. The
argument parser, `parseInput`, now preserves quoted groups.” This is an
illustrative explanation, not a claim about a particular product.

User instructions come before developer-only architecture or implementation.
Developer-focused docs start with the engineering task. Keep PRs and issues
self-contained but link extensive tutorials, designs, protocols, and reports.
Source identifiers belong in summaries only when readers use them directly.

## Structure and accuracy

Use the selected template's core sections in order. Conditional sections apply
only when their stated trigger holds. Add relevant subsections; remove prompts
and empty optional sections. Keep a short artifact short: avoid repeating its
summary under each heading. Translate headings without changing their jobs.

For abstract rules, use concise [Pattern/Anti-pattern cases](../../rules/project/docs/write.md#make-abstract-rules-concrete) when they clarify application.

Use the shared [language rules](../../rules/project/language.md) and [claim verification](../../rules/project/docs/prose.md).
Preserve conditions, quantities, exceptions, uncertainty, and required compatibility.
Separate shipped behavior, accepted target, proposals, and historical evidence.
A file observation, for example, does not necessarily mean a file changed.

Keep essential use, limits, and evidence visible. Fold optional technical detail
with named `<details>` blocks where supported. Put further reading in References;
keep citations beside claims and prefer maintained same-language links. Omit an
empty References section rather than inventing sources.

Comments need no template: lead with the finding, answer, or question, then
provide enough context, evidence, and next action. Separate blockers from
suggestions. Use the existing task, log, and scratch owners; do not append an
unrestricted log or parallel queue. Preparing an artifact does not authorize
publishing it. Add no word-count or template validators.
