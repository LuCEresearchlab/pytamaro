from pytamaro.color_names import red
from pytamaro.operations import pin
from pytamaro.primitives import empty_graphic, rectangle

from tests.testing_utils import HEIGHT, WIDTH


def test_pin_position():
    semiwidth = 10
    semiheight = 5
    # odd sizes, no rounding errors expected
    img = rectangle(semiwidth * 2 + 1, semiheight * 2 + 1, red)
    assert img.get_pin_position() == (semiwidth, semiheight)


def test_equality():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(WIDTH, HEIGHT, red)
    assert r1 == r2


def test_equality_empty_graphic():
    i1 = empty_graphic()
    i2 = empty_graphic()
    assert i1 == i2


def test_equality_different_pin_positions():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = pin("left", "top", r1)
    assert r1 != r2


def test_equality_not_an_graphic():
    graphic = rectangle(WIDTH, HEIGHT, red)
    assert graphic != 42


def test_hash():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(WIDTH, HEIGHT, red)
    s = set()
    s.add(r1)
    s.add(r2)
    assert len(s) == 1


def test_hash_empty_graphic():
    i1 = empty_graphic()
    i2 = empty_graphic()
    s = set()
    s.add(i1)
    s.add(i2)
    assert len(s) == 1
