from pytamaro.color_names import red
from pytamaro.it.primitives import (ellisse, grafica_vuota, rettangolo,
                                    settore_circolare, testo, triangolo)
from pytamaro.primitives import (circular_sector, ellipse, empty_graphic,
                                 rectangle, text, triangle)
from tests.testing_utils import HEIGHT, RADIUS, WIDTH


def test_rectangle():
    assert rectangle(WIDTH, HEIGHT, red) == rettangolo(WIDTH, HEIGHT, red)


def test_empty_graphic():
    assert empty_graphic() == grafica_vuota()


def test_ellipse():
    assert ellipse(WIDTH, HEIGHT, red) == ellisse(WIDTH, HEIGHT, red)


def test_text():
    assert text("hello", "", 12, red) == testo("hello", "", 12, red)


def test_circular_sector():
    assert circular_sector(
        RADIUS, 360, red) == settore_circolare(RADIUS, 360, red)


def test_equilateral_triangle():
    assert triangle(WIDTH, WIDTH, 60, red) == triangolo(WIDTH, WIDTH, 60, red)
