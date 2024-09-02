"""
Nomi di punti notevoli, che possono essere usati come posizioni di fissaggio per
una grafica.
"""

from __future__ import annotations

import pytamaro as _pytamaro
from pytamaro.it.point import Punto

centro: Punto = _pytamaro.center
"""Il punto centrale del rettangolo di delimitazione della grafica

:meta hide-value:
"""


alto_centro: Punto = _pytamaro.top_center
"""Il punto centrale del lato superiore del rettangolo di delimitazione della grafica

:meta hide-value:
"""

basso_centro: Punto = _pytamaro.bottom_center
"""Il punto centrale del lato inferiore del rettangolo di delimitazione della grafica

:meta hide-value:
"""

centro_sinistra: Punto = _pytamaro.center_left
"""Il punto centrale del lato sinistro del rettangolo di delimitazione della grafica

:meta hide-value:
"""


centro_destra: Punto = _pytamaro.center_right
"""Il punto centrale del lato destro del rettangolo di delimitazione della grafica

:meta hide-value:
"""


alto_sinistra: Punto = _pytamaro.top_left
"""Il vertice in alto a sinistra del rettangolo di delimitazione della grafica

:meta hide-value:
"""

alto_destra: Punto = _pytamaro.top_right
"""Il vertice in alto a destra del rettangolo di delimitazione della grafica

:meta hide-value:
"""

basso_sinistra: Punto = _pytamaro.bottom_left
"""Il vertice in basso a sinistra del rettangolo di delimitazione della grafica

:meta hide-value:
"""

basso_destra: Punto = _pytamaro.bottom_right
"""Il vertice in basso a destra del rettangolo di delimitazione della grafica

:meta hide-value:
"""
