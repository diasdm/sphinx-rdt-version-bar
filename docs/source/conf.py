"""Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

"""

import os
import sys
from typing import List

sys.path.insert(0, os.path.abspath("../.."))

# pylint: disable=redefined-builtin
# pylint: disable=invalid-name

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "sphinx-rdt-version-bar"
copyright = "2023, David Dias"
author = "David Dias"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions: List[str] = [
    "sphinx.ext.autodoc",  # Include documentation from docstrings
    "sphinx.ext.napoleon",  # Add support for Google style docstrings
    "sphinx.ext.todo",  # Catch and show TODOs within docstrings
    "sphinx_mdinclude",  # Markdown to rst
    "sphinx.ext.inheritance_diagram",  # Classes inheritance diagram
    "sphinx_rdt_version_bar",
]

# display TODOs
todo_include_todos = True

templates_path = ["_templates"]
exclude_patterns: List[str] = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
