# Assets

Static bundles for agents (not loaded unless needed). Target-project evidence stays outside the distributed skill.

## default-glossary.md

Bundled en–zh terminology table for doc-sync and doc-trans.
Project glossary files take precedence (`_docs-guide/terminology.md`, `reference/glossary.mdx`); when those are absent, use this fallback.

## MacOS-env.md

Shared macOS setup-maintenance playbook for package-manager ownership, update commands, Docker database caution, and host-environment guardrails.

## instance/

Ignored `*.local.md` files contain non-secret machine notes for local agent sessions. Do not commit host identity, user paths, hardware inventory, or private infrastructure topology.

Generate a local machine note from the skill root:

```bash
python scripts/machine.py
```

The skill index excludes local instance notes.

## Local evidence

Inspect target and reference repositories at their own locations. Do not package their source, project names, observed tool versions, architecture, or release coupling into this skill. Optional maintainer caches ending in `-reference/` are ignored and excluded from installation; `install.py` performs no network or reference-project synchronization.
