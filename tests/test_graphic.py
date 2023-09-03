from pytamaro import beside, center_right, center_left, bottom_center, top_center, center
from pytamaro.color_names import blue, red
from pytamaro.operations import _compose_pin_center, above, overlay
from pytamaro.primitives import empty_graphic, rectangle, ellipse

from tests.testing_utils import HEIGHT, WIDTH


def test_pin_position():
    semiwidth = 10
    semiheight = 5
    img = rectangle(semiwidth * 2, semiheight * 2, red)
    assert tuple(img.pin_position) == (semiwidth, semiheight)


def test_equality():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(WIDTH, HEIGHT, red)
    assert r1 == r2


def test_equality_empty_graphic():
    i1 = empty_graphic()
    i2 = empty_graphic()
    assert i1 == i2


def test_equality_not_a_graphic():
    graphic = rectangle(WIDTH, HEIGHT, red)
    assert graphic != 42


def test_hash():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(WIDTH, HEIGHT, red)
    s = set()
    s.add(r1)
    s.add(r2)
    assert len(s) == 1


def test_hash_same_path_different_color():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(WIDTH, HEIGHT, blue)
    s = set()
    s.add(r1)
    s.add(r2)
    assert len(s) == 2


def test_hash_empty_graphic():
    i1 = empty_graphic()
    i2 = empty_graphic()
    s = set()
    s.add(i1)
    s.add(i2)
    assert len(s) == 1


def test_empty_area_not_empty_graphic():
    g = rectangle(0, HEIGHT, red)
    assert g.empty_area()


def test_beside():
    r1 = rectangle(100, 100, red)
    r2 = rectangle(200, 50, blue)
    # The original beside function
    e_graphic = _compose_pin_center(r1, r2, center_right, center_left)
    # The new beside function
    a_graphic = beside(r1, r2)
    assert e_graphic.path == a_graphic.path
    assert e_graphic.bounds() == a_graphic.bounds()
    assert e_graphic.pin_position == a_graphic.pin_position


def test_above():
    r1 = ellipse(100, 200, red)
    r2 = rectangle(200, 50, blue)
    # The original above function
    e_graphic = _compose_pin_center(r1, r2, bottom_center, top_center)
    # The new above function
    a_graphic = above(r1, r2)
    assert e_graphic.path == a_graphic.path
    assert e_graphic.bounds() == a_graphic.bounds()
    assert e_graphic.pin_position == a_graphic.pin_position


def test_overlay():
    r1 = ellipse(100, 100, red)
    r2 = rectangle(200, 200, blue)
    # The original overlay function
    e_graphic = _compose_pin_center(r1, r2, center, center)
    # The new overlay function
    a_graphic = overlay(r1, r2)
    assert e_graphic.path == a_graphic.path
    assert e_graphic.bounds() == a_graphic.bounds()
    assert e_graphic.pin_position == a_graphic.pin_position
