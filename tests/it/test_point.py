import pytamaro as _pytamaro
from pytamaro.it.point_names import (alto_centro, alto_destra, alto_sinistra,
                                     basso_centro, basso_destra,
                                     basso_sinistra, centro, centro_destra,
                                     centro_sinistra)
from tests.testing_utils import assert_repr


def test_point_names():
    assert _pytamaro.top_left == alto_sinistra
    assert _pytamaro.top_center == alto_centro
    assert _pytamaro.top_right == alto_destra
    assert _pytamaro.center_left == centro_sinistra
    assert _pytamaro.center == centro
    assert _pytamaro.center_right == centro_destra
    assert _pytamaro.bottom_left == basso_sinistra
    assert _pytamaro.bottom_center == basso_centro
    assert _pytamaro.bottom_right == basso_destra


def test_point_localized_repr():
    assert_repr(alto_sinistra, "it")
    assert "alto" in repr(alto_sinistra)
