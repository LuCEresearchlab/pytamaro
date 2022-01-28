from typing import List

from pytamaro.de import *


def _assert_names(names: List[str]):
    for name in names:
        assert name in globals()


def test_operations_primitives_io():
    _assert_names(["kombiniere", "leere_grafik", "zeige_grafik"])


def test_import_types():
    _assert_names(["Grafik", "Farbe"])


def test_colors():
    _assert_names(["rgb_farbe", "rgba_farbe"])
    _assert_names(["rot", "transparent"])
