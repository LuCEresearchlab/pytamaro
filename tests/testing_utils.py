from typing import Tuple

from PIL import ImageChops, ImageFilter
from pytamaro.color import Color
from pytamaro.color_names import transparent
from pytamaro.graphic import Graphic
from pytamaro.operations import graphic_height, graphic_width

WIDTH = 10
HEIGHT = 20
RADIUS = 20


def assert_unique_color(g: Graphic,
                        color: Color):
    colors = list(
        filter(lambda c: c[1] != transparent.as_tuple(),
               g.get_image().getcolors()))
    assert len(colors) == 1
    assert colors[0][1] == color.as_tuple()


def assert_size(g: Graphic, expected_size: Tuple[int, int]):
    assert_size_tolerance(g, expected_size, tolerance=0)


def assert_size_tolerance(g: Graphic, expected_size: Tuple[int, int],
                          tolerance: float = 0.05):
    # 5% of tolerance by default
    assert expected_size[0] * (1 - tolerance) <= \
        graphic_width(g) <= expected_size[0] * (1 + tolerance)
    assert expected_size[1] * (1 - tolerance) <= \
        graphic_height(g) <= expected_size[1] * (1 + tolerance)


def assert_graphics_equals_tolerance(g1: Graphic, g2: Graphic):
    diff = ImageChops.difference(g1.get_image(), g2.get_image())
    filtered_diff = diff.filter(ImageFilter.MinFilter())
    colors = filtered_diff.getcolors()
    assert len(colors) == 1
    assert colors[0][1] == transparent.as_tuple()


def assert_pin_tolerance(g: Graphic, expected_pin: Tuple[int, int]):
    x_pin, y_pin = g.get_pin_position()
    assert expected_pin[0] - 1 <= x_pin <= expected_pin[0] + 1
    assert expected_pin[1] - 1 <= y_pin <= expected_pin[1] + 1
