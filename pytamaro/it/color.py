"""
Tipo `Colore` e funzioni per produrre colori.
"""

from __future__ import annotations

from pytamaro.color import Color, rgb_color, hsv_color, hsl_color

Colore = Color
"""
Rappresenta un colore nello spazio colore RGBA (usando interi tra 0 e 255) .
"""


def colore_rgb(rosso: int, verde: int, blu: int, alpha: float = 1.0) -> Colore:
    """
    Ritorna un colore con le componenti indicate per rosso, verde e blu e un
    certo grado di trasparenza determinato da `alpha`.

    :param rosso: componente rosso (0 -- 255)
    :param verde: componente verde (0 -- 255)
    :param blu: componente blu (0 -- 255)
    :param alpha: componente alpha (trasparenza), dove 0 è completamente
                  trasparente e 1 completamente opaco
    :returns: un colore con le componenti RGBA indicate
    """
    return rgb_color(rosso, verde, blu, alpha)


def colore_hsv(tonalita: float, saturazione: float, valore: float, alpha: float = 1.0) -> Colore:
    """
    Ritorna un colore con la tonalità, la saturazione, il `valore` forniti e un certo
    grado di trasparenza determinato da `alpha`

    :param tonalita: tinta del colore (0 - 360)
    :param saturazione: saturazione del colore (0, 1)
    :param valore: quantità di luce applicata (0, 1)
    :param alpha: componente alpha (trasparenza), dove 0 è completamente
                  trasparente e 1 completamente opaco
    :returns: un colore con le componenti HSV indicate
    """
    chroma = valore * saturazione
    lato = (tonalita / 60) % 6
    x = chroma * (1 - abs(lato % 2 - 1))
    colore_fondo = (chroma, x, 0)
    if 2 > lato >= 1:
        colore_fondo = (x, chroma, 0)
    if 3 > lato >= 2:
        colore_fondo = (0, chroma, x)
    if 4 > lato >= 3:
        colore_fondo = (0, x, chroma)
    if 5 > lato >= 4:
        colore_fondo = (x, 0, chroma)
    if lato >= 5:
        colore_fondo = (chroma, 0, x)
    aggiunta = valore - chroma
    colore = tuple((x + aggiunta) * 255 for x in colore_fondo)
    return rgb_color(*colore, alpha)


def colore_hsl(tonalita: float, saturazione: float, luce: float, alpha: float = 1.0) -> Color:
    """
    Ritorna un colore con la tonalità, la saturazione, la luce forniti e un certo
    grado di trasparenza determinato da `alpha`

    :param tonalita: tinta del colore (0 - 360)
    :param saturazione: saturazione del colore (0, 1)
    :param luce: quantità di luce applicata (0, 1)
    :param alpha: componente alpha (trasparenza), dove 0 è completamente
                  trasparente e 1 completamente opaco
    :returns: un colore con le componenti HSL indicate
    """
    chroma = (1 - abs(2 * luce - 1)) * saturazione
    lato = (tonalita / 60) % 6
    x = chroma * (1 - abs(lato % 2 - 1))
    bottom_color = (chroma, x, 0)
    if 2 > lato >= 1:
        bottom_color = (x, chroma, 0)
    if 3 > lato >= 2:
        bottom_color = (0, chroma, x)
    if 4 > lato >= 3:
        bottom_color = (0, x, chroma)
    if 5 > lato >= 4:
        bottom_color = (x, 0, chroma)
    if lato >= 5:
        bottom_color = (chroma, 0, x)
    aggiunta = luce - chroma / 2
    colore = tuple((x + aggiunta) * 255 for x in bottom_color)
    return rgb_color(*colore, alpha)
