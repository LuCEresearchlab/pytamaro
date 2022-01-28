"""
Functions to create primitive graphics (shapes and text)
"""

from math import sqrt

from PIL import Image as PILImageMod
from PIL import ImageFont

from pytamaro.color import Color
from pytamaro.graphic import Graphic
from pytamaro.graphic_utils import (IMAGE_MODE, canvas, crop_to_bounding_box,
                                    ensure_size, half_position)
from pytamaro.utils import export


@export
def rectangle(width: int, height: int, color: Color) -> Graphic:
    """
    Creates a rectangle of the given size, filled with a color.

    :param width: width of the rectangle, in pixel
    :param height: height of the rectangle, in pixel
    :param color: the color to be used to fill the rectangle
    :returns: the specified rectangle as a graphic
    """
    ensure_size(width)
    ensure_size(height)
    return Graphic(PILImageMod.new(IMAGE_MODE, (width, height),
                                   color.as_tuple()))


@export
def empty_graphic() -> Graphic:
    """
    Creates an empty graphic.
    When an empty graphic is composed with any other graphic, it behaves
    as a neutral element: the result is always identical to the other graphic.

    An empty graphic cannot be shown nor saved.

    :returns: an empty graphic (width and height 0 pixels)
    """
    return Graphic(PILImageMod.new(IMAGE_MODE, (0, 0)))


@export
def ellipse(width: int, height: int, color: Color) -> Graphic:
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
    image, draw = canvas((width, height))
    draw.ellipse([(0, 0), image.size], fill=color.as_tuple())
    return Graphic(image)


@export
def circular_sector(radius: int, angle: int, color: Color) \
        -> Graphic:
    """
    Creates a circular sector belonging to a circle of the given radius, filled
    with a color.

    A circular sector is a portion of a circle enclosed between two radii and
    an arc.
    Considering a circle as a clock, the first radius is supposed to "point"
    towards 3 o'clock. The `angle` determines the position of the second
    radius, computed starting from the first one in the clockwise direction.
    When `angle` is 360 degrees, the circular sector is effectively the full
    circle.

    :param radius: radius of the circle from which the circular sector is
                   taken, in pixel
    :param angle: central angle, in degrees
    :param color: the color to be used to fill the circular sector
    :returns: the specified circular sector as a graphic
    """
    ensure_size(radius)
    side = radius * 2
    image, draw = canvas((side, side))
    draw.pieslice(((0, 0), image.size), 0, angle, fill=color.as_tuple())
    return Graphic(crop_to_bounding_box(image))


@export
def triangle(side: int, color: Color) -> Graphic:
    """
    Creates an equilateral triangle pointing upwards of the given side, filled
    with a color.

    :param side: length of the side of the triangle, in pixel
    :param color: the color to be used to fill the triangle
    :returns: the specified triangle as a graphic
    """
    ensure_size(side)
    height = half_position(side * sqrt(3))
    image, draw = canvas((side, height))
    bottom_left = (0, height)
    top_middle = (half_position(side), 0)
    bottom_right = (side, height)
    draw.polygon([bottom_left, top_middle, bottom_right],
                 fill=color.as_tuple())
    return Graphic(image)


@export
def text(content: str, font: str, points: int, color: Color) \
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
    try:
        loadedfont = ImageFont.truetype(f"{font}.ttf", size=points)
    except OSError:
        loadedfont = ImageFont.load_default()
    image, draw = canvas(loadedfont.getsize(content))
    draw.text((0, 0), content, fill=color.as_tuple(), font=loadedfont)
    return Graphic(image)
