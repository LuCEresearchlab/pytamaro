"""
Funktionen zum Erzeugen primitiver Grafiken (Figuren und Texte).
Falls nicht anders angegeben befindet sich die Fixierposition
in der Mitte des Begrenzungsrahmens der erzeugten Grafik.
"""

from __future__ import annotations

from pytamaro.de.color import Farbe
from pytamaro.de.graphic import Grafik
from pytamaro.primitives import (circular_sector, empty_graphic,
                                 rectangle, triangle)
from pytamaro.primitives import (ellipse as ellipse_e, text as text_e)


def rechteck(breite: float, hoehe: float, farbe: Farbe) -> Grafik:
    """
    Erzeugt ein Rechteck mit der gegebenen Breite und Höhe,
    gefüllt in der gegebenen Farbe.

    :param breite: die Breite des Rechtecks
    :param hoehe: die Höhe des Rechtecks
    :param farbe: Füllfarbe des Rechtecks
    :returns: eine Grafik mit dem gegebenen Rechteck
    """
    return rectangle(breite, hoehe, farbe)


def leere_grafik() -> Grafik:
    """
    Erzeugt eine leere Grafik.
    Wenn eine leere Grafik mit einer anderen Grafik kombiniert wird
    verhält sie sich als neutrales Element:
    das Ergebnis der Komposition ist einfach gleich der anderen Grafik.

    :returns: eine leere Grafik (Breite und Höhe sind 0)
    """
    return empty_graphic()


def ellipse(breite: float, hoehe: float, farbe: Farbe) -> Grafik:
    """
    Erzeugt eine Ellipse mit der gegebenen Breite und Höhe,
    gefüllt in der gegebenen Farbe.

    Wenn Breite und Höhe gleich gross sind wird die Ellipse zum Kreis
    mit dem entsprechenden Durchmesser.

    :param breite: Breite der Ellipse
    :param hoehe: Höhe der Ellipse
    :param farbe: Füllfarbe der Ellipse
    :returns: eine Grafik mit der gegebenen Ellipse
    """
    return ellipse_e(breite, hoehe, farbe)


def kreis_sektor(radius: float, winkel: float, farbe: Farbe) -> Grafik:
    """
    Erzeugt einen Kreissektor mit dem gegebenen Radius,
    der den gegebenen Winkel umspannt,
    gefüllt in der gegebenen Farbe.

    Ein Kreissektor ist ein Teil eines Kreises
    begrenzt durch zwei Radien und einen Bogen.
    Wenn man den Kreis als Uhr betrachtet
    dann zeigt der erste Radius in Richtung 3 Uhr.
    Der Winkel bestimmt die Position des zweiten Radius,
    ausgehend vom ersten Radius im Gegenuhrzeigersinn.
    Ein Winkel von 360 Grad entspricht einem ganzen Kreis.

    Die Fixierposition liegt in der Mitte des Kreises,
    aus dem der Kreissektor ausgeschnitten wurde.

    :param radius: Kreisradius
    :param winkel: Winkel des Sektors, in Grad
    :param farbe: Füllfarbe des Kreissektors
    :returns: eine Grafik mit dem gegebenen Kreissektor
    """
    return circular_sector(radius, winkel, farbe)


def dreieck(seite1: float, seite2: float, winkel: float, farbe: Farbe) -> Grafik:
    """
    Erzeugt ein Dreieck mit den gegebenen Seitenlängen und dem gegebenen Winkel,
    gefüllt in der gegebenen Farbe.
    Die erste Seite verläuft horizontal nach rechts.
    Der Winkel gibt an, wie viel die zweite Seite
    im Gegenuhrzeigersinn von der ersten Seite abweicht.

    Für alle Dreiecke, ausser für stumpfe Dreiecke,
    liegt die untere linke Ecke des Begrenzungsrahmens
    auf dem Eckpunkt des Dreiecks, für das der Winkel angegeben ist.

    Die Fixierposition liegt auf dem Schwerpunkt des Dreiecks.

    :param seite1: Länge der ersten, horizontalen Seite
    :param seite2: Länge der zweiten Seite
    :param winkel: Winkel von der ersten zu der zweiten Seiten, in Grad
    :param farbe: Farbe des Dreiecks
    :returns: eine Grafik mit dem gegebenen Dreieck
    """
    return triangle(seite1, seite2, winkel, farbe)


def text(inhalt: str, schriftart: str, punkte: float, farbe: Farbe) -> Grafik:
    """
    Erzeugt einen Text in der gegebenen Schriftart und Schriftgrösse,
    gefüllt in der gegebenen Farbe.

    Falls für die gegebene Schriftart auf dem System keine True-Type Schrift
    zur Verfügung steht, wird eine einfache Standardschriftart verwendet.
    Die resultierende Grafik hat die minimale Grösse,
    die den gesamten Text umschliesst.

    Die Fixierposition liegt auf der linken Kante des Begrenzungsrahmens,
    auf der Höhe der Grundlinie des Textes.

    :param inhalt: der Text, der dargestellt werden soll
    :param schriftart: der Name der Schriftart
                       (zum Beispiel "arial" auf Windows, "Arial" auf macOS)
    :param punkte: Schriftgrösse in typografischen Punkten (zum Beispiel 16)
    :param farbe: Farbe, in der der Text dargestellt werden soll
    :returns: eine Grafik bestehend aus dem gegebenen Text
    """
    return text_e(inhalt, schriftart, punkte, farbe)
