"""
`Color` type and functions to produce colors.
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass
class Color:
    """
    Represents a color in the RGBA color space (using integers between 0 and
    255).
    """
    rgba: Tuple[int, int, int, int]

    def __init__(self, red: int, green: int, blue: int, alpha: int):
        self.rgba = (red, green, blue, alpha)

    def as_tuple(self) -> Tuple[int, int, int, int]:
        """
        Returns the current color as an RGBA tuple.

        :meta private:
        :returns: a tuple with four components (0 -- 255) that identifies this
                  color
        """
        return self.rgba


def rgb_color(red: int, green: int, blue: int) -> Color:
    """
    Returns a fully-opaque color with the provided components for red, green
    and blue.

    :param red: red component (0 -- 255)
    :param green: green component (0 -- 255)
    :param blue: blue component (0 -- 255)
    :returns: a color with the provided RGB components
    """
    return rgba_color(red, green, blue, 255)


def rgba_color(red: int, green: int, blue: int, alpha: int) -> Color:
    """
    Returns a color with the provided components for red, green and blue and a
    certain degree of transparency controlled by `alpha`.

    :param red: red component (0 -- 255)
    :param green: green component (0 -- 255)
    :param blue: blue component (0 -- 255)
    :param alpha: alpha (transparency) component where 0 means fully
           transparent and 255 fully opaque
    :returns: a color with the provided RGBA components
    """
    return Color(red, green, blue, alpha)
