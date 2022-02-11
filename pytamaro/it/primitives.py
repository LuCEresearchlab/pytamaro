"""
Funzioni per creare grafiche primitive (forme e testo)
"""

from __future__ import annotations

from pytamaro.it.color import Colore
from pytamaro.it.graphic import Grafica
from pytamaro.primitives import (circular_sector, ellipse, empty_graphic,
                                 rectangle, text, triangle)


def rettangolo(larghezza: float, altezza: float, colore: Colore) -> Grafica:
    """
    Crea un rettangolo delle dimensioni indicate, riempito con un colore.

    :param larghezza: larghezza del rettangolo, in pixel
    :param altezza: altezza del rettangolo, in pixel
    :param colore: colore da usare per riempire il rettangolo
    :returns: una grafica con il rettangolo specificato
    """
    return rectangle(larghezza, altezza, colore)


def grafica_vuota() -> Grafica:
    """
    Crea una grafica vuota.
    Quando una grafica vuota viene composta con ogni altra grafica, si comporta
    da elemento neutro: il risultato è sempre uguale all'altra grafica.

    Una grafica vuota non può essere visualizzata né salvata.

    :returns: una grafica vuota (larghezza e altezza 0 pixel)
    """
    return empty_graphic()


def ellisse(larghezza: float, altezza: float, colore: Colore) -> Grafica:
    """
    Crea un ellisse delle dimensioni indicate, riempito con un colore.

    Quando larghezza e altezza coincidono, l'ellisse diventa un cerchio di
    diametro pari alla dimensione indicata.

    :param larghezza: larghezza dell'ellisse, in pixel
    :param altezza: altezza dell'ellisse, in pixel
    :param colore: colore da usare per riempire l'ellisse
    :returns: una grafica con l'ellisse specificato
    """
    return ellipse(larghezza, altezza, colore)


def settore_circolare(raggio: float, angolo: float, colore: Colore) -> Grafica:
    """
    Crea un settore circolare appartenente a un cerchio del raggio indicato,
    riempito con un colore.

    Un settore circolare è una porzione di cerchio racchiusa tra due raggi e un
    arco.
    Considerando il cerchio come un orologio, il primo raggio "punta" in
    direzione delle ore 3. L'`angolo` determina la posizione del secondo
    raggio, calcolata a partire dalla posizione del primo in senso orario.

    :param raggio: raggio del cerchio da cui è preso il settore circolare, in
                   pixel
    :param angolo: angolo al centro, in gradi
    :param colore: colore da usare per riempire il settore circolare
    :returns: una grafica con il settore circolare specificato
    """
    return circular_sector(raggio, angolo, colore)


def triangolo(lato: float, colore: Colore) -> Grafica:
    """
    Crea un triangolo equilatero del lato indicato con la punta verso l'alto,
    riempito con un colore.

    :param lato: lunghezza del lato del triangolo, in pixel
    :param colore: colore da usare per riempire il triangolo
    :returns: una grafica con il triangolo specificato
    """
    return triangle(lato, colore)


def testo(contenuto: str, font: str, punti: float, colore: Colore) -> Grafica:
    """
    Crea una grafica con il testo renderizzato usando font, dimensione e colore
    indicati.

    Quando il font True-Type indicato non è disponibile nel sistema, al suo
    posto viene usato un font estremamente basilare e sempre disponibile. La
    grafica risultante ha la dimensione minima in modo da racchiudere l'intero
    testo.

    :param contenuto: il testo di cui fare rendering
    :param font: il nome del font (ad esempio "arial" su Windows, "Arial" su
           macOS)
    :param punti: dimensione in punti tipografici (ad esempio 16)
    :param colore: colore da usare per fare il rendering del testo
    :returns: una grafica con il testo specificato
    """
    return text(contenuto, font, punti, colore)
