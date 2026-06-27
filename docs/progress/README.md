# Progress

Use this folder for append-only progress notes that help future agents and maintainers resume work.

Progress notes are dated handoff records, not the canonical home for stable architecture, requirements, or reference material. Promote durable conclusions into `docs/resources/`, `docs/goals/`, or shipped docs.

## Organization

Create one folder per day:

```text
docs/progress/YYYY-MM-DD/
```

Each daily folder should contain:

- `README.md`: the append-only daily summary, active context, decisions, verification, blockers, and next steps.
- Optional focused notes for substantial work slices, named with a short slug.

Example:

```text
docs/progress/2026-06-08/
  README.md
  skill-rule-cleanup.md
```

Prefer one daily summary over many scattered status files. Detailed notes are useful only when they preserve decisions, evidence, or handoff context.

## When to Update

Append a progress entry when:

- a major feature, refactor, release, docs sweep, or generated-doc sync starts or closes;
- a plan, report, issue, or PR changes state;
- a decision, blocker, waiver, or verification result matters to future work;
- work is paused or handed off to another agent or human.

Routine one-pass edits do not need progress notes unless they change public behavior or leave useful handoff context.

## Daily README Format

Use this shape for each dated `README.md`:

```markdown
# YYYY-MM-DD Progress

## <Topic>

- Type: feature | refactor | review | survey | docs | release | blocker
- Links: plan/report/issue/PR paths or "none"
- Summary: what changed or what was learned
- Decisions: durable decisions made today
- Verification: commands, checks, demos, or "not run" with reason
- Next: concrete next action or "none"
```

Append new sections as the day evolves. Do not rewrite older entries except for typo, path, or formatting fixes. If an older entry is wrong in substance, add a dated correction section.
