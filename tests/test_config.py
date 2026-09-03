"""Configuration boundary behavior."""

from dataclasses import FrozenInstanceError

import pytest

from blueprint import DEFAULT_CONFIG, define_config, load_config


def test_load_config_uses_defaults_and_environment() -> None:
    """Environment values override the complete defaults."""

    assert load_config({}) == DEFAULT_CONFIG
    assert load_config({"BLUEPRINT_PROJECT_NAME": " Example ", "BLUEPRINT_OUTPUT": "json"}).project.name == "Example"


def test_define_config_rejects_invalid_external_values() -> None:
    """Invalid field shapes fail at the owner boundary."""

    with pytest.raises(TypeError, match="config.project must be a mapping"):
        define_config({"project": [], "cli": {"output": "text"}})

    with pytest.raises(TypeError, match="config.cli.output"):
        define_config({"project": {"name": "Example"}, "cli": {"output": "xml"}})


def test_config_is_immutable() -> None:
    """Callers cannot mutate admitted configuration."""

    with pytest.raises(FrozenInstanceError):
        setattr(DEFAULT_CONFIG.project, "name", "Changed")
