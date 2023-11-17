from pytamaro.fr.point_names import *


def test_point_names():
    assert top_left == haut_gauche
    assert top_center == haut_centre
    assert top_right == haut_droite
    assert center_left == centre_gauche
    assert center == centre
    assert center_right == centre_droite
    assert bottom_left == bas_gauche
    assert bottom_center == bas_centre
    assert bottom_right == bas_droite
