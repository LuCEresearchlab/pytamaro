from pytamaro.color_names import red
from pytamaro.de.primitives import (ellipse, leere_grafik, rechteck,
                                    kreis_sektor, text, dreieck)
from pytamaro.primitives import (circular_sector, ellipse, empty_graphic,
                                 rectangle, text, triangle)
from tests.testing_utils import HEIGHT, RADIUS, WIDTH


def test_rectangle():
    assert rectangle(WIDTH, HEIGHT, red) == rechteck(WIDTH, HEIGHT, red)


def test_empty_graphic():
    assert empty_graphic() == leere_grafik()


def test_ellipse():
    assert ellipse(WIDTH, HEIGHT, red) == ellipse(WIDTH, HEIGHT, red)


def test_text():
    assert text("hello", "", 12, red) == text("hello", "", 12, red)


def test_circular_sector():
    assert circular_sector(
        RADIUS, 360, red) == kreis_sektor(RADIUS, 360, red)


def test_equilateral_triangle():
    assert triangle(WIDTH, WIDTH, 60, red) == dreieck(WIDTH, WIDTH, 60, red)
