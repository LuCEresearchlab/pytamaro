import pytamaro as _pytamaro
from pytamaro.it.operations import (accanto, altezza_grafica, componi, fissa,
                                    larghezza_grafica, ruota, sopra,
                                    sovrapponi)
from pytamaro.it.point_names import alto_sinistra, basso_destra, centro
from tests.testing_utils import HEIGHT, WIDTH, assert_repr

g = _pytamaro.rectangle(WIDTH, HEIGHT, _pytamaro.red)


def test_width():
    assert _pytamaro.graphic_width(g) == larghezza_grafica(g)


def test_height():
    assert _pytamaro.graphic_height(g) == altezza_grafica(g)


def test_rotate():
    assert _pytamaro.rotate(45, g) == ruota(45, g)


def test_beside():
    assert _pytamaro.beside(g, g) == accanto(g, g)


def test_above():
    assert _pytamaro.above(g, g) == sopra(g, g)


def test_overlay():
    assert _pytamaro.overlay(g, g) == sovrapponi(g, g)


def test_compose():
    assert _pytamaro.compose(g, g) == componi(g, g)


def test_fissa():
    assert _pytamaro.pin(_pytamaro.top_left, g) == fissa(alto_sinistra, g)
    assert _pytamaro.pin(_pytamaro.center, g) == fissa(centro, g)
    assert _pytamaro.pin(_pytamaro.bottom_right, g) == fissa(basso_destra, g)


def test_operation_localized_repr():
    composed = _pytamaro.compose(g, g)
    assert_repr(composed, "it")
    assert "componi" in repr(composed)
