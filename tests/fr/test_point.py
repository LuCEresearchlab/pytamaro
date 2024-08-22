from pytamaro.fr.point_names import (
    haut_gauche, haut_centre, haut_droite,
    centre_gauche, centre, centre_droite,
    bas_gauche, bas_centre, bas_droite,
)
import pytamaro as _en


def test_point_names():
    assert _en.top_left == haut_gauche
    assert _en.top_center == haut_centre
    assert _en.top_right == haut_droite
    assert _en.center_left == centre_gauche
    assert _en.center == centre
    assert _en.center_right == centre_droite
    assert _en.bottom_left == bas_gauche
    assert _en.bottom_center == bas_centre
    assert _en.bottom_right == bas_droite
