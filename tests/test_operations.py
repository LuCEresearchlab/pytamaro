from pytamaro.color_names import blue, red
from pytamaro.operations import (above, beside, compose, graphic_height,
                                 graphic_width, overlay, pin, rotate)
from pytamaro.point_names import bottom_left, bottom_right, top_left
from pytamaro.primitives import ellipse, rectangle, triangle
from tests.testing_utils import (HEIGHT, RADIUS, WIDTH, assert_color,
                                 assert_equals_rendered, assert_pin_tolerance,
                                 assert_repr, assert_size,
                                 assert_size_tolerance, assert_unique_color)


def test_width():
    assert graphic_width(rectangle(WIDTH, HEIGHT, red)) == WIDTH


def test_height():
    assert graphic_height(rectangle(WIDTH, HEIGHT, red)) == HEIGHT


# Rotation


def test_rotate_multiples_90():
    r = rectangle(WIDTH, HEIGHT, red)
    rot = rotate(90, r)
    assert_size(rot, (HEIGHT, WIDTH))
    assert_unique_color(rot, red)
    flipped = rotate(180, r)
    assert_size(flipped, (WIDTH, HEIGHT))
    assert_unique_color(flipped, red)


def test_rotate_45():
    c = ellipse(2 * RADIUS, 2 * RADIUS, red)
    rot = rotate(45, c)
    assert_size_tolerance(rot, (RADIUS * 2, RADIUS * 2))
    assert_color(rot, red)  # color might not be unique due to antialiasing


def test_rotate_pin_left_top():
    r = pin(top_left, rectangle(WIDTH, HEIGHT, red))
    bottomleft = rotate(90, r)
    topright = rotate(180, bottomleft)
    assert_size(compose(bottomleft, topright), (2 * HEIGHT, 2 * WIDTH))


def test_rotate_pin_left_bottom_negative():
    r = pin(bottom_left, rectangle(WIDTH, HEIGHT, red))
    bottomright = rotate(-90, r)
    topleft = rotate(180, bottomright)
    assert_size(compose(bottomright, topleft), (2 * HEIGHT, 2 * WIDTH))


def test_rotate_pin_right_bottom():
    r = pin(bottom_right, rectangle(WIDTH, HEIGHT, red))
    rot = rotate(180, r)
    assert_size(compose(r, rot), (2 * WIDTH, 2 * HEIGHT))


def test_rotate_pin_triangle():
    t = pin(top_left, triangle(WIDTH, WIDTH, 90, red))
    assert_size(
        compose(t, rotate(270, t)), (2 * graphic_width(t), graphic_height(t)))


def test_rotate_pin_circle():
    c = ellipse(2 * RADIUS, 2 * RADIUS, red)
    assert_pin_tolerance(rotate(90, c), (RADIUS, RADIUS))


def test_rotate_repr():
    r = rotate(90, rectangle(WIDTH, HEIGHT, red))
    assert_repr(r, "en")


# Beside


def test_beside_same_height():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(2 * WIDTH, HEIGHT, red)
    joined = beside(r1, r2)
    assert_size(joined, (3 * WIDTH, HEIGHT))
    assert_unique_color(joined, red)


def test_beside_different_height():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(2 * WIDTH, 2 * HEIGHT, red)
    joined = beside(r1, r2)
    assert_size(joined, (3 * WIDTH, 2 * HEIGHT))
    assert_color(joined, red)  # color might not be unique due to antialiasing


def test_beside_pinning_position():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(2 * WIDTH, HEIGHT, red)
    joined = beside(r1, r2)
    # Joined should have the pinning position at its center
    assert graphic_width(compose(rectangle(3 * WIDTH, HEIGHT, red), joined)) == 3 * WIDTH


def test_beside_repr():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(2 * WIDTH, HEIGHT, red)
    joined = beside(r1, r2)
    assert_repr(joined, "en")


# Above


def test_above_same_width():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(WIDTH, 2 * HEIGHT, red)
    joined = above(r1, r2)
    assert_size(joined, (WIDTH, 3 * HEIGHT))
    assert_unique_color(joined, red)


def test_above_different_width():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(2 * WIDTH, 2 * HEIGHT, red)
    joined = above(r1, r2)
    assert_size(joined, (2 * WIDTH, 3 * HEIGHT))
    assert_color(joined, red)  # color might not be unique due to antialiasing


def test_above_pinning_position():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(WIDTH, HEIGHT * 2, red)
    joined = above(r1, r2)
    # Joined should have the pinning position at its center
    assert graphic_height(compose(rectangle(WIDTH, 3 * HEIGHT, red), joined)) == 3 * HEIGHT


def test_above_repr():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(WIDTH, 2 * HEIGHT, red)
    joined = above(r1, r2)
    assert_repr(joined, "en")


# Overlay


def test_overlay_squares():
    s1 = rectangle(WIDTH, WIDTH, blue)
    s2 = rectangle(WIDTH, WIDTH, red)
    s_blue = overlay(s1, s2)
    assert_size(s_blue, (WIDTH, WIDTH))
    assert_unique_color(s_blue, blue)
    s_red = overlay(s2, s1)
    assert_size(s_red, (WIDTH, WIDTH))
    assert_unique_color(s_red, red)


def test_overlay_small_large():
    large = 2 * WIDTH
    small = WIDTH
    s1 = rectangle(large, large, blue)
    s2 = rectangle(small, small, red)
    s_blue = overlay(s1, s2)
    assert_size(s_blue, (large, large))
    assert_unique_color(s_blue, blue)
    s_blue_red = overlay(s2, s1)
    assert_size(s_blue_red, (large, large))


def test_overlay_repr():
    large = 2 * WIDTH
    small = WIDTH
    s1 = rectangle(large, large, blue)
    s2 = rectangle(small, small, red)
    s_blue_red = overlay(s2, s1)
    assert_repr(s_blue_red, "en")


# Compose


def test_compose():
    s1 = rectangle(WIDTH, WIDTH, blue)
    s2 = rectangle(WIDTH, WIDTH, red)
    composed = compose(s1, s2)
    assert_size(composed, (WIDTH, WIDTH))
    assert_unique_color(composed, blue)


def test_compose_visually_equals_overlay():
    s1 = rectangle(WIDTH, WIDTH, blue)
    s2 = rectangle(WIDTH, WIDTH, red)
    assert_equals_rendered(compose(s1, s2), overlay(s1, s2))


def test_compose_pin_repr():
    s1 = rectangle(WIDTH, WIDTH, blue)
    s2 = rectangle(WIDTH, WIDTH, red)
    composed = compose(pin(top_left, s1), s2)
    assert_repr(composed, "en")
