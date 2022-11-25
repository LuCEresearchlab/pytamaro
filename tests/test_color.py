from pytamaro.color import Color
from PIL.ImageColor import getrgb
from pytamaro.color import hsv_color, hsl_color
from pytamaro.color_names import *


def _same_color(color: Color, name: str):
    assert color.as_tuple()[:3] == getrgb(name)


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
    assert transparent.as_tuple()[-1] == 0.0


def test_hsl_rgb_conversion():
    # Check red, green and blue colors
    assert hsl_color(0, 1, 0.5) == rgb_color(255, 0, 0)
    assert hsl_color(120, 1, 0.5) == rgb_color(0, 255, 0)
    assert hsl_color(240, 1, 0.5) == rgb_color(0, 0, 255)


def test_hsv_rbg_conversion():
    # Check red, green and blue colors
    assert hsv_color(0, 1, 1) == rgb_color(255, 0, 0)
    assert hsv_color(120, 1, 1) == rgb_color(0, 255, 0)
    assert hsv_color(240, 1, 1) == rgb_color(0, 0, 255)
