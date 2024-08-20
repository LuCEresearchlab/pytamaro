from tests.testing_utils import assert_repr

from pytamaro.fr.color import (
    couleur_hsl, couleur_hsv, couleur_rgb,
)
from pytamaro.fr.color_names import (
    bleu, cyan, jaune,
    magenta, noir, rouge,
    transparent, vert, blanc,
)
import pytamaro.color_names as _color_names_en
import pytamaro.color_functions as _color_functions_en


def test_rgb_color():
    assert _color_functions_en.rgb_color(255, 0, 0) == couleur_rgb(255, 0, 0)


def test_hsv_color():
    assert _color_functions_en.hsv_color(255, 0, 0) == couleur_hsv(255, 0, 0)


def test_hsl_color():
    assert _color_functions_en.hsl_color(255, 0, 0) == couleur_hsl(255, 0, 0)


def test_rgba_color():
    assert _color_functions_en.rgb_color(0, 0, 0, 0.0) == couleur_rgb(0, 0, 0, 0.0)


def test_color_names():
    assert _color_names_en.red == rouge
    assert _color_names_en.green == vert
    assert _color_names_en.blue == bleu
    assert _color_names_en.magenta == magenta
    assert _color_names_en.cyan == cyan
    assert _color_names_en.yellow == jaune
    assert _color_names_en.black == noir
    assert _color_names_en.white == blanc


def test_transparent_color_name():
    assert _color_names_en.transparent == transparent


def test_color_localized_repr():
    assert_repr(rouge, "fr")
    assert "rouge" in repr(rouge)
