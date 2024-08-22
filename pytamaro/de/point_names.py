"""
Namen nennenswerter Punkte, die als Fixierpositionen für eine Grafik verwendet werden können
"""

from __future__ import annotations

from pytamaro.de.point import Punkt
import pytamaro as _en


mitte: Punkt = _en.center
"""Der Mittelpunkt des Begrenzungsrahmens

:meta hide-value:
"""


oben_mitte: Punkt = _en.top_center
"""Der Mittelpunkt der oberen Kante des Begrenzungsrahmens

:meta hide-value:
"""

unten_mitte: Punkt = _en.bottom_center
"""Der Mittelpunkt der unteren Kante des Begrenzungsrahmens

:meta hide-value:
"""

mitte_links: Punkt = _en.center_left
"""Der Mittelpunkt der linken Kante des Begrenzungsrahmens

:meta hide-value:
"""


mitte_rechts: Punkt = _en.center_right
"""Der Mittelpunkt der rechten Kante des Begrenzungsrahmens

:meta hide-value:
"""


oben_links: Punkt = _en.top_left
"""Die obere linke Ecke des Begrenzungsrahmens

:meta hide-value:
"""

oben_rechts: Punkt = _en.top_right
"""Die obere rechte Ecke des Begrenzungsrahmens

:meta hide-value:
"""

unten_links: Punkt = _en.bottom_left
"""Die untere linke Ecke des Begrenzungsrahmens

:meta hide-value:
"""

unten_rechts: Punkt = _en.bottom_right
"""Die untere rechte Ecke des Begrenzungsrahmens

:meta hide-value:
"""
