"""(Re-)Export German names for:
- basic types (Graphic and Color)
- color names
- operations
- primitves
- I/O
from this top-level module.
"""  # noqa: D205

import sys

# ruff: noqa: F403
from pytamaro.de.color import *
from pytamaro.de.color_names import *
from pytamaro.de.graphic import *
from pytamaro.de.io import *
from pytamaro.de.operations import *
from pytamaro.de.point_names import *
from pytamaro.de.primitives import *

sys.modules["pytamaro"].LANGUAGE = "de"  # type: ignore
