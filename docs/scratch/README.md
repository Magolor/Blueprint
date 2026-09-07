# Scratch Notes

Use this folder only for short-lived requirements, brainstorms, rough comparisons, or design questions that another maintainer may need before a decision is accepted.

Pure local slop belongs in ignored `.temp/notes/` or `docs/scratch/local/`. A tracked Markdown note must start with:

```yaml
---
status: scratch
created: 2026-07-21
expires: 2026-08-20
task: PROJECT-001
---
```

The expiry may be at most 45 days after creation. Before it expires, either promote the durable conclusion into user or engineering documentation and delete the note, or delete it without promotion. Scratch is never an authority source.
