"""
Funktionen für Operationen mit Grafiken (hauptsächlich für deren Komposition).
"""

from __future__ import annotations

from pytamaro.de.graphic import Grafik
from pytamaro.operations import (above, beside, compose, graphic_height,
                                 graphic_width, overlay, pin, rotate)
from pytamaro.point import Point
from pytamaro import Graphic


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


def fixiere(point: Point, graphic: Graphic) -> Graphic:
    """
    Need to translate
    Changes the pinning position of a graphic, returning a new graphic with
    the same content but with an updated pinning position.
    The new pinning position is determined by the parameter `point`.

    :param point: a point that identifies one of the 9 points of interest.
    Each graphic is contained in a rectangular bounding box, the 9 points corresponds to:
    the four corners, the middle point of the four edges and the center of the rectangle.
    The names of these points are: `top_left`, `top_right`, `bottom_left`, `bottom_right`,
    `top_center`, `center_right`, `bottom_center`, `center_left` and `center`
    :param graphic: original graphic
    :returns: a new graphic with an updated pinning position
    """
    return pin(point, graphic)


def ueberlagere(vordere_grafik: Grafik, hintere_grafik: Grafik) \
        -> Grafik:
    """
    Erzeugt eine neue Grafik,
    die aus der zentrierten Überlagerung der zwei gegebenen Grafiken besteht.
    Die erste gegebene Grafik liegt im Vordergrund
    und die zweite im Hintergrund,
    und ihre Fixierungspositionen liegen übereinander im Zentrum.

    The pinning position of the resulting graphic is at its center.

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

    The pinning position of the resulting graphic is at its center.

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

    The pinning position of the resulting graphic is at its center.

    :param obere_grafik: obere Grafik (im Norden)
    :param untere_grafik: untere Grafik (im Süden)
    :returns: die zusammengesetzte Grafik
    """
    return above(obere_grafik, untere_grafik)


def drehe(grad: float, grafik: Grafik) -> Grafik:
    """
    Erzeugt eine neue Grafik, die einer Rotation der gegebenen Grafik
    um ihre Fixierungsposition im Gegenuhrzeigersinn
    um den gegebenen Winkel entspricht.

    Es kann wegen der Approximation auf die nächstgelegenen Pixel
    zu kleinen Rundungsfehlern kommen.

    :param grad: Drehwinkel, in Grad im Gegenuhrzeigersinn
    :param grafik: zu rotierende Grafik
    :returns: die neue, rotierte Grafik
    """
    return rotate(grad, grafik)
