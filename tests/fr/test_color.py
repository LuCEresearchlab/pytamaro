from pytamaro.color import *
import pytamaro.color_names as en
from pytamaro.fr.color import *
import pytamaro.fr.color_names as fr
from tests.testing_utils import assert_repr


def test_rgb_color():
    assert rgb_color(255, 0, 0) == couleur_rgb(255, 0, 0)


def test_hsv_color():
    assert hsv_color(255, 0, 0) == couleur_hsv(255, 0, 0)


def test_hsl_color():
    assert hsl_color(255, 0, 0) == couleur_hsl(255, 0, 0)


def test_rgba_color():
    assert rgb_color(0, 0, 0, 0.0) == couleur_rgb(0, 0, 0, 0.0)


def test_color_names():
    assert en.red == fr.rouge
    assert en.green == fr.vert
    assert en.blue == fr.bleu
    assert en.magenta == fr.magenta
    assert en.cyan == fr.cyan
    assert en.yellow == fr.jaune
    assert en.black == fr.noir
    assert en.white == fr.blanc


def test_transparent_color_name():
    assert en.transparent == fr.transparent


def test_color_localized_repr():
    assert_repr(fr.rouge, "fr")
    assert "rouge" in repr(fr.rouge)
