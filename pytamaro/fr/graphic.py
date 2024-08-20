"""
Type `Graphique`, qui inclut un graphique avec un point d'ancrage.
"""

from __future__ import annotations

import pytamaro.graphic as _graphic_en

Graphique = _graphic_en.Graphic
"""
Un graphique (image) avec un point d'ancrage.

Le point d'ancrage est utilisé pour les opérations suivantes:

- rotation (pour déterminer le centre de rotation)
- composition de graphiques (deux graphiques sont composés en alignant leur point
  d'ancrage).
"""
