"""
Der Typ `Farbe`, Funktionen, die Farben erzeugen
und Konstanten für wichtige Farben.
"""

from __future__ import annotations

from pytamaro.color import Color, rgb_color

Farbe = Color
"""
Repräsentiert eine Farbe.
Eine Farbe hat auch eine gewisse Durchsichtigkeit,
von komplett undurchsichtig, wie die Farbe `rot`,
bis komplett durchsichtig, wie die Farbe `transparent`.
"""


def rgb_farbe(rot: int, gruen: int, blau: int, alpha: float = 1.0) -> Farbe:
    """
    Erzeugt eine Farbe mit den gegebenen Komponenten für Rot, Grün, Blau,
    und die Opazität (Undurchsichtigkeit) `alpha` (RGBA).

    :param rot: die rote Farb-Komponente (0 -- 255)
    :param gruen: die grüne Farb-Komponente (0 -- 255)
    :param blau: die blaue Farb-Komponente (0 -- 255)
    :param alpha: die alpha-Komponente (Undurchsichtigkeit, Opazität),
                  wobei 0 komplett durchsichtig und 1 komplett undurchsichtig
                  entspricht
    :returns: eine Farbe mit den gegebenen RGBA-Komponenten
    """
    return rgb_color(rot, gruen, blau, alpha)


def hsv_farbe(hue: float, saturation: float, value: float, alpha: float = 1.0) -> Color:
    """
    Returns a color with the provided hue, saturation, value and a
    certain degree of transparency controlled by `alpha`.
    The parameters are converted to RGB and used to get the color with rgb_color().

    :param hue: hue of the color (0 - 360)
    :param saturation: saturation of the color (0, 1)
    :param value: the amount of light that is applied (0, 1)
    :param alpha: alpha (transparency) component where 0 means fully
           transparent and 1 fully opaque. By default, all colors are fully opaque
    :returns: a color with the provided HSV components.
    """
    chroma = value * saturation
    side = (hue / 60) % 6
    x = chroma * (1 - abs(side % 2 - 1))
    bottom_color = (chroma, x, 0)
    if 2 > side >= 1:
        bottom_color = (x, chroma, 0)
    if 3 > side >= 2:
        bottom_color = (0, chroma, x)
    if 4 > side >= 3:
        bottom_color = (0, x, chroma)
    if 5 > side >= 4:
        bottom_color = (x, 0, chroma)
    if side >= 5:
        bottom_color = (chroma, 0, x)
    to_add = value - chroma
    color = tuple((x + to_add) * 255 for x in bottom_color)
    return rgb_color(*color, alpha)


def hsl_farbe(hue: float, saturation: float, lightness: float, alpha: float = 1.0) -> Color:
    """
    Returns a color with the provided hue, saturation, lightness  and a
    certain degree of transparency controlled by `alpha`.
    The parameters are converted to RGB and used to get the color with rgb_color().

    :param hue: hue of the color (0 - 360)
    :param saturation: saturation of the color (0, 1)
    :param lightness: the amount of white or black applied (0, 1).
            Fully saturated colors have a lightness value of 1/2
    :param alpha: alpha (transparency) component where 0 means fully
           transparent and 1 fully opaque. By default, all colors are fully opaque
    :returns: a color with the provided HSL components.
    """
    chroma = (1 - abs(2 * lightness - 1)) * saturation
    side = (hue / 60) % 6
    x = chroma * (1 - abs(side % 2 - 1))
    bottom_color = (chroma, x, 0)
    if 2 > side >= 1:
        bottom_color = (x, chroma, 0)
    if 3 > side >= 2:
        bottom_color = (0, chroma, x)
    if 4 > side >= 3:
        bottom_color = (0, x, chroma)
    if 5 > side >= 4:
        bottom_color = (x, 0, chroma)
    if side >= 5:
        bottom_color = (chroma, 0, x)
    to_add = lightness - chroma / 2
    color = tuple((x + to_add) * 255 for x in bottom_color)
    return rgb_color(*color, alpha)