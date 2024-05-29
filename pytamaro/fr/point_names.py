"""
Noms de points particuliers, qui peuvent être utilisés comme des points d'ancrage pour des
graphiques.
"""

from __future__ import annotations

from pytamaro.point_names import (top_left, top_center, top_right,
                                  center_left, center, center_right,
                                  bottom_left, bottom_center, bottom_right)
from pytamaro.fr.point import Point


centre: Point = center
"""Le point central du cadre de délimitation du graphique

:meta hide-value:
"""


haut_centre: Point = top_center
"""Le point central du côté supérieur du cadre de délimitation du graphique

:meta hide-value:
"""

bas_centre: Point = bottom_center
"""Le point central du côté inférieur du cadre de délimitation du graphique

:meta hide-value:
"""

centre_gauche: Point = center_left
"""Le point central du côté gauche du cadre de délimitation du graphique

:meta hide-value:
"""


centre_droite: Point = center_right
"""Le point central du côté droit du cadre de délimitation du graphique

:meta hide-value:
"""


haut_gauche: Point = top_left
"""Le coin en haut à gauche du cadre de délimitation du graphique

:meta hide-value:
"""

haut_droite: Point = top_right
"""Le coin en haut à droite du cadre de délimitation du graphique

:meta hide-value:
"""

bas_gauche: Point = bottom_left
"""Le coin en bas à gauche du cadre de délimitation du graphique

:meta hide-value:
"""

bas_droite: Point = bottom_right
"""Le coin en bas à droite du cadre de délimitation du graphique

:meta hide-value:
"""
