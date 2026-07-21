---
id: manager
task_kind: manager
status: active
enabled: true
order: 50
keywords: [project manager, status report, track tasks, triage linear, triage github, orchestrate agents, project status]
triggers: [manager, project status, what's ongoing, stale tasks, next steps, orchestrate, track Linear, track GitHub]
description: Use when tracking GitHub/Linear status, stale work, recent activity, next steps, or multi-agent coordination.
related_rules: [overview, review, docs, test]
---

# Manager Task

## Goal

Maintain an operational view from the repository's declared task authority, then propose or coordinate the next useful work. Operational repositories have exactly one; template-source repositories may instead declare direct requests or one external tracker and keep consumer queue starters inert. GitHub and Linear are linked evidence or explicit mirrors unless repository policy selects one of them as the sole writable authority.

## Sources

1. Read repo `AGENTS.md`, determine whether it is operational or a template source, and resolve its declared task authority before interpreting goals, plans, reports, logs, GitHub, or Linear as work state.
2. Read current branch, `git status`, recent commits, CI/check status, the docs authority map, development log, and active tasks when an operational authority exists.
3. Use GitHub tools or `gh` for linked PRs, branches, issues, checks, reviews, and recent activity; use Linear for linked project/cycle/issue evidence.
4. If a connector/MCP auth fails repeatedly, use [../failures/auth-secrets.md](../failures/auth-secrets.md) and fall back to direct API paths when possible.
5. If Linear issue creation is blocked by project pressure, or a continuous issue has accumulated too many routine comments, use [../failures/linear-pressure.md](../failures/linear-pressure.md).
6. Never expose secrets, tokens, or private auth details in status reports.

## Status Analysis

Classify work into:

- Ongoing: active tasks from the declared authority, their linked branches/plans/issues/PRs, recent commits, or active review threads.
- Recent: tasks completed or materially changed in the selected lookback window.
- Stale: no recent activity, blocked status, failing checks, old review comments, unclear owner, missing acceptance criteria, or docs/test sync gaps.
- Risk: issues with ambiguous scope, hidden dependencies, stale docs, unverified fixes, auth/env blockers, or too-large PRs.
- Next steps: concrete actions with owner, target artifact, verification, and suggested task route.

When evidence disagrees, the declared authority owns coordination state; code/tests own shipped behavior. Do not merge multiple trackers into a new shadow list or turn a template starter into live state.

## Orchestration Authority

- The manager may update the operational repository's canonical authority within repository/user authorization. It may create or update GitHub/Linear mirrors only when the user or repository policy authorizes that external write. It must not activate a template-source queue starter.
- For continuous Linear issues, the manager should maintain one rolling status comment and edit it for routine progress, verification, and next steps. Do not pile up new comments unless the update is a distinct decision, blocker, handoff, or explicitly requested separate note.
- The manager may move Linear issues up to `In Review` when implementation evidence and review readiness are clear.
- The manager must not set Linear issues to `Done` unless the user explicitly instructs it or explicitly grants that authority for the current run.
- The manager may spawn or propose subagents when available. Use narrow prompts and clear task routes such as `code -> code-review -> doc-sync -> doc-trans -> code-explain`.
- The manager should monitor spawned work by collecting artifacts, verification output, review findings, docs updates, and Linear/GitHub status changes before reporting completion.

## Workflow

1. Resolve scope: project, repository role, canonical task authority if any, linked Linear/GitHub scope, and lookback window.
2. Gather the declared authority first when one exists, then current GitHub/Linear evidence. Prefer live connector data for external state and local git/code/docs for repository state.
3. Cross-check queue, code, docs, GitHub, and Linear claims for mismatch.
4. Identify ongoing, recent, stale, blocked, and risky items.
5. Propose next steps in priority order. Include which task playbook should execute each step.
6. Update the canonical operational authority first. For a template source without one, preserve direct-request evidence or make only authorized external-tracker updates. State every update made.
7. If orchestrating agents, launch or propose the smallest useful chain, then monitor until each handoff has an artifact or explicit blocker.

## Report Format

Use concise sections:

- Scope and data sources.
- Ongoing work.
- Recent changes.
- Stale or blocked work.
- Risks and mismatches.
- Recommended next steps.
- Linear/GitHub updates made, including whether an existing rolling Linear comment was edited or a separate comment was intentionally added.
- Agent workflow started or proposed.
