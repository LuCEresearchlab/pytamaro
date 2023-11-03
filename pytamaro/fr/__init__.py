"""
(Re-)Export Italian names for:
- basic types (Graphic and Color)
- color names
- operations
- primitves
- I/O
from this top-level module.
"""


import sys

from pytamaro.it.color import *
from pytamaro.it.color_names import *
from pytamaro.it.graphic import *
from pytamaro.it.io import *
from pytamaro.it.operations import *
from pytamaro.it.primitives import *
from pytamaro.it.point_names import *

setattr(sys.modules["pytamaro"], "LANGUAGE", "it")
