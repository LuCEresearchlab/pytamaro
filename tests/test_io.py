from tempfile import NamedTemporaryFile

from PIL import Image as ImageMod
from pytamaro.color_names import blue, red
from pytamaro.io import save_gif, save_graphic, show_graphic
from pytamaro.primitives import empty_graphic, rectangle
from pytest import raises

from tests.testing_utils import HEIGHT, WIDTH


def test_show_graphic():
    # Implicitly assert that it does not throw
    show_graphic(rectangle(WIDTH, HEIGHT, red))


def test_show_empty_graphic():
    # Implicitly assert that it does not throw
    show_graphic(empty_graphic())


def test_show_debug_graphic():
    # Implicitly assert that it does not throw
    show_graphic(rectangle(WIDTH, HEIGHT, red), debug=True)


def test_empty_save_gif():
    with raises(ValueError):
        save_gif("foo", [])


def test_save_gif():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(WIDTH, HEIGHT, blue)
    with NamedTemporaryFile() as f:
        save_gif(f.name, [r1, r2])
        gif = ImageMod.open(f"{f.name}.gif")
        assert gif.n_frames == 2


def test_save_graphic():
    r = rectangle(WIDTH, HEIGHT, red)
    with NamedTemporaryFile() as f:
        save_graphic(f.name, r)
        graphic = ImageMod.open(f"{f.name}.png")
        assert graphic.size == (WIDTH, HEIGHT)


def test_save_empty_graphic():
    # Implicitly assert that it does not throw
    with NamedTemporaryFile() as f:
        save_graphic(f.name, empty_graphic())
