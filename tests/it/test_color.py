from tests.testing_utils import assert_repr

from pytamaro.it.color_names import (
    rosso, verde, blu,
    magenta, ciano, giallo,
    nero, bianco, trasparente,
)
from pytamaro.it.color import (
    colore_rgb, colore_hsv, colore_hsl,
)
import pytamaro as _en


def test_rgb_color():
    assert _en.rgb_color(255, 0, 0) == colore_rgb(255, 0, 0)


def test_hsv_color():
    assert _en.hsv_color(255, 0, 0) == colore_hsv(255, 0, 0)


def test_hsl_color():
    assert _en.hsl_color(255, 0, 0) == colore_hsl(255, 0, 0)


def test_rgba_color():
    assert _en.rgb_color(0, 0, 0, 0.0) == colore_rgb(0, 0, 0, 0.0)


def test_color_names():
    assert _en.red == rosso
    assert _en.green == verde
    assert _en.blue == blu
    assert _en.magenta == magenta
    assert _en.cyan == ciano
    assert _en.yellow == giallo
    assert _en.black == nero
    assert _en.white == bianco


def test_transparent_color_name():
    assert _en.transparent == trasparente


def test_color_localized_repr():
    assert_repr(rosso, "it")
    assert "rosso" in repr(rosso)
