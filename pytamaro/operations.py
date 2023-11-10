"""
Functions to do operations on graphics (mainly, to combine them).
"""

from pytamaro.checks import check_angle, check_graphic, check_point
from pytamaro.graphic import (Above, Beside, Compose, Graphic, Overlay, Pin,
                              Rotate)
from pytamaro.point import Point
from pytamaro.utils import export


@export
def graphic_width(graphic: Graphic) -> int:
    """
    Returns the width of a graphic.

    :param graphic: graphic to calculate the width of
    :returns: width of the graphic
    """
    check_graphic(graphic)
    return graphic.size().toCeil().width()


@export
def graphic_height(graphic: Graphic) -> int:
    """
    Returns the height of a graphic.

    :param graphic: graphic to calculate the height of
    :returns: height of the graphic
    """
    check_graphic(graphic)
    return graphic.size().toCeil().height()


@export
def compose(foreground_graphic: Graphic, background_graphic: Graphic) -> Graphic:
    """
    Creates a new graphic by composing the two provided graphics.
    The first graphic is kept in the foreground, the second one in the
    background.
    The graphics are aligned by superimposing their pinning positions.

    The pinning position used to compose becomes the pinning position of the
    resulting graphic.

    :param foreground_graphic: graphic in the foreground
    :param background_graphic: graphic in the background
    :returns: the resulting composed graphic
    """
    check_graphic(foreground_graphic, "foreground_graphic")
    check_graphic(background_graphic, "background_graphic")
    return Compose(foreground_graphic, background_graphic)


@export
def pin(point: Point, graphic: Graphic) -> Graphic:
    """
    Creates a new graphic that corresponds to the provided graphic,
    with a new pinning position.

    Each graphic is contained in a rectangular bounding box.
    There are 9 notable points, corresponding to the four corners of this rectangle,
    the middle points of the four edges and the center of the rectangle.
    These points can be referred to using these names: `top_left`, `top_right`,
    `bottom_left`, `bottom_right`, `top_center`, `center_right`,
    `bottom_center`, `center_left` and `center`.

    :param point: the point indicating the new pinning position
    :param graphic: original graphic
    :returns: a new graphic with the specified pinning position
    """
    check_point(point)
    check_graphic(graphic)
    return Pin(graphic, point)


@export
def overlay(foreground_graphic: Graphic, background_graphic: Graphic) -> Graphic:
    """
    Creates a new graphic by overlaying the two provided graphics,
    keeping the first one in the foreground and the second one in background.
    The two graphics are overlaid on their centers.

    The pinning position of the new graphic is at its center.

    :param foreground_graphic: graphic in the foreground
    :param background_graphic: graphic in the background
    :returns: the resulting graphic after overlaying the two provided ones
    """
    check_graphic(foreground_graphic, "foreground_graphic")
    check_graphic(background_graphic, "background_graphic")
    return Overlay(foreground_graphic, background_graphic)


@export
def beside(left_graphic: Graphic, right_graphic: Graphic) -> Graphic:
    """
    Creates a new graphic by placing the two graphics one besides the other.
    The two graphics are vertically centered.

    The pinning position of the new graphic is at its center.

    :param left_graphic: graphic to place on the left
    :param right_graphic: graphic to place on the right
    :returns: the resulting graphic after placing the two graphics one besides
              the other
    """
    check_graphic(left_graphic, "left_graphic")
    check_graphic(right_graphic, "right_graphic")
    return Beside(left_graphic, right_graphic)


@export
def above(top_graphic: Graphic, bottom_graphic: Graphic) -> Graphic:
    """
    Creates a new graphic by placing the two graphics one above the other.
    The two graphics are horizontally centered.

    The pinning position of the new graphic is at its center.

    :param top_graphic: graphic to place on the top
    :param bottom_graphic: graphic to place on the bottom
    :returns: the resulting graphic after placing the two graphics one above
              the other
    """
    check_graphic(top_graphic, "top_graphic")
    check_graphic(bottom_graphic, "bottom_graphic")
    return Above(top_graphic, bottom_graphic)


@export
def rotate(angle: float, graphic: Graphic) -> Graphic:
    """
    Creates a new graphic by rotating counterclockwise the provided graphic
    around its pinning position by the given angle.
    A negative angle corresponds to a clockwise rotation.

    :param angle: angle of counterclockwise rotation, in degrees
    :param graphic: the graphic to rotate
    :returns: a new, rotated graphic
    """
    check_angle(angle)
    check_graphic(graphic)
    return Rotate(graphic, angle)
