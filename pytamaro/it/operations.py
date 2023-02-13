"""
Funzioni per operazioni con grafiche (principlamente per combinarle).
"""

from __future__ import annotations

from pytamaro.it.graphic import Grafica
from pytamaro.it.point import Punto
from pytamaro.operations import (above, beside, compose, graphic_height,
                                 graphic_width, overlay, pin, rotate)


def larghezza_grafica(grafica: Grafica) -> int:
    """
    Ritorna la larghezza di una grafica, in pixel.

    :param grafica: grafica di cui calcolare la larghezza
    :returns: larghezza della grafica
    """
    return graphic_width(grafica)


def altezza_grafica(grafica: Grafica) -> int:
    """
    Ritorna l'altezza di una grafica, in pixel.

    :param grafica: grafica di cui calcolare l'altezza
    :returns: altezza della grafica
    """
    return graphic_height(grafica)


def componi(grafica_primopiano: Grafica, grafica_secondopiano: Grafica) \
        -> Grafica:
    """
    Compone due grafiche tenendo la prima in primo piano e la seconda sullo
    sfondo, allineandole usando le loro posizioni di fissaggio.

    La posizione di fissaggio usata per comporre diventa la posizione di
    fissaggio della grafica risultante.

    :param grafica_primopiano: grafica da tenere in primo piano
    :param grafica_secondopiano: grafica da tenere sullo sfondo
    :returns: grafica risultante dalla composizione delle due fornite
    """
    return compose(grafica_primopiano, grafica_secondopiano)


def fissa(punto: Punto, grafica: Grafica) -> Grafica:
    """
    Cambia la posizione di fissaggio di una grafica, ritornando una nuova
    grafica con lo stesso contenuto ma una posizione di fissaggio aggiornata.
    La nuova posizione di fissaggio è determinata dal parametro `punto`.

    Ogni grafica è racchiusa in un rettangolo di delimitazione (bounding box).
    Ci sono 9 punti notevoli, corrispondenti ai quattro angoli di questo rettangolo,
    ai punti centrali dei quattro lati e al centro del rettangolo.
    Ci si può riferire a questi punti usando i nomi `alto_sinistra`, `alto_destra`,
    `basso_sinistra`, `basso_destra`, `alto_centro`, `centro_destra`, `basso_centro`,
    `centro_sinistra` e `centro`.

    :param punto: il punto indicante la nuova posizione di fissaggio
    :param grafica: grafica originale
    :returns: una nuova grafica con una posizione di fissaggio aggiornata
    """
    return pin(punto, grafica)


def sovrapponi(grafica_primopiano: Grafica, grafica_secondopiano: Grafica) \
        -> Grafica:
    """
    Sovrappone due grafiche tenendo la prima in primo piano e la seconda sullo
    sfondo, allineandole sui loro centri.

    La posizione di fissaggio della grafica risultante è il suo centro.

    :param grafica_primopiano: grafica da tenere in primo piano
    :param grafica_secondopiano: grafica da tenere sullo sfondo
    :returns: grafica risultante dalla sovrapposizione delle due fornite
    """
    return overlay(grafica_primopiano, grafica_secondopiano)


def accanto(grafica_sinistra: Grafica, grafica_destra: Grafica) -> Grafica:
    """
    Compone due grafiche affiancandole, posizionando la prima a sinistra e la
    seconda a destra. Le due grafiche vengono allineate verticalmente al
    centro.

    La posizione di fissaggio della grafica risultante è il suo centro.

    :param grafica_sinistra: grafica da posizionare a sinistra
    :param grafica_destra: grafica da posizionare a destra
    :returns: grafica risultante dall'affiancamento orizzontale delle due
              grafiche fornite
    """
    return beside(grafica_sinistra, grafica_destra)


def sopra(grafica_alto: Grafica, grafica_basso: Grafica) -> Grafica:
    """
    Compone due grafiche affiancandole verticalmente, posizionando la prima in
    alto e la seconda in basso. Le due grafiche vengono allineate
    orizzontalmente al centro.

    La posizione di fissaggio della grafica risultante è il suo centro.

    :param grafica_sopra: grafica da posizionare sopra
    :param grafica_sotto: grafica da posizionare sotto
    :returns: grafica risultante dall'affiancamento verticale delle due
              grafiche fornite
    """
    return above(grafica_alto, grafica_basso)


def ruota(gradi: float, grafica: Grafica) -> Grafica:
    """
    Ruota una grafica di un certo numero di gradi in senso antiorario attorno
    alla sua posizione di fissaggio.

    È possibile che si verifichino piccoli errori di arrotondamento (a causa
    dell'approssimazione al pixel più vicino).

    :param gradi: numero di gradi di cui ruotare la grafica
    :param grafica: grafica da ruotare
    :returns: la grafica originale ruotata attorno alla sua posizione di
              fissaggio
    """
    return rotate(gradi, grafica)
