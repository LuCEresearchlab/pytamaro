import pytamaro as _pytamaro
from pytamaro.fr.primitives import (ellipse, rectangle, triangle,
                                    graphique_vide, secteur_circulaire, texte)
from pytamaro.fr.color_names import rouge
from tests.testing_utils import HEIGHT, RADIUS, WIDTH


def test_rectangle():
    assert _pytamaro.rectangle(WIDTH, HEIGHT, _pytamaro.red) == rectangle(WIDTH, HEIGHT, rouge)


def test_empty_graphic():
    assert _pytamaro.empty_graphic() == graphique_vide()


def test_ellipse():
    assert _pytamaro.ellipse(WIDTH, HEIGHT, _pytamaro.red) == ellipse(WIDTH, HEIGHT, rouge)


def test_text():
    assert _pytamaro.text("hello", "", 12, _pytamaro.red) == texte("hello", "", 12, rouge)


def test_circular_sector():
    assert _pytamaro.circular_sector(
        RADIUS, 360, _pytamaro.red) == secteur_circulaire(RADIUS, 360, rouge)


def test_equilateral_triangle():
    assert _pytamaro.triangle(WIDTH, WIDTH, 60, _pytamaro.red) == triangle(WIDTH, WIDTH, 60, rouge)
