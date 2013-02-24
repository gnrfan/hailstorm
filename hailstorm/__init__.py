"""
Hailstorm is a templating system extracted from Tornado.
"""

__version__ = "1.0.0"

version = __version__
version_info = tuple(version.split("."))

from template import Template
from template import BaseLoader
from template import Loader
from template import DictLoader
from template import ParseError