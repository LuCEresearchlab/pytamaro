"""
(Re-)Export German names for:
- basic types (Graphic and Color)
- color names
- operations
- primitves
- I/O
from this top-level module.
"""


import sys

from pytamaro.de.color import *
from pytamaro.de.color_names import *
from pytamaro.de.graphic import *
from pytamaro.de.io import *
from pytamaro.de.operations import *
from pytamaro.de.primitives import *

setattr(sys.modules["pytamaro"], "LANGUAGE", "de")
