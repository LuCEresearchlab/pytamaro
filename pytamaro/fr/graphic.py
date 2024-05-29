"""
Type `Graphique`, qui inclut un graphique avec un point d'ancrage.
"""

from __future__ import annotations

from pytamaro.graphic import Graphic

Graphique = Graphic
"""
Un graphique (image) avec un point d'ancrage.

Le point d'ancrage est utilisé pour les opérations suivantes:

- rotation (pour déterminer le centre de rotation)
- composition de graphiques (deux graphiques sont composés en alignant leur point
  d'ancrage).
"""
