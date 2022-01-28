from typing import List

from pytamaro.it import *


def _assert_names(names: List[str]):
    for name in names:
        assert name in globals()


def test_operations_primitives_io():
    _assert_names(["componi", "grafica_vuota", "visualizza_grafica"])


def test_import_types():
    _assert_names(["Grafica", "Colore"])


def test_colors():
    _assert_names(["colore_rgb", "colore_rgba"])
    _assert_names(["rosso", "trasparente"])
