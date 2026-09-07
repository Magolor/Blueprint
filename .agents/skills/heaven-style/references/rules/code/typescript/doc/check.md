---
id: ts-doc-check
title: TypeScript API documentation checks
description: Read for TypeScript api documentation checks.
blocking: true
---

# TypeScript API documentation checks

## One authoritative home

- Give each durable fact one source of truth. Link to the owning type/schema/config page instead of copying tables into multiple READMEs.
- Generate catalogs, module graphs, event lists, config references, or API inventories from source when repeated manual sync has caused drift.
- Generated artifacts have a regeneration command and a check mode that fails when stale.
- Documentation describes the current contract, not the chronology of how it changed. Put historical decisions in ADRs, release notes, or progress reports.
- Planned behavior is labeled planned and does not appear in current API reference/examples.

## Examples and snippets

- Public examples import through the package's supported entry point, not source aliases or internal modules.
- Typecheck documentation snippets when the repository has enough examples for drift to be a recurring risk.
- Run important examples or smoke them against built/packed output before release.
- Use realistic values without real credentials or secret-shaped placeholders that users may copy into commits.
- Keep generated/runtime example output in the repository's declared temp path.
- If an example demonstrates an optional integration, name the install/config prerequisite and expected failure when absent.

## Mechanical gates

For a published library or large extension SDK, add narrow gates when they enforce real standing promises:

- `/** ... */` appears only in reviewed public-source locations and non-public code uses `//` for implementation comments;
- exported symbols have description prose and explicit function return types;
- package exports match declarations and built files;
- checked snippets compile;
- generated API/config/event catalogs are current;
- links and package subpaths resolve;
- a clean consumer imports the public surface.

Do not impose module-level TSDoc on every file, a word budget, documentation for mechanically obvious re-exports, or a custom documentation generator without demonstrated maintenance pressure. A gate can verify comment location and delimiter use. Code review must determine whether prose adds caller-relevant meaning.

## Suppressions and waivers

- Documentation/lint/type escapes are line- or symbol-scoped and include why the invariant remains safe.
- A public symbol omitted from docs has a deliberate reason such as framework protocol inheritance, generated heritage, or an internal-marked export.
- Do not disable export documentation for an entire package because one generated symbol is awkward; add a narrow allowlist and a removal condition.
