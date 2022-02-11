"""
Funktionen zum Erzeugen primitiver Grafiken (Figuren und Texte)
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

    :param breite: die Breite des Rechtecks, in Pixel
    :param hoehe: die Höhe des Rechtecks, in Pixel
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

    Eine leere Grafik kann weder angezeigt noch gespeichert werden.

    :returns: eine leere Grafik (Breite und Höhe sind 0 Pixel)
    """
    return empty_graphic()


def ellipse(breite: float, hoehe: float, farbe: Farbe) -> Grafik:
    """
    Erzeugt eine Ellipse mit der gegebenen Breite und Höhe,
    gefüllt in der gegebenen Farbe.

    Wenn Breite und Höhe gleich gross sind wird die Ellipse zum Kreis
    mit dem entsprechenden Durchmesser.

    :param breite: Breite der Ellipse, in Pixel
    :param hoehe: Höhe der Ellipse, in Pixel
    :param farbe: Füllfarbe der Ellipse
    :returns: eine Grafik mit dem gegebenen Rechteck
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
    ausgehend vom ersten Radius im Uhrzeigersinn.

    :param radius: Kreisradius, in Pixel
    :param winkel: Winkel des Sektors, in Grad
    :param farbe: Füllfarbe des Kreissektors
    :returns: eine Grafik mit dem gegebenen Kreissektor
    """
    return circular_sector(radius, winkel, farbe)


def dreieck(seite: float, farbe: Farbe) -> Grafik:
    """
    Erzeugt ein gleichseitiges Dreieck mit der gegebenen Seitenlänge
    und einer nach oben zeigenden Ecke,
    gefüllt in der gegebenen Farbe.

    :param seite: Seitenlänge des Dreiecks, in Pixel
    :param farbe: Füllfarbe des Dreiecks
    :returns: eine Grafik mit dem gegebenen Dreieck
    """
    return triangle(seite, farbe)


def text(inhalt: str, schriftart: str, punkte: float, farbe: Farbe) -> Grafik:
    """
    Erzeugt einen Text in der gegebenen Schriftart und Schriftgrösse,
    gefüllt in der gegebenen Farbe.

    Falls für die gegebene Schriftart auf dem System keine True-Type Schrift
    zur Verfügung steht, wird eine einfache Standardschriftart verwendet.
    Die resultierende Grafik hat die minimale Grösse,
    die den gesamten Text umschliesst.

    :param inhalt: der Text, der dargestellt werden soll
    :param schriftart: der Name der Schriftart
                       (zum Beispiel "arial" auf Windows, "Arial" auf macOS)
    :param punkte: Schriftgrösse in typografischen Punkten (zum Beispiel 16)
    :param farbe: Farbe, in der der Text dargestellt werden soll
    :returns: eine Grafik bestehend aus dem gegebenen Text
    """
    return text_e(inhalt, schriftart, punkte, farbe)
