"""
Funktionen zur Ausgabe (Anzeigen oder Speichern) von Grafiken.
"""

from __future__ import annotations

import pytamaro as _pytamaro
from pytamaro.de.graphic import Grafik


def zeige_grafik(grafik: Grafik, debug: bool = False):
    """
    Zeige die gegebene Grafik an.

    Eine Grafik ohne Fläche kann nicht angezeigt werden.

    Falls `debug` `True` ist werden auf der Grafik zusätzliche Informationen
    dargestellt, welche für das Debugging nützlich sein können.
    Ein roter Rahmen markiert den Begrenzungsrahmen der Grafik,
    und ein gelbliches Kreuz gibt die Fixierposition an.

    :param grafik: die anzuzeigende Grafik
    :param debug: kann optional auf `True` gesetzt werden, um über der Grafik
                  Debug-Informationen darzustellen
    """
    _pytamaro.show_graphic(grafik, debug)


def speichere_grafik(datei_name: str, grafik: Grafik, debug: bool = False):
    """
    Speichere die gegebene Grafik in einer Datei.

    Zwei Dateiformate werden unterstützt: PNG (Rastergrafik) und SVG (Vektorgrafik).
    Die Dateinamenerweiterung (entweder ".png" oder ".svg") bestimmt das Dateiformat.

    Grafiken ohne Fläche können nicht als PNG-Datei gespeichert werden.

    Falls `debug` `True` ist werden auf der Grafik zusätzliche Informationen
    dargestellt, welche für das Debugging nützlich sein können.
    Ein roter Rahmen markiert den Begrenzungsrahmen der Grafik,
    und ein gelbliches Kreuz gibt die Fixierposition an.

    :param datei_name: Name der zu kreierenden Datei (mit Erweiterung)
    :param grafik: zu speichernde Grafik
    :param debug: kann optional auf `True` gesetzt werden, um über der Grafik
                  Debug-Informationen darzustellen
    """
    _pytamaro.save_graphic(datei_name, grafik, debug)


def speichere_animation(
    datei_name: str, grafiken: list[Grafik], dauer: int = 40, loop: bool = True
):
    """
    Speichere eine Sequenz von Grafiken als Animation (GIF).

    Beim Anzeigen des GIFs werden die Grafiken in einer unendlichen Schleife
    animiert (normalerweise mit 25 Grafiken pro Sekunde).

    :param datei_name: Name der zu kreierenden Datei (mit Erweiterung '.gif')
    :param grafiken: Liste der zu speichernden Grafiken
    :param dauer: Dauer jeder Grafik, in Millisekunden (Default: 40
           Millisekunden, enspricht 25 Grafiken pro Sekunde)
    :param loop: bestimmt ob das GIF in einer unendlichen Schleife abgespielt
           werden soll (Default: true)
    """
    _pytamaro.save_animation(datei_name, grafiken, dauer, loop)


def zeige_animation(grafiken: list[Grafik], dauer: int = 40, loop: bool = True):
    """
    Zeige eine Sequenz von Grafiken als Animation (GIF) an.

    Beim Anzeigen des GIFs werden die Grafiken in einer unendlichen Schleife
    animiert (normalerweise mit 25 Grafiken pro Sekunde).

    :param grafiken: Liste der anzuzeigenden Grafiken
    :param dauer: Dauer jeder Grafik, in Millisekunden (Default: 40
           Millisekunden, enspricht 25 Grafiken pro Sekunde)
    :param loop: bestimmt ob das GIF in einer unendlichen Schleife abgespielt
           werden soll (Default: true)
    """
    _pytamaro.show_animation(grafiken, dauer, loop)
