"""Automatically configure rdt theme.
"""

import os
from pathlib import Path
from typing import Any, Dict

import sphinx
from sphinx.application import Sphinx

EXT_DIR = Path(os.path.dirname(os.path.realpath(__file__)))


class EditConfigs:
    """Edits configs to enable versioning with RTD theme."""

    def __init__(self, app: Sphinx, config) -> None:
        """Edit configs."""
        self.config = app.config

        config._raw_config["templates_path"] = [str(EXT_DIR / "_templates")]
        config._raw_config["todo_include_todos"] = True
        config._raw_config["html_static_path"] = [str(EXT_DIR / "_static")]

        # path relative to html_static_path
        config._raw_config["html_js_files"] = ["versions.js"]

        config._raw_config["html_context"] = {}
        # used in versions.html
        config._raw_config["html_context"]["current_version"] = "version"

        # -- Theme options -----------------------------------------------------------
        # https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html#configuration
        config._raw_config["html_context"]["display_github"] = True

        # TODO get these programatically
        config._raw_config["html_context"]["github_user"] = "diasdm"
        config._raw_config["html_context"]["github_repo"] = "sphinx-rdt-version-bar"

        print(f"Configs after edit: {config._raw_config}")


def setup(app: Sphinx) -> Dict[str, Any]:
    """Setup exetension."""

    app.connect("config-inited", EditConfigs)

    return {
        "version": sphinx.__display_version__,
        "env_version": 2,
        "parallel_read_safe": True,
    }
