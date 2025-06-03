from pytamaro.graphic import Graphic

from pytamaro.color_names import blue, red

from tests.testing_utils import (
    HEIGHT,
    RADIUS,
    WIDTH,
    assert_color,
    assert_graphics_equals_tolerance,
    assert_repr,
    assert_size,
    assert_unique_color,
    assert_value_tolerance,
    pixels_colors,
    assert_serializer_deserializer,
)


def test_rectangle():

    from pytamaro import rectangle

    rect = rectangle(WIDTH, HEIGHT, red)

    assert_serializer_deserializer(rect)


def test_ellipse():
    from pytamaro import ellipse

    ellipse = ellipse(WIDTH, HEIGHT, red)

    assert_serializer_deserializer(ellipse)


def test_text():
    from pytamaro import text

    text_ = text("hello", "Arial", 12, red)

    assert_serializer_deserializer(text_)


def test_empty_graphic():
    from pytamaro import empty_graphic

    empty = empty_graphic()

    assert_serializer_deserializer(empty)


def test_triangle():
    from pytamaro import triangle

    tri = triangle(WIDTH, HEIGHT, 42, red)

    assert_serializer_deserializer(tri)


def test_above():
    from pytamaro import above, rectangle, triangle

    rect = rectangle(WIDTH, HEIGHT, red)
    tri = triangle(WIDTH, HEIGHT, 42, blue)

    above_graphic = above(rect, tri)

    assert_serializer_deserializer(above_graphic)


def test_beside():
    from pytamaro import beside, rectangle, triangle

    rect = rectangle(WIDTH, HEIGHT, red)
    tri = triangle(WIDTH, HEIGHT, 42, blue)

    beside_graphic = beside(rect, tri)

    assert_serializer_deserializer(beside_graphic)


def test_overlay():
    from pytamaro import overlay, rectangle, triangle

    rect = rectangle(WIDTH, HEIGHT, red)
    tri = triangle(WIDTH, HEIGHT, 42, blue)

    overlay_graphic = overlay(rect, tri)

    assert_serializer_deserializer(overlay_graphic)


def test_circular_sector():
    from pytamaro import circular_sector

    sector = circular_sector(RADIUS, 90, red)

    assert_serializer_deserializer(sector)


def test_compose():
    from pytamaro import compose, rectangle, triangle

    rect = rectangle(WIDTH, HEIGHT, red)
    tri = triangle(WIDTH, HEIGHT, 42, blue)

    composed_graphic = compose(rect, tri)

    assert_serializer_deserializer(composed_graphic)


def test_rotate():
    from pytamaro import rotate, rectangle

    rect = rectangle(WIDTH, HEIGHT, red)
    rotated_graphic = rotate(42, rect)

    assert_serializer_deserializer(rotated_graphic)


def test_pin():
    from pytamaro import pin, rectangle, top_center

    rect = rectangle(WIDTH, HEIGHT, red)
    pinned_graphic = pin(top_center, rect)

    assert_serializer_deserializer(pinned_graphic)
