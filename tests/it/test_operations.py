from pytamaro.color_names import blue, red
from pytamaro.it.operations import (accanto, altezza_grafica, componi, fissa,
                                    larghezza_grafica, ruota, sopra,
                                    sovrapponi)
from pytamaro.operations import (above, beside, compose, graphic_height,
                                 graphic_width, overlay, pin, rotate)
from pytamaro.primitives import rectangle
from tests.testing_utils import HEIGHT, WIDTH

g = rectangle(WIDTH, HEIGHT, red)


def test_width():
    assert graphic_width(g) == larghezza_grafica(g)


def test_height():
    assert graphic_height(g) == altezza_grafica(g)


def test_rotate():
    assert rotate(45, g) == ruota(45, g)


def test_beside():
    assert beside(g, g) == accanto(g, g)


def test_above():
    assert above(g, g) == sopra(g, g)


def test_overlay():
    assert overlay(g, g) == sovrapponi(g, g)


def test_compose():
    assert compose(g, g) == componi(g, g)


def test_fissa():
    assert pin("left", "top", g) == fissa("sinistra", "alto", g)
    assert pin("middle", "middle", g) == fissa("centro", "centro", g)
    assert pin("right", "bottom", g) == fissa("destra", "basso", g)
