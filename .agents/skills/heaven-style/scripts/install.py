#!/usr/bin/env python3
"""Install the standalone heaven-style skill and optional harness bridges."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from uuid import uuid4

SKILL_ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "heaven-style"
CLAUDE_MARKETPLACE = "heaven-style-local"
VERSION_RE = re.compile(r"^metadata:\s*\n(?:[ \t].*\n)*?[ \t]+version:\s*(\S+)", re.M)
NAME_RE = re.compile(r"^name:\s*(\S+)", re.M)
DESCRIPTION_RE = re.compile(r"^description:\s*(.+)", re.M)
SKIP_NAMES = {"__pycache__"}
MANAGED_ROOT_NAMES = {"SKILL.md", "assets", "references", "scripts"}


def is_reference_cache(name: str) -> bool:
    """Return whether name is a local evidence cache excluded from installs."""
    return name.endswith("-reference")


def read_skill_version(skill_root: Path) -> str:
    """Return metadata.version from SKILL.md."""
    skill_file = skill_root / "SKILL.md"
    text = skill_file.read_text(encoding="utf-8")
    match = VERSION_RE.search(text)
    if match:
        return match.group(1)
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("version:"):
            return stripped.split(":", 1)[1].strip()
    raise ValueError(f"missing metadata.version in {skill_file}")


def read_skill_name(skill_root: Path) -> str | None:
    """Return SKILL.md name when present."""
    skill_file = skill_root / "SKILL.md"
    if not skill_file.is_file():
        return None
    match = NAME_RE.search(skill_file.read_text(encoding="utf-8"))
    return match.group(1).strip("'\"") if match else None


def read_skill_description(skill_root: Path) -> str:
    """Return the SKILL.md description."""
    text = (skill_root / "SKILL.md").read_text(encoding="utf-8")
    match = DESCRIPTION_RE.search(text)
    if match:
        return match.group(1).strip()
    return "Standalone Heaven-style code-quality and project-management guide for TypeScript and Python repositories."


def is_heaven_style_skill(path: Path) -> bool:
    """Return whether path is a verified heaven-style skill."""
    return path.is_dir() and read_skill_name(path) == SKILL_NAME


def agents_root() -> Path:
    """Return the user-level Agent Skills root."""
    override = os.environ.get("HEAVEN_STYLE_AGENTS_ROOT")
    return Path(override).expanduser().resolve() if override else Path("~/.agents/skills").expanduser().resolve()


def global_agents_skill_dir(skill_root: Path) -> Path:
    """Return the standard user-level install path under ~/.agents/skills."""
    return agents_root() / (read_skill_name(skill_root) or SKILL_NAME)


def claude_root(config_dir: str | None = None) -> Path:
    """Return the Claude Code config root."""
    configured = config_dir or os.environ.get("HEAVEN_STYLE_CLAUDE_ROOT") or os.environ.get("CLAUDE_CONFIG_DIR") or "~/.claude"
    return Path(configured).expanduser().resolve()


def claude_plain_skill_dir(config_dir: str | None = None) -> Path:
    """Return the duplicate-prone plain Claude skill path."""
    return claude_root(config_dir) / "skills" / SKILL_NAME


def claude_marketplace_root(path: str | None = None) -> Path:
    """Return the local Claude plugin marketplace root."""
    configured = path or os.environ.get("HEAVEN_STYLE_CLAUDE_MARKETPLACE_ROOT")
    if configured:
        return Path(configured).expanduser().resolve()
    return agents_root().parent / "heaven-style-claude-marketplace"


def run(args: list[str], *, cwd: Path | None = None, env: dict[str, str] | None = None) -> None:
    """Run a child command."""
    print("+", " ".join(args))
    subprocess.run(args, check=True, cwd=cwd or SKILL_ROOT, env=env, text=True)


def _copy_path(source: Path, target: Path) -> None:
    """Copy one file, symlink, or directory into a prepared tree."""
    target.parent.mkdir(parents=True, exist_ok=True)
    if source.is_symlink():
        target.symlink_to(os.readlink(source), target_is_directory=source.is_dir())
    elif source.is_dir():
        shutil.copytree(source, target, dirs_exist_ok=True)
    else:
        shutil.copy2(source, target)


def copy_skill_tree(source: Path, target: Path) -> None:
    """Copy distributed skill files to a fresh or staged target."""
    target.mkdir(parents=True, exist_ok=True)
    for path in sorted(source.iterdir(), key=lambda item: item.name.lower()):
        name = path.name
        if name in SKIP_NAMES or is_reference_cache(name) or name.startswith("."):
            continue
        destination = target / name
        if name != "assets" or not path.is_dir():
            _copy_path(path, destination)
            continue
        destination.mkdir(parents=True, exist_ok=True)
        for asset in sorted(path.iterdir(), key=lambda item: item.name.lower()):
            asset_name = asset.name
            if asset_name in SKIP_NAMES or is_reference_cache(asset_name):
                continue
            if asset_name.startswith(".") and asset_name != ".gitignore":
                continue
            _copy_path(asset, destination / asset_name)


def _delete_path(path: Path) -> None:
    """Delete one explicit file, symlink, or directory."""
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    elif path.exists() or path.is_symlink():
        path.unlink()


def _swap_directory(staged: Path, target: Path) -> None:
    """Replace target with a staged directory and restore it if publication fails."""
    backup = target.with_name(f".{target.name}.backup-{uuid4().hex}")
    had_target = target.exists() or target.is_symlink()
    if had_target:
        target.rename(backup)
    try:
        staged.rename(target)
    except Exception:
        if target.exists() or target.is_symlink():
            _delete_path(target)
        if had_target:
            backup.rename(target)
        raise
    if had_target:
        _delete_path(backup)


def _stage_directory(target: Path) -> Path:
    """Create a same-filesystem staging directory beside target."""
    target.parent.mkdir(parents=True, exist_ok=True)
    return Path(tempfile.mkdtemp(prefix=f".{target.name}.stage-", dir=target.parent))


def _preserve_mirror_extras(existing: Path, staged: Path, *, preserve_root_extras: bool = True) -> None:
    """Preserve explicit local content while pruning managed paths."""
    if preserve_root_extras:
        for path in sorted(existing.iterdir(), key=lambda item: item.name.lower()):
            if path.name in MANAGED_ROOT_NAMES:
                continue
            _copy_path(path, staged / path.name)

    assets = existing / "assets"
    if not assets.is_dir():
        return
    staged_assets = staged / "assets"
    for path in sorted(assets.iterdir(), key=lambda item: item.name.lower()):
        if is_reference_cache(path.name) or (path.name.startswith(".") and path.name != ".gitignore"):
            _copy_path(path, staged_assets / path.name)

    instance = assets / "instance"
    if instance.is_dir():
        for path in sorted(instance.glob("*.local.md"), key=lambda item: item.name.lower()):
            _copy_path(path, staged_assets / "instance" / path.name)


def require_replaceable_skill(path: Path, label: str) -> None:
    """Fail unless an existing path is a verified heaven-style skill."""
    if not path.exists() and not path.is_symlink():
        return
    if not is_heaven_style_skill(path):
        raise RuntimeError(f"refusing to replace {label} at {path}; it is not a verified {SKILL_NAME} skill")


def remove_legacy_global_installs() -> list[Path]:
    """Remove verified legacy versioned heaven-style installs."""
    root = agents_root()
    if not root.is_dir():
        return []

    removed: list[Path] = []
    prefix = f"{SKILL_NAME}-"
    for path in sorted(root.iterdir(), key=lambda item: item.name.lower()):
        if not path.name.startswith(prefix):
            continue
        if is_heaven_style_skill(path):
            _delete_path(path)
            removed.append(path)
        else:
            print(f"[heaven-style] skipped unverified legacy install {path}", file=sys.stderr)
    return removed


def index_skill(skill_root: Path) -> None:
    """Regenerate index.yaml for a skill checkout."""
    run([sys.executable, str(skill_root / "scripts" / "index.py")], cwd=skill_root)


def install_global() -> Path:
    """Install the standard global heaven-style checkout transactionally."""
    target = global_agents_skill_dir(SKILL_ROOT)
    require_replaceable_skill(target, "global skill install")
    staged = _stage_directory(target)
    try:
        copy_skill_tree(SKILL_ROOT, staged)
        if target.is_dir():
            _preserve_mirror_extras(target, staged, preserve_root_extras=False)
        index_skill(staged)
        _swap_directory(staged, target)
    finally:
        if staged.exists() or staged.is_symlink():
            _delete_path(staged)

    for path in remove_legacy_global_installs():
        print(f"[heaven-style] removed stale install {path}")
    print(f"[heaven-style] installed global copy at {target}")
    return target


def backup_claude_plain_skill(config_dir: str | None) -> Path | None:
    """Back up a verified plain Claude skill that would duplicate discovery."""
    path = claude_plain_skill_dir(config_dir)
    if not path.exists() and not path.is_symlink():
        return None
    if not is_heaven_style_skill(path):
        raise RuntimeError(f"refusing to move {path}; it is not a verified {SKILL_NAME} skill")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup = path.with_name(f"{SKILL_NAME}.backup-{stamp}")
    _copy_path(path, backup)
    _delete_path(path)
    return backup


def guard_claude_plain_skill(*, config_dir: str | None, backup: bool) -> None:
    """Prevent duplicate discovery through ~/.claude/skills."""
    path = claude_plain_skill_dir(config_dir)
    if not path.exists() and not path.is_symlink():
        return
    if backup:
        target = backup_claude_plain_skill(config_dir)
        print(f"[heaven-style] backed up duplicate-prone Claude skill to {target}")
        return
    raise RuntimeError(
        f"Plain Claude skill found at {path}. Cursor, OpenCode, and Kilo may also scan this location, "
        f"so installing the Claude plugin would duplicate {SKILL_NAME}. Remove it or rerun with --backup-claude-skill."
    )


def read_claude_plugin_name(plugin_root: Path) -> str | None:
    """Return a Claude plugin name when present."""
    manifest = plugin_root / ".claude-plugin" / "plugin.json"
    if not manifest.is_file():
        return None
    data: object = json.loads(manifest.read_text(encoding="utf-8"))
    return data.get("name") if isinstance(data, dict) and isinstance(data.get("name"), str) else None


def require_replaceable_claude_plugin(plugin_root: Path) -> None:
    """Fail unless an existing Claude plugin path is managed by heaven-style."""
    if not plugin_root.exists() and not plugin_root.is_symlink():
        return
    if read_claude_plugin_name(plugin_root) != SKILL_NAME:
        raise RuntimeError(f"refusing to replace Claude plugin source at {plugin_root}; it is not {SKILL_NAME}")


def _write_json(value: object, path: Path) -> None:
    """Write deterministic UTF-8 JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"{json.dumps(value, indent=2, ensure_ascii=False)}\n", encoding="utf-8")


