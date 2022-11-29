"""
Tipo `Colore` e funzioni per produrre colori.
"""

from __future__ import annotations

from pytamaro.color import Color, rgb_color, hsl_color, hsv_color

Colore = Color
"""
Rappresenta un colore.
"""


def colore_rgb(rosso: int, verde: int, blu: int, alpha: float = 1.0) -> Colore:
    """
    Ritorna un colore con le componenti indicate per rosso, verde e blu e un
    certo grado di trasparenza determinato da `alpha`.

    .. figure:: https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/RGBCube_a.svg/524px-RGBCube_a.svg.png
       :height: 120px
       :align: center

       `Cubo RGB (SharkD via Wikimedia Commons) <https://commons.wikimedia.org/wiki/File:RGBCube_a.svg>`_

    :param rosso: componente rosso [0-255]
    :param verde: componente verde [0-255]
    :param blu: componente blu [0-255]
    :param alpha: componente alpha (trasparenza), dove 0 è completamente
                  trasparente e 1 completamente opaco
    :returns: un colore con le componenti RGBA indicate
    """
    return rgb_color(rosso, verde, blu, alpha)


def colore_hsv(tonalita: float, saturazione: float, valore: float, alpha: float = 1.0) -> Colore:
    """
    Ritorna un colore con la tonalità, la saturazione, il `valore` forniti e un certo
    grado di trasparenza determinato da `alpha`

    .. figure:: https://upload.wikimedia.org/wikipedia/commons/4/4e/HSV_color_solid_cylinder.png
       :height: 120px
       :align: center

       `Cilindro HSV (SharkD via Wikimedia Commons) <https://commons.wikimedia.org/wiki/File:HSV_color_solid_cylinder.png>`_

    :param tonalita: tinta del colore [0-360]
    :param saturazione: saturazione del colore [0-1]
    :param valore: quantità di luce applicata [0-1]
    :param alpha: componente alpha (trasparenza), dove 0 è completamente
                  trasparente e 1 completamente opaco
    :returns: un colore con le componenti HSV indicate
    """
    return hsv_color(tonalita, saturazione, valore, alpha)


def colore_hsl(tonalita: float, saturazione: float, luce: float, alpha: float = 1.0) -> Colore:
    """
    Ritorna un colore con la tonalità, la saturazione, la luce forniti e un certo
    grado di trasparenza determinato da `alpha`

    .. figure:: https://upload.wikimedia.org/wikipedia/commons/3/35/HSL_color_solid_cylinder.png
       :height: 120px
       :align: center

       `Cilindro HSL: SharkD via Wikimedia Commons <https://commons.wikimedia.org/wiki/File:HSL_color_solid_cylinder.png>`_

    :param tonalita: tinta del colore [0-360]
    :param saturazione: saturazione del colore [0-1]
    :param luce: quantità di luce applicata [0-1]
    :param alpha: componente alpha (trasparenza), dove 0 è completamente
                  trasparente e 1 completamente opaco
    :returns: un colore con le componenti HSL indicate
    """
    return hsl_color(tonalita, saturazione, luce, alpha)
