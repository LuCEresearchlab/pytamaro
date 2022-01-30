"""
Der Typ `Farbe`, Funktionen, die Farben erzeugen
und Konstanten für wichtige Farben.
"""

from __future__ import annotations

from pytamaro.color import Color, rgb_color, rgba_color

Farbe = Color
"""
Repräsentiert eine Farbe.
Eine Farbe hat auch eine gewisse Durchsichtigkeit,
von komplett undurchsichtig, wie die Farbe `rot`,
bis komplett durchsichtig, wie die Farbe `transparent`.
"""


def rgb_farbe(rot: int, gruen: int, blau: int) -> Farbe:
    """
    Erzeugt eine komplett opake (undurchsichtige) Farbe
    mit den gegebenen Rot-, Grün- und Blau-Komponenten (RGB).

    :param rot: die rote Farb-Komponente (0 -- 255)
    :param gruen: die grüne Farb-Komponente (0 -- 255)
    :param blau: die blaue Farb-Komponente (0 -- 255)
    :returns: eine Farbe mit den gegebenen RGB-Komponenten
    """
    return rgb_color(rot, gruen, blau)


def rgba_farbe(rot: int, gruen: int, blau: int, alpha: int) -> Farbe:
    """
    Erzeugt eine Farbe mit den gegebenen Komponenten für Rot, Grün, Blau,
    und die Opazität (Undurchsichtigkeit) `alpha` (RGBA).

    :param rot: die rote Farb-Komponente (0 -- 255)
    :param gruen: die grüne Farb-Komponente (0 -- 255)
    :param blau: die blaue Farb-Komponente (0 -- 255)
    :param alpha: die alpha-Komponente (Undurchsichtigkeit, Opazität),
                  wobei 0 komplett durchsichtig und 255 komplett undurchsichtig
                  entspricht
    :returns: eine Farbe mit den gegebenen RGBA-Komponenten
    """
    return rgba_color(rot, gruen, blau, alpha)
