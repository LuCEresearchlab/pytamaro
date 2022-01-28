from pytamaro.color_names import red
from pytamaro.operations import above, graphic_height, graphic_width, rotate
from pytamaro.primitives import (ellipse, circular_sector, empty_graphic,
                                 rectangle, text, triangle)
from pytest import raises

from tests.testing_utils import (HEIGHT, RADIUS, WIDTH,
                                 assert_graphics_equals_tolerance, assert_size,
                                 assert_unique_color)


def test_rectangle():
    rect = rectangle(WIDTH, HEIGHT, red)
    assert_size(rect, (WIDTH, HEIGHT))
    assert_unique_color(rect, red)


def test_negative_size():
    with raises(ValueError):
        rectangle(WIDTH, -1, red)


def test_zero_size():
    with raises(ValueError):
        rectangle(0, HEIGHT, red)


def test_empty_graphic():
    empty = empty_graphic()
    assert_size(empty, (0, 0))


def test_ellipse():
    e = ellipse(WIDTH, HEIGHT, red)
    assert_size(e, (WIDTH, HEIGHT))
    assert_unique_color(e, red)


def test_text():
    graphic = text("hello", "", 12, red)
    assert graphic_width(graphic) > 0 and graphic_height(graphic) > 0
    assert_unique_color(graphic, red)


def test_full_circular_sector():
    assert circular_sector(RADIUS, 360, red) == ellipse(
        2 * RADIUS, 2 * RADIUS, red)


def test_half_circular_sector():
    s1 = circular_sector(RADIUS, 180, red)
    assert_size(s1, (RADIUS * 2, RADIUS))
    s2 = rotate(180, s1)
    s12 = above(s2, s1)
    assert_graphics_equals_tolerance(s12, ellipse(2 * RADIUS, 2 * RADIUS, red))


def test_equilateral_triangle():
    side = 100  # large enough
    t = triangle(side, red)
    assert_unique_color(t, red)
    # Assert that the number of red pixels is almost equal (2%)
    # to the number of transparent pixels.
    colors = t.get_image().getcolors()
    pixels = graphic_width(t) * graphic_height(t)
    assert abs(colors[0][0] - colors[1][0]) <= pixels * 0.02
