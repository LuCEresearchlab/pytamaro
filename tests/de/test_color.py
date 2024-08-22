from tests.testing_utils import assert_repr

from pytamaro.de.color_names import (
    rot, gruen, blau,
    magenta, cyan, gelb,
    schwarz, weiss, transparent,
)
from pytamaro.de.color import (
    rgb_farbe, hsv_farbe, hsl_farbe,
)
import pytamaro as _en


def test_rgb_color():
    assert _en.rgb_color(255, 0, 0) == rgb_farbe(255, 0, 0)


def test_hsv_color():
    assert _en.hsv_color(255, 0, 0) == hsv_farbe(255, 0, 0)


def test_hsl_color():
    assert _en.hsl_color(255, 0, 0) == hsl_farbe(255, 0, 0)


def test_rgba_color():
    assert _en.rgb_color(0, 0, 0, 0.0) == rgb_farbe(0, 0, 0, 0.0)


def test_color_names():
    assert _en.red == rot
    assert _en.green == gruen
    assert _en.blue == blau
    assert _en.magenta == magenta
    assert _en.cyan == cyan
    assert _en.yellow == gelb
    assert _en.black == schwarz
    assert _en.white == weiss


def test_transparent_color_name():
    assert transparent == transparent


def test_color_localized_repr():
    assert_repr(rot, "de")
    assert "rot" in repr(rot)
