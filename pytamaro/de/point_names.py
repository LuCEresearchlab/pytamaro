"""
Namen nennenswerter Punkte, die als Fixierpositionen für eine Grafik verwendet werden können
"""

from __future__ import annotations

import pytamaro as _pytamaro
from pytamaro.de.point import Punkt

mitte: Punkt = _pytamaro.center
"""Der Mittelpunkt des Begrenzungsrahmens

:meta hide-value:
"""


oben_mitte: Punkt = _pytamaro.top_center
"""Der Mittelpunkt der oberen Kante des Begrenzungsrahmens

:meta hide-value:
"""

unten_mitte: Punkt = _pytamaro.bottom_center
"""Der Mittelpunkt der unteren Kante des Begrenzungsrahmens

:meta hide-value:
"""

mitte_links: Punkt = _pytamaro.center_left
"""Der Mittelpunkt der linken Kante des Begrenzungsrahmens

:meta hide-value:
"""


mitte_rechts: Punkt = _pytamaro.center_right
"""Der Mittelpunkt der rechten Kante des Begrenzungsrahmens

:meta hide-value:
"""


oben_links: Punkt = _pytamaro.top_left
"""Die obere linke Ecke des Begrenzungsrahmens

:meta hide-value:
"""

oben_rechts: Punkt = _pytamaro.top_right
"""Die obere rechte Ecke des Begrenzungsrahmens

:meta hide-value:
"""

unten_links: Punkt = _pytamaro.bottom_left
"""Die untere linke Ecke des Begrenzungsrahmens

:meta hide-value:
"""

unten_rechts: Punkt = _pytamaro.bottom_right
"""Die untere rechte Ecke des Begrenzungsrahmens

:meta hide-value:
"""
