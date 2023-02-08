from typing import List, Tuple

from PIL import ImageChops, ImageFilter
from pytamaro.color import Color
from pytamaro.color_names import transparent
from pytamaro.graphic import Graphic
from pytamaro.graphic_utils import graphic_to_image
from pytamaro.operations import graphic_height, graphic_width

WIDTH = 10
HEIGHT = 20
RADIUS = 20


def pixels_colors(g: Graphic) -> List[int]:
    bitmap = g.as_image().bitmap()
    return [bitmap.getColor(x, y)
            for y in range(bitmap.height()) for x in range(bitmap.width())]


def assert_unique_color(g: Graphic,
                        color: Color):
    all_colors = pixels_colors(g)
    colors = set(filter(lambda c: c != int(transparent.color), all_colors))
    assert len(colors) == 1
    assert int(color.color) in colors


def assert_size(g: Graphic, expected_size: Tuple[int, int]):
    assert_size_tolerance(g, expected_size, tolerance=0)


def assert_value_tolerance(actual_value: float, expected_value: float, tolerance: float = 0.02):
    assert expected_value * (1 - tolerance) <= actual_value <= expected_value * (1 + tolerance)


def assert_size_tolerance(g: Graphic, expected_size: Tuple[int, int],
                          tolerance: float = 0.02):
    # 2% of tolerance by default
    assert_value_tolerance(graphic_width(g), expected_size[0], tolerance)
    assert_value_tolerance(graphic_height(g), expected_size[1], tolerance)


def assert_graphics_equals_tolerance(g1: Graphic, g2: Graphic):
    diff = ImageChops.difference(graphic_to_image(g1), graphic_to_image(g2))
    filtered_diff = diff.filter(ImageFilter.MinFilter())
    colors = filtered_diff.getcolors()
    assert len(colors) == 1
    assert colors[0][1] == transparent.as_tuple()


def assert_pin_tolerance(g: Graphic, expected_pin: Tuple[int, int]):
    x_pin, y_pin = g.pin_position
    assert expected_pin[0] - 1 <= x_pin <= expected_pin[0] + 1
    assert expected_pin[1] - 1 <= y_pin <= expected_pin[1] + 1
