from tests.testing_utils import HEIGHT, WIDTH, assert_repr

from pytamaro.it.operations import (
    larghezza_grafica, altezza_grafica, ruota,
    accanto, sopra, sovrapponi, componi, fissa,
)
from pytamaro.it.point_names import (
    alto_sinistra, centro, basso_destra,
)
import pytamaro as _en

g = _en.rectangle(WIDTH, HEIGHT, _en.red)


def test_width():
    assert _en.graphic_width(g) == larghezza_grafica(g)


def test_height():
    assert _en.graphic_height(g) == altezza_grafica(g)


def test_rotate():
    assert _en.rotate(45, g) == ruota(45, g)


def test_beside():
    assert _en.beside(g, g) == accanto(g, g)


def test_above():
    assert _en.above(g, g) == sopra(g, g)


def test_overlay():
    assert _en.overlay(g, g) == sovrapponi(g, g)


def test_compose():
    assert _en.compose(g, g) == componi(g, g)


def test_fissa():
    assert _en.pin(_en.top_left, g) == fissa(alto_sinistra, g)
    assert _en.pin(_en.center, g) == fissa(centro, g)
    assert _en.pin(_en.bottom_right, g) == fissa(basso_destra, g)


def test_operation_localized_repr():
    composed = _en.compose(g, g)
    assert_repr(composed, "it")
    assert "componi" in repr(composed)
