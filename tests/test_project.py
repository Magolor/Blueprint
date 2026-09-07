"""Starter project behavior."""

from blueprint import CliConfig, ProjectConfig, ProjectIdentity, __version__, get_project_info


def test_project_info_reports_configured_identity() -> None:
    """The SDK reports immutable project information."""

    info = get_project_info(ProjectConfig(project=ProjectIdentity(name="Example"), cli=CliConfig(output="text")))

    assert info.name == "Example"
    assert info.version == __version__
    assert info.output == "text"
