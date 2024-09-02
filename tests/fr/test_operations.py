import pytamaro as _pytamaro
from pytamaro.fr.operations import (ancre, au_dessus, compose, cote_a_cote,
                                    hauteur_graphique, largeur_graphique,
                                    pivote, superpose)
from pytamaro.fr.point_names import bas_droite, centre, haut_gauche
from tests.testing_utils import HEIGHT, WIDTH, assert_repr

g = _pytamaro.rectangle(WIDTH, HEIGHT, _pytamaro.red)


def test_width():
    assert _pytamaro.graphic_width(g) == largeur_graphique(g)


def test_height():
    assert _pytamaro.graphic_height(g) == hauteur_graphique(g)


def test_rotate():
    assert _pytamaro.rotate(45, g) == pivote(45, g)


def test_beside():
    assert _pytamaro.beside(g, g) == cote_a_cote(g, g)


def test_above():
    assert _pytamaro.above(g, g) == au_dessus(g, g)


def test_overlay():
    assert _pytamaro.overlay(g, g) == superpose(g, g)


def test_compose():
    assert _pytamaro.compose(g, g) == compose(g, g)


def test_pin():
    assert _pytamaro.pin(_pytamaro.top_left, g) == ancre(haut_gauche, g)
    assert _pytamaro.pin(_pytamaro.center, g) == ancre(centre, g)
    assert _pytamaro.pin(_pytamaro.bottom_right, g) == ancre(bas_droite, g)


def test_operation_localized_repr():
    composed = _pytamaro.compose(g, g)
    assert_repr(composed, "fr")
    assert "compose" in repr(composed)
