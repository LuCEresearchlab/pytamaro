"""
Type `Graphisme`, qui inclue un graphisme avec un point d'ancrage.
"""

from __future__ import annotations

from pytamaro.graphic import Graphic

Graphisme = Graphic
"""
Un graphisme (image) avec un point à ancrer.

Le point d'ancrage est utilisé pour les opérations suivantes:

- rotation (pour déterminer le centre de rotation)
- composition de graphismes (deux graphismes sont composés en alignant leur point
  d'ancrage).
"""
