from collections import Counter

from pytest import raises

from pytamaro.color_names import blue, red
from pytamaro.operations import (above, compose, graphic_height, graphic_width,
                                 rotate)
from pytamaro.primitives import (circular_sector, ellipse, empty_graphic,
                                 rectangle, text, triangle)
from tests.testing_utils import (HEIGHT, RADIUS, WIDTH, assert_color,
                                 assert_graphics_equals_tolerance, assert_repr,
                                 assert_size, assert_unique_color,
                                 assert_value_tolerance, pixels_colors)


def test_rectangle():
    rect = rectangle(WIDTH, HEIGHT, red)
    assert_size(rect, (WIDTH, HEIGHT))
    assert_unique_color(rect, red)


def test_rectangle_repr():
    assert_repr(rectangle(WIDTH, HEIGHT, red), "en")


def test_negative_size():
    with raises(ValueError):
        rectangle(WIDTH, -1, red)


def test_empty_graphic():
    empty = empty_graphic()
    assert_size(empty, (0, 0))


def test_empty_graphic_repr():
    assert_repr(empty_graphic(), "en")


def test_ellipse():
    e = ellipse(WIDTH, HEIGHT, red)
    assert_size(e, (WIDTH, HEIGHT))
    assert_color(e, red)  # color might not be unique due to antialiasing


def test_ellipse_repr():
    assert_repr(ellipse(WIDTH, HEIGHT, red), "en")


def test_text():
    graphic = text("hello", "", 32, red)
    assert graphic_width(graphic) > 0 and graphic_height(graphic) > 0
    assert_color(graphic, red)  # color might not be unique due to antialiasing


def test_text_leading_trailing_spaces():
    regular = "hello"
    leading = " " + regular
    trailing = regular + " "
    graphic_regular = text(regular, "", 12, red)
    graphic_leading = text(leading, "", 12, red)
    graphic_trailing = text(trailing, "", 12, red)
    assert graphic_width(graphic_leading) > graphic_width(graphic_regular)
    assert graphic_width(graphic_trailing) > graphic_width(graphic_regular)


def test_text_repr():
    assert_repr(text("hello", "", 12, red), "en")


def test_circular_sector_0_deg():
    s = circular_sector(RADIUS, 0, red)
    assert_size(s, (RADIUS, 0))


def test_circular_sector_360_deg():
    s = circular_sector(RADIUS, 360, red)
    c = ellipse(2 * RADIUS, 2 * RADIUS, red)
    assert_graphics_equals_tolerance(s, c)


def test_half_circular_sector():
    s1 = circular_sector(RADIUS, 180, red)
    assert_size(s1, (RADIUS * 2, RADIUS))
    s2 = rotate(180, s1)
    s12 = above(s1, s2)
    assert_graphics_equals_tolerance(s12, ellipse(2 * RADIUS, 2 * RADIUS, red))


def test_circular_sector_original_pin_position():
    s359 = circular_sector(RADIUS, 359, red)
    s360 = circular_sector(RADIUS, 360, red)
    circle = ellipse(2 * RADIUS, 2 * RADIUS, red)
    # When the pinning position is correctly set to the center,
    # composing it with a circle of the same radius should
    # result in a graphic of the same size.
    assert_size(compose(circle, s359), (2 * RADIUS, 2 * RADIUS))
    assert_size(compose(circle, s360), (2 * RADIUS, 2 * RADIUS))


def test_circular_sector_pin_position():
    s1 = circular_sector(RADIUS, 180, red)  # pin at top_center
    s2 = rotate(180, s1)  # pin at bottom_center
    s12 = compose(s1, s2)
    assert_graphics_equals_tolerance(s12, ellipse(2 * RADIUS, 2 * RADIUS, red))


def test_circular_sector_negative_angle():
    with raises(ValueError, match='[0, 360]'):
        circular_sector(RADIUS, -1, red)


def test_circular_sector_repr():
    assert_repr(circular_sector(RADIUS, 180, red), "en")


def test_equilateral_triangle():
    side = 100  # large enough
    t = triangle(side, side, 60, red)
    assert_color(t, red)  # color might not be unique due to antialiasing
    # Assert that the number of red pixels is almost equal (<=5%)
    # to the number of transparent pixels.
    colors = Counter(pixels_colors(t))
    pixels = graphic_width(t) * graphic_height(t)
    common = colors.most_common(2)
    assert abs(common[0][1] - common[1][1]) <= pixels * 0.05


def test_right_triangle_pinning_position():
    small = 100
    redt = triangle(small, small, 90, red)
    small_area = small * small / 2
    large = 200
    bluet = triangle(large, large, 90, blue)
    large_area = large * large / 2
    t = compose(redt, bluet)
    # Most common expected to be transparent, then blue, then red.
    colors = Counter(pixels_colors(t))
    common = colors.most_common(3)
    assert_value_tolerance(common[1][1], large_area - small_area, 0.05)
    assert_value_tolerance(common[2][1], small_area, 0.05)


def test_triangle_repr():
    assert_repr(triangle(WIDTH, HEIGHT, 90, red), "en")
