from pytamaro.color_names import blue, red
from pytamaro.impl.ffi.specs import to_specs
from pytamaro.operations import beside
from pytamaro.primitives import circular_sector, empty_graphic, rectangle
from pytamaro.point_names import center, center_left, center_right

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


def _enable_ffi_impl():
    import sys
    from unittest.mock import MagicMock
    sys.modules['pytamaro_js_ffi'] = MagicMock()
    import pytamaro
    import pytamaro.impl.ffi.primitives
    import pytamaro.impl.ffi.operations
    pytamaro.primitives.__impl = pytamaro.impl.ffi.primitives  # type: ignore
    pytamaro.operations.__impl = pytamaro.impl.ffi.operations  # type: ignore


def _enable_skia_impl():
    import pytamaro
    import pytamaro.impl.skia.primitives
    import pytamaro.impl.skia.operations
    pytamaro.primitives.__impl = pytamaro.impl.skia.primitives  # type: ignore
    pytamaro.operations.__impl = pytamaro.impl.skia.operations  # type: ignore


def test_to_spec():
    _enable_ffi_impl()
    r = rectangle(WIDTH, HEIGHT, red)
    specs = to_specs(r)
    rect_spec = specs[0]
    assert rect_spec["type"] == "Rectangle"
    assert rect_spec["width"] == WIDTH
    assert rect_spec["height"] == HEIGHT
    color = rect_spec["color"]
    assert color["alpha"] == 1.0
    assert color["red"] == 255
    assert color["green"] == 0
    assert color["blue"] == 0
    _enable_skia_impl()
