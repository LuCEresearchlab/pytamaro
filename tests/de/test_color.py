from tests.testing_utils import assert_repr

from pytamaro.de.color_names import (
    rot, gruen, blau,
    magenta, cyan, gelb,
    schwarz, weiss, transparent,
)
from pytamaro.de.color import (
    rgb_farbe, hsv_farbe, hsl_farbe,
)
import pytamaro.color_names as _color_names_en
import pytamaro.color_functions as _color_functions_en


def test_rgb_color():
    assert _color_functions_en.rgb_color(255, 0, 0) == rgb_farbe(255, 0, 0)


def test_hsv_color():
    assert _color_functions_en.hsv_color(255, 0, 0) == hsv_farbe(255, 0, 0)


def test_hsl_color():
    assert _color_functions_en.hsl_color(255, 0, 0) == hsl_farbe(255, 0, 0)


def test_rgba_color():
    assert _color_functions_en.rgb_color(0, 0, 0, 0.0) == rgb_farbe(0, 0, 0, 0.0)


def test_color_names():
    assert _color_names_en.red == rot
    assert _color_names_en.green == gruen
    assert _color_names_en.blue == blau
    assert _color_names_en.magenta == magenta
    assert _color_names_en.cyan == cyan
    assert _color_names_en.yellow == gelb
    assert _color_names_en.black == schwarz
    assert _color_names_en.white == weiss


def test_transparent_color_name():
    assert transparent == transparent


def test_color_localized_repr():
    assert_repr(rot, "de")
    assert "rot" in repr(rot)
