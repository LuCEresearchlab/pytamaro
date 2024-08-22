from tests.testing_utils import HEIGHT, WIDTH, assert_repr

from pytamaro.fr.point_names import (
    haut_gauche, centre, bas_droite,
)
from pytamaro.fr.operations import (
    largeur_graphique, hauteur_graphique, ancre,
    superpose, cote_a_cote, au_dessus, pivote,
    compose,
)
import pytamaro as _en


g = _en.rectangle(WIDTH, HEIGHT, _en.red)


def test_width():
    assert _en.graphic_width(g) == largeur_graphique(g)


def test_height():
    assert _en.graphic_height(g) == hauteur_graphique(g)


def test_rotate():
    assert _en.rotate(45, g) == pivote(45, g)


def test_beside():
    assert _en.beside(g, g) == cote_a_cote(g, g)


def test_above():
    assert _en.above(g, g) == au_dessus(g, g)


def test_overlay():
    assert _en.overlay(g, g) == superpose(g, g)


def test_compose():
    assert _en.compose(g, g) == compose(g, g)


def test_pin():
    assert _en.pin(_en.top_left, g) == ancre(haut_gauche, g)
    assert _en.pin(_en.center, g) == ancre(centre, g)
    assert _en.pin(_en.bottom_right, g) == ancre(bas_droite, g)


def test_operation_localized_repr():
    composed = _en.compose(g, g)
    assert_repr(composed, "fr")
    assert "compose" in repr(composed)
