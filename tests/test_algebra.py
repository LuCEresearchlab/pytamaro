from pytamaro.color_names import red
from pytamaro.operations import compose
from pytamaro.primitives import empty_graphic, rectangle
from tests.testing_utils import HEIGHT, WIDTH, assert_equals_pixels


def test_empty_graphic_left_identity():
    r = rectangle(WIDTH, HEIGHT, red)
    assert_equals_pixels(compose(empty_graphic(), r), r)


def test_empty_graphic_right_identity():
    r = rectangle(WIDTH, HEIGHT, red)
    assert_equals_pixels(compose(r, empty_graphic()), r)
