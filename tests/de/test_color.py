from pytamaro.color import *
from pytamaro.color_names import *
from pytamaro.de.color import *
from pytamaro.de.color_names import *


def test_rgb_color():
    assert rgb_color(255, 0, 0) == rgb_farbe(255, 0, 0)


def test_hsv_color():
    assert hsv_color(255, 0, 0) == hsv_farbe(255, 0, 0)

    
def test_hsl_color():
    assert hsl_color(255, 0, 0) == hsl_farbe(255, 0, 0)


def test_rgba_color():
    assert rgb_color(0, 0, 0, 0.0) == rgb_farbe(0, 0, 0, 0.0)


def test_color_names():
    assert red == rot
    assert green == gruen
    assert blue == blau
    assert magenta == magenta
    assert cyan == cyan
    assert yellow == gelb
    assert black == schwarz
    assert white == weiss


def test_transparent_color_name():
    assert transparent == transparent
