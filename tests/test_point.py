from pytamaro.point import Point
from pytamaro.point_names import *
from tests.testing_utils import assert_repr


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


def test_point_repr():
    from pytamaro.point_names import _known_points
    for point in _known_points:
        assert_repr(point, "en")
    assert_repr(Point(42, -42), "en")
