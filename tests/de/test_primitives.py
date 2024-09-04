import pytamaro as _pytamaro

from pytamaro.de.primitives import (dreieck, ellipse, kreis_sektor,
                                    leere_grafik, rechteck, text)
from pytamaro.de.color_names import rot
from tests.testing_utils import HEIGHT, RADIUS, WIDTH, assert_repr


def test_rectangle():
    assert _pytamaro.rectangle(WIDTH, HEIGHT, _pytamaro.red) == rechteck(WIDTH, HEIGHT, rot)


def test_empty_graphic():
    assert _pytamaro.empty_graphic() == leere_grafik()


def test_ellipse():
    assert _pytamaro.ellipse(WIDTH, HEIGHT, _pytamaro.red) == ellipse(WIDTH, HEIGHT, rot)


def test_text():
    assert _pytamaro.text("hello", "", 12, _pytamaro.red) == text("hello", "", 12, rot)


def test_circular_sector():
    assert _pytamaro.circular_sector(
        RADIUS, 360, _pytamaro.red) == kreis_sektor(RADIUS, 360, rot)


def test_equilateral_triangle():
    assert _pytamaro.triangle(WIDTH, WIDTH, 60, _pytamaro.red) == dreieck(WIDTH, WIDTH, 60, rot)


def test_primitive_localized_repr():
    r = _pytamaro.rectangle(WIDTH, HEIGHT, _pytamaro.red)
    assert_repr(r, "de")
    assert "rechteck" in repr(r)
