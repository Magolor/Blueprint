"""Stateless starter-project behavior."""

from __future__ import annotations

from dataclasses import dataclass

from .config import DEFAULT_CONFIG, ProjectConfig, define_config
from .version import __version__


@dataclass(frozen=True, slots=True)
class ProjectInfo:
    """Describe one configured starter project."""

    name: str
    version: str
    output: str


def get_project_info(config: ProjectConfig = DEFAULT_CONFIG) -> ProjectInfo:
    """Validate configuration and return immutable project information.

    Args:
        config: Complete project configuration.

    Returns:
        Immutable project information.

    Raises:
        TypeError: A field is invalid.
    """

    admitted = define_config(
        {
            "project": {"name": config.project.name},
            "cli": {"output": config.cli.output},
        }
    )
    return ProjectInfo(name=admitted.project.name, version=__version__, output=admitted.cli.output)
