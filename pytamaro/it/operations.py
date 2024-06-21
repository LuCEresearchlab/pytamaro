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
    Ritorna la larghezza di una grafica.

    :param grafica: grafica di cui calcolare la larghezza
    :returns: larghezza della grafica
    """
    return graphic_width(grafica)


def altezza_grafica(grafica: Grafica) -> int:
    """
    Ritorna l'altezza di una grafica.

    :param grafica: grafica di cui calcolare l'altezza
    :returns: altezza della grafica
    """
    return graphic_height(grafica)


def componi(grafica_primopiano: Grafica, grafica_secondopiano: Grafica) \
        -> Grafica:
    """
    Crea una nuova grafica componendo le due grafiche fornite.
    La prima grafica viene tenuta in primo piano, la seconda sullo sfondo.
    Le grafiche vengono allineate superimponendo le loro posizioni di fissaggio.

    La posizione di fissaggio usata per comporre diventa la posizione di
    fissaggio della grafica risultante.

    :param grafica_primopiano: grafica in primo piano
    :param grafica_secondopiano: grafica sullo sfondo
    :returns: la grafica risultante composta
    """
    return compose(grafica_primopiano, grafica_secondopiano)


def fissa(punto: Punto, grafica: Grafica) -> Grafica:
    """
    Crea una nuova grafica che corrisponde alla grafica fornita,
    con una nuova posizione di fissaggio.

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
    Crea una nuova grafica sovrapponendo le due grafiche fornite,
    tenendo la prima in primo piano e la seconda sullo sfondo.
    Le due grafiche vengono sovrapposte sui loro centri.

    La posizione di fissaggio della grafica risultante è nel suo centro.

    :param grafica_primopiano: grafica in primo piano
    :param grafica_secondopiano: grafica sullo sfondo
    :returns: grafica risultante dalla sovrapposizione delle due fornite
    """
    return overlay(grafica_primopiano, grafica_secondopiano)


def accanto(grafica_sinistra: Grafica, grafica_destra: Grafica) -> Grafica:
    """
    Crea una nuova grafica affiancando orizzontalmente le due grafiche fornite.
    Le due grafiche vengono centrate verticalmente.

    La posizione di fissaggio della grafica risultante è nel suo centro.

    :param grafica_sinistra: grafica da posizionare a sinistra
    :param grafica_destra: grafica da posizionare a destra
    :returns: grafica risultante dall'affiancamento orizzontale delle due
              grafiche fornite
    """
    return beside(grafica_sinistra, grafica_destra)


def sopra(grafica_alto: Grafica, grafica_basso: Grafica) -> Grafica:
    """
    Crea una nuova grafica posizionando le due grafiche fornite una sopra l'altra.
    Le due grafiche vengono centrate orizzontalmente.

    La posizione di fissaggio della grafica risultante è nel suo centro.

    :param grafica_alto: grafica da posizionare in alto
    :param grafica_basso: grafica da posizionare in basso
    :returns: grafica risultante dall'affiancamento verticale delle due
              grafiche fornite
    """
    return above(grafica_alto, grafica_basso)


def ruota(angolo: float, grafica: Grafica) -> Grafica:
    """
    Crea una nuova grafica ruotando dell'angolo indicato, in senso antiorario,
    una grafica attorno alla sua posizione di fissaggio.
    Un angolo negativo corrisponde a una rotazione in senso orario.

    :param angolo: angolo di rotazione in senso antiorario, in gradi
    :param grafica: grafica da ruotare
    :returns: una nuova grafica, ruotata
    """
    return rotate(angolo, grafica)
