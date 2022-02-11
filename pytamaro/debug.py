"""
Functions to enrich a graphic with information useful for debugging purposes.
"""

from pytamaro.color import Color, rgb_color
from pytamaro.graphic import Graphic
from pytamaro.operations import (compose, graphic_height, graphic_width,
                                 overlay, pin, rotate)
from pytamaro.primitives import rectangle


def add_debug_info(graphic: Graphic) -> Graphic:
    """
    Overlays debugging information onto a graphic (a border around it and a
    cross at the pin location).

    :param graphic: original graphic
    :returns: a graphic with debugging information
    :meta private:
    """
    pin_pos = graphic.pin_position
    border_width = 5
    border_color = rgb_color(240, 16, 16)
    img_with_border = add_border(graphic, border_width, border_color)
    img_with_border.set_pin_position(pin_pos.x() + border_width,
                                     pin_pos.y() + border_width)
    return show_pin_position(img_with_border)


def add_border(graphic: Graphic, width: float, color: Color) -> Graphic:
    """
    Adds a border with the given width (thickness) around the
    (bounding box of the) graphic.

    :param graphic: original graphic
    :param width: width of the border in pixel
    :param color: color of the border
    :returns: a new graphic with the border
    """
    horizontal = rectangle(graphic_width(graphic) + 2 * width, width, color)
    vertical = rectangle(width, graphic_height(graphic) + 2 * width, color)
    top_left = compose(
        pin("left", "top", horizontal),
        pin("left", "top", vertical))
    border = compose(
        pin("left", "bottom", top_left),
        pin("left", "bottom", rotate(180, top_left))
    )
    return overlay(graphic, border)


def show_pin_position(graphic: Graphic) -> Graphic:
    """
    Overlays a yellowish cross onto the graphic at its pin location,
    to make it visibile for debugging purposes.

    :param graphic: original graphic
    :returns: the graphic with the highlighted pin position
    """
    arm = rectangle(35, 5, rgb_color(250, 200, 0))
    cross = rotate(45, compose(arm, rotate(90, arm)))
    return compose(cross, graphic)
