"""
Tipo `Colore`, funzioni per produrre colori e costanti per colori notevoli.
"""

from __future__ import annotations

from pytamaro.color import Color
from pytamaro.color_functions import rgb_color, hsl_color, hsv_color

Colore = Color
"""
Rappresenta un colore.
Un colore ha anche un grado di opacità,
da completamente trasparente (come il colore `trasparente`)
a completamente opaco (come il colore `rosso`).
"""


def colore_rgb(rosso: int, verde: int, blu: int, opacita: float = 1.0) -> Colore:
    """
    Ritorna un colore con le componenti indicate per rosso (R), verde (G) e blu (B) e un
    certo grado di opacità (alpha, A).

    .. figure:: https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/RGBCube_a.svg/524px-RGBCube_a.svg.png
       :height: 120px
       :align: center

       `Cubo RGB (SharkD via Wikimedia Commons) <https://commons.wikimedia.org/wiki/File:RGBCube_a.svg>`_

    :param rosso: componente rosso [0-255]
    :param verde: componente verde [0-255]
    :param blu: componente blu [0-255]
    :param opacita: opacità (alpha) del colore, dove 0 significa completamente
           trasparente e 1 completamente opaco.
           Di default, tutti i colori sono completamente opachi.
    :returns: un colore con le componenti RGBA indicate
    """
    return rgb_color(rosso, verde, blu, opacita)


def colore_hsv(tonalita: float, saturazione: float, valore: float, opacita: float = 1.0) -> Colore:
    """
    Ritorna un colore con la tonalità (H), saturazione (S) e valore (V) indicati,
    e un certo grado di opacità (alpha, A).

    .. figure:: https://upload.wikimedia.org/wikipedia/commons/4/4e/HSV_color_solid_cylinder.png
       :height: 120px
       :align: center

       `Cilindro HSV (SharkD via Wikimedia Commons) <https://commons.wikimedia.org/wiki/File:HSV_color_solid_cylinder.png>`_

    :param tonalita: tonalità del colore [0-360]
    :param saturazione: saturazione del colore [0-1]
    :param valore: quantità di luce applicata [0-1]
    :param opacita: opacità (alpha) del colore, dove 0 significa completamente
           trasparente e 1 completamente opaco.
           Di default, tutti i colori sono completamente opachi.
    :returns: un colore con le componenti HSVA indicate
    """
    return hsv_color(tonalita, saturazione, valore, opacita)


def colore_hsl(tonalita: float, saturazione: float, luce: float, opacita: float = 1.0) -> Colore:
    """
    Ritorna un colore con la tonalità (H), saturazione (S) e luce (L) indicati,
    e un certo grado di opacità (alpha, A).

    .. figure:: https://upload.wikimedia.org/wikipedia/commons/3/35/HSL_color_solid_cylinder.png
       :height: 120px
       :align: center

       `Cilindro HSL: SharkD via Wikimedia Commons <https://commons.wikimedia.org/wiki/File:HSL_color_solid_cylinder.png>`_

    :param tonalita: tonalità del colore [0-360]
    :param saturazione: saturazione del colore [0-1]
    :param luce: quantità di bianco o nero applicata [0-1].
           Colori completamente saturi hanno un valore di luce di 1/2.
    :param opacita: opacità (alpha) del colore, dove 0 significa completamente
           trasparente e 1 completamente opaco.
           Di default, tutti i colori sono completamente opachi.
    :returns: un colore con le componenti HSLA indicate
    """
    return hsl_color(tonalita, saturazione, luce, opacita)
