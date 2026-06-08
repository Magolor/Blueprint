"""Blueprint command line entry point backed by HeavenBase CLI specs."""

from __future__ import annotations

__all__ = ["build_registry", "create_cli", "main"]

import sys
from collections.abc import Sequence

from heavenbase.cli import ArgumentSpec, CLIOutput, CLIRegistry, CommandGroupSpec, CommandSpec, OptionSpec, PackageCLIContext
from heavenbase.cli.backends import build_argparse, build_click, build_typer, run_argparse, run_click, run_typer
from heavenbase.cli.spec import raise_cli_error
from heavenbase.utils.config_api import config_get, config_list, config_set, config_unset, resolve_config_scope
from heavenbase.utils.typing import Any, Callable, Dict, Optional, Tuple

from .config import CM_BLUEPRINT
from .version import __version__

BackendFactory = Callable[[CLIRegistry, PackageCLIContext], Any]
BackendRunner = Callable[[Any, Optional[list[str]]], Any]
BACKENDS: Dict[str, Tuple[BackendFactory, BackendRunner]] = {
    "argparse": (build_argparse, run_argparse),
    "click": (build_click, run_click),
    "typer": (build_typer, run_typer),
}


def _emit(context: PackageCLIContext, value: Any, as_json: bool = False) -> None:
    """Print one CLI result."""
    if as_json:
        context.out.json(value)
    elif isinstance(value, (dict, list, tuple)):
        context.out.yaml(value)
    elif value is not None:
        context.out.echo(value)


def _setup(context: PackageCLIContext, reset: bool = False) -> None:
    """Initialize the Blueprint config store."""
    context.cm.setup(reset=reset)
    context.out.echo(f"setup {context.cm.base_scope}")


def _init(context: PackageCLIContext, scope: str | None = None, reset: bool = False) -> None:
    """Initialize one Blueprint config scope."""
    created = context.cm.init(scope=scope, reset=reset)
    context.out.echo(f"{'initialized' if created else 'exists'} {scope or context.cm.scope}")


def _pj(context: PackageCLIContext, parts: list[str] | None = None, abs_path: bool = False) -> None:
    """Resolve a path with Blueprint config path aliases."""
    context.out.echo(context.cm.pj(*(parts or []), abs=abs_path))


def _config_get(
    context: PackageCLIContext,
    key: str | None = None,
    scope: str | None = None,
    raw_layer: bool = False,
    as_json: bool = False,
) -> None:
    """Read one config key or the full config."""
    _emit(context, config_get(context.cm, key=key, scope=scope, merged=not raw_layer), as_json=as_json)


def _config_list(
    context: PackageCLIContext,
    prefix: str | None = None,
    scope: str | None = None,
    raw_layer: bool = False,
    as_json: bool = False,
) -> None:
    """List flattened config rows."""
    _emit(context, config_list(context.cm, prefix=prefix, scope=scope, merged=not raw_layer), as_json=as_json)


def _config_set(context: PackageCLIContext, key: str, value: str, scope: str | None = None, parse: str = "auto") -> None:
    """Set one config key."""
    config_set(context.cm, key, value, scope=scope, parse=parse)
    context.out.echo(f"set {key}")


def _config_unset(context: PackageCLIContext, key: str, scope: str | None = None) -> None:
    """Unset one config key."""
    config_unset(context.cm, key, scope=scope)
    context.out.echo(f"unset {key}")


def _config_scopes(context: PackageCLIContext, as_json: bool = False) -> None:
    """List stored config scopes."""
    _emit(context, context.cm.scopes(), as_json=as_json)


def _config_history(context: PackageCLIContext, scope: str | None = None, limit: int = 10, as_json: bool = False) -> None:
    """List config history for a scope."""
    _emit(context, context.cm.history(scope=resolve_config_scope(context.cm, scope), limit=limit), as_json=as_json)


def _json_option() -> OptionSpec:
    return OptionSpec.from_flags("as_json", "--json", "-j", help="Render structured output as JSON.", default=False, is_flag=True, type=bool)


