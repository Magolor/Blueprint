#!/usr/bin/env python3
"""Install heaven-style globally, mirror optional checkouts, and refresh assets."""

from __future__ import annotations

import argparse
import os
import re
import sys

from heavenbase.utils import (
    cmd,
    copy_dir,
    copy_file,
    delete_path,
    exists_dir,
    exists_file,
    get_file_basename,
    get_file_dir,
    list_paths,
    load_txt,
    pj,
    touch_dir,
)

SKILL_ROOT = get_file_dir(get_file_dir(__file__, abs=True))
SCRIPTS = pj(SKILL_ROOT, "scripts")
VERSION_RE = re.compile(r"^metadata:\s*\n(?:[ \t].*\n)*?[ \t]+version:\s*(\S+)", re.M)
ASSET_FILES = ("REFERENCE.md", "default-glossary.md", ".gitignore")
SKIP_NAMES = {"__pycache__", "heavenbase-reference"}


def read_skill_version(skill_root: str) -> str:
    """Return metadata.version from SKILL.md."""
    text = load_txt(pj(skill_root, "SKILL.md"))
    match = VERSION_RE.search(text)
    if match:
        return match.group(1)
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("version:"):
            return stripped.split(":", 1)[1].strip()
    raise ValueError(f"missing metadata.version in {pj(skill_root, 'SKILL.md')}")


def version_key(version: str) -> tuple[int, ...]:
    """Return a comparable numeric key for heaven-style version strings."""
    return tuple(int(part) for part in re.findall(r"\d+", version))


def agents_root() -> str:
    """Return the user-level Agent Skills root."""
    override = os.environ.get("HEAVEN_STYLE_AGENTS_ROOT")
    if override:
        return pj(override, abs=True)
    return pj("~", ".agents", "skills", abs=True)


def global_agents_skill_dir(skill_root: str) -> str:
    """Return the versioned user-level install path under ~/.agents/skills."""
    return pj(agents_root(), f"heaven-style-{read_skill_version(skill_root)}", abs=True)


def embedded_heavenbase_root(skill_root: str) -> str | None:
    """Return the HeavenBase repo root when this skill is checked in there."""
    current = pj(skill_root, abs=True)
    for _ in range(8):
        if exists_file(pj(current, "src", "heavenbase", "version.py")):
            return current
        parent = get_file_dir(current)
        if parent == current:
            break
        current = parent
    return None


def run(args: list[str], *, cwd: str | None = None) -> None:
    """Run a child command."""
    print("+", " ".join(args))
    cmd(args, check=True, cwd=cwd or SKILL_ROOT)


def copy_skill_tree(source: str, target: str) -> None:
    """Copy skill files to target, excluding the reference clone."""
    touch_dir(target)
    for path in list_paths(source, abs=True):
        name = get_file_basename(path)
        if name in SKIP_NAMES or name.startswith("."):
            continue
        dest = pj(target, name, abs=True)
        if name == "assets" and exists_dir(path):
            touch_dir(dest)
            for asset in ASSET_FILES:
                asset_path = pj(path, asset)
                if exists_file(asset_path):
                    copy_file(asset_path, pj(dest, asset))
            continue
        if exists_dir(path):
            copy_dir(path, dest)
        else:
            copy_file(path, dest)


def remove_stale_global_installs(version: str) -> list[str]:
    """Remove unversioned and older-or-equal heaven-style installs."""
    root = agents_root()
    if not exists_dir(root):
        return []

    current_key = version_key(version)
    removed: list[str] = []

    legacy = pj(root, "heaven-style", abs=True)
    if exists_dir(legacy) or exists_file(legacy):
        delete_path(legacy)
        removed.append(legacy)

    prefix = "heaven-style-"
    for path in list_paths(root, abs=True):
        name = get_file_basename(path)
        if not name.startswith(prefix):
            continue
        suffix = name[len(prefix) :]
        if version_key(suffix) <= current_key:
            delete_path(path)
            removed.append(path)
    return removed


def sync_and_index(
    skill_root: str,
    *,
    skip_sync: bool,
    local: str | None,
) -> bool:
    """Refresh reference assets and index.yaml for a skill checkout."""
    embedded_root = embedded_heavenbase_root(skill_root)
    did_sync = not skip_sync
    if embedded_root is not None:
        if not skip_sync:
            print(
                f"Skipping reference sync for embedded HeavenBase skill ({embedded_root}); " f"use {global_agents_skill_dir(SKILL_ROOT)}",
                file=sys.stderr,
            )
        did_sync = False
    elif did_sync:
        sync = [sys.executable, pj(SCRIPTS, "sync.py")]
        if local is not None:
            sync.extend(["--local", local])
        run(sync, cwd=skill_root)

    run([sys.executable, pj(SCRIPTS, "index.py")], cwd=skill_root)
    return did_sync


def install_global(*, skip_sync: bool, local: str | None) -> str:
    """Install the versioned global heaven-style checkout."""
    version = read_skill_version(SKILL_ROOT)
    target = global_agents_skill_dir(SKILL_ROOT)
    removed = remove_stale_global_installs(version)
    for path in removed:
        print(f"[heaven-style] removed stale install {path}")
    copy_skill_tree(SKILL_ROOT, target)
    sync_and_index(target, skip_sync=skip_sync, local=local)
    print(f"[heaven-style] installed global copy at {target}")
    return target


def mirror_skill(target: str) -> None:
    """Mirror the skill tree to another checkout without touching global installs."""
    mirror_root = pj(target, abs=True)
    copy_skill_tree(SKILL_ROOT, mirror_root)
    run([sys.executable, pj(SCRIPTS, "index.py")], cwd=mirror_root)
    print(f"[heaven-style] mirrored skill to {mirror_root}")


def main() -> int:
    """CLI entrypoint."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-sync", action="store_true", help="Do not refresh the HeavenBase reference asset")
    parser.add_argument("--local", default=None, help="Refresh the reference asset from a local repo path")
    parser.add_argument(
        "--print-global-dir",
        action="store_true",
        help="Print the versioned ~/.agents/skills install directory for this skill",
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Sync and index only at the current skill root; do not install globally",
    )
    parser.add_argument(
        "--mirror",
        metavar="PATH",
        default=None,
        help="Mirror the skill tree to PATH (for example a HeavenBase in-repo copy)",
    )
    parser.add_argument(
        "--skip-global",
        action="store_true",
        help="Skip the versioned ~/.agents/skills install",
    )
    args = parser.parse_args()

    if args.print_global_dir:
        print(global_agents_skill_dir(SKILL_ROOT))
        return 0

    embedded_root = embedded_heavenbase_root(SKILL_ROOT)
    local = args.local
    if embedded_root is not None and local is not None and pj(local, abs=True) == embedded_root:
        print(
            f"Ignoring --local for embedded HeavenBase skill; use {global_agents_skill_dir(SKILL_ROOT)} " "for reference assets",
            file=sys.stderr,
        )
        local = None

    if args.mirror is not None:
        mirror_skill(args.mirror)

    if args.in_place:
        did_sync = sync_and_index(SKILL_ROOT, skip_sync=args.skip_sync, local=local)
        print("heaven-style is synced and indexed" if did_sync else "heaven-style index is current; sync skipped")
        return 0

    if not args.skip_global:
        install_global(skip_sync=args.skip_sync, local=local)
    return 0


if __name__ == "__main__":
    sys.exit(main())
