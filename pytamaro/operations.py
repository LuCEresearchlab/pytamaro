"""
Functions to do operations on graphics (mainly, to combine them).
"""


from pytamaro.graphic import Compose, Graphic, Pin, Rotate
from pytamaro.utils import export
from pytamaro.point import Point
from pytamaro.point_names import center, top_center, bottom_center, center_right, center_left


@export
def graphic_width(graphic: Graphic) -> int:
    """
    Returns the width of a graphic, in pixel.

    :param graphic: graphic to calculate the width of
    :returns: width of the graphic
    """
    return graphic.size().toCeil().width()


@export
def graphic_height(graphic: Graphic) -> int:
    """
    Returns the height of a graphic, in pixel.

    :param graphic: graphic to calculate the height of
    :returns: height of the graphic
    """
    return graphic.size().toCeil().height()


@export
def compose(foreground_graphic: Graphic, background_graphic: Graphic) -> Graphic:
    """
    Composes two graphics keeping the first one in the foreground and the
    second one in background, aligning them using their pin positions.

    The pin location used to compose becomes the pin location of the resulting
    graphic.

    :param foreground_graphic: graphic to keep in the foreground
    :param background_graphic: graphic to keep in the background
    :returns: the resulting graphic after combining the two provided ones
    """
    return Compose(foreground_graphic, background_graphic)


@export
def pin(point: Point, graphic: Graphic) -> Graphic:
    """
    Changes the pinning position of a graphic, returning a new graphic with
    the same content but with an updated pinning position.
    The new pinning position is determined by the parameter `point`.

    Each graphic is contained in a rectangular bounding box.
    There are 9 notable points, corresponding to the four corners of this rectangle,
    the middle points of the four edges and the center of the rectangle.
    These points can be referred to using these names: `top_left`, `top_right`,
    `bottom_left`, `bottom_right`, `top_center`, `center_right`,
    `bottom_center`, `center_left` and `center`.

    :param point: the point indicating the new pinning position
    :param graphic: original graphic
    :returns: a new graphic with an updated pinning position
    """
    return Pin(graphic, point)


def _compose_pin_center(graphic1: Graphic, graphic2: Graphic,
                        point1: Point, point2: Point) -> Graphic:
    """
    Composes the two graphics, pinning the first one at `point1` and the second one
    at `point2`. The composed graphic is then pinned at its center.

    :param graphic1: first graphic to compose
    :param graphic2: second graphic to compose
    :param point1: pinning position for the first graphic
    :param point2: pinning position for the second graphic

    :returns: the combined graphic, pinned at its center
    """
    return pin(center, compose(pin(point1, graphic1), pin(point2, graphic2)))


@export
def overlay(foreground_graphic: Graphic, background_graphic: Graphic) -> Graphic:
    """
    Overlays two graphics keeping the first one in the foreground and the
    second one in background, aligning them on their centers.

    The pinning position of the resulting graphic is at its center.

    :param foreground_graphic: graphic to keep in the foreground
    :param background_graphic: graphic to keep in the background
    :returns: the resulting graphic after overlaying the two provided ones
    """
    return _compose_pin_center(foreground_graphic, background_graphic, center, center)


@export
def beside(left_graphic: Graphic, right_graphic: Graphic) -> Graphic:
    """
    Composes two graphics placing the first on the left and the second on the
    right.  The two graphics are aligned vertically on their centers.

    The pinning position of the resulting graphic is at its center.

    :param left_graphic: graphic to place on the left
    :param right_graphic: graphic to place on the right
    :returns: the resulting graphic after placing the two graphics one besides
              the other
    """
    return _compose_pin_center(left_graphic, right_graphic, center_right, center_left)


@export
def above(top_graphic: Graphic, bottom_graphic: Graphic) -> Graphic:
    """
    Composes two graphics placing the first on the top and the second on the
    bottom.
    The two graphics are aligned horizontally on their centers.

    The pinning position of the resulting graphic is at its center.

    :param top_graphic: graphic to place on the top
    :param bottom_graphic: graphic to place on the bottom
    :returns: the resulting graphic after placing the two graphics one above
              the other
    """
    return _compose_pin_center(top_graphic, bottom_graphic, bottom_center, top_center)


@export
def rotate(degrees: float, graphic: Graphic) -> Graphic:
    """
    Rotates an graphic by a given amount of degrees counterclockwise around
    its pinning position.

    Small rounding errors (due to approximations to the nearest pixel) may
    occur.

    :param degrees: amount of degrees the graphic needs to be rotated
    :param graphic: the graphic to rotate
    :returns: the original graphic rotated around its pinning position
    """
    # Negate the angle given that Rotate is clockwise.
    return Rotate(graphic, -degrees)
