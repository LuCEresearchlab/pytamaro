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
    Erzeugt eine Farbe mit den gegebenen Anteilen Rot (R), Grün (G), Blau (B)
    und der Opazität (Undurchsichtigkeit) `alpha`.

    :param rot: der rote Farbanteil [0-255]
    :param gruen: der grüne Farbanteil [0-255]
    :param blau: der blaue Farbanteil [0-255]
    :param alpha: die Opazität (Undurchsichtigkeit),
           wobei 0 komplett durchsichtig und 1 komplett undurchsichtig
           entspricht. Standardmäßig sind alle Farben vollständig undurchsichtig
    :returns: eine Farbe mit den gegebenen RGBA-Komponenten
    """
    return rgb_color(rot, gruen, blau, alpha)


def hsv_farbe(farbton: float, saettigung: float, hellwert: float, alpha: float = 1.0) -> Farbe:
    """
    Erzeugt eine Farbe mit dem gegebenen Farbton (H), der Sättigung (S),
    dem Hellwert (V) und der Opazität (Undurchsichtigkeit) `alpha`.

    :param farbton: der Farbton (hue) [0-360] als Farbwinkel, in Grad,
           auf dem Farbkreis (0 für Rot, 120 für Grün, 240 für Blau)
    :param saettigung: Farbsättigung (saturation) [0-1]
           (0 = Grau, 0.5 = wenig gesättigte Farbe, 1 = gesättigte, reine Farbe)
    :param hellwert: Hellwert (value) der Farbe [0-1]
           (0 = dunkel, 1 = hell)
    :param alpha: die Opazität (Undurchsichtigkeit),
           wobei 0 komplett durchsichtig und 1 komplett undurchsichtig
           entspricht. Standardmäßig sind alle Farben vollständig undurchsichtig
    :returns: eine Farbe mit den gegebenen HSVA-Komponenten
    """
    return hsv_color(farbton, saettigung, hellwert, alpha)


def hsl_farbe(farbton: float, saettigung: float, helligkeit: float, alpha: float = 1.0) -> Farbe:
    """
    Erzeugt eine Farbe mit dem gegebenen Farbton (H), der Sättigung (S),
    dem Helligkeit (L) und der Opazität (Undurchsichtigkeit) `alpha`.

    :param farbton: der Farbton (hue) [0-360] als Farbwinkel, in Grad,
           auf dem Farbkreis (0 für Rot, 120 für Grün, 240 für Blau)
    :param saettigung: Farbsättigung (saturation) [0-1]
           (0 = Grau, 0.5 = wenig gesättigte Farbe, 1 = gesättigte, reine Farbe)
    :param helligkeit: der Anteil Schwarz oder Weiss [0-1].
           (0 = Schwarz, 0.5 = weder abgedunkelt noch aufgehellt, 1 = Weiss)
    :param alpha: die Opazität (Undurchsichtigkeit),
           wobei 0 komplett durchsichtig und 1 komplett undurchsichtig
           entspricht. Standardmäßig sind alle Farben vollständig undurchsichtig
    :returns: eine Farbe mit den gegebenen HSLA-Komponenten
    """
    return hsl_color(farbton, saettigung, helligkeit, alpha)
