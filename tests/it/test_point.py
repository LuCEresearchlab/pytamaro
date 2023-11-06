from pytamaro.it.point_names import *
from tests.testing_utils import assert_repr


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


def test_point_localized_repr():
    assert_repr(alto_sinistra, "it")
    assert "alto" in repr(alto_sinistra)
