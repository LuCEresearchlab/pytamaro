"""
Nomi di punti notevoli, che possono essere usati come posizioni di fissaggio per
una grafica.
"""

from __future__ import annotations

from pytamaro.point_names import (top_left, top_center, top_right,
                                  center_left, center, center_right,
                                  bottom_left, bottom_center, bottom_right)
from pytamaro.it.point import Punto


centro: Punto = center
"""Il punto centrale del rettangolo di delimitazione della grafica

:meta hide-value:
"""


alto_centro: Punto = top_center
"""Il punto centrale del lato superiore del rettangolo di delimitazione della grafica

:meta hide-value:
"""

basso_centro: Punto = bottom_center
"""Il punto centrale del lato inferiore del rettangolo di delimitazione della grafica

:meta hide-value:
"""

centro_sinistra: Punto = center_left
"""Il punto centrale del lato sinistro del rettangolo di delimitazione della grafica

:meta hide-value:
"""


centro_destra: Punto = center_right
"""Il punto centrale del lato destro del rettangolo di delimitazione della grafica

:meta hide-value:
"""


alto_sinistra: Punto = top_left
"""Il vertice in alto a sinistra del rettangolo di delimitazione della grafica

:meta hide-value:
"""

alto_destra: Punto = top_right
"""Il vertice in alto a destra del rettangolo di delimitazione della grafica

:meta hide-value:
"""

basso_sinistra: Punto = bottom_left
"""Il vertice in basso a sinistra del rettangolo di delimitazione della grafica

:meta hide-value:
"""

basso_destra: Punto = bottom_right
"""Il vertice in basso a destra del rettangolo di delimitazione della grafica

:meta hide-value:
"""
