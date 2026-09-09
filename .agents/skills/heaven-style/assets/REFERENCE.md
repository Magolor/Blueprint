---
name: assets
description: Read when selecting skill assets for the current task.
---

# Assets

## Summary

Load only resources needed for the current task. Assets can be textual or
nontextual resources, including configuration and local reference material;
their folder does not determine sensitivity or redistribution rights.

## Distribution boundary

This Heaven Style distribution ships reviewed portable resources. Its installer
copies ordinary assets, so keep secrets and unapproved private material outside
that distributed tree. Local reference caches use the exclusions documented below.
This is Heaven Style packaging policy, not a universal restriction on what another
skill may keep in its local assets directory.

## Artifact templates

[templates/index.md](templates/index.md) selects reusable document, PR, issue, evidence, and devlog templates. Load only the template for the requested artifact.

## Translation terminology

[default-glossary.md](default-glossary.md) provides the English–Chinese fallback
for doc-sync and doc-trans. Project glossary files take precedence, including
`_docs-guide/terminology.md` and `reference/glossary.mdx`.

## Environment guidance

[MacOS-env.md](MacOS-env.md) defines setup ownership, missing-information recovery,
project/host boundaries, and stateful-service guardrails.
[instance/README.md](instance/README.md) routes to the selected setup and reviewed
non-secret machine/Docker notes. These notes may be tracked. They do not prove
that a later session runs on the same machine or configuration.

Generate observations from the skill root with a known-good Python:

```bash
rtk python3 scripts/machine.py
```

The default report is outside the skill at `~/.config/heaven-style/machine.md`.
Use `--output <path>` for an intentional reviewed snapshot. Credentials and
transient probe dumps stay outside Git and outside the distributed skill.

## Local evidence

Inspect target and reference repositories at their own locations. Do not package
their source, project names, observed tool versions, architecture, or release
coupling into this skill. The user-selected setup locator is a scoped personal
reference, not a product architecture dependency. Optional maintainer caches
ending in `-reference/` remain ignored and excluded from installation.
`install.py` performs no network or reference-project synchronization.
