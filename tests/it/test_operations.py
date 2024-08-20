from tests.testing_utils import HEIGHT, WIDTH, assert_repr

from pytamaro.it.operations import (
    larghezza_grafica, altezza_grafica, ruota,
    accanto, sopra, sovrapponi, componi, fissa,
)
from pytamaro.it.point_names import (
    alto_sinistra, centro, basso_destra,
)
import pytamaro.color_names as _color_names_en
import pytamaro.primitives as _primitives_en
import pytamaro.operations as _operations_en
import pytamaro.point_names as _point_names_en

g = _primitives_en.rectangle(WIDTH, HEIGHT, _color_names_en.red)


def test_width():
    assert _operations_en.graphic_width(g) == larghezza_grafica(g)


def test_height():
    assert _operations_en.graphic_height(g) == altezza_grafica(g)


def test_rotate():
    assert _operations_en.rotate(45, g) == ruota(45, g)


def test_beside():
    assert _operations_en.beside(g, g) == accanto(g, g)


def test_above():
    assert _operations_en.above(g, g) == sopra(g, g)


def test_overlay():
    assert _operations_en.overlay(g, g) == sovrapponi(g, g)


def test_compose():
    assert _operations_en.compose(g, g) == componi(g, g)


def test_fissa():
    assert _operations_en.pin(_point_names_en.top_left, g) == fissa(alto_sinistra, g)
    assert _operations_en.pin(_point_names_en.center, g) == fissa(centro, g)
    assert _operations_en.pin(_point_names_en.bottom_right, g) == fissa(basso_destra, g)


def test_operation_localized_repr():
    composed = _operations_en.compose(g, g)
    assert_repr(composed, "it")
    assert "componi" in repr(composed)