def config_group() -> CommandGroupSpec:
    """Return Blueprint config commands."""
    scope_opt = OptionSpec.from_flags("scope", "--scope", help="Optional config scope.")
    raw_opt = OptionSpec.from_flags(
        "raw_layer", "--raw-layer", help="Read the raw scope layer instead of merged config.", default=False, is_flag=True, type=bool
    )
    return CommandGroupSpec(
        "config",
        help="Read and write Blueprint config.",
        aliases=["cfg"],
        commands=[
            CommandSpec(
                "get",
                _config_get,
                help="Read one config key or the full config.",
                args=[ArgumentSpec("key", help="Optional dotted config key.", required=False)],
                options=[scope_opt, raw_opt, _json_option()],
            ),
            CommandSpec(
                "list",
                _config_list,
                help="List flattened config rows.",
                aliases=["ls"],
                options=[
                    OptionSpec.from_flags("prefix", "--prefix", help="Only include keys with this prefix."),
                    scope_opt,
                    raw_opt,
                    _json_option(),
                ],
            ),
            CommandSpec(
                "set",
                _config_set,
                help="Set one config key.",
                args=[ArgumentSpec("key", help="Dotted config key."), ArgumentSpec("value", help="Config value.")],
                options=[scope_opt, OptionSpec.from_flags("parse", "--parse", help="Value parser: auto, json, or raw.", default="auto")],
            ),
            CommandSpec(
                "unset",
                _config_unset,
                help="Unset one config key.",
                aliases=["remove", "rm", "del", "delete"],
                args=[ArgumentSpec("key", help="Dotted config key.")],
                options=[scope_opt],
            ),
            CommandSpec("scopes", _config_scopes, help="List stored config scopes.", options=[_json_option()]),
            CommandSpec(
                "history",
                _config_history,
                help="List config history for a scope.",
                options=[
                    scope_opt,
                    OptionSpec.from_flags("limit", "--limit", help="Maximum history rows.", default=10, type=int),
                    _json_option(),
                ],
            ),
        ],
    )


def root_commands() -> list[CommandSpec]:
    """Return Blueprint root commands."""
    return [
        CommandSpec(
            "setup",
            _setup,
            help="Initialize the project config store.",
            options=[OptionSpec.from_flags("reset", "--reset", help="Reset stored project config before setup.", default=False, is_flag=True, type=bool)],
        ),
        CommandSpec(
            "init",
            _init,
            help="Initialize one config scope.",
            args=[ArgumentSpec("scope", help="Optional config scope.", required=False)],
            options=[OptionSpec.from_flags("reset", "--reset", help="Reset the scope before initializing it.", default=False, is_flag=True, type=bool)],
        ),
        CommandSpec(
            "pj",
            _pj,
            help="Join path parts using the project config path aliases.",
            args=[ArgumentSpec("parts", help="Path parts to join.", required=False, nargs=-1)],
            options=[OptionSpec.from_flags("abs_path", "--abs", help="Return an absolute path.", default=False, is_flag=True, type=bool)],
        ),
    ]


def build_registry() -> CLIRegistry:
    """Build the default Blueprint CLI registry."""
    registry = CLIRegistry()
    for command in root_commands():
        registry.add_root(command)
    registry.add_group(config_group())
    return registry


def _context(context: PackageCLIContext | None = None) -> PackageCLIContext:
    result = context or PackageCLIContext(package="bp", version=__version__, cm=CM_BLUEPRINT, out=CLIOutput())
    if result.out is None:
        result.out = CLIOutput()
    return result


def _backend(context: PackageCLIContext, backend: str | None = None) -> str:
    selected = backend if backend is not None else "typer"
    if not selected:
        raise ValueError("Missing CLI backend config: blueprint.cli.backend")
    return str(selected).lower()


def create_cli(backend: str | None = None, context: PackageCLIContext | None = None) -> Any:
    """Create a Blueprint CLI app for the selected HeavenBase backend."""
    ctx = _context(context)
    selected = _backend(ctx, backend)
    if selected not in BACKENDS:
        raise ValueError(f"Unsupported CLI backend {selected!r}; expected one of {sorted(BACKENDS)}")
    return BACKENDS[selected][0](build_registry(), ctx)


def _strip_path_prefix(argv: Sequence[str]) -> list[str]:
    prefix = "path:"
    return [arg.removeprefix(prefix) if arg.startswith(prefix) else arg for arg in argv]


def main(argv: Sequence[str] | None = None) -> Any:
    """Run the configured Blueprint CLI entry point."""
    args = _strip_path_prefix(argv if argv is not None else sys.argv[1:])
    ctx = _context()
    try:
        selected = _backend(ctx)
        app = create_cli(selected, context=ctx)
        return BACKENDS[selected][1](app, args)
    except SystemExit:
        raise
    except KeyboardInterrupt as error:
        raise_cli_error(ctx, error, code=130, msg="interrupted")
    except Exception as error:
        raise_cli_error(ctx, error)


if __name__ == "__main__":
    main()
