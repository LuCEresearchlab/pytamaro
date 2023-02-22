from pytamaro.de.point_names import *


def test_point_names():
    assert top_left == oben_links
    assert top_center == oben_mitte
    assert top_right == oben_rechts
    assert center_left == mitte_links
    assert center == mitte
    assert center_right == mitte_rechts
    assert bottom_left == unten_links
    assert bottom_center == unten_mitte
    assert bottom_right == unten_rechts
