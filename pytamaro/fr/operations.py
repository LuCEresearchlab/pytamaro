"""
Fonctions pour faire des opérations sur des graphiques (principalement pour les combiner).
"""

from __future__ import annotations

from pytamaro import operations
from pytamaro.fr.graphic import Graphique
from pytamaro.fr.point import Point
from pytamaro.operations import (above, beside, graphic_height, graphic_width,
                                 overlay, pin, rotate)


def largeur_graphique(graphique: Graphique) -> int:
    """
    Retourne la largeur du graphique.

    :param graphique: graphique duquel calculer la largeur
    :returns: la largeur du graphique
    """
    return graphic_width(graphique)


def hauteur_graphique(graphique: Graphique) -> int:
    """
    Retourne la hauteur du graphique.

    :param graphique: graphique duquel calculer la hauteur
    :returns: la hauteur du graphique
    """
    return graphic_height(graphique)


def compose(graphique_premier_plan: Graphique, graphique_arriere_plan: Graphique) \
        -> Graphique:
    """
    Crée un nouveau graphique en composant les deux graphiques fournis.
    Le premier graphique est maintenu au premier plan, le second en arrière plan.
    Les graphiques sont alignés en superposant les points d'ancrage.

    Le point d'ancrage du graphique résultant est celui utilisé pour la composition.

    :param graphique_premier_plan: le graphique au premier plan
    :param graphique_premier_plan: le graphique en arrière plan
    :returns: le graphique qui résulte de la composition
    """
    return operations.compose(graphique_premier_plan, graphique_arriere_plan)


def ancre(point: Point, graphique: Graphique) -> Graphique:
    """
    Créé un nouveau graphique qui correspond au graphique fourni avec un nouveau point d'ancrage.

    Chaque graphique est compris dans un cadre de délimitation.
    Il y a 9 points d'ancrages particuliers, qui correspondent aux quatre coins du cadre
    (rectangle), le milieu de chaque côté ainsi que le centre du cadre.
    Les points peuvent être désignés avec les noms suivants: `haut_gauche`, `haut_droite`,
    `bas_gauche`, `bas_droite`, `haut_centre`, `centre_droite`, `bas_centre`, `centre_gauche` et
    `centre`.

    :param point: le point indiquant le nouveau point d'ancrage
    :param graphique: le graphique originel
    :returns: un nouveau graphique avec le nouveau point d'ancrage
    """
    return pin(point, graphique)


def superpose(graphique_premier_plan: Graphique, graphique_arriere_plan: Graphique) \
        -> Graphique:
    """
    Créé un nouveau graphique en superposant les deux graphiques fournis, en gardant le premier au
    premier plan et en mettant le second en arrière plan.
    Les graphiques sont superposés par rapport à leur centre.

    Le point d'ancrage du nouveau graphique est en son centre.

    :param graphique_premier_plan: le graphique au premier plan
    :param graphique_arriere_plan: le graphique en arrière plan
    :returns: le graphique résultant de la superposition des deux graphiques fournis
    """
    return overlay(graphique_premier_plan, graphique_arriere_plan)


def cote_a_cote(graphique_gauche: Graphique, graphique_droite: Graphique) -> Graphique:
    """
    Créé un graphique en plaçant les deux graphiques fournis côte à côte.
    Les deux graphiques sont centrés verticalement.

    Le point d'ancrage du nouveau graphique est en son centre.

    :param graphique_gauche: le graphique à placer à gauche
    :param graphique_droite: le graphique à placer à droite
    :returns: le graphique résultant après avoir placé les deux graphiques l'un à côté de l'autre
    """
    return beside(graphique_gauche, graphique_droite)


def au_dessus(graphique_haut: Graphique, graphique_bas: Graphique) -> Graphique:
    """
    Créé un graphique en plaçant les deux graphiques fournis l'un au-dessus de l'autre.
    Les deux graphiques sont centrés horizontalement.

    Le point d'ancrage du nouveau graphique est en son centre.

    :param graphique_haut: le graphique à placer au dessus
    :param graphique_bas: le graphique à placer en dessous
    :returns: le graphique résultant après avoir placé les deux graphiques l'un au-dessus de l'autre
    """
    return above(graphique_haut, graphique_bas)


def pivote(angle: float, graphique: Graphique) -> Graphique:
    """
    Crée un nouveau graphique en pivotant dans le sens inverse des aiguilles d'une montre le
    graphique fourni autour de son point d'ancrage selon l'angle donné. Un angle négatif
    correspond à une rotation dans le sens des aiguilles d'une montre.

    :param angle: angle dans le sens inverse des aiguilles d'une montre, en degrés
    :param graphique: le graphique à pivoter
    :returns: un nouveau graphique pivoté
    """
    return rotate(angle, graphique)
