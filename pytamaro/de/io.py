"""
Funktionen zur Ausgabe (Anzeigen oder Speichern) von Grafiken.
"""

from __future__ import annotations

from pytamaro.io import save_gif, save_graphic, show_graphic
from pytamaro.de.graphic import Grafik


def zeige_grafik(grafik: Grafik, debug: bool = False):
    """
    Zeige die gegebene Grafik in einem neuen Fenster an.

    Eine leere Grafik kann nicht angezeigt werden;
    deshalb hat der Aufruf dieser Funktion mit einer leeren Grafik
    keinen Effekt.

    Falls `debug` `True` ist werden auf der Grafik zusätzliche Informationen
    dargestellt, welche für das Debugging nützlich sein können.
    Ein roter Rahmen markiert die Bounding Box der Grafik,
    und ein gelbliches Kreuz gibt den Fixierpunkt an.

    :param grafik: die anzuzeigende Grafik
    :param debug: kann optional auf `True` gesetzt werden, um über der Grafik
                  Debug-Informationen darzustellen
    """
    show_graphic(grafik, debug)


def speichere_grafik(datei_name: str, grafik: Grafik, debug: bool = False):
    """
    Speichere die gegebene Grafik als PNG-Datei.

    Eine leere Grafik kann nicht gespeichert werden;
    deshalb hat der Aufruf dieser Funktion mit einer leeren Grafik
    keinen Effekt.

    Falls `debug` `True` ist werden auf der Grafik zusätzliche Informationen
    dargestellt, welche für das Debugging nützlich sein können.
    Ein roter Rahmen markiert die Bounding Box der Grafik,
    und ein gelbliches Kreuz gibt den Fixierpunkt an.

    :param datei_name: Name der zu kreierenden Datei (ohne Erweiterung)
    :param grafik: zu speichernde Grafik
    :param debug: kann optional auf `True` gesetzt werden, um über der Grafik
                  Debug-Informationen darzustellen
    """
    save_graphic(datei_name, grafik, debug)


def speichere_gif(
    datei_name: str, grafiken: list[Grafik], dauer: int = 40, loop: bool = True
):
    """
    Speichere die gegebene Sequenz von Grafiken als animierte GIF-Datei.

    Beim Anzeigen des GIFs werden die Grafiken in einer unendlichen Schleife
    animiert (normalerweise mit 25 Grafiken pro Sekunde).

    :param datei_name: Name der zu kreierenden Datei (ohne Erweiterung)
    :param grafiken: Liste der zu speichernden Grafiken
    :param dauer: Dauer jeder Grafik, in Millisekunden (Default: 40
           millisekunden, enspricht 25 Grafiken pro Sekunde)
    :param loop: bestimmt ob das GIF in einer unendlichen Schleife abgespielt
           werden soll (Default: true)
    """
    save_gif(datei_name, grafiken, dauer, loop)
