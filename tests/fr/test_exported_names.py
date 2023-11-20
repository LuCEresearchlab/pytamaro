from typing import List

from pytamaro.fr import *


def _assert_names(names: List[str]):
    for name in names:
        assert name in globals()


def test_operations_primitives_io():
    _assert_names(["compose", "graphique_vide", "montre_graphique"])


def test_import_types():
    _assert_names(["Graphique", "Couleur"])


def test_colors():
    _assert_names(["couleur_rgb", "couleur_hsv", "couleur_hsl"])
    _assert_names(["rouge", "transparent"])


def test_points():
    _assert_names(["haut_gauche", "haut_centre", "haut_droite", "centre_gauche",
                   "centre", "centre_droite", "bas_gauche", "bas_centre",
                   "bas_droite"])
