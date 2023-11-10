"""
Functions to enrich a graphic with information useful for debugging purposes.
"""

from skia import Point

from pytamaro.color import Color
from pytamaro.color_functions import rgb_color
from pytamaro.graphic import Graphic
from pytamaro.operations import (compose, graphic_height, graphic_width,
                                 overlay, pin, rotate)
from pytamaro.point_names import bottom_left, top_left
from pytamaro.primitives import rectangle


def top_left_point(graphic: Graphic) -> Point:
    """
    Returns the top left corner of the bounding box of the graphic.

    :param graphic: graphic to compute the top left corner of
    :returns: the top left corner of the bounding box
    """
    return graphic.bounds().toQuad()[0]


def add_debug_info(graphic: Graphic) -> Graphic:
    """
    Overlays debugging information onto a graphic (a border around it and a
    cross at the pin location).

    :param graphic: original graphic
    :returns: a graphic with debugging information
    :meta private:
    """
    relative_pin_pos = graphic.pin_position - top_left_point(graphic)
    border_thickness = 5
    border_color = rgb_color(240, 16, 16)
    g_with_border = add_border(graphic, border_thickness, border_color)
    new_rel_pin_pos = relative_pin_pos + (border_thickness, border_thickness)
    new_abs_pin_pos = top_left_point(g_with_border) + new_rel_pin_pos
    object.__setattr__(g_with_border, "pin_position", new_abs_pin_pos)
    return show_pin_position(g_with_border)


def add_border(graphic: Graphic, width: float, color: Color) -> Graphic:
    """
    Adds a border with the given width (thickness) around the
    (bounding box of the) graphic.

    :param graphic: original graphic
    :param width: width of the border
    :param color: color of the border
    :returns: a new graphic with the border
    """
    horizontal = rectangle(graphic_width(graphic) + 2 * width, width, color)
    vertical = rectangle(width, graphic_height(graphic) + 2 * width, color)
    top_left_g = compose(pin(top_left, horizontal), pin(top_left, vertical))
    border = compose(
        pin(bottom_left, top_left_g), pin(bottom_left, rotate(180, top_left_g))
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
