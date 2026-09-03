---
id: doc-sync
task_kind: doc-sync
status: active
enabled: true
order: 30
keywords: [write docs, create docs, review docs, audit docs, restructure docs, sync docs, update docs, YAML frontmatter, controlled technical English, canonical docs, generated docs, navigation, documentation task]
triggers: [write docs, create documentation, review documentation, audit documentation, restructure docs, doc sync, update documentation, docs out of date, sync generated docs]
description: Use when creating, restructuring, reviewing, auditing, or syncing canonical authored documentation, generated pages or contracts, navigation, examples, or declared sibling projections.
related_rules: [overview, docs, test, extension]
---

# Documentation Writing and Sync Task

## Goal

Create and maintain user and engineering documentation that is accurate, audience-shaped, navigable, source-backed, and consistent with the repository's professional TypeScript or Python surface.

## Sources

1. Read the target repository's `AGENTS.md`, docs guide, docs navigation/configuration, authority map, target page, and nearby pages.
2. Identify the canonical source, target audience and outcome, and every declared generated or sibling projection. Do not guess synchronization relationships from similar filenames.
3. Resolve terminology from the repository's documentation or product glossary when present. The bundled English–Chinese glossary is a translation fallback, not an English authoring standard.
4. Read nearby pages to match voice, YAML metadata, headings, examples, components, and navigation.
5. Verify behavior against code, tests, generated artifacts, and executable examples. Label accepted targets and known gaps; do not claim planned behavior as shipped.
6. If the docs platform has a dedicated installed skill, use it for current components, configuration, and validation commands.

## Scope

- Handle authored Markdown/MDX creation, revision, restructuring, and evidence-based review as well as synchronization after code changes.
- Default to the repository's canonical language unless the user requests translation; existing Heaven workflows use canonical English when the repository does not declare another authority.
- Regenerate declared copies rather than editing generated files by hand.
- Report translations or sibling projections that became stale but are outside the requested scope.
- Use [doc translation](doc-trans.md) only when line-aligned Chinese translation is explicitly requested or repository policy already requires atomic pair updates.
- Keep content synchronization separate from website deployment or publication unless the user explicitly requests both.

## Writing criteria

- Follow the repository's page structure and YAML frontmatter contract. For authored bilingual pages, apply the metadata and line-alignment requirements in [doc translation](doc-trans.md).
- Define the reader's starting state, intended outcome, likely failure and recovery path, and next useful depth before drafting details.
- Explain what a concept enables before setup steps or commands. Progress from the shortest safe user path through advanced operation to concept-level developer detail; link exact API, schema, or inventory owners instead of restating them.
- Use second person where it clarifies an instruction, active voice when the actor matters, precise claims, and realistic examples.
- Apply the non-certified ASD-STE100-inspired pass in [documentation and task lifecycle](../rules/project/docs.md#controlled-technical-english): stable terms, direct verbs, separated instructions and conditions, and unchanged modality and exceptions.
- Keep code fences language-tagged and test examples when practical.
- In TypeScript documentation, use strict, production-valid examples through supported package entry points. Keep promise, cancellation, resource, runtime, and ESM ownership consistent with the matched `ts-*` rules; do not import Python-only documentation mechanics.
- Use the repository's internal-link convention and update navigation when pages move or are added.
- Keep current behavior, accepted target, known gap, and non-goal distinct.
- Prefer generated API/config/schema/catalog material when repeated manual copies have drifted.
- Do not impose a universal document kind, template, fixed heading sequence, word budget, pairing sidecar, checksum, website manifest, or CI command. The target repository must own any such mechanism.

## Workflow

1. Classify the page by primary reader and job, then identify the required outcome, public contracts, examples, and architecture claims.
2. Map each material claim to its one canonical owner and choose verification proportional to its risk.
3. Draft or revise the canonical page using the repository format and the authored-document standard in [the project docs rule](../rules/project/docs.md#authored-document-standard).
4. Run safe commands, configurations, and examples exactly as documented when the required environment is available. Label anything that remains unverified and name its verification owner.
5. Regenerate declared copies, schemas, catalogs, navigation, or sibling projections through repository commands.
6. Remove or supersede contradictory legacy pages and broken navigation in the same change.
7. Run repository docs, link, snippet, schema, and build checks appropriate to the changed surface.
8. Re-read the complete page for factual completeness, then for brevity, navigation, ownership, and controlled technical English.
9. Report canonical files, generated outputs, stale out-of-scope projections, verification, and any unverified claims.

## Avoid

- Editing a generated copy while leaving its source stale.
- Treating a plan, report, task queue, or development log as permanent API authority.
- Copying one docs platform's page template into repositories that use another.
- Copying a reference repository's package taxonomy, template set, pair-state records, or publication pipeline into an unrelated project.
- Synchronizing unrelated sibling repositories merely because they share a product name.
- Translating during ordinary canonical-source sync without explicit scope or a repository-owned atomic-pair requirement.
- Expanding TSDoc, Python docstring, or inline-comment coverage through a page-writing rule; use the language-specific API documentation owner.
