"""
Tipo `Grafica`, che include una grafica con una posizione di fissaggio.
"""

from __future__ import annotations

import pytamaro.graphic as _graphic_en

Grafica = _graphic_en.Graphic
"""
Una grafica (immagine) con una posizione per fissare.

La posizione di fissaggio viene usata nelle seguenti operazioni:

- rotazione (per determinare il centro di rotazione)
- composizione di grafiche (due grafiche vengono composte allineando le loro
  posizioni di fissaggio).
"""
