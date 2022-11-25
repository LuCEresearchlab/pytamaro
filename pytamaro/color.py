"""
`Color` type and functions to produce colors.
"""

from dataclasses import dataclass
from typing import Tuple

from skia import Color4f


@dataclass
class Color:
    """
    Represents a color in the RGBA color space (using integers between 0 and
    255).
    """
    color: Color4f

    def __init__(self, red: int, green: int, blue: int, alpha: float):
        self.color = Color4f(red / 255, green / 255, blue / 255, alpha)

    def as_tuple(self) -> Tuple[int, int, int, float]:
        """
        Returns the current color as an RGBA tuple.

        :meta private:
        :returns: a tuple with four components. The first three (0 -- 255) identify the
                  color, the last one (0, 1) identifies the transparency
        """
        return tuple(self.color[i] * 255 for i in range(3)) + (self.color[3], )


def rgb_color(red: int, green: int, blue: int, alpha: float = 1.0) -> Color:
    """
    Returns a color with the provided components for red, green and blue and a
    certain degree of transparency controlled by `alpha`.

    :param red: red component (0 -- 255)
    :param green: green component (0 -- 255)
    :param blue: blue component (0 -- 255)
    :param alpha: alpha (transparency) component where 0 means fully
           transparent and 1 fully opaque. By default, all colors are fully opaque
    :returns: a color with the provided RGBA components
    """
    return Color(red, green, blue, alpha)


def hsv_color(hue: float, saturation: float, value: float, alpha: float = 1.0) -> Color:
    """
    Returns a color with the provided hue, saturation, value and a
    certain degree of transparency controlled by `alpha`.
    The parameters are converted to RGB and used to get the color with rgb_color().

    :param hue: hue of the color (0 - 360)
    :param saturation: saturation of the color (0, 1)
    :param value: the amount of light that is applied (0, 1)
    :param alpha: alpha (transparency) component where 0 means fully
           transparent and 1 fully opaque. By default, all colors are fully opaque
    :returns: a color with the provided HSV components.
    """
    chroma = value * saturation
    side = (hue / 60) % 6
    x = chroma * (1 - abs(side % 2 - 1))
    bottom_color = (chroma, x, 0)
    if 2 > side >= 1:
        bottom_color = (x, chroma, 0)
    if 3 > side >= 2:
        bottom_color = (0, chroma, x)
    if 4 > side >= 3:
        bottom_color = (0, x, chroma)
    if 5 > side >= 4:
        bottom_color = (x, 0, chroma)
    if side >= 5:
        bottom_color = (chroma, 0, x)
    to_add = value - chroma
    color = tuple(int((x + to_add) * 255) for x in bottom_color)
    return rgb_color(*color, alpha)


def hsl_color(hue: float, saturation: float, lightness: float, alpha: float = 1.0) -> Color:
    """
    Returns a color with the provided hue, saturation, lightness  and a
    certain degree of transparency controlled by `alpha`.
    The parameters are converted to RGB and used to get the color with rgb_color().

    :param hue: hue of the color (0 - 360)
    :param saturation: saturation of the color (0, 1)
    :param lightness: the amount of white or black applied (0, 1).
            Fully saturated colors have a lightness value of 1/2
    :param alpha: alpha (transparency) component where 0 means fully
           transparent and 1 fully opaque. By default, all colors are fully opaque
    :returns: a color with the provided HSL components.
    """
    chroma = (1 - abs(2 * lightness - 1)) * saturation
    side = (hue / 60) % 6
    x = chroma * (1 - abs(side % 2 - 1))
    bottom_color = (chroma, x, 0)
    if 2 > side >= 1:
        bottom_color = (x, chroma, 0)
    if 3 > side >= 2:
        bottom_color = (0, chroma, x)
    if 4 > side >= 3:
        bottom_color = (0, x, chroma)
    if 5 > side >= 4:
        bottom_color = (x, 0, chroma)
    if side >= 5:
        bottom_color = (chroma, 0, x)
    to_add = lightness - chroma / 2
    color = tuple(int((x + to_add) * 255) for x in bottom_color)
    return rgb_color(*color, alpha)