from tests.testing_utils import assert_repr

from pytamaro.fr.color import (
    couleur_hsl, couleur_hsv, couleur_rgb,
)
from pytamaro.fr.color_names import (
    bleu, cyan, jaune,
    magenta, noir, rouge,
    transparent, vert, blanc,
)
import pytamaro as _en


def test_rgb_color():
    assert _en.rgb_color(255, 0, 0) == couleur_rgb(255, 0, 0)


def test_hsv_color():
    assert _en.hsv_color(255, 0, 0) == couleur_hsv(255, 0, 0)


def test_hsl_color():
    assert _en.hsl_color(255, 0, 0) == couleur_hsl(255, 0, 0)


def test_rgba_color():
    assert _en.rgb_color(0, 0, 0, 0.0) == couleur_rgb(0, 0, 0, 0.0)


def test_color_names():
    assert _en.red == rouge
    assert _en.green == vert
    assert _en.blue == bleu
    assert _en.magenta == magenta
    assert _en.cyan == cyan
    assert _en.yellow == jaune
    assert _en.black == noir
    assert _en.white == blanc


def test_transparent_color_name():
    assert _en.transparent == transparent


def test_color_localized_repr():
    assert_repr(rouge, "fr")
    assert "rouge" in repr(rouge)
