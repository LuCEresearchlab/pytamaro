from tests.testing_utils import assert_repr

from pytamaro.de.point_names import (
    oben_links, oben_mitte, oben_rechts,
    mitte_links, mitte, mitte_rechts,
    unten_links, unten_mitte, unten_rechts,
)
import pytamaro.point_names as _point_names_en


def test_point_names():
    assert _point_names_en.top_left == oben_links
    assert _point_names_en.top_center == oben_mitte
    assert _point_names_en.top_right == oben_rechts
    assert _point_names_en.center_left == mitte_links
    assert _point_names_en.center == mitte
    assert _point_names_en.center_right == mitte_rechts
    assert _point_names_en.bottom_left == unten_links
    assert _point_names_en.bottom_center == unten_mitte
    assert _point_names_en.bottom_right == unten_rechts


def test_point_localized_repr():
    assert_repr(oben_links, "de")
    assert "oben" in repr(oben_links)
