from pytamaro.color_names import red
from pytamaro.fr.primitives import ellipse as fr_ellipse
from pytamaro.fr.primitives import graphique_vide
from pytamaro.fr.primitives import rectangle as fr_rectangle
from pytamaro.fr.primitives import secteur_circulaire, texte
from pytamaro.fr.primitives import triangle as fr_triangle
from pytamaro.primitives import circular_sector
from pytamaro.primitives import ellipse as en_ellipse
from pytamaro.primitives import empty_graphic
from pytamaro.primitives import rectangle as en_rectangle
from pytamaro.primitives import text
from pytamaro.primitives import triangle as en_triangle
from tests.testing_utils import HEIGHT, RADIUS, WIDTH


def test_rectangle():
    assert en_rectangle(WIDTH, HEIGHT, red) == fr_rectangle(WIDTH, HEIGHT, red)


def test_empty_graphic():
    assert empty_graphic() == graphique_vide()


def test_ellipse():
    assert en_ellipse(WIDTH, HEIGHT, red) == fr_ellipse(WIDTH, HEIGHT, red)


def test_text():
    assert text("hello", "", 12, red) == texte("hello", "", 12, red)


def test_circular_sector():
    assert circular_sector(
        RADIUS, 360, red) == secteur_circulaire(RADIUS, 360, red)


def test_equilateral_triangle():
    assert en_triangle(WIDTH, WIDTH, 60, red) == fr_triangle(WIDTH, WIDTH, 60, red)
