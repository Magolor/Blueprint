"""Validated, immutable Blueprint configuration."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
import os
from typing import Literal

OutputFormat = Literal["text", "json"]


@dataclass(frozen=True, slots=True)
class ProjectIdentity:
    """Identify one Blueprint project."""

    name: str


@dataclass(frozen=True, slots=True)
class CliConfig:
    """Control Blueprint command output."""

    output: OutputFormat


@dataclass(frozen=True, slots=True)
class ProjectConfig:
    """Store one complete Blueprint configuration snapshot."""

    project: ProjectIdentity
    cli: CliConfig


DEFAULT_CONFIG = ProjectConfig(project=ProjectIdentity(name="Blueprint"), cli=CliConfig(output="text"))


def _require_mapping(value: object, path: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise TypeError(f"{path} must be a mapping")
    return value


def _require_name(value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise TypeError("config.project.name must be a non-empty string")
    return value.strip()


def _require_output(value: object) -> OutputFormat:
    if value not in ("text", "json"):
        raise TypeError('config.cli.output must be either "text" or "json"')
    return value


def define_config(value: object) -> ProjectConfig:
    """Validate and detach one complete configuration value.

    Args:
        value: Untrusted configuration data.

    Returns:
        A validated immutable snapshot.

    Raises:
        TypeError: A required value is absent or invalid.
    """

    config = _require_mapping(value, "config")
    project = _require_mapping(config.get("project"), "config.project")
    cli = _require_mapping(config.get("cli"), "config.cli")
    return ProjectConfig(
        project=ProjectIdentity(name=_require_name(project.get("name"))),
        cli=CliConfig(output=_require_output(cli.get("output"))),
    )


def load_config(environment: Mapping[str, str] | None = None) -> ProjectConfig:
    """Build a configuration snapshot from process-style environment data.

    Args:
        environment: Environment values. The process environment is used when omitted.

    Returns:
        A validated immutable snapshot.

    Raises:
        TypeError: An environment value is invalid.
    """

    source = os.environ if environment is None else environment
    return define_config(
        {
            "project": {"name": source.get("BLUEPRINT_PROJECT_NAME", DEFAULT_CONFIG.project.name)},
            "cli": {"output": source.get("BLUEPRINT_OUTPUT", DEFAULT_CONFIG.cli.output)},
        }
    )
