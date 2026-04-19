import os
import sys
from importlib.metadata import version as _get_version

sys.path.insert(0, os.path.abspath("../src"))

project = "domainrobot"
author = "DigitalTolk"
release = _get_version("domainrobot")

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

autodoc_member_order = "bysource"
autodoc_typehints = "description"

suppress_warnings = ["ref.python"]

html_theme = "sphinx_rtd_theme"
