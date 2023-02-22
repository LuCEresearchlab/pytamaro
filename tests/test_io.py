from tempfile import NamedTemporaryFile

from PIL import Image as ImageMod
from pytamaro.color_names import blue, red
from pytamaro.io import save_gif, save_graphic, show_graphic
from pytamaro.primitives import empty_graphic, rectangle
from pytest import raises

from tests.testing_utils import HEIGHT, WIDTH, assert_SVG_file_width_height


def test_show_graphic():
    # Implicitly assert that it does not throw
    show_graphic(rectangle(WIDTH, HEIGHT, red))


def test_show_empty_graphic(capfd):
    # Implicitly assert that it does not throw
    show_graphic(empty_graphic())
    out, _ = capfd.readouterr()
    assert "0x0" in out


def test_show_debug_graphic():
    # Implicitly assert that it does not throw
    show_graphic(rectangle(WIDTH, HEIGHT, red), debug=True)


def test_gif_no_ext():
    with raises(ValueError, match=".gif"):
        save_gif("foo", [rectangle(WIDTH, HEIGHT, red)])


def test_empty_save_gif():
    with raises(ValueError):
        save_gif("foo.gif", [])


def test_show_wrong_type():
    with raises(TypeError, match="NoneType"):
        show_graphic(None)  # type: ignore


def test_save_gif():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(WIDTH, HEIGHT, blue)
    with NamedTemporaryFile() as f:
        filename = f"{f.name}.gif"
        save_gif(filename, [r1, r2])
        gif = ImageMod.open(filename)
        assert gif.n_frames == 2


def test_save_graphic_PNG():
    r = rectangle(WIDTH, HEIGHT, red)
    with NamedTemporaryFile() as f:
        filename = f"{f.name}.png"
        save_graphic(filename, r)
        graphic = ImageMod.open(filename)
        assert graphic.size == (WIDTH, HEIGHT)


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


def test_data_uri_output(capfd):
    import os

    VAR = "PYTAMARO_OUTPUT_DATA_URI"
    os.environ[VAR] = "True"
    r = rectangle(1, 1, red)
    show_graphic(r)
    out, _ = capfd.readouterr()
    assert (
        out
        == "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR4nGP4z8DwHwAFAAH/iZk9HQAAAABJRU5ErkJggg=="
    )
    del os.environ[VAR]
