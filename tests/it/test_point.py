from tests.testing_utils import assert_repr

from pytamaro.it.point_names import (
    alto_sinistra, alto_centro, alto_destra,
    centro_sinistra, centro, centro_destra,
    basso_sinistra, basso_centro, basso_destra,
)
import pytamaro as _en


def test_point_names():
    assert _en.top_left == alto_sinistra
    assert _en.top_center == alto_centro
    assert _en.top_right == alto_destra
    assert _en.center_left == centro_sinistra
    assert _en.center == centro
    assert _en.center_right == centro_destra
    assert _en.bottom_left == basso_sinistra
    assert _en.bottom_center == basso_centro
    assert _en.bottom_right == basso_destra


def test_point_localized_repr():
    assert_repr(alto_sinistra, "it")
    assert "alto" in repr(alto_sinistra)
