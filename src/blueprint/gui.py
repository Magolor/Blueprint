"""Default GUI entry point for Blueprint."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from .version import __version__


def build_parser() -> argparse.ArgumentParser:
    """Build the Blueprint GUI launcher parser."""

    parser = argparse.ArgumentParser(prog="blueprint-gui", description="Blueprint GUI launcher.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the placeholder GUI endpoint."""

    build_parser().parse_args(argv)
    print("Blueprint GUI endpoint")
    return 0
