from tests.testing_utils import HEIGHT, WIDTH, assert_repr

import pytamaro.color_names as _color_names_en
import pytamaro.primitives as _primitives_en
import pytamaro.operations as _operations_en
import pytamaro.point_names as _point_names_en
from pytamaro.de.operations import (drehe, fixiere, grafik_breite,
                                    grafik_hoehe, kombiniere, neben, ueber,
                                    ueberlagere)
from pytamaro.de.point_names import (mitte, oben_links, unten_rechts)

g = _primitives_en.rectangle(WIDTH, HEIGHT, _color_names_en.red)


def test_width():
    assert _operations_en.graphic_width(g) == grafik_breite(g)


def test_height():
    assert _operations_en.graphic_height(g) == grafik_hoehe(g)


def test_rotate():
    assert _operations_en.rotate(45, g) == drehe(45, g)


def test_beside():
    assert _operations_en.beside(g, g) == neben(g, g)


def test_above():
    assert _operations_en.above(g, g) == ueber(g, g)


def test_overlay():
    assert _operations_en.overlay(g, g) == ueberlagere(g, g)


def test_compose():
    assert _operations_en.compose(g, g) == kombiniere(g, g)


def test_fixiere():
    assert _operations_en.pin(_point_names_en.top_left, g) == fixiere(oben_links, g)
    assert _operations_en.pin(_point_names_en.center, g) == fixiere(mitte, g)
    assert _operations_en.pin(_point_names_en.bottom_right, g) == fixiere(unten_rechts, g)


def test_operation_localized_repr():
    composed = _operations_en.compose(g, g)
    assert_repr(composed, "de")
    assert "kombiniere" in repr(composed)
