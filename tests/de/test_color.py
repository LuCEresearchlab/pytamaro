import pytamaro as _pytamaro
from pytamaro.de.color import hsl_farbe, hsv_farbe, rgb_farbe
from pytamaro.de.color_names import (blau, cyan, gelb, gruen, magenta, rot,
                                     schwarz, transparent, weiss)
from tests.testing_utils import assert_repr


def test_rgb_color():
    assert _pytamaro.rgb_color(255, 0, 0) == rgb_farbe(255, 0, 0)


def test_hsv_color():
    assert _pytamaro.hsv_color(255, 0, 0) == hsv_farbe(255, 0, 0)


def test_hsl_color():
    assert _pytamaro.hsl_color(255, 0, 0) == hsl_farbe(255, 0, 0)


def test_rgba_color():
    assert _pytamaro.rgb_color(0, 0, 0, 0.0) == rgb_farbe(0, 0, 0, 0.0)


def test_color_names():
    assert _pytamaro.red == rot
    assert _pytamaro.green == gruen
    assert _pytamaro.blue == blau
    assert _pytamaro.magenta == magenta
    assert _pytamaro.cyan == cyan
    assert _pytamaro.yellow == gelb
    assert _pytamaro.black == schwarz
    assert _pytamaro.white == weiss


def test_transparent_color_name():
    assert transparent == transparent


def test_color_localized_repr():
    assert_repr(rot, "de")
    assert "rot" in repr(rot)
