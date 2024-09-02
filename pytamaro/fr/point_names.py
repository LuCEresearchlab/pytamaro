"""
Noms de points particuliers, qui peuvent être utilisés comme des points d'ancrage pour des
graphiques.
"""

from __future__ import annotations

import pytamaro as _pytamaro
from pytamaro.fr.point import Point

centre: Point = _pytamaro.center
"""Le point central du cadre de délimitation du graphique

:meta hide-value:
"""


haut_centre: Point = _pytamaro.top_center
"""Le point central du côté supérieur du cadre de délimitation du graphique

:meta hide-value:
"""

bas_centre: Point = _pytamaro.bottom_center
"""Le point central du côté inférieur du cadre de délimitation du graphique

:meta hide-value:
"""

centre_gauche: Point = _pytamaro.center_left
"""Le point central du côté gauche du cadre de délimitation du graphique

:meta hide-value:
"""


centre_droite: Point = _pytamaro.center_right
"""Le point central du côté droit du cadre de délimitation du graphique

:meta hide-value:
"""


haut_gauche: Point = _pytamaro.top_left
"""Le coin en haut à gauche du cadre de délimitation du graphique

:meta hide-value:
"""

haut_droite: Point = _pytamaro.top_right
"""Le coin en haut à droite du cadre de délimitation du graphique

:meta hide-value:
"""

bas_gauche: Point = _pytamaro.bottom_left
"""Le coin en bas à gauche du cadre de délimitation du graphique

:meta hide-value:
"""

bas_droite: Point = _pytamaro.bottom_right
"""Le coin en bas à droite du cadre de délimitation du graphique

:meta hide-value:
"""
