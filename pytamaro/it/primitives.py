"""
Funzioni per creare grafiche primitive (forme e testo).
Tranne quando specificato diversamente, la posizione di fissaggio iniziale è al
centro del rettangolo di delimitazione (bounding box) della grafica.
"""

from __future__ import annotations

import pytamaro as _pytamaro
from pytamaro.it.color import Colore
from pytamaro.it.graphic import Grafica


def rettangolo(larghezza: float, altezza: float, colore: Colore) -> Grafica:
    """
    Crea un rettangolo delle dimensioni indicate, riempito con un colore.

    :param larghezza: larghezza del rettangolo
    :param altezza: altezza del rettangolo
    :param colore: colore da usare per riempire il rettangolo
    :returns: una grafica con il rettangolo specificato
    """
    return _pytamaro.rectangle(larghezza, altezza, colore)


def grafica_vuota() -> Grafica:
    """
    Crea una grafica vuota.
    Quando una grafica vuota viene composta con ogni altra grafica, si comporta
    da elemento neutro: il risultato è sempre uguale all'altra grafica.

    :returns: una grafica vuota (larghezza e altezza 0)
    """
    return _pytamaro.empty_graphic()


def ellisse(larghezza: float, altezza: float, colore: Colore) -> Grafica:
    """
    Crea un ellisse delle dimensioni indicate, riempito con un colore.

    Quando larghezza e altezza coincidono, l'ellisse diventa un cerchio di
    diametro pari alla dimensione indicata.

    :param larghezza: larghezza dell'ellisse
    :param altezza: altezza dell'ellisse
    :param colore: colore da usare per riempire l'ellisse
    :returns: una grafica con l'ellisse specificato
    """
    return _pytamaro.ellipse(larghezza, altezza, colore)


def settore_circolare(raggio: float, angolo: float, colore: Colore) -> Grafica:
    """
    Crea un settore circolare appartenente a un cerchio del raggio indicato,
    riempito con un colore.

    Un settore circolare è una porzione di cerchio racchiusa tra due raggi e un
    arco.
    Considerando il cerchio come un orologio, il primo raggio "punta" in
    direzione delle ore 3. L'`angolo` determina la posizione del secondo
    raggio, calcolata a partire dalla posizione del primo in senso antiorario.
    Un angolo di 360 gradi corrisponde a un cerchio completo.

    La posizione di fissaggio è al centro del cerchio da cui è preso il settore
    circolare.

    :param raggio: raggio del cerchio da cui è preso il settore circolare
    :param angolo: angolo al centro, in gradi
    :param colore: colore da usare per riempire il settore circolare
    :returns: una grafica con il settore circolare specificato
    """
    return _pytamaro.circular_sector(raggio, angolo, colore)


def triangolo(lato1: float, lato2: float, angolo: float, colore: Colore) -> Grafica:
    """
    Crea un triangolo dati due lati e l'angolo tra essi compreso,
    riempito con un colore.

    Il primo lato si estende orizzontalmente verso destra. Il secondo lato si
    estende dall'estremità sinistra del primo lato, ruotato dell'angolo specificato
    in senso antiorario. Questo punto sarà in basso a sinistra nella grafica,
    a meno che l'angolo specificato sia più grande di 90 gradi.

    La posizione di fissaggio è il centroide del triangolo.

    :param lato1: lunghezza del primo lato (orizzontale) del triangolo
    :param lato2: lunghezza del secondo lato del triangolo
    :param angolo: angolo compreso tra i due lati, in gradi
    :param colore: colore da usare per riempire il triangolo
    :returns: una grafica con il triangolo specificato
    """
    return _pytamaro.triangle(lato1, lato2, angolo, colore)


def testo(contenuto: str, font: str, punti: float, colore: Colore) -> Grafica:
    """
    Crea una grafica con il testo renderizzato usando font, dimensione e colore
    indicati.

    Quando il font True-Type indicato non è disponibile nel sistema, al suo
    posto viene usato un font estremamente basilare e sempre disponibile. La
    grafica risultante ha la dimensione minima in modo da racchiudere l'intero
    testo.

    La posizione di fissaggio è allineata orizzontalmente a sinistra e
    verticalmente sulla linea di base (baseline) del testo.

    :param contenuto: il testo di cui fare rendering
    :param font: il nome del font (ad esempio "Arial" o "Fira Sans")
    :param punti: dimensione in punti tipografici (ad esempio 16)
    :param colore: colore da usare per fare il rendering del testo
    :returns: una grafica con il testo specificato
    """
    return _pytamaro.text(contenuto, font, punti, colore)
