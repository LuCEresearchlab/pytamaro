from pytamaro.color_names import blue, red
from pytamaro.fr.point_names import *
from pytamaro.operations import (above, beside, compose, graphic_height,
                                 graphic_width, overlay, pin, rotate)
from pytamaro.fr.operations import (largeur_graphique, hauteur_graphique, ancre,
                                    superpose, cote_a_cote, au_dessus, pivote)
from pytamaro.fr.operations import compose as fr_compose


from pytamaro.primitives import rectangle
from tests.testing_utils import HEIGHT, WIDTH, assert_repr

g = rectangle(WIDTH, HEIGHT, red)


def test_width():
    assert graphic_width(g) == largeur_graphique(g)


def test_height():
    assert graphic_height(g) == hauteur_graphique(g)


def test_rotate():
    assert rotate(45, g) == pivote(45, g)


def test_beside():
    assert beside(g, g) == cote_a_cote(g, g)


def test_above():
    assert above(g, g) == au_dessus(g, g)


def test_overlay():
    assert overlay(g, g) == superpose(g, g)


def test_compose():
    assert compose(g, g) == fr_compose(g, g)


def test_pin():
    assert pin(top_left, g) == ancre(haut_gauche, g)
    assert pin(center, g) == ancre(centre, g)
    assert pin(bottom_right, g) == ancre(bas_droite, g)


def test_operation_localized_repr():
    composed = compose(g, g)
    assert_repr(composed, "fr")
    assert "compose" in repr(composed)
