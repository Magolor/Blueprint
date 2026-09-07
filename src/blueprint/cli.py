"""Blueprint command-line adapter."""

from __future__ import annotations

import argparse
from collections.abc import Callable, Mapping, Sequence
from dataclasses import asdict
import json

from .config import load_config
from .project import get_project_info
from .version import __version__


def build_parser() -> argparse.ArgumentParser:
    """Build the closed Blueprint command grammar."""

    parser = argparse.ArgumentParser(prog="bp", description="Inspect Blueprint package information.")
    parser.add_argument("--version", action="version", version=__version__)
    commands = parser.add_subparsers(dest="command")
    info = commands.add_parser("info", help="Print package information.")
    info.add_argument("--json", action="store_true", help="Write JSON output.")
    return parser


def run(
    arguments: Sequence[str] | None = None,
    *,
    environment: Mapping[str, str] | None = None,
    write: Callable[[str], None] = print,
) -> int:
    """Run one CLI command.

    Args:
        arguments: Command arguments without the executable name.
        environment: Environment values for configuration.
        write: Output sink for successful command output.

    Returns:
        Zero after a successful command.
    """

    parser = build_parser()
    parsed = parser.parse_args(arguments)
    if parsed.command is None:
        parser.print_help()
        return 0

    info = get_project_info(load_config(environment))
    write(json.dumps(asdict(info)) if parsed.json else f"{info.name} {info.version}")
    return 0


def main() -> int:
    """Run the installed `bp` entry point."""

    return run()


if __name__ == "__main__":
    raise SystemExit(main())
