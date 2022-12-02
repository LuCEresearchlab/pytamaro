from pytamaro.point_names import *
from pytamaro.point import point


def test_exported_points():
    # Check red, green and blue colors
    assert center == point(0.0, 0.0)
    assert top_left == point(-1.0, 1.0)
    assert top_center == point(0.0, 1.0)
    assert top_right == point(1.0, 1.0)
    assert center_left == point(-1.0, 0.0)
    assert center_right == point(1.0, 0.0)
    assert bottom_left == point(-1.0, -1.0)
    assert bottom_right == point(1.0, -1.0)
