"""
Der Typ `Farbe`, Funktionen, die Farben erzeugen
und Konstanten für wichtige Farben.
"""

from __future__ import annotations

from pytamaro.color import Color, rgb_color, hsv_color, hsl_color

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

    :param rot: die rote Farb-Komponente [0-255]
    :param gruen: die grüne Farb-Komponente [0-255]
    :param blau: die blaue Farb-Komponente [0-255]
    :param alpha: die alpha-Komponente (Undurchsichtigkeit, Opazität),
                  wobei 0 komplett durchsichtig und 1 komplett undurchsichtig
                  entspricht
    :returns: eine Farbe mit den gegebenen RGBA-Komponenten
    """
    return rgb_color(rot, gruen, blau, alpha)


def hsv_farbe(hue: float, saturation: float, value: float, alpha: float = 1.0) -> Farbe:
    """
    Returns a color with the provided hue, saturation, value and a
    certain degree of transparency controlled by `alpha`.

    :param hue: hue of the color [0-360]
    :param saturation: saturation of the color [0-1]
    :param value: the amount of light that is applied [0-1]
    :param alpha: alpha (transparency) component where 0 means fully
           transparent and 1 fully opaque. By default, all colors are fully opaque
    :returns: a color with the provided HSV components.
    """
    return hsv_color(hue, saturation, value, alpha)


def hsl_farbe(hue: float, saturation: float, lightness: float, alpha: float = 1.0) -> Farbe:
    """
    Returns a color with the provided hue, saturation, lightness and a
    certain degree of transparency controlled by `alpha`.

    :param hue: hue of the color [0-360]
    :param saturation: saturation of the color [0-1]
    :param lightness: the amount of white or black applied [0-1].
            Fully saturated colors have a lightness value of 1/2
    :param alpha: alpha (transparency) component where 0 means fully
           transparent and 1 fully opaque. By default, all colors are fully opaque
    :returns: a color with the provided HSL components.
    """
    return hsl_color(hue, saturation, lightness, alpha)
