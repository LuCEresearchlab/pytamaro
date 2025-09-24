"""
Der Typ `Grafik`, kombiniert eine Grafik mit einer Fixierposition.
"""

from __future__ import annotations
from typing import TypeAlias

import pytamaro as _pytamaro

Grafik: TypeAlias = _pytamaro.Graphic
"""
Eine Grafik mit einer Fixierposition.

Die Fixierposition wird von den folgenden Operationen verwendet:

- `drehe` (das Rotationszentrum ist die Fixierposition)
- `kombiniere` (die zwei Grafiken werden so ausgerichtet,
  dass ihre Fixierpositionen übereinanderliegen).
"""