def write_claude_marketplace(market_root: Path, plugin_root: Path, version: str, description: str) -> None:
    """Write Claude plugin marketplace manifests."""
    author = {"name": "Magolor", "email": "magolorcz@gmail.com"}
    plugin: dict[str, object] = {
        "name": SKILL_NAME,
        "description": description,
        "version": version,
        "author": author,
        "homepage": "https://github.com/Magolor/Blueprint",
        "repository": "https://github.com/Magolor/Blueprint",
        "license": "MIT",
        "keywords": ["skills", "typescript", "python", "code-quality", "codex", "claude-code"],
    }
    marketplace_plugin = dict(plugin)
    marketplace_plugin["source"] = f"./{plugin_root.name}"
    _write_json(plugin, plugin_root / ".claude-plugin" / "plugin.json")
    _write_json(
        {
            "name": CLAUDE_MARKETPLACE,
            "metadata": {"description": "Local marketplace for the Heaven-style skill."},
            "owner": author,
            "plugins": [marketplace_plugin],
        },
        market_root / ".claude-plugin" / "marketplace.json",
    )


def run_with_claude_config(args: list[str], config_dir: str | None) -> None:
    """Run Claude with an optional isolated config dir."""
    if not config_dir:
        run(args)
        return
    env = dict(os.environ)
    env["CLAUDE_CONFIG_DIR"] = str(Path(config_dir).expanduser().resolve())
    run(args, env=env)


