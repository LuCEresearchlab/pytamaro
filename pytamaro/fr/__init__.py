"""
(Re-)Export French names for:
- basic types (Graphic and Color)
- color names
- operations
- primitves
- I/O
from this top-level module.
"""


import sys

from pytamaro.fr.color import *
from pytamaro.fr.color_names import *
from pytamaro.fr.graphic import *
from pytamaro.fr.io import *
from pytamaro.fr.operations import *
from pytamaro.fr.primitives import *
from pytamaro.fr.point_names import *

setattr(sys.modules["pytamaro"], "LANGUAGE", "fr")
