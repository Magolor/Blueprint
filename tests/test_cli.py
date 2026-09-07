"""Command-line adapter behavior."""

import json

import pytest

from blueprint import __version__
from blueprint.cli import run


def test_info_writes_text_and_json() -> None:
    """The CLI adapts SDK information to both supported output forms."""

    output: list[str] = []
    environment = {"BLUEPRINT_PROJECT_NAME": "Example"}

    assert run(["info"], environment=environment, write=output.append) == 0
    assert run(["info", "--json"], environment=environment, write=output.append) == 0
    assert output[0] == f"Example {__version__}"
    assert json.loads(output[1]) == {"name": "Example", "version": __version__, "output": "text"}


def test_unknown_option_is_a_usage_error() -> None:
    """The closed grammar rejects unknown options."""

    with pytest.raises(SystemExit) as raised:
        run(["info", "--unknown"])

    assert raised.value.code == 2
