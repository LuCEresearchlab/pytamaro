import pytamaro as _pytamaro
from pytamaro.it.primitives import (ellisse, grafica_vuota, rettangolo,
                                    settore_circolare, testo, triangolo)
from pytamaro.it.color_names import rosso
from tests.testing_utils import HEIGHT, RADIUS, WIDTH, assert_repr


def test_rectangle():
    assert _pytamaro.rectangle(WIDTH, HEIGHT, _pytamaro.red) == rettangolo(WIDTH, HEIGHT, rosso)


def test_empty_graphic():
    assert _pytamaro.empty_graphic() == grafica_vuota()


def test_ellipse():
    assert _pytamaro.ellipse(WIDTH, HEIGHT, _pytamaro.red) == ellisse(WIDTH, HEIGHT, rosso)


def test_text():
    assert _pytamaro.text("hello", "", 12, _pytamaro.red) == testo("hello", "", 12, rosso)


def test_circular_sector():
    assert _pytamaro.circular_sector(
        RADIUS, 360, _pytamaro.red) == settore_circolare(RADIUS, 360, rosso)


def test_equilateral_triangle():
    assert _pytamaro.triangle(WIDTH, WIDTH, 60, _pytamaro.red) == triangolo(WIDTH, WIDTH, 60, rosso)


def test_primitive_localized_repr():
    r = _pytamaro.rectangle(WIDTH, HEIGHT, _pytamaro.red)
    assert_repr(r, "it")
    assert "rettangolo" in repr(r)