def install_claude_plugin(
    *,
    config_dir: str | None,
    marketplace_root: str | None,
    backup_plain_skill: bool,
    scope: str,
) -> Path:
    """Install heaven-style as a Claude Code plugin without plain skill duplication."""
    guard_claude_plain_skill(config_dir=config_dir, backup=backup_plain_skill)
    market_root = claude_marketplace_root(marketplace_root)
    plugin_root = market_root / SKILL_NAME
    require_replaceable_claude_plugin(plugin_root)
    staged = _stage_directory(plugin_root)
    try:
        plugin_skill_root = staged / "skills" / SKILL_NAME
        copy_skill_tree(SKILL_ROOT, plugin_skill_root)
        index_skill(plugin_skill_root)
        write_claude_marketplace(market_root, staged, read_skill_version(SKILL_ROOT), read_skill_description(SKILL_ROOT))
        _swap_directory(staged, plugin_root)
    finally:
        if staged.exists() or staged.is_symlink():
            _delete_path(staged)

    write_claude_marketplace(market_root, plugin_root, read_skill_version(SKILL_ROOT), read_skill_description(SKILL_ROOT))
    run_with_claude_config(["claude", "plugin", "validate", str(market_root)], config_dir)
    run_with_claude_config(["claude", "plugin", "marketplace", "add", str(market_root)], config_dir)
    run_with_claude_config(["claude", "plugin", "install", "--scope", scope, f"{SKILL_NAME}@{CLAUDE_MARKETPLACE}"], config_dir)
    print(f"[heaven-style] installed Claude plugin from {market_root}")
    return market_root


