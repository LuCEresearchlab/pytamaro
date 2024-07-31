from tempfile import NamedTemporaryFile

from PIL import Image as ImageMod
from pytest import raises

from pytamaro.color_names import blue, red
from pytamaro.io import (save_animation, save_graphic, show_animation,
                         show_graphic)
from pytamaro.operations import above, beside, rotate
from pytamaro.primitives import empty_graphic, rectangle
from tests.testing_utils import (HEIGHT, WIDTH, assert_frames_count,
                                 assert_SVG_file_width_height)


def test_show_graphic():
    # Implicitly assert that it does not throw
    show_graphic(rectangle(WIDTH, HEIGHT, red))


def test_show_animation():
    # Implicitly assert that it does not throw
    show_animation([rectangle(WIDTH, HEIGHT, red)])


def test_show_empty_graphic(capfd):
    # Implicitly assert that it does not throw
    show_graphic(empty_graphic())
    out, _ = capfd.readouterr()
    # Assert that a nice warning message with the (rounded) size is reported
    assert "0x0" in out


def test_show_round_to_zero_graphic(capfd):
    # Implicitly assert that it does not throw
    show_graphic(rectangle(0.1, 100, red))
    out, _ = capfd.readouterr()
    # Assert that a nice warning message with the (rounded) size is reported
    assert "0x100" in out


def test_show_debug_graphic():
    # Implicitly assert that it does not throw
    show_graphic(rectangle(WIDTH, HEIGHT, red), debug=True)


def test_gif_no_ext():
    with raises(ValueError, match=".gif"):
        save_animation("foo", [rectangle(WIDTH, HEIGHT, red)])


def test_empty_save_animation():
    with raises(ValueError):
        save_animation("foo.gif", [])


def test_show_wrong_type():
    with raises(TypeError, match="NoneType"):
        show_graphic(None)  # type: ignore


def test_show_animation_wrong_type():
    with raises(TypeError, match="str"):
        show_animation("bar")  # type: ignore


def test_show_animation_wrong_element_type():
    with raises(TypeError, match="1"):
        show_animation([rectangle(WIDTH, HEIGHT, red), "bar"])  # type: ignore


def test_save_animation():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(WIDTH, HEIGHT, blue)
    with NamedTemporaryFile() as f:
        filename = f"{f.name}.gif"
        save_animation(filename, [r1, r2])
        gif = ImageMod.open(filename)
        assert_frames_count(gif, 2)


def test_save_graphic_PNG():
    r = rectangle(WIDTH, HEIGHT, red)
    with NamedTemporaryFile() as f:
        filename = f"{f.name}.png"
        save_graphic(filename, r)
        graphic = ImageMod.open(filename)
        assert graphic.size == (WIDTH, HEIGHT)


def test_save_empty_graphic_SVG():
    with NamedTemporaryFile() as f:
        filename = f"{f.name}.svg"
        save_graphic(filename, empty_graphic())
        assert_SVG_file_width_height(filename, 0, 0)


def test_save_graphic_SVG():
    r = rectangle(WIDTH, HEIGHT, red)
    with NamedTemporaryFile() as f:
        filename = f"{f.name}.svg"
        save_graphic(filename, r)
        assert_SVG_file_width_height(filename, WIDTH, HEIGHT)


def test_save_graphic_wrong_no_ext():
    r = rectangle(WIDTH, HEIGHT, red)
    with NamedTemporaryFile() as f:
        filename = f"{f.name}"
        with raises(ValueError, match="png|svg"):
            save_graphic(filename, r)


def test_save_empty_graphic_as_PNG(capfd):
    # Implicitly assert that it does not throw
    with NamedTemporaryFile() as f:
        save_graphic(f"{f.name}.png", empty_graphic())
        out, _ = capfd.readouterr()
        assert "0x0" in out


def test_save_animation_empty_graphic(capfd):
    # Implicitly assert that it does not throw
    with NamedTemporaryFile() as f:
        save_animation(f"{f.name}.gif", [rectangle(100, 0, red)])
        out, _ = capfd.readouterr()
        assert "100x0" in out


