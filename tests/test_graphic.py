from dataclasses import asdict
from pytamaro.color_names import blue, red
from pytamaro.operations import beside
from pytamaro.primitives import circular_sector, empty_graphic, rectangle

from tests.testing_utils import HEIGHT, WIDTH


def test_pin_position():
    semiwidth = 10
    semiheight = 5
    img = rectangle(semiwidth * 2, semiheight * 2, red)
    assert tuple(img.pin_position) == (semiwidth, semiheight)  # pyright: ignore[reportAttributeAccessIssue]


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
    assert g.zero_pixels()  # pyright: ignore[reportAttributeAccessIssue]


def _mock_pytamaro_ffi():
    import sys
    from unittest.mock import MagicMock
    sys.modules['pytamaro_ffi'] = MagicMock()
    import pytamaro
    import pytamaro.impl.ffi.primitives
    import pytamaro.impl.ffi.operations
    pytamaro.primitives.__impl = pytamaro.impl.ffi.primitives  # type: ignore
    pytamaro.operations.__impl = pytamaro.impl.ffi.operations  # type: ignore


def test_asdict():
    _mock_pytamaro_ffi()
    r = rectangle(WIDTH, HEIGHT, red)
    d = asdict(r)
    assert d["type"] == "Rectangle"
    assert d["width"] == WIDTH
    assert d["height"] == HEIGHT
    color = d["color"]
    assert color["alpha"] == 1.0
    assert color["red"] == 255
    assert color["green"] == 0
    assert color["blue"] == 0


def test_asdict_recursive():
    _mock_pytamaro_ffi()
    r = rectangle(WIDTH, HEIGHT, red)
    c = circular_sector(WIDTH, HEIGHT, red)
    g = beside(r, c)
    d = asdict(g)
    assert d["type"] == "Beside"
    assert d["left_graphic"]["type"] == "Rectangle"
    assert d["right_graphic"]["type"] == "CircularSector"
