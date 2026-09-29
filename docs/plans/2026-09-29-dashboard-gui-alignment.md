---
name: dashboard-gui-alignment-plan
description: Read while aligning Heaven Style GUI guidance and palette values with Dashboard.
status: Done
created: 2026-09-29
scope: Heaven Style GUI guidance
task: BP-001
---

# Dashboard GUI Alignment Plan

## Summary

Align Heaven Style's six palette values and workbench guidance with Dashboard's accepted GUI template, while keeping repository rules authoritative. Synchronize the exact skill tree to both Blueprint product branches and reinstall the verified skill.

- Status: Done
- Created: 2026-09-29
- Task: BP-001
- Scope: Heaven Style GUI guidance

## Outcome and boundaries

The six palette pages should match Dashboard's `resources/theme-presets.json`; the surrounding guidance should describe its current theme, geometry, typography, localization, and frontend boundary decisions. Keep the skill general enough for other repositories to override via their own policy. Do not change Blueprint or Heaven Style's frozen `0.2.0-alpha.1` version.

## Steps

### Slice 1: Align guide contracts

1. Compare the installed and canonical GUI pages with Dashboard's accepted design and checked-in preset resource.
2. Update the canonical GUI palette pages and the shared theme, color, spacing, motion, element, and stack guidance where a direct mismatch exists.
3. Regenerate the skill index and run its check mode.

Acceptance: all six palette token maps match Dashboard's resource, and affected guide paths remain navigable.

### Slice 2: Distribute and verify

1. Synchronize the tracked skill tree to the Blueprint `python` branch under its branch contract.
2. Run both branch gates, reinstall the skill, and compare the installed tracked files with canonical source.
3. Record verification in `docs/DEVLOG.md`, mark this plan done, and remove the completed queue row.

Acceptance: branch parity, required checks, and installed-copy comparison pass; any unverified step is recorded explicitly.

## Dependencies and checkpoints

The canonical edit occurs on Blueprint's `typescript` branch. Preserve unrelated changes, including the existing untracked Rust-rule path. Stop the distribution slice if a branch has conflicting work that cannot be preserved safely.

## Closeout

The six palette maps match Dashboard's preset resource. The skill index check, scan, and Python compile passed. `pnpm check` passed on `typescript`, `bash scripts/check.bash full` passed on `python`, and both branches contain the same 207-file tracked skill tree. The global installation matches those 207 files byte for byte. This guidance update did not change a rendered Blueprint GUI, so no visual regression check applies.

## References

- [Heaven Style maintenance](../resources/heaven-style.md)
- [Blueprint maintainer contract](../../BLUEPRINT.md)
- Dashboard `docs/design.md` and `resources/theme-presets.json` in the sibling checkout
