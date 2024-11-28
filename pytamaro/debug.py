"""
Functions to enrich a graphic with information useful for debugging purposes.
"""

from skia import Point

from pytamaro.color import Color
from pytamaro.color_functions import rgb_color
from pytamaro.graphic import Graphic
from pytamaro.operations import (compose, graphic_height, graphic_width,
                                 overlay, pin, rotate)
from pytamaro.point_names import (bottom_left, center_left, center_right,
                                  top_left)
from pytamaro.primitives import ellipse, rectangle


def top_left_point(graphic: Graphic) -> Point:
    """
    Returns the top left corner of the bounding box of the graphic.

    :param graphic: graphic to compute the top left corner of
    :returns: the top left corner of the bounding box
    """
    return graphic.bounds.toQuad()[0]


def add_debug_info(graphic: Graphic) -> Graphic:
    """
    Overlays debugging information onto a graphic (a border with the nine
    relevant points on the bounding box and an indicator on the pinning
    position).

    :param graphic: original graphic
    :returns: a graphic with debugging information
    """
    whiteish = rgb_color(235, 235, 235)
    blueish = rgb_color(41, 98, 193)
    blackish = rgb_color(20, 20, 20)
    relative_pin_pos = graphic.pin_position - top_left_point(graphic)
    g_with_border = add_border(graphic, whiteish, blueish)
    half_increase = (graphic_width(g_with_border) - graphic_width(graphic)) / 2
    new_rel_pin_pos = relative_pin_pos + (half_increase, half_increase)
    new_abs_pin_pos = top_left_point(g_with_border) + new_rel_pin_pos
    object.__setattr__(g_with_border, "pin_position", new_abs_pin_pos)
    return show_pin_position(g_with_border, whiteish, blackish)


def circle(diameter: float, color: Color) -> Graphic:
    """
    Creates a circle with the given diameter and color.

    :param diameter: diameter of the circle
    :param color: color of the circle
    :returns: a graphic representing the circle
    """
    return ellipse(diameter, diameter, color)


def add_border(graphic: Graphic, light: Color, dark: Color) -> Graphic:
    """
    Adds a dark border around the graphic, and nine "control points" rendered as
    circles at the nine relevant points on the bounding box of the graphic.

    :param graphic: original graphic
    :param light: color of the inside of the control points
    :param dark: color of the outside of the control points and the border
    :returns: a new graphic adorned with a border and control points
    """
    outer_diameter = min(graphic_width(graphic), graphic_height(graphic), 10)
    control_point = overlay(circle(4 / 5 * outer_diameter, light), circle(outer_diameter, dark))

    def border_with_control_points(length: float) -> Graphic:
        b_with_center = overlay(control_point, rectangle(length, 1, dark))
        b_with_center_left = compose(control_point, pin(center_left, b_with_center))
        return compose(control_point, pin(center_right, b_with_center_left))

    horizontal = border_with_control_points(graphic_width(graphic))
    vertical = rotate(90, border_with_control_points(graphic_height(graphic)))
    top_left_g = compose(pin(top_left, horizontal), pin(top_left, vertical))
    border = compose(
        pin(bottom_left, top_left_g), pin(bottom_left, rotate(180, top_left_g))
    )
    return overlay(control_point, overlay(border, graphic))


def show_pin_position(graphic: Graphic, light: Color, dark: Color) -> Graphic:
    """
    Overlays a dark indicator at the pinning position of the graphic.

    :param graphic: original graphic
    :param light: color for the padding of the indicator
    :param dark: color for the indicator itself

    :returns: the graphic with the indicator at the pinning position
    """
    def indicator(color, padding=0):
        arm = rectangle(15 + padding, 1 + padding, color)
        cross = overlay(rotate(90, arm), arm)
        central_circle = circle(8 + padding, color)
        return overlay(cross, central_circle)
    return compose(overlay(indicator(dark), indicator(light, 3)), graphic)
