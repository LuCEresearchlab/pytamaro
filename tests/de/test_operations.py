import pytamaro as _pytamaro
from pytamaro.de.operations import (drehe, fixiere, grafik_breite,
                                    grafik_hoehe, kombiniere, neben, ueber,
                                    ueberlagere)
from pytamaro.de.point_names import mitte, oben_links, unten_rechts
from tests.testing_utils import HEIGHT, WIDTH, assert_repr

g = _pytamaro.rectangle(WIDTH, HEIGHT, _pytamaro.red)


def test_width():
    assert _pytamaro.graphic_width(g) == grafik_breite(g)


def test_height():
    assert _pytamaro.graphic_height(g) == grafik_hoehe(g)


def test_rotate():
    assert _pytamaro.rotate(45, g) == drehe(45, g)


def test_beside():
    assert _pytamaro.beside(g, g) == neben(g, g)


def test_above():
    assert _pytamaro.above(g, g) == ueber(g, g)


def test_overlay():
    assert _pytamaro.overlay(g, g) == ueberlagere(g, g)


def test_compose():
    assert _pytamaro.compose(g, g) == kombiniere(g, g)


def test_fixiere():
    assert _pytamaro.pin(_pytamaro.top_left, g) == fixiere(oben_links, g)
    assert _pytamaro.pin(_pytamaro.center, g) == fixiere(mitte, g)
    assert _pytamaro.pin(_pytamaro.bottom_right, g) == fixiere(unten_rechts, g)


def test_operation_localized_repr():
    composed = _pytamaro.compose(g, g)
    assert_repr(composed, "de")
    assert "kombiniere" in repr(composed)
