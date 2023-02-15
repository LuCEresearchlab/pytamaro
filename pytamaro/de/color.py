"""
Der Typ `Farbe`, Funktionen, die Farben erzeugen
und Konstanten für wichtige Farben.
"""

from __future__ import annotations

from pytamaro.color import Color
from pytamaro.color_functions import rgb_color, hsl_color, hsv_color

Farbe = Color
"""
Repräsentiert eine Farbe.
Eine Farbe hat auch eine gewisse Opazität,
von komplett durchsichtig (wie die Farbe `transparent`),
bis komplett undurchsichtig (wie die Farbe `rot`).
"""


def rgb_farbe(rot: int, gruen: int, blau: int, opazitaet: float = 1.0) -> Farbe:
    """
    Erzeugt eine Farbe mit den gegebenen Anteilen Rot (R), Grün (G) und Blau (B)
    und der gegebenen Opazität (Undurchsichtigkeit, alpha, A).

    .. figure:: https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/RGBCube_a.svg/524px-RGBCube_a.svg.png
       :height: 120px
       :align: center

       `RGB Würfel (SharkD via Wikimedia Commons) <https://commons.wikimedia.org/wiki/File:RGBCube_a.svg>`_

    :param rot: der rote Farbanteil [0-255]
    :param gruen: der grüne Farbanteil [0-255]
    :param blau: der blaue Farbanteil [0-255]
    :param opazitaet: die Undurchsichtigkeit (alpha),
           wobei 0 komplett durchsichtig und 1 komplett undurchsichtig
           entspricht. Standardmäßig sind alle Farben vollständig undurchsichtig.
    :returns: eine Farbe mit den gegebenen RGBA-Komponenten
    """
    return rgb_color(rot, gruen, blau, opazitaet)


def hsv_farbe(farbton: float, saettigung: float, hellwert: float, opazitaet: float = 1.0) -> Farbe:
    """
    Erzeugt eine Farbe mit dem gegebenen Farbton (H), der Sättigung (S),
    dem Hellwert (V) und der Opazität (Undurchsichtigkeit, alpha, A).

    .. figure:: https://upload.wikimedia.org/wikipedia/commons/4/4e/HSV_color_solid_cylinder.png
       :height: 120px
       :align: center

       `HSV Zylinder (SharkD via Wikimedia Commons) <https://commons.wikimedia.org/wiki/File:HSV_color_solid_cylinder.png>`_

    :param farbton: der Farbton (hue) [0-360] als Farbwinkel, in Grad,
           auf dem Farbkreis (0 für Rot, 120 für Grün, 240 für Blau)
    :param saettigung: Farbsättigung (saturation) [0-1]
           (0 = Grau, 0.5 = wenig gesättigte Farbe, 1 = gesättigte, reine Farbe)
    :param hellwert: Hellwert (value) der Farbe [0-1]
           (0 = dunkel, 1 = hell)
    :param opazitaet: die Undurchsichtigkeit (alpha),
           wobei 0 komplett durchsichtig und 1 komplett undurchsichtig
           entspricht. Standardmäßig sind alle Farben vollständig undurchsichtig.
    :returns: eine Farbe mit den gegebenen HSVA-Komponenten
    """
    return hsv_color(farbton, saettigung, hellwert, opazitaet)


def hsl_farbe(farbton: float, saettigung: float, helligkeit: float,
              opazitaet: float = 1.0) -> Farbe:
    """
    Erzeugt eine Farbe mit dem gegebenen Farbton (H), der Sättigung (S),
    dem Helligkeit (L) und der Opazität (Undurchsichtigkeit, alpha, A).

    .. figure:: https://upload.wikimedia.org/wikipedia/commons/3/35/HSL_color_solid_cylinder.png
       :height: 120px
       :align: center

       `HSL Zylinder: SharkD via Wikimedia Commons <https://commons.wikimedia.org/wiki/File:HSL_color_solid_cylinder.png>`_

    :param farbton: der Farbton (hue) [0-360] als Farbwinkel, in Grad,
           auf dem Farbkreis (0 für Rot, 120 für Grün, 240 für Blau)
    :param saettigung: Farbsättigung (saturation) [0-1]
           (0 = Grau, 0.5 = wenig gesättigte Farbe, 1 = gesättigte, reine Farbe)
    :param helligkeit: der Anteil Schwarz oder Weiss [0-1].
           (0 = Schwarz, 0.5 = weder abgedunkelt noch aufgehellt, 1 = Weiss)
    :param opazitaet: die Undurchsichtigkeit (alpha),
           wobei 0 komplett durchsichtig und 1 komplett undurchsichtig
           entspricht. Standardmäßig sind alle Farben vollständig undurchsichtig.
    :returns: eine Farbe mit den gegebenen HSLA-Komponenten
    """
    return hsl_color(farbton, saettigung, helligkeit, opazitaet)
