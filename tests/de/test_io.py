from tempfile import NamedTemporaryFile

from PIL import Image as ImageMod
from pytamaro.color_names import blue, red
from pytamaro.de.io import speichere_gif, speichere_grafik, zeige_grafik
from pytamaro.primitives import rectangle
from tests.testing_utils import HEIGHT, WIDTH


def test_show_graphic():
    # Implicitly assert that it does not throw
    zeige_grafik(rectangle(WIDTH, HEIGHT, red))


def test_save_gif():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(WIDTH, HEIGHT, blue)
    with NamedTemporaryFile() as f:
        speichere_gif(f.name, [r1, r2])
        gif = ImageMod.open(f"{f.name}.gif")
        assert gif.n_frames == 2


def test_save_graphic():
    r = rectangle(WIDTH, HEIGHT, red)
    with NamedTemporaryFile() as f:
        speichere_grafik(f.name, r)
        graphic = ImageMod.open(f"{f.name}.png")
        assert graphic.size == (WIDTH, HEIGHT)
