"""
Fonctions pour visualiser ou sauvegarder des graphiques.
"""

from __future__ import annotations

from pytamaro.io import save_animation, save_graphic, show_animation, show_graphic
from pytamaro.fr.graphic import Graphique


def montre_graphique(graphique: Graphique, debug: bool = False):
    """
    Montre un graphique. Les graphiques n'ayant pas de surface ne peuvent pas
    être montrés.

    Quand `debug` est `True`, la visualisation est ornée d'informations utiles
    pour le débogage:
    une bordure rouge autour du cadre de délimitation et une croix jaunâtre
    autour du point d'ancrage.

    :param graphique: le graphique à montrer
    :param debug: (optionnel) peut être assigné à `True` pour superposer les
           informations de débogage
    """
    show_graphic(graphique, debug)


def sauvegarde_graphique(nom_fichier: str, graphique: Graphique, debug: bool = False):
    """
    Sauvegarde un graphique dans un fichier.
    Deux formats de fichiers sont supportés: PNG (graphiques tramés) et SVG
    (graphiques vectoriels). L'extension du fichier (".png" ou ".svg") détermine
    le format.


    Les graphiques sans surface ne peuvent pas être sauvegardés au format
    PNG.

    Quand `debug` est `True`, la visualisation est ornée d'informations utiles
    pour le débogage:
    une bordure rouge autour du cadre de délimitation et une croix jaunâtre
    autour du point d'ancrage.

    :param nom_fichier: le nom du fichier à créer (avec l'extension)
    :param graphique: le graphique à sauvegarder
    :param debug: (optionnel) peut être assigné à `True` pour superposer les
           informations de débogage
    """
    save_graphic(nom_fichier, graphique, debug)


def sauvegarde_animation(
    nom_fichier: str, graphiques: list[Graphique], duree: int = 40, en_boucle: bool = True
):
    """
    Sauvegarde une séquence de graphiques en tant qu'animation (GIF).

    Les graphiques sont reproduits de manière séquentielle (normalement à 25
    images par secondes) en boucle (à moins que ça ne soit indiqué autrement).


    :param nom_fichier: le nom du fichier à créer (contenant l'extension ".gif")
    :param graphiques: la liste des graphiques à sauvegarder en tant
           qu'animation.
    :param duree: durée en millisecondes entre chaque image (par défaut est
           égale à 40 millisecondes, ce qui amène à avoir 25 images par secondes)
    :param en_boucle: si le GIF doit tourner en boucle indéfiniment (par défaut
           est `True`)
    """
    save_animation(nom_fichier, graphiques, duree, en_boucle)


def montre_animation(graphiques: list[Graphique], duree: int = 40, en_boucle: bool = True):
    """
    Montre une séquence de graphiques en tant qu'animation (GIF).

    Les graphiques sont reproduits de manière séquentielle (normalement à 25
    images par secondes) en boucle (à moins que ça ne soit indiqué autrement).


    :param graphiques: la liste des graphiques à sauvegarder en tant
           qu'animation.
    :param duree: durée en millisecondes entre chaque image (par défaut est
           égale à 40 millisecondes, ce qui amène à avoir 25 images par secondes)
    :param en_boucle: si le GIF doit tourner en boucle indéfiniment (par défaut
           est `True`)
    """
    show_animation(graphiques, duree, en_boucle)
