# Blueprint Maintainer Notes

This file records template-level design decisions for Blueprint itself. It is intentionally outside the downstream project scaffold: `docs/` is the scaffolded documentation tree that new projects should rewrite for their own domain. Keep this file focused on decisions that should remain with Blueprint.

## Dependency Model

Blueprint uses `requirements.txt` and `requirements-dev.txt` as the human-edited source of truth for direct dependencies. We are aware that requirements files are the older, less modern dependency surface compared with inline `pyproject.toml` dependencies. The choice is still intentional: requirements files are the best generalizable source format because they can be reused by the broadest set of Python environment tools without making every tool own a separate dependency list.

The requirements files give Blueprint the simplest portable source format. pip consumes them directly, uv can lock and sync from them, setuptools can expose them through dynamic `pyproject.toml` metadata, conda can use a thin pip-backed environment adapter, Poetry can keep a compatibility lock, and Docker can build dependency layers from the same files. Starting from inline `pyproject.toml` dependencies is a strong default for many Python packages, but for this template it would add export and resolution steps before pip, conda, Poetry, and Docker could share the same clean direct-dependency list.

`pyproject.toml` still remains the package metadata front door. It owns project name, scripts, build backend, classifiers, Python support, and dynamic wiring. Using `pyproject.toml` with requirements-backed dynamic metadata is the comprehensive solution here: modern package metadata stays in `pyproject.toml`, while the reusable dependency source stays in `requirements*.txt`. The lockfiles and environment adapters are generated or validated from the requirements sources; they are not edited as independent dependency authorities.

Keep the requirements sources portable. Normal package specifiers, version bounds, and environment markers are fine. Avoid pip-only options, nested includes, local paths, VCS URLs, hashes, and platform-specific install tricks unless the project has explicitly decided that every supported adapter can handle them.

Docker follows the same rule. The Dockerfile installs runtime dependencies from `requirements.txt`, then installs the project with dependency resolution disabled so the image does not become another package-management surface.

## Harness Support

Blueprint treats repo-local `.agents/skills` and `AGENTS.md` as the canonical, standards-oriented skill surface for templates. Global installs should use one unversioned common skill path, `~/.agents/skills/heaven-style`, with `metadata.version` inside `SKILL.md`; harness-specific copies are avoided by default so Cursor, OpenCode, Kilo, Codex, Copilot, and similar agents do not discover the same skill twice.

Claude Code is the main exception because it does not follow the [AGENTS.md](https://agents.md) protocol by default; it needs a `CLAUDE.md` file with an `@AGENTS.md` import to work. Its plugin marketplace path can expose the same canonical skill without copying it into `~/.claude/skills/heaven-style`. The template-level rule is therefore to prefer shared standards paths and thin harness bridges, and only add per-harness files when a concrete project has a tool-specific reason. Claude Code is the only per-harness special case included here because of its popularity and current protocol gap.

## Release Model

Blueprint has one long-lived branch, `master`. Formal releases are annotated tags named `v<version>` on clean `master` commits, where `<version>` exactly matches `src/blueprint/version.py`. `scripts/release.bash` rejects development versions, branch or worktree ambiguity, divergent history, lightweight tags, and reused tags that point anywhere except the current commit. An identical local or remote tag is treated as an idempotent success.

The tag-triggered workflow independently rejects development or mismatched versions, lightweight tags, and tags whose commit is not the current published `origin/master`. It runs the full repository gate on Python 3.10 through 3.13, then builds one reproducibly timestamped wheel and one source distribution, checks their metadata, installs the wheel on Linux, macOS, and Windows, installs the source distribution on Linux, and verifies the installed version and CLI entry points. Only after those checks pass does it attach both files to a GitHub Release. Existing assets must be byte-identical and are never overwritten. Blueprint does not publish the unrelated PyPI project named `blueprint`; a downstream project must establish its own package identity and publication policy.

## Primary Consumer Contract

HeavenBase is Blueprint's primary continuously maintained consumer. `.blueprint-template.yaml` classifies every Blueprint path into one of three synchronization modes:

- **Exact:** source-neutral infrastructure copied byte-for-byte.
- **Adapted:** the same contract or intent, rewritten for HeavenBase's real package, branches, risks, and docs.
- **Excluded:** Blueprint history, package identity, generated state, and the canonical `heaven-style` source.

`scripts/template_sync.py` fails when a source path has no classification, when exact inventory or bytes drift, when a reviewed adapted counterpart changes, or when HeavenBase's manifest does not name the current Blueprint commit and source digest. A Blueprint template change is not complete until the HeavenBase adaptation is reviewed and recorded. This is a per-consumer synchronization checkpoint, not a claim of distributed atomicity. Commit the prospective Blueprint tree locally, review and record that exact commit in a local HeavenBase candidate, and commit both repositories before publishing either one. Push Blueprint `master` first so the private consumer CI can fetch its pinned public SHA, then push HeavenBase `master`. The short convergence window is explicit; release tags are created only after both repositories and CI agree. Blueprint's pre-push hook enforces the local checkpoint, while HeavenBase CI performs the authoritative reciprocal check. Blueprint CI cannot read private HeavenBase with its repository-scoped token, and this design deliberately avoids copying a personal token into Actions or maintaining a staging branch.

Blueprint and HeavenBase requirements take precedence when they conflict with generic lessons imported from CDASE, DeepSeek, or other references. The references supply enforcement patterns; they do not own either repository's design.

The skill follows a separate boundary. Blueprint remains its only repository source, HeavenBase carries no mirror, and a verified Blueprint skill change is installed globally for supported harnesses.
