from typing import List

from pytamaro import *


def _assert_names(names: List[str]):
    for name in names:
        assert name in globals()


def test_operations_primitives_io():
    _assert_names(["compose", "empty_graphic", "show_graphic"])


def test_import_types():
    _assert_names(["Graphic", "Color", "Point"])


def test_colors():
    _assert_names(["rgb_color", "hsv_color", "hsl_color"])
    _assert_names(["red", "transparent"])


def test_points():
    _assert_names(["top_left", "top_center", "top_right", "center_left",
                   "center", "center_right", "bottom_left", "bottom_center", "bottom_right"])
