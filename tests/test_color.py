from PIL.ImageColor import getrgb

from pytamaro.color import Color
from pytamaro.color_functions import hsl_color, hsv_color
from pytamaro.color_names import *
from tests.testing_utils import assert_repr


def _same_color(color: Color, name: str):
    assert (color.red, color.green, color.blue) == getrgb(name)


def test_rgb_color():
    _same_color(rgb_color(255, 0, 0), "red")


def test_color_names():
    _same_color(red, "red")
    _same_color(green, "lime")  # green is #008000, lime is #00FF00
    _same_color(blue, "blue")
    _same_color(magenta, "magenta")
    _same_color(cyan, "cyan")
    _same_color(yellow, "yellow")
    _same_color(black, "black")
    _same_color(white, "white")


def test_transparent_color_name():
    assert transparent.alpha == 0.0


def test_hsl_rgb_conversion():
    # Check corners of RGB / CMY color cube
    assert hsl_color(0, 1, 0.5) == rgb_color(255, 0, 0)      # red
    assert hsl_color(60, 1, 0.5) == rgb_color(255, 255, 0)   # yellow
    assert hsl_color(120, 1, 0.5) == rgb_color(0, 255, 0)    # green
    assert hsl_color(180, 1, 0.5) == rgb_color(0, 255, 255)  # cyan
    assert hsl_color(240, 1, 0.5) == rgb_color(0, 0, 255)    # blue
    assert hsl_color(300, 1, 0.5) == rgb_color(255, 0, 255)  # magenta
    assert hsl_color(0, 0, 1) == rgb_color(255, 255, 255)    # white
    assert hsl_color(0, 0, 0) == rgb_color(0, 0, 0)          # black


def test_hsv_rbg_conversion():
    # Check corners of RGB / CMY color cube
    assert hsv_color(0, 1, 1) == rgb_color(255, 0, 0)      # red
    assert hsv_color(60, 1, 1) == rgb_color(255, 255, 0)   # yellow
    assert hsv_color(120, 1, 1) == rgb_color(0, 255, 0)    # green
    assert hsv_color(180, 1, 1) == rgb_color(0, 255, 255)  # cyan
    assert hsv_color(240, 1, 1) == rgb_color(0, 0, 255)    # blue
    assert hsv_color(300, 1, 1) == rgb_color(255, 0, 255)  # magenta
    assert hsv_color(0, 0, 1) == rgb_color(255, 255, 255)  # white
    assert hsv_color(0, 0, 0) == rgb_color(0, 0, 0)        # black


def test_color_repr():
    from pytamaro.color_names import _known_colors
    for color in _known_colors:
        assert_repr(color, "en")
    assert_repr(rgb_color(1, 1, 1), "en")
    assert_repr(rgb_color(1, 1, 1, 0.5), "en")
