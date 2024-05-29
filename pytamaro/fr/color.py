"""
Type `Couleur`, ainsi des fonctions pour produire des couleurs et constantes représentants des
couleurs particulières.
"""

from __future__ import annotations

from pytamaro.color import Color
from pytamaro.color_functions import rgb_color, hsl_color, hsv_color

Couleur = Color
"""
Représente une couleur.
Une couleur a aussi un taux d'opacité,
de complètement transparent (comme la couleur `transparent`)
à complètement opaque (comme la couleur `rouge`).
"""


def couleur_rgb(rouge: int, vert: int, bleu: int, opacite: float = 1.0) -> Couleur:
    """
    Retourne une couleur avec les composantes indiquant le rouge (R), vert (G) et bleu (B)
    et un certain taux d'opacité (alpha, A).

    .. figure:: https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/RGBCube_a.svg/524px-RGBCube_a.svg.png
       :height: 120px
       :align: center

       `Cube RGB (SharkD via Wikimedia Commons) <https://commons.wikimedia.org/wiki/File:RGBCube_a.svg>`_

    :param rouge: composante rouge [0-255]
    :param vert: composante verte [0-255]
    :param bleu: composante bleue [0-255]
    :param opacite: opacité (alpha) de la couleur, où 0 est complètement transparent
            et 1 complètement opaque.
            Par défaut, toutes les couleurs sont complètement opaques.
    :returns: une couleur avec les composantes RGBA données
    """
    return rgb_color(rouge, vert, bleu, opacite)


def couleur_hsv(teinte: float, saturation: float, valeur: float, opacite: float = 1.0) -> Couleur:
    """
    Retourne une couleur avec la teinte (H), saturation (S) et valeur (V) données,
    ainsi que le taux d'opacité (alpha, A).

    .. figure:: https://upload.wikimedia.org/wikipedia/commons/4/4e/HSV_color_solid_cylinder.png
       :height: 120px
       :align: center

       `Cylindre HSV (SharkD via Wikimedia Commons) <https://commons.wikimedia.org/wiki/File:HSV_color_solid_cylinder.png>`_

    :param teinte: teinte de la couleur [0-360]
    :param saturation: saturation de la couleur [0-1]
    :param valeur: quantité de lumière appliquée [0-1]
           Les couleurs complètement saturées ont une quantité de lumière de 1.
    :param opacite: opacité (alpha) de la couleur, où 0 est complètement transparent
            et 1 complètement opaque.
            Par défaut, toutes les couleurs sont complètement opaques.
    :returns: une couleur avec le composantes HSVA données
    """
    return hsv_color(teinte, saturation, valeur, opacite)


def couleur_hsl(teinte: float, saturation: float, luminosite: float, opacite: float = 1.0
                ) -> Couleur:
    """
    Retourne une couleur avec la teinte (H), saturation (S) et luminosité (V) données,
    ainsi que le taux d'opacité (alpha, A).

    .. figure:: https://upload.wikimedia.org/wikipedia/commons/3/35/HSL_color_solid_cylinder.png
       :height: 120px
       :align: center

       `Cylindre HSL: SharkD via Wikimedia Commons <https://commons.wikimedia.org/wiki/File:HSL_color_solid_cylinder.png>`_

    :param teinte: teinte de la couleur [0-360]
    :param saturation: saturation de la couleur [0-1]
    :param luminosite: quantité de blanc ou noire appliquée [0-1].
           Les couleurs complètement saturées ont un valeur de luminosité de 1/2.
    :param opacite: opacité (alpha) de la couleur, où 0 est complètement transparent
            et 1 complètement opaque.
            Par défaut, toutes les couleurs sont complètement opaques.
    :returns: une couleur avec les composantes HSLA données.
    """
    return hsl_color(teinte, saturation, luminosite, opacite)
