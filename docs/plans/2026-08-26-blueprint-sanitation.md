# Blueprint Sanitation Plan

- Status: Done
- Created: 2026-08-26
- Scope: Complete the common workflow contract and sanitize both Blueprint product lines.
- Task: `BP-006` (closed)
- Links: `docs/reports/reviews/2026-08-26-blueprint-heaven-style-review.md`

## Problem

Blueprint did not define each requested workflow through closeout. Both branches also retained architecture and documentation defects.

## Success criteria

- [x] Each listed workflow has a complete start, resume, verification, and closeout contract.
- [x] Both product lines have small, explicit, tested architecture.
- [x] Canonical documentation passes a non-certified ASD-STE100 Issue 9 review.
- [x] Both complete verification gates pass.
- [x] Each public branch contains one verified root commit.
- [x] The final Heaven Style tree is installed globally.

## Non-goals

- Do not add product features that a starter repository does not need.
- Do not add speculative packages, interfaces, services, or extension systems.
- Do not claim formal ASD-STE100 certification.
- Do not change or remove unrelated external worktrees.

## Slices

### Slice 1: Complete the workflow contract

- Goal: Define every requested work type.
- Touch: Heaven Style workflow references and index.
- Acceptance: Each route has start, resume, evidence, verification, and closeout rules.
- Verification: Run the skill index and dependency scans.
- Docs: Update the skill front door.

### Slice 2: Sanitize the TypeScript line

- Goal: Remove duplicate or weak boundaries.
- Touch: Source, tests, scripts, and canonical docs.
- Acceptance: One public SDK path and one closed CLI grammar remain.
- Verification: Run `rtk pnpm check`.
- Docs: Update the README, engineering guide, audit report, and log.

### Slice 3: Sanitize the Python line

- Goal: Remove ambient runtime coupling and placeholder interfaces.
- Touch: Source, tests, dependencies, scripts, and canonical docs.
- Acceptance: Import is inert and the package owns its configuration and CLI.
- Verification: Run `rtk bash scripts/check.bash full` and `rtk uv build`.
- Docs: Update the README, engineering guide, audit report, and log.

### Slice 4: Publish verified branch snapshots

- Goal: Create and push one root commit per product branch.
- Touch: Local and public Git refs plus the global skill install.
- Acceptance: Public refs match clean verified local refs.
- Verification: Count commits, compare refs and skill trees, then verify the installed version.
- Docs: Record final evidence before the root commits.

## Checkpoints

- 2026-08-26: Confirmed branch scope, remote tips, and explicit publication authority.

## Closeout

- Verification: TypeScript and Python behavior, documentation, formatting, lint, package, skill, history, and public-ref gates pass. Docker verification is waived because the local daemon is stopped.
- Follow-up: None unless a required gate exposes a new defect.
