"""(Re-)Export German names for:
- basic types (Graphic and Color)
- color names
- operations
- primitves
- I/O
from this top-level module.
"""

# ruff: noqa: F403

import sys

from pytamaro.de.color import *
from pytamaro.de.color_names import *
from pytamaro.de.graphic import *
from pytamaro.de.io import *
from pytamaro.de.operations import *
from pytamaro.de.point_names import *
from pytamaro.de.primitives import *

sys.modules["pytamaro"].LANGUAGE = "de"  # type: ignore
