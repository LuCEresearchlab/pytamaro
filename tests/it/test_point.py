from pytamaro.it.point_names import *


def test_point_names():
    assert top_left == alto_sinistra
    assert top_center == alto_centro
    assert top_right == alto_destra
    assert center_left == centro_sinistra
    assert center == centro
    assert center_right == centro_destra
    assert bottom_left == basso_sinistra
    assert bottom_center == basso_centro
    assert bottom_right == basso_destra
