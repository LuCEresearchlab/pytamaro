import pytamaro as _pytamaro
from pytamaro.it.color import colore_hsl, colore_hsv, colore_rgb
from pytamaro.it.color_names import (bianco, blu, ciano, giallo, magenta, nero,
                                     rosso, trasparente, verde)
from tests.testing_utils import assert_repr


def test_rgb_color():
    assert _pytamaro.rgb_color(255, 0, 0) == colore_rgb(255, 0, 0)


def test_hsv_color():
    assert _pytamaro.hsv_color(255, 0, 0) == colore_hsv(255, 0, 0)


def test_hsl_color():
    assert _pytamaro.hsl_color(255, 0, 0) == colore_hsl(255, 0, 0)


def test_rgba_color():
    assert _pytamaro.rgb_color(0, 0, 0, 0.0) == colore_rgb(0, 0, 0, 0.0)


def test_color_names():
    assert _pytamaro.red == rosso
    assert _pytamaro.green == verde
    assert _pytamaro.blue == blu
    assert _pytamaro.magenta == magenta
    assert _pytamaro.cyan == ciano
    assert _pytamaro.yellow == giallo
    assert _pytamaro.black == nero
    assert _pytamaro.white == bianco


def test_transparent_color_name():
    assert _pytamaro.transparent == trasparente


def test_color_localized_repr():
    assert_repr(rosso, "it")
    assert "rosso" in repr(rosso)
