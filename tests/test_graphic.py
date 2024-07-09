from pytamaro.color_names import blue, red
from pytamaro.primitives import empty_graphic, rectangle

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
    assert g.zero_pixels()
