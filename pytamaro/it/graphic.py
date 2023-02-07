"""
Tipo `Grafica`, che include una grafica con una posizione di fissaggio.
"""

from __future__ import annotations

from pytamaro.graphic import Graphic

Grafica = Graphic
"""
Una grafica (immagine) con una posizione per fissare.

La posizione di fissaggio viene usata nelle seguenti operazioni:

- rotazione (per determinare il centro di rotazione)
- composizione di grafiche (due grafiche vengono composte allineando le loro
  posizioni di fissaggio).
"""
