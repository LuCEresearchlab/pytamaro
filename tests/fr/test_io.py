from tempfile import NamedTemporaryFile

from PIL import Image as ImageMod

from pytamaro.color_names import blue, red
from pytamaro.fr.io import (montre_animation, montre_graphique,
                            sauvegarde_animation, sauvegarde_graphique)
from pytamaro.primitives import rectangle
from tests.testing_utils import HEIGHT, WIDTH, assert_frames_count


def test_show_graphic():
    # Implicitly assert that it does not throw
    montre_graphique(rectangle(WIDTH, HEIGHT, red))


def test_show_animation():
    # Implicitly assert that it does not throw
    montre_animation([rectangle(WIDTH, HEIGHT, red)])


def test_save_animation():
    r1 = rectangle(WIDTH, HEIGHT, red)
    r2 = rectangle(WIDTH, HEIGHT, blue)
    with NamedTemporaryFile() as f:
        filename = f"{f.name}.gif"
        sauvegarde_animation(filename, [r1, r2])
        gif = ImageMod.open(filename)
        assert_frames_count(gif, 2)


def test_save_graphic():
    r = rectangle(WIDTH, HEIGHT, red)
    with NamedTemporaryFile() as f:
        filename = f"{f.name}.png"
        sauvegarde_graphique(filename, r)
        graphic = ImageMod.open(filename)
        assert graphic.size == (WIDTH, HEIGHT)
