"""(Re-)Export French names for:
- basic types (Graphic and Color)
- color names
- operations
- primitves
- I/O
from this top-level module.
"""  # noqa: D205

import sys

# ruff: noqa: F403
from pytamaro.fr.color import *
from pytamaro.fr.color_names import *
from pytamaro.fr.graphic import *
from pytamaro.fr.io import *
from pytamaro.fr.operations import *
from pytamaro.fr.point_names import *
from pytamaro.fr.primitives import *

sys.modules["pytamaro"].LANGUAGE = "fr"  # type: ignore
