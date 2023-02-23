"""
Funzioni per I/O con grafiche, come visualizzarle oppure salvarle.
"""

from __future__ import annotations

from pytamaro.io import save_gif, save_graphic, show_graphic
from pytamaro.it.graphic import Grafica


def visualizza_grafica(grafica: Grafica, debug: bool = False):
    """
    Visualizza una grafica in una nuova finestra.
    Grafiche prive di area non possono essere visualizzate.

    Quando `debug` è `True`, adorna la visualizzazione con informazioni utili
    per debugging: un bordo rosso attorno alla bounding box e una croce
    giallastra attorno al punto di fissaggio.

    :param grafica: grafica da visualizzare
    :param debug: può facoltativamente essere impostato a `True` per
           sovrapporre informazioni di debug
    """
    show_graphic(grafica, debug)


def salva_grafica(nome_file: str, grafica: Grafica, debug: bool = False):
    """
    Salva una grafica in un file.
    Due formati di file sono supportati: PNG (grafica raster) e SVG (grafica
    vettoriale).
    L'estensione del nome del file (o ".png" o ".svg") determina il formato.

    Una grafica priva di area non può essere salvata nel formato PNG.

    Quando `debug` è `True`, adorna la visualizzazione con informazioni utili
    per debugging: un bordo rosso attorno alla bounding box e una croce
    giallastra attorno al punto di fissaggio.

    :param nome_file: nome del file da creare (con l'estensione)
    :param grafica: grafica da visualizzare
    :param debug: può facoltativamente essere impostato a `True` per
           sovrapporre informazioni di debug
    """
    save_graphic(nome_file, grafica, debug)


def salva_gif(
    nome_file: str, grafiche: list[Grafica], durata: int = 40, loop: bool = True
):
    """
    Salva una sequenza di grafiche come una GIF animata.

    Le grafiche vengono riprodotte sequenzialmente (normalmente a 25 frame al
    secondo) a ciclo continuo.

    :param nome_file: nome del file da creare (inclusa l'estensione '.gif')
    :param grafiche: lista di grafiche da salvare come GIF
    :param durata: durata in millisecondi di ciascun frame (default a 40
           millisecondi, ovvero 25 frame al secondo)
    :param loop: determina se la GIF debba riprodursi in loop indefinitamente (default a True)
    """
    save_gif(nome_file, grafiche, durata, loop)