def mirror_skill(target: str) -> None:
    """Mirror the skill transactionally while preserving explicitly unmanaged content."""
    mirror_root = Path(target).expanduser().resolve()
    require_replaceable_skill(mirror_root, "skill mirror")
    staged = _stage_directory(mirror_root)
    try:
        copy_skill_tree(SKILL_ROOT, staged)
        if mirror_root.exists():
            _preserve_mirror_extras(mirror_root, staged)
        index_skill(staged)
        _swap_directory(staged, mirror_root)
    finally:
        if staged.exists() or staged.is_symlink():
            _delete_path(staged)
    print(f"[heaven-style] mirrored skill to {mirror_root}")


def main() -> int:
    """CLI entrypoint."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--print-global-dir",
        action="store_true",
        help="Print the standard ~/.agents/skills install directory for this skill",
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Regenerate the index at the current skill root; do not install globally",
    )
    parser.add_argument(
        "--mirror",
        metavar="PATH",
        default=None,
        help="Mirror the skill tree to PATH for a repository that intentionally embeds it",
    )
    parser.add_argument(
        "--skip-global",
        action="store_true",
        help="Skip the standard ~/.agents/skills install",
    )
    parser.add_argument(
        "--all-harnesses",
        action="store_true",
        help="Install the common Agent Skill and the Claude Code plugin bridge",
    )
    parser.add_argument(
        "--claude-plugin",
        action="store_true",
        help="Install the Claude Code plugin bridge without writing ~/.claude/skills",
    )
    parser.add_argument(
        "--backup-claude-skill",
        action="store_true",
        help="Back up an existing verified ~/.claude/skills/heaven-style before installing the Claude plugin",
    )
    parser.add_argument(
        "--claude-config-dir",
        default=None,
        help="Use a Claude Code config directory for plugin commands (defaults to Claude's normal config)",
    )
    parser.add_argument(
        "--claude-marketplace-root",
        default=None,
        help="Write the local Claude plugin marketplace at PATH",
    )
    parser.add_argument(
        "--claude-scope",
        default="user",
        choices=("user", "project", "local"),
        help="Claude plugin install scope",
    )
    args = parser.parse_args()

    if args.print_global_dir:
        print(global_agents_skill_dir(SKILL_ROOT))
        return 0

    if args.mirror is not None:
        mirror_skill(args.mirror)

    if args.in_place:
        index_skill(SKILL_ROOT)
        print("heaven-style index is current")
        return 0

    if not args.skip_global:
        install_global()
    if args.all_harnesses or args.claude_plugin:
        install_claude_plugin(
            config_dir=args.claude_config_dir,
            marketplace_root=args.claude_marketplace_root,
            backup_plain_skill=args.backup_claude_skill,
            scope=args.claude_scope,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