def test_save_animation_multiple_empty_graphics(capfd):
    # Implicitly assert that it does not throw
    with NamedTemporaryFile() as f:
        save_animation(f"{f.name}.gif", [rectangle(200, 0, red), rectangle(0, 200, blue)])
        out, _ = capfd.readouterr()
        assert "200x0" in out


def test_antialiasing():
    # Two red squares rotated 45 degrees, one above the other, should have no visible seam in between
    # (i.e., all pixels should be pure red).
    side = 100
    r = rectangle(side, side, red)
    g = rotate(45, above(r, r))
    with NamedTemporaryFile() as f:
        filename = f"{f.name}.png"
        save_graphic(filename, g)
        image = ImageMod.open(filename)
        image_rotated = image.rotate(-45)
        h_center = image_rotated.width // 2
        v_center = image_rotated.height // 2
        pixels_seams = [image_rotated.getpixel((x, y)) for x in range(h_center - 20, h_center + 21) for y in range(v_center - 1, v_center + 2)]
        print(pixels_seams)
        assert all(pixel == (255, 0, 0, 255) for pixel in pixels_seams)


DATA_URI_11RED_RECT = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR4nGP4z8DwHwAFAAH/iZk9HQAAAABJRU5ErkJggg=="
DATA_URI_11RED_RECT_GIF = "data:image/gif;base64,R0lGODlhAQABAIEAAP8AAAAAAAAAAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQIBAAAACwAAAAAAQABAAAIBAABBAQAOw=="
PREFIX = "@@@PYTAMARO_DATA_URI_BEGIN@@@"
SUFFIX = "@@@PYTAMARO_DATA_URI_END@@@"


def test_data_uri_output(capfd):
    import os

    VAR = "PYTAMARO_OUTPUT_DATA_URI"
    os.environ[VAR] = "True"
    r = rectangle(1, 1, red)
    show_graphic(r)
    out, _ = capfd.readouterr()
    assert (
        out == f"{PREFIX}{DATA_URI_11RED_RECT}{SUFFIX}"
    )
    del os.environ[VAR]


def test_multiple_data_uri_mixed_output(capfd):
    import os

    VAR = "PYTAMARO_OUTPUT_DATA_URI"
    os.environ[VAR] = "True"
    r = rectangle(1, 1, red)
    print(42)
    show_graphic(r)
    print(42)
    show_graphic(r)
    print(42)
    out, _ = capfd.readouterr()
    assert (
        out == f"42\n{PREFIX}{DATA_URI_11RED_RECT}{SUFFIX}42\n{PREFIX}{DATA_URI_11RED_RECT}{SUFFIX}42\n"
    )
    del os.environ[VAR]


def test_data_uri_gif_output(capfd):
    import os

    VAR = "PYTAMARO_OUTPUT_DATA_URI"
    os.environ[VAR] = "True"
    r = rectangle(1, 1, red)
    show_animation([r])
    out, _ = capfd.readouterr()
    assert (
        out
        == f"{PREFIX}{DATA_URI_11RED_RECT_GIF}{SUFFIX}"
    )
    del os.environ[VAR]


def test_show_deeply_nested_graphic():
    element = rectangle(WIDTH, HEIGHT, red)
    from functools import reduce
    graphic = reduce(beside, [element] * 1000, empty_graphic())
    # Implicitly assert that it does not throw
    show_graphic(graphic)


def test_animation_frames_not_overlaid():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(HEIGHT, WIDTH, blue)
    with NamedTemporaryFile() as f:
        filename = f"{f.name}.gif"
        save_animation(filename, [beside(r1, r2), beside(r2, r1)])
        gif = ImageMod.open(filename)
        assert_frames_count(gif, 2)

        def non_transparent_pixels(frame):
            return sum(1 for pixel in frame.convert("RGBA").getdata() if pixel[3] > 0)

        gif.seek(0)
        colored_frame0 = non_transparent_pixels(gif)
        gif.seek(1)
        colored_frame1 = non_transparent_pixels(gif)
        assert colored_frame0 == colored_frame1
