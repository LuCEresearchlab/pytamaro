"""
Classe `Grafica`, che racchiude un'immagine Pillow e una posizione per fissare.
"""

from __future__ import annotations

from pytamaro.graphic import Graphic

Grafica = Graphic
"""
Una grafica (immagine) con una posizione per fissare.

La posizione per fissare viene usata nelle seguenti operazioni:

- rotazione (per determinare il centro di rotazione)
- composizione di grafiche (due grafiche vengono composte allineando le loro
  posizioni di fissaggio).
"""
