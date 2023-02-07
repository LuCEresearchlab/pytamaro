from pytamaro.point_names import *
from pytamaro.point import Point


def test_exported_points():
    assert center == Point(0.0, 0.0)
    assert top_left == Point(-1.0, 1.0)
    assert top_center == Point(0.0, 1.0)
    assert top_right == Point(1.0, 1.0)
    assert center_left == Point(-1.0, 0.0)
    assert center_right == Point(1.0, 0.0)
    assert bottom_left == Point(-1.0, -1.0)
    assert bottom_right == Point(1.0, -1.0)


def test_add():
    assert center.translate(i_hat + j_hat) == top_right
