import pytamaro as _pytamaro
from pytamaro.de.point_names import (mitte, mitte_links, mitte_rechts,
                                     oben_links, oben_mitte, oben_rechts,
                                     unten_links, unten_mitte, unten_rechts)
from tests.testing_utils import assert_repr


def test_point_names():
    assert _pytamaro.top_left == oben_links
    assert _pytamaro.top_center == oben_mitte
    assert _pytamaro.top_right == oben_rechts
    assert _pytamaro.center_left == mitte_links
    assert _pytamaro.center == mitte
    assert _pytamaro.center_right == mitte_rechts
    assert _pytamaro.bottom_left == unten_links
    assert _pytamaro.bottom_center == unten_mitte
    assert _pytamaro.bottom_right == unten_rechts


def test_point_localized_repr():
    assert_repr(oben_links, "de")
    assert "oben" in repr(oben_links)
