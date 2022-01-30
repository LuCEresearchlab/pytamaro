"""
Klasse `Grafik`, kombiniert ein Pillow Bild und eine Fixier-Position.
"""

from __future__ import annotations

from pytamaro.graphic import Graphic

Grafik = Graphic
"""
Eine Grafik mit einer Fixierposition.

Die Fixierposition wird von den folgenden Operationen verwendet:

- `drehe` (das Rotationszentrum ist die Fixierposition)
- `kombiniere` (die zwei Grafiken werden so ausgerichtet,
  dass ihre Fixierpositionen übereinanderliegen).
"""
