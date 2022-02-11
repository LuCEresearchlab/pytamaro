"""
Functions to create primitive graphics (shapes and text)
"""

from pytamaro.color import Color
from pytamaro.graphic import (CircularSector, Ellipse, Empty, Graphic,
                              Rectangle, Text, Triangle)
from pytamaro.graphic_utils import ensure_size
from pytamaro.utils import export


@export
def rectangle(width: float, height: float, color: Color) -> Graphic:
    """
    Creates a rectangle of the given size, filled with a color.

    :param width: width of the rectangle, in pixel
    :param height: height of the rectangle, in pixel
    :param color: the color to be used to fill the rectangle
    :returns: the specified rectangle as a graphic
    """
    ensure_size(width)
    ensure_size(height)
    return Rectangle(width, height, color)


@export
def empty_graphic() -> Graphic:
    """
    Creates an empty graphic.
    When an empty graphic is composed with any other graphic, it behaves
    as a neutral element: the result is always identical to the other graphic.

    An empty graphic cannot be shown nor saved.

    :returns: an empty graphic (width and height 0 pixels)
    """
    return Empty()


@export
def ellipse(width: float, height: float, color: Color) -> Graphic:
    """
    Creates an ellipse with the given width and height, filled with a color.

    When width and height are the same, the ellipse becomes a circle with a
    diameter equal to the provided size.

    :param width: width of the ellipse, in pixel
    :param height: height of the ellipse, in pixel
    :param color: the color to be used to fill the circle
    :returns: the specified circle as a graphic
    """
    ensure_size(width)
    ensure_size(height)
    return Ellipse(width, height, color)


@export
def circular_sector(radius: float, angle: float, color: Color) \
        -> Graphic:
    """
    Creates a circular sector belonging to a circle of the given radius, filled
    with a color.

    A circular sector is a portion of a circle enclosed between two radii and
    an arc.
    Considering a circle as a clock, the first radius is supposed to "point"
    towards 3 o'clock. The `angle` determines the position of the second
    radius, computed starting from the first one in the clockwise direction.

    :param radius: radius of the circle from which the circular sector is
                   taken, in pixel
    :param angle: central angle, in degrees
    :param color: the color to be used to fill the circular sector
    :returns: the specified circular sector as a graphic
    """
    ensure_size(radius)
    return CircularSector(radius, angle, color)


@export
def triangle(side: float, color: Color) -> Graphic:
    """
    Creates an equilateral triangle pointing upwards of the given side, filled
    with a color.

    :param side: length of the side of the triangle, in pixel
    :param color: the color to be used to fill the triangle
    :returns: the specified triangle as a graphic
    """
    ensure_size(side)
    return Triangle(side, color)


@export
def text(content: str, font: str, points: float, color: Color) \
        -> Graphic:
    """
    Creates a graphic with the text rendered using the specified font, size and
    color.

    When the indicated True-Type Font is not found in the system, a very
    basilar font that is always available is used instead. The resulting
    graphic has the minimal size that still fits the whole text.

    :param content: the text to render
    :param font: the name of the font (e.g., "arial" on Windows, "Arial" on
           macOS)
    :param points: size in typographic points (e.g., 16)
    :param color: the color to be used to render the text
    :returns: the specified text as a graphic
    """
    return Text(content, font, points, color)
