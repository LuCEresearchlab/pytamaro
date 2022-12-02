"""
Funzioni per operazioni con grafiche (principlamente per combinarle).
"""

from __future__ import annotations

from pytamaro.it.graphic import Grafica
from pytamaro.it.point import Punto
from pytamaro.point import Point
from pytamaro.operations import (above, beside, compose, graphic_height,
                                 graphic_width, overlay, pin, rotate)
from pytamaro.point_names import (top_left, top_center, top_right,
                                  center_left, center, center_right,
                                  bottom_left, bottom_center, bottom_right)
from pytamaro.it.point_names import (alto_sinistra, alto_centro, alto_destra,
                                     centro_sinistra, centro, centro_destra,
                                     basso_sinistra, basso_centro, basso_destra)


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


def fissa(posizione_di_fissaggio: Punto, grafica: Grafica) -> Grafica:
    """
    Cambia la posizione di fissaggio di una grafica, ritornando una nuova
    grafica coon lo stesso contenuto ma una posizione di fissaggio aggiornata.
    La nuova posizione di fissaggio è determinata dal parametro `posizione_di_fissaggio`

    :param posizione_di_fissaggio: un oggetto di tipo punto che
    identifica uno dei 9 punti d'interesse:
    I punti di fissaggio validi sono:
        centro = point(0.0, 0.0)
        alto_sinitra = punto(-1.0, 1.0)
        alto_centro = punto(0.0, 1.0)
        alto_destra = punto(1.0, 1.0)
        centro_sinistra = punto(-1.0, 0.0)
        centro_destra = punto(1.0, 0.0)
        basso_sinistra = punto(-1.0, -1.0)
        basso_centro = punto(0.0, -1.0)
        basso_destra = punto(1.0, -1.0)
    :param grafica: grafica originale
    :returns: una nuova grafica con una posizione di fissaggio aggiornata
    """
    mapping = {
        Point.as_tuple(alto_sinistra): top_left,
        Point.as_tuple(alto_centro): top_center,
        Point.as_tuple(alto_destra): top_right,
        Point.as_tuple(centro_sinistra): center_left,
        Point.as_tuple(centro): center,
        Point.as_tuple(centro_destra): center_right,
        Point.as_tuple(basso_sinistra): bottom_left,
        Point.as_tuple(basso_centro): bottom_center,
        Point.as_tuple(basso_destra): bottom_right
    }
    return pin(mapping[Point.as_tuple(posizione_di_fissaggio)], grafica)


def sovrapponi(grafica_primopiano: Grafica, grafica_secondopiano: Grafica) \
        -> Grafica:
    """
    Sovrappone due grafiche tenendo la prima in primo piano e la seconda sullo
    sfondo, allineandole sui loro centri.

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
