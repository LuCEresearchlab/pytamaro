"""
Funktionen für Operationen mit Grafiken (hauptsächlich für deren Komposition).
"""

from __future__ import annotations

from pytamaro.de.graphic import Grafik
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


def fixiere(horizontale_position: str, vertikale_position: str,
            grafik: Grafik) -> Grafik:
    """
    Erzeugt eine neue Grafik, die der gegebenen Grafik
    mit einer anderen Fixierungsposition entspricht.

    Die neue Fixierungsposition wird mit den Parametern
    `horizontale_position` und `vertikale_position` bestimmt.

    :param horizontale_position: "links", "mitte" oder "rechts" um
           die Fixierungsposition auf den linken Rand, in die Mitte,
           oder auf den rechten Rand der Grafik zu setzen.
    :param vertikale_position: "oben", "mitte" oder "unten" um
           die Fixierungsposition auf den oberen Rand, in die Mitte,
           oder auf den unteren Rand der Grafik zu setzen.
    :param grafik: die ursprüngliche Grafik
    :returns: die neue Grafik mit der gegebenen Fixierungsposition
    """
    h_mapping = {
        "links": "left",
        "mitte": "middle",
        "rechts": "right"
    }
    v_mapping = {
        "oben": "top",
        "mitte": "middle",
        "unten": "bottom"
    }
    return pin(h_mapping[horizontale_position],
               v_mapping[vertikale_position],
               grafik)


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
