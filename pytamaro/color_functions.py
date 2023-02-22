# pylint: disable=missing-docstring
# Separated from color.py only in the main English version to avoid circular imports

from pytamaro.color import Color
from pytamaro.checks import check_range


def rgb_color(red: int, green: int, blue: int, opacity: float = 1.0) -> Color:
    """
    Returns a color with the provided components for red (R), green (G) and blue (B) and a
    certain degree of opacity (alpha, A).

    .. figure:: https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/RGBCube_a.svg/524px-RGBCube_a.svg.png
       :height: 120px
       :align: center

       `RGB cube (SharkD via Wikimedia Commons) <https://commons.wikimedia.org/wiki/File:RGBCube_a.svg>`_

    :param red: red component [0-255]
    :param green: green component [0-255]
    :param blue: blue component [0-255]
    :param opacity: opacity (alpha) of the color, where 0 means fully
           transparent and 1 fully opaque. By default, all colors are fully opaque.
    :returns: a color with the provided RGBA components
    """
    check_range(red, 0, 255, "red")
    check_range(green, 0, 255, "green")
    check_range(blue, 0, 255, "blue")
    check_range(opacity, 0, 1, "opacity")
    return Color(red, green, blue, opacity)


def hsv_color(hue: float, saturation: float, value: float, opacity: float = 1.0) -> Color:
    """
    Returns a color with the provided hue (H), saturation (S), value (V) and a
    certain degree of opacity (alpha, A).

    .. figure:: https://upload.wikimedia.org/wikipedia/commons/4/4e/HSV_color_solid_cylinder.png
       :height: 120px
       :align: center

       `HSV cylinder (SharkD via Wikimedia Commons) <https://commons.wikimedia.org/wiki/File:HSV_color_solid_cylinder.png>`_

    :param hue: hue of the color [0-360]
    :param saturation: saturation of the color [0-1]
    :param value: the amount of light that is applied [0-1]
    :param opacity: opacity (alpha) of the color, where 0 means fully
           transparent and 1 fully opaque. By default, all colors are fully opaque.
    :returns: a color with the provided HSVA components.
    """
    check_range(hue, 0, 360, "hue")
    check_range(saturation, 0, 1, "saturation")
    check_range(value, 0, 1, "value")
    check_range(opacity, 0, 1, "opacity")
    chroma = value * saturation
    side = (hue / 60) % 6
    x_value = chroma * (1 - abs(side % 2 - 1))
    bottom_color = (chroma, x_value, 0)
    if 2 > side >= 1:
        bottom_color = (x_value, chroma, 0)
    if 3 > side >= 2:
        bottom_color = (0, chroma, x_value)
    if 4 > side >= 3:
        bottom_color = (0, x_value, chroma)
    if 5 > side >= 4:
        bottom_color = (x_value, 0, chroma)
    if side >= 5:
        bottom_color = (chroma, 0, x_value)
    to_add = value - chroma
    color = tuple(int((x + to_add) * 255) for x in bottom_color)
    return rgb_color(color[0], color[1], color[2], opacity)


def hsl_color(hue: float, saturation: float, lightness: float, opacity: float = 1.0) -> Color:
    """
    Returns a color with the provided hue (H), saturation (S), lightness (L) and a
    certain degree of opacity (alpha, A).

    .. figure:: https://upload.wikimedia.org/wikipedia/commons/3/35/HSL_color_solid_cylinder.png
       :height: 120px
       :align: center

       `HSL cylinder: SharkD via Wikimedia Commons <https://commons.wikimedia.org/wiki/File:HSL_color_solid_cylinder.png>`_

    :param hue: hue of the color [0-360]
    :param saturation: saturation of the color [0-1]
    :param lightness: the amount of white or black applied [0-1].
            Fully saturated colors have a lightness value of 1/2.
    :param opacity: opacity (alpha) of the color, where 0 means fully
           transparent and 1 fully opaque. By default, all colors are fully opaque.
    :returns: a color with the provided HSLA components
    """
    check_range(hue, 0, 360, "hue")
    check_range(saturation, 0, 1, "saturation")
    check_range(lightness, 0, 1, "lightness")
    check_range(opacity, 0, 1, "opacity")
    chroma = (1 - abs(2 * lightness - 1)) * saturation
    side = (hue / 60) % 6
    x_value = chroma * (1 - abs(side % 2 - 1))
    bottom_color = (chroma, x_value, 0)
    if 2 > side >= 1:
        bottom_color = (x_value, chroma, 0)
    if 3 > side >= 2:
        bottom_color = (0, chroma, x_value)
    if 4 > side >= 3:
        bottom_color = (0, x_value, chroma)
    if 5 > side >= 4:
        bottom_color = (x_value, 0, chroma)
    if side >= 5:
        bottom_color = (chroma, 0, x_value)
    to_add = lightness - chroma / 2
    color = tuple(int((x + to_add) * 255) for x in bottom_color)
    return rgb_color(color[0], color[1], color[2], opacity)
