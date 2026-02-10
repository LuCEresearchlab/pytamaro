from pytamaro.color_names import blue, green, red
from pytamaro.impl.ffi.specs import to_specs
from pytamaro.operations import beside, compose, pin, rotate
from pytamaro.primitives import ellipse, empty_graphic, rectangle, triangle
from pytamaro.point_names import center, center_left, center_right, top_left

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

    sys.modules["pytamaro_js_ffi"] = MagicMock()
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


def test_to_specs_empty_graphic():
    _enable_ffi_impl()
    empty = empty_graphic()
    specs = to_specs(empty)
    assert len(specs) == 1
    assert specs[0]["t"] == "Empty"
    _enable_skia_impl()


def test_to_specs_rectangle():
    _enable_ffi_impl()
    r = rectangle(WIDTH, HEIGHT, red)
    specs = to_specs(r)
    assert len(specs) == 1
    rect_spec = specs[0]
    assert rect_spec["t"] == "Rectangle"
    assert rect_spec["width"] == WIDTH
    assert rect_spec["height"] == HEIGHT
    color = rect_spec["color"]
    # color is an ARGB 32-word
    a = (color >> 24) & 0xFF
    r = (color >> 16) & 0xFF
    g = (color >> 8) & 0xFF
    b = color & 0xFF
    assert a == 1.0 * 255
    assert r == 255
    assert g == 0
    assert b == 0
    _enable_skia_impl()


def test_to_specs_pin():
    _enable_ffi_impl()
    r = rectangle(WIDTH, HEIGHT, red)
    pinned = pin(top_left, r)
    specs = to_specs(pinned)
    assert len(specs) == 2
    assert specs[1]["t"] == "Pin"
    pin_value = specs[1]["pin"]
    from struct import pack, unpack
    x = unpack('>f', pack('>I', (pin_value >> 32) & 0xFFFFFFFF))[0]
    y = unpack('>f', pack('>I', pin_value & 0xFFFFFFFF))[0]
    assert x == -1.0
    assert y == 1.0
    _enable_skia_impl()


def test_to_specs_beside():
    _enable_ffi_impl()
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(WIDTH, HEIGHT, blue)
    combined = beside(r1, r2)
    specs = to_specs(combined)
    assert len(specs) == 3
    assert specs[2]["t"] == "Compose"
    assert "fg_pin" in specs[2]
    assert "bg_pin" in specs[2]
    assert "pin" in specs[2]
    rect_specs = [s for s in specs if s["t"] == "Rectangle"]
    assert len(rect_specs) == 2
    _enable_skia_impl()


def test_to_specs_nested_beside():
    _enable_ffi_impl()
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(WIDTH, HEIGHT, blue)
    r3 = ellipse(WIDTH, HEIGHT, green)
    r123 = beside(beside(r1, r2), r3)
    specs = to_specs(r123)
    types = [s["t"] for s in specs]
    assert types == ["Ellipse", "Rectangle", "Rectangle", "Compose", "Compose"]
    _enable_skia_impl()


def test_to_specs_rotate():
    _enable_ffi_impl()
    r = rectangle(WIDTH, HEIGHT, red)
    rotated = rotate(45, r)
    rotated_again = rotate(-720, rotated)
    specs = to_specs(rotated_again)
    types = [s["t"] for s in specs]
    assert types == ["Rectangle", "Rotate"]
    rotate_specs = [s for s in specs if s["t"] == "Rotate"]
    assert len(rotate_specs) == 1
    assert rotate_specs[0]["angle"] == 45
    _enable_skia_impl()


def test_to_specs_pin_compose():
    _enable_ffi_impl()
    r = rectangle(WIDTH, HEIGHT, red)
    combined = compose(pin(center_left, r), pin(center_right, r))
    specs = to_specs(combined)
    types = [s["t"] for s in specs]
    assert types == ["Rectangle", "Rectangle", "Compose"]
    _enable_skia_impl()


def test_to_specs_nested_compose():
    _enable_ffi_impl()
    g1 = rectangle(WIDTH, HEIGHT, red)
    g2 = empty_graphic()
    g3 = ellipse(WIDTH, HEIGHT, red)
    g4 = triangle(WIDTH, HEIGHT, 60, red)
    c1 = compose(g1, g2)
    c2 = compose(g3, g4)
    specs = to_specs(compose(c1, c2))
    types = [s["t"] for s in specs]
    assert types == ["Triangle", "Ellipse", "Compose", "Empty", "Rectangle", "Compose", "Compose"]
    _enable_skia_impl()
