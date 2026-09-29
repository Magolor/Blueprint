---
name: project-docs-check
description: Read before checking documentation consistency or lifecycle.
---

# Documentation checks

## Summary

Verify authoritative claims, generated projections, links, and lifecycle state through their existing owners.

## Enforcement owners

Strong documentation promises need a named fitness function:

- Generated copies: deterministic generator plus exact `--check` comparison. Check mode is read-only, network-free, and does not initialize application/runtime state.
- Cross-repository or persisted projections: a source revision or content digest, explicit non-authoritative status, and a synchronization checkpoint.
- Task queue: schema, unique IDs, state-dependent fields, dependency-cycle, and link validation.
- Development log: one declared surface and deterministic newest-entry rule. A rolling file keeps one explicit order. Separate immutable entries use stable chronological coordinates and one routing rule. If an index lists entries, it is authoritative or generated from them rather than a second manual chronology. When the repository records `Next`, its newest value refers to the active queue or `none`; older entries preserve historical task IDs.
- Scratch: ignored local lane plus tracked-note owner/created/expiry validation.
- Local docs: relative-link and retired-path checks.
- Architecture “must” rules: a focused behavioral test, import/dependency check, generated inventory, or explicit human review owner.
- Current/target claims: source/test evidence and a status audit; a diagram alone is not proof.

Every new validator needs a valid fixture and an invalid fixture that proves the real top-level gate can fail. Prefer focused behavior checks over a large scanner that merely reproduces the repository topology.

## Completion gate

Before declaring docs-impacting work complete:

- [ ] The canonical task source is current; closed work is removed.
- [ ] User docs match shipped public behavior.
- [ ] Engineering docs distinguish current, target, gap, and non-goal.
- [ ] Stable conclusions were promoted from plans, reports, logs, and scratch.
- [ ] The development log records substantial closeout/handoff evidence.
- [ ] Scratch is unexpired or removed.
- [ ] Generated artifacts and README copies pass freshness checks.
- [ ] Local links, navigation, translation state, and repository docs validation pass.
