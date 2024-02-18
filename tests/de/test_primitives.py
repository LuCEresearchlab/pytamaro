from pytamaro.color_names import red
from pytamaro.de.primitives import (dreieck, ellipse, kreis_sektor,
                                    leere_grafik, rechteck, text)
from pytamaro.primitives import circular_sector
from pytamaro.primitives import ellipse as ellipse_en
from pytamaro.primitives import empty_graphic, rectangle
from pytamaro.primitives import text as text_en
from pytamaro.primitives import triangle
from tests.testing_utils import HEIGHT, RADIUS, WIDTH, assert_repr


def test_rectangle():
    assert rectangle(WIDTH, HEIGHT, red) == rechteck(WIDTH, HEIGHT, red)


def test_empty_graphic():
    assert empty_graphic() == leere_grafik()


def test_ellipse():
    assert ellipse_en(WIDTH, HEIGHT, red) == ellipse(WIDTH, HEIGHT, red)


def test_text():
    assert text_en("hello", "", 12, red) == text("hello", "", 12, red)


def test_circular_sector():
    assert circular_sector(
        RADIUS, 360, red) == kreis_sektor(RADIUS, 360, red)


def test_equilateral_triangle():
    assert triangle(WIDTH, WIDTH, 60, red) == dreieck(WIDTH, WIDTH, 60, red)


def test_primitive_localized_repr():
    r = rectangle(WIDTH, HEIGHT, red)
    assert_repr(r, "de")
    assert "rechteck" in repr(r)
