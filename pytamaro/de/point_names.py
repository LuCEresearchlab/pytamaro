"""
Namen nennenswerter Punkte, die als Fixierpositionen für eine Grafik verwendet werden können
"""

from __future__ import annotations

from pytamaro.point_names import (top_left, top_center, top_right,
                                  center_left, center, center_right,
                                  bottom_left, bottom_center, bottom_right)
from pytamaro.de.point import Punkt


mitte: Punkt = center
"""Der Mittelpunkt des Begrenzungsrahmens

:meta hide-value:
"""


oben_mitte: Punkt = top_center
"""Der Mittelpunkt der oberen Kante des Begrenzungsrahmens

:meta hide-value:
"""

unten_mitte: Punkt = bottom_center
"""Der Mittelpunkt der unteren Kante des Begrenzungsrahmens

:meta hide-value:
"""

mitte_links: Punkt = center_left
"""Der Mittelpunkt der linken Kante des Begrenzungsrahmens

:meta hide-value:
"""


mitte_rechts: Punkt = center_right
"""Der Mittelpunkt der rechten Kante des Begrenzungsrahmens

:meta hide-value:
"""


oben_links: Punkt = top_left
"""Die obere linke Ecke des Begrenzungsrahmens

:meta hide-value:
"""

oben_rechts: Punkt = top_right
"""Die obere rechte Ecke des Begrenzungsrahmens

:meta hide-value:
"""

unten_links: Punkt = bottom_left
"""Die untere linke Ecke des Begrenzungsrahmens

:meta hide-value:
"""

unten_rechts: Punkt = bottom_right
"""Die untere rechte Ecke des Begrenzungsrahmens

:meta hide-value:
"""
