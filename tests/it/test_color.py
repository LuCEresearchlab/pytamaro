from tests.testing_utils import assert_repr

from pytamaro.it.color_names import (
    rosso, verde, blu,
    magenta, ciano, giallo,
    nero, bianco, trasparente,
)
from pytamaro.it.color import (
    colore_rgb, colore_hsv, colore_hsl,
)
import pytamaro.color_names as _color_names_en
import pytamaro.color_functions as _color_functions_en


def test_rgb_color():
    assert _color_functions_en.rgb_color(255, 0, 0) == colore_rgb(255, 0, 0)


def test_hsv_color():
    assert _color_functions_en.hsv_color(255, 0, 0) == colore_hsv(255, 0, 0)


def test_hsl_color():
    assert _color_functions_en.hsl_color(255, 0, 0) == colore_hsl(255, 0, 0)


def test_rgba_color():
    assert _color_functions_en.rgb_color(0, 0, 0, 0.0) == colore_rgb(0, 0, 0, 0.0)


def test_color_names():
    assert _color_names_en.red == rosso
    assert _color_names_en.green == verde
    assert _color_names_en.blue == blu
    assert _color_names_en.magenta == magenta
    assert _color_names_en.cyan == ciano
    assert _color_names_en.yellow == giallo
    assert _color_names_en.black == nero
    assert _color_names_en.white == bianco


def test_transparent_color_name():
    assert _color_names_en.transparent == trasparente


def test_color_localized_repr():
    assert_repr(rosso, "it")
    assert "rosso" in repr(rosso)
