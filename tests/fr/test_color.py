import pytamaro as _pytamaro
from pytamaro.fr.color import couleur_hsl, couleur_hsv, couleur_rgb
from pytamaro.fr.color_names import (blanc, bleu, cyan, jaune, magenta, noir,
                                     rouge, transparent, vert)
from tests.testing_utils import assert_repr


def test_rgb_color():
    assert _pytamaro.rgb_color(255, 0, 0) == couleur_rgb(255, 0, 0)


def test_hsv_color():
    assert _pytamaro.hsv_color(255, 0, 0) == couleur_hsv(255, 0, 0)


def test_hsl_color():
    assert _pytamaro.hsl_color(255, 0, 0) == couleur_hsl(255, 0, 0)


def test_rgba_color():
    assert _pytamaro.rgb_color(0, 0, 0, 0.0) == couleur_rgb(0, 0, 0, 0.0)


def test_color_names():
    assert _pytamaro.red == rouge
    assert _pytamaro.green == vert
    assert _pytamaro.blue == bleu
    assert _pytamaro.magenta == magenta
    assert _pytamaro.cyan == cyan
    assert _pytamaro.yellow == jaune
    assert _pytamaro.black == noir
    assert _pytamaro.white == blanc


def test_transparent_color_name():
    assert _pytamaro.transparent == transparent


def test_color_localized_repr():
    assert_repr(rouge, "fr")
    assert "rouge" in repr(rouge)
