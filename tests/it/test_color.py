from pytamaro.color import *
from pytamaro.color_names import *
from pytamaro.it.color import *
from pytamaro.it.color_names import *
from tests.testing_utils import assert_repr


def test_rgb_color():
    assert rgb_color(255, 0, 0) == colore_rgb(255, 0, 0)


def test_hsv_color():
    assert hsv_color(255, 0, 0) == colore_hsv(255, 0, 0)


def test_hsl_color():
    assert hsl_color(255, 0, 0) == colore_hsl(255, 0, 0)


def test_rgba_color():
    assert rgb_color(0, 0, 0, 0.0) == colore_rgb(0, 0, 0, 0.0)


def test_color_names():
    assert red == rosso
    assert green == verde
    assert blue == blu
    assert magenta == magenta
    assert cyan == ciano
    assert yellow == giallo
    assert black == nero
    assert white == bianco


def test_transparent_color_name():
    assert transparent == trasparente


def test_color_localized_repr():
    assert_repr(rosso, "it")
    assert "rosso" in repr(rosso)
