import pytamaro as _pytamaro
from pytamaro.fr.point_names import (bas_centre, bas_droite, bas_gauche,
                                     centre, centre_droite, centre_gauche,
                                     haut_centre, haut_droite, haut_gauche)


def test_point_names():
    assert _pytamaro.top_left == haut_gauche
    assert _pytamaro.top_center == haut_centre
    assert _pytamaro.top_right == haut_droite
    assert _pytamaro.center_left == centre_gauche
    assert _pytamaro.center == centre
    assert _pytamaro.center_right == centre_droite
    assert _pytamaro.bottom_left == bas_gauche
    assert _pytamaro.bottom_center == bas_centre
    assert _pytamaro.bottom_right == bas_droite
