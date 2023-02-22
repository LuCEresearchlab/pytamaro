"""
Funktionen für Operationen mit Grafiken (hauptsächlich für deren Komposition).
"""

from __future__ import annotations

from pytamaro.de.graphic import Grafik
from pytamaro.de.point import Punkt
from pytamaro.operations import (above, beside, compose, graphic_height,
                                 graphic_width, overlay, pin, rotate)


def grafik_breite(grafik: Grafik) -> int:
    """
    Gibt die Breite (in Pixel) der gegebenen Grafik zurück.

    :param grafik: Grafik deren Breite gesucht ist
    :returns: Breite der Grafik
    """
    return graphic_width(grafik)


def grafik_hoehe(grafik: Grafik) -> int:
    """
    Gibt die Höhe (in Pixel) der gegebenen Grafik zurück.

    :param grafik: Grafik deren Höhe gesucht ist
    :returns: Höhe der Grafik
    """
    return graphic_height(grafik)


def kombiniere(vordere_grafik: Grafik, hintere_grafik: Grafik) \
        -> Grafik:
    """
    Erzeugt eine neue Grafik,
    die aus der Kombination der zwei gegebenen Grafiken besteht.
    Die erste gegebene Grafik liegt im Vordergrund
    und die zweite im Hintergrund.
    Die Grafiken werden so ausgerichtet,
    dass ihre Fixierungspositionen übereinanderliegen.

    Die überlappenden Fixierungspositionen werden zur Fixierungsposition der
    resultierenden Grafik.

    :param vordere_grafik: Grafik im Vordergrund
    :param hintere_grafik: Grafik im Hintergrund
    :returns: die zusammengesetzte Grafik
    """
    return compose(vordere_grafik, hintere_grafik)


def fixiere(punkt: Punkt, grafik: Grafik) -> Grafik:
    """
    Erzeugt eine neue Grafik,
    die der gegebenen Grafik mit einer neuen Fixierungsposition entspricht.

    Jede Grafik liegt in einem rechteckigen Begrenzungsrahmen.
    Der Rahmen definiert 9 nennenswerte Punkte:
    die vier Ecken, die Mittelpunkte der vier Kanten und die Mitte des Rahmens.
    Die Namen dieser Punkte sind: `oben_links`, `oben_mitte`, `oben_rechts`,
    `mitte_links`, `mitte`, `mitte_rechts`, `unten_links`, `unten_mitte` und `unten_rechts`.

    :param point: ein Punkt welcher die neue Fixierungsposition bestimmt
    :param graphic: die ursprüngliche Grafik
    :returns: eine neue Grafik mit der gegebenen Fixierungsposition
    """
    return pin(punkt, grafik)


def ueberlagere(vordere_grafik: Grafik, hintere_grafik: Grafik) \
        -> Grafik:
    """
    Erzeugt eine neue Grafik,
    die aus der zentrierten Überlagerung der zwei gegebenen Grafiken besteht.
    Die erste gegebene Grafik liegt im Vordergrund
    und die zweite im Hintergrund.
    
    Die Fixierungsposition der neuen Grafik liegt in deren Mitte.

    :param vordere_grafik: Grafik im Vordergrund
    :param hintere_grafik: Grafik im Hintergrund
    :returns: die zusammengesetzte Grafik
    """
    return overlay(vordere_grafik, hintere_grafik)


def neben(linke_grafik: Grafik, rechte_grafik: Grafik) -> Grafik:
    """
    Erzeugt eine neue Grafik,
    die aus dem Nebeneinanderlegen der zwei gegebenen Grafiken besteht.
    Die zwei Grafiken sind vertikal zentriert.

    Die Fixierungsposition der neuen Grafik liegt in deren Mitte.

    :param linke_grafik: linke Grafik (im Westen)
    :param rechte_grafik: rechte Grafik (im Osten)
    :returns: die zusammengesetzte Grafik
    """
    return beside(linke_grafik, rechte_grafik)


def ueber(obere_grafik: Grafik, untere_grafik: Grafik) -> Grafik:
    """
    Erzeugt eine neue Grafik,
    die aus dem Übereinanderlegen der zwei gegebenen Grafiken besteht.
    Die zwei Grafiken sind horizontal zentriert.

    Die Fixierungsposition der neuen Grafik liegt in deren Mitte.

    :param obere_grafik: obere Grafik (im Norden)
    :param untere_grafik: untere Grafik (im Süden)
    :returns: die zusammengesetzte Grafik
    """
    return above(obere_grafik, untere_grafik)


def drehe(winkel: float, grafik: Grafik) -> Grafik:
    """
    Erzeugt eine neue Grafik, die einer Rotation der gegebenen Grafik
    um ihre Fixierungsposition im Gegenuhrzeigersinn
    um den gegebenen Winkel entspricht.
    Negative Winkel entsprechen einer Rotation um Uhrzeigersinn.

    Es kann wegen der Approximation auf die nächstgelegenen Pixel
    zu kleinen Rundungsfehlern kommen.

    :param winkel: Drehwinkel, in Grad im Gegenuhrzeigersinn
    :param grafik: zu rotierende Grafik
    :returns: die neue, rotierte Grafik
    """
    return rotate(winkel, grafik)
