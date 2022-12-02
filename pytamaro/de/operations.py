"""
Funktionen für Operationen mit Grafiken (hauptsächlich für deren Komposition).
"""

from __future__ import annotations

from pytamaro.de.graphic import Grafik
from pytamaro.operations import (above, beside, compose, graphic_height,
                                 graphic_width, overlay, pin, rotate)
# Remove this imports after translation
from pytamaro.de.point_names import (german_top_left, german_top_center, german_top_right,
                                     german_center_left, german_center, german_center_right,
                                     german_bottom_left, german_bottom_center, german_bottom_right)
from pytamaro.point_names import (top_left, top_center, top_right,
                                  center_left, center, center_right,
                                  bottom_left, bottom_center, bottom_right)
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


def fixiere(pinning_point: Point, graphic: Graphic) -> Graphic:
    """
    Need to translate
    Changes the pinning position of a graphic, returning a new graphic with
    the same content but with an updated pinning position.
    The new pinning position is determined by the parameter `pinning_point`.

    :param pinning_point: an object of type `Point` that identifies one of the 9 points of interest.
    The accepted points are:
        center = point(0.0, 0.0)
        top_left = point(-1.0, 1.0)
        top_center = point(0.0, 1.0)
        top_right = point(1.0, 1.0)
        center_left = point(-1.0, 0.0)
        center_right = point(1.0, 0.0)
        bottom_left = point(-1.0, -1.0)
        bottom_center = point(0.0, -1.0)
        bottom_right = point(1.0, -1.0)
    :param graphic: original graphic
    :returns: a new graphic with an updated pinning position
    """
    mapping = {
        Point.as_tuple(german_top_left): top_left,
        Point.as_tuple(german_top_center): top_center,
        Point.as_tuple(german_top_right): top_right,
        Point.as_tuple(german_center_left): center_left,
        Point.as_tuple(german_center): center,
        Point.as_tuple(german_center_right): center_right,
        Point.as_tuple(german_bottom_left): bottom_left,
        Point.as_tuple(german_bottom_center): bottom_center,
        Point.as_tuple(german_bottom_right): bottom_right
    }
    return pin(mapping[Point.as_tuple(pinning_point)], graphic)


def ueberlagere(vordere_grafik: Grafik, hintere_grafik: Grafik) \
        -> Grafik:
    """
    Erzeugt eine neue Grafik,
    die aus der zentrierten Überlagerung der zwei gegebenen Grafiken besteht.
    Die erste gegebene Grafik liegt im Vordergrund
    und die zweite im Hintergrund,
    und ihre Fixierungspositionen liegen übereinander im Zentrum.

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
