from pytamaro.color import Color, rgb_color, rgba_color
from pytamaro.color_names import *
from PIL.ImageColor import getrgb


def _same_color(color: Color, name: str):
    assert color.as_tuple()[:3] == getrgb(name)


def test_rgb_color():
    _same_color(rgb_color(255, 0, 0), "red")


def test_rgba_color():
    assert rgba_color(0, 0, 0, 0).as_tuple() == (0, 0, 0, 0)


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
    transparent.as_tuple()[-1] == 0
