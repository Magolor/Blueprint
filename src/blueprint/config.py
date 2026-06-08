"""Blueprint configuration surface backed by HeavenBase utilities."""

from __future__ import annotations

import os

from heavenbase.utils import ConfigManager

DEFAULT_CONFIG = {
    "blueprint": {
        "project": {
            "name": "Blueprint",
        },
        "cli": {
            "backend": "typer",
            "output": "yaml",
        },
    },
}

BOOTSTRAP_CONFIG = {
    "store": {
        "database": "file:%/config.db",
        "keep_last_k": 10,
    },
}

CM_BLUEPRINT = ConfigManager(
    package="blueprint",
    scope="blueprint",
    root=os.environ.get("BLUEPRINT_ROOT") or None,
    default=DEFAULT_CONFIG,
    bootstrap=BOOTSTRAP_CONFIG,
    setup=True,
)
