from tests.testing_utils import HEIGHT, WIDTH, assert_repr

from pytamaro.fr.point_names import (
    haut_gauche, centre, bas_droite,
)
from pytamaro.fr.operations import (
    largeur_graphique, hauteur_graphique, ancre,
    superpose, cote_a_cote, au_dessus, pivote,
    compose,
)
import pytamaro.color_names as _color_names_en
import pytamaro.point_names as _point_names_en
import pytamaro.operations as _operations_en
import pytamaro.primitives as _primitives_en

g = _primitives_en.rectangle(WIDTH, HEIGHT, _color_names_en.red)


def test_width():
    assert _operations_en.graphic_width(g) == largeur_graphique(g)


def test_height():
    assert _operations_en.graphic_height(g) == hauteur_graphique(g)


def test_rotate():
    assert _operations_en.rotate(45, g) == pivote(45, g)


def test_beside():
    assert _operations_en.beside(g, g) == cote_a_cote(g, g)


def test_above():
    assert _operations_en.above(g, g) == au_dessus(g, g)


def test_overlay():
    assert _operations_en.overlay(g, g) == superpose(g, g)


def test_compose():
    assert _operations_en.compose(g, g) == compose(g, g)


def test_pin():
    assert _operations_en.pin(_point_names_en.top_left, g) == ancre(haut_gauche, g)
    assert _operations_en.pin(_point_names_en.center, g) == ancre(centre, g)
    assert _operations_en.pin(_point_names_en.bottom_right, g) == ancre(bas_droite, g)


def test_operation_localized_repr():
    composed = _operations_en.compose(g, g)
    assert_repr(composed, "fr")
    assert "compose" in repr(composed)
