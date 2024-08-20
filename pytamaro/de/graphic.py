"""
Der Typ `Grafik`, kombiniert eine Grafik mit einer Fixierposition.
"""

from __future__ import annotations

import pytamaro.graphic as _graphic_en

Grafik = _graphic_en.Graphic
"""
Eine Grafik mit einer Fixierposition.

Die Fixierposition wird von den folgenden Operationen verwendet:

- `drehe` (das Rotationszentrum ist die Fixierposition)
- `kombiniere` (die zwei Grafiken werden so ausgerichtet,
  dass ihre Fixierpositionen übereinanderliegen).
"""
