# pylint:disable=duplicate-code
"""
Fonctions pour créer des graphiques primitifs (formes et texte).
À moins d'être spécifié autrement, le point d'ancrage initial est le centre du
cadre de délimitation (bounding box) du graphique.
"""

from __future__ import annotations

from pytamaro.fr.color import Couleur
from pytamaro.fr.graphic import Graphique
from pytamaro.primitives import circular_sector
from pytamaro.primitives import ellipse as en_ellipse
from pytamaro.primitives import empty_graphic
from pytamaro.primitives import rectangle as en_rectangle
from pytamaro.primitives import text
from pytamaro.primitives import triangle as en_triangle


def rectangle(largeur: float, hauteur: float, couleur: Couleur) -> Graphique:
    """
    Créé un rectangle de dimensions indiquées et rempli avec la couleur donnée.

    :param largeur: largeur du rectangle
    :param hauteur: hauteur du rectangle
    :param couleur: couleur qui remplira le rectangle
    :returns: un graphique avec le rectangle spécifié
    """
    return en_rectangle(largeur, hauteur, couleur)


def graphique_vide() -> Graphique:
    """
    Créé un graphique vide.
    Quand un graphique vide est composé avec n'importe quel autre graphique, il
    se comporte comme l'élément neutre: le résultat est toujours égal à l'autre
    graphique.

    :returns: un graphique vide (largeur et hauteur 0)
    """
    return empty_graphic()


def ellipse(largeur: float, hauteur: float, couleur: Couleur) -> Graphique:
    """
    Créé une ellipse avec les dimensions indiquées et rempli avec la couleur
    donnée.

    Lorsque la largeur et la hauteur coïncident, l'ellipse devient un cercle
    dont le diamètre est égal à la taille indiquée.

    :param largeur: largeur de l'ellipse
    :param hauteur: hauteur de l'ellipse
    :param couleur: couleur à utiliser pour remplir l'ellipse
    :returns: un graphique avec l'ellipse spécifiée
    """
    return en_ellipse(largeur, hauteur, couleur)


def secteur_circulaire(rayon: float, angle: float, couleur: Couleur) -> Graphique:
    """
    Crée un secteur circulaire appartenant à un cercle du rayon indiqué, rempli
    d'une couleur.

    Un secteur circulaire est une portion de cercle comprise entre deux rayons
    et un arc.
    Si l'on considère le cercle comme une horloge, le premier rayon "pointe"
    dans la direction de 3 heures. L'`angle` détermine la position du deuxième
    rayon, calculée à partir de la position du premier rayon dans le sens
    inverse des aiguilles d'une montre. Un angle de 360 degrés correspond à un
    cercle complet.

    Le point d'ancrage se trouve au centre du cercle à partir duquel le
    secteur circulaire est pris.

    :param rayon: rayon du cercle duquel est pris le secteur circulaire
    :param angle: angle au centre, en degrés
    :param couleur: couleur à utiliser pour remplir le secteur circulaire
    :returns: un graphique avec le secteur circulaire spécifié
    """
    return circular_sector(rayon, angle, couleur)


def triangle(cote1: float, cote2: float, angle: float, couleur: Couleur) -> Graphique:
    """
    Crée un triangle en spécifiant deux côtés et l'angle qui les sépare, remplis
    d'une couleur.
    Le premier côté s'étend horizontalement vers la droite. L'angle spécifie la
    rotation du deuxième côté, dans le sens inverse des aiguilles d'une montre,
    par rapport au premier.

    Pour tous les triangles, à l'exception des triangles obtus, le point
    inférieur gauche du graphique résultant coïncide avec le sommet du triangle
    dont l'angle a été spécifié.

    Le point d'ancrage est le centroïde du triangle.

    :param cote1: longueur du premier côté (horizontal) du triangle
    :param cote2: longueur du second côté du triangle
    :param angle: angle compris entre les deux côté, en degrés
    :param couleur: couleur à utiliser pour remplir le secteur circulaire
    :returns: un graphique avec le triangle spécifié
    """
    return en_triangle(cote1, cote2, angle, couleur)


def texte(contenu: str, police: str, points: float, couleur: Couleur) -> Graphique:
    """
    Crée un graphique avec le texte rendu à l'aide de la police, de la taille et
    de la couleur spécifiées.

    Lorsque la police True-Type indiquée n'est pas disponible dans le système,
    une police très basique toujours disponible est utilisée à la place. Le
    graphique qui en résulte a la taille minimale nécessaire pour contenir
    l'ensemble du texte.

    La point d'ancrage est alignée horizontalement sur la gauche et
    verticalement sur la ligne de base du texte.

    :param contenu: le texte à présenter
    :param police: le nom de la police (par exemple, "arial" sous Windows, "Arial"
           sous macOS)
    :param points: la taille en points typographiques (par exemple, 16)
    :param couleur: la couleur à utiliser pour le rendu du texte
    :returns: le texte spécifié sous forme de graphique
    """
    return text(contenu, police, points, couleur)
