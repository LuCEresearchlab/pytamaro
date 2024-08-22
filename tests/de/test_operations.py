from tests.testing_utils import HEIGHT, WIDTH, assert_repr

import pytamaro as _en
from pytamaro.de.operations import (drehe, fixiere, grafik_breite,
                                    grafik_hoehe, kombiniere, neben, ueber,
                                    ueberlagere)
from pytamaro.de.point_names import (mitte, oben_links, unten_rechts)

g = _en.rectangle(WIDTH, HEIGHT, _en.red)


def test_width():
    assert _en.graphic_width(g) == grafik_breite(g)


def test_height():
    assert _en.graphic_height(g) == grafik_hoehe(g)


def test_rotate():
    assert _en.rotate(45, g) == drehe(45, g)


def test_beside():
    assert _en.beside(g, g) == neben(g, g)


def test_above():
    assert _en.above(g, g) == ueber(g, g)


def test_overlay():
    assert _en.overlay(g, g) == ueberlagere(g, g)


def test_compose():
    assert _en.compose(g, g) == kombiniere(g, g)


def test_fixiere():
    assert _en.pin(_en.top_left, g) == fixiere(oben_links, g)
    assert _en.pin(_en.center, g) == fixiere(mitte, g)
    assert _en.pin(_en.bottom_right, g) == fixiere(unten_rechts, g)


def test_operation_localized_repr():
    composed = _en.compose(g, g)
    assert_repr(composed, "de")
    assert "kombiniere" in repr(composed)
