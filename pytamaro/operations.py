"""
Functions to do operations on graphics (mainly, to combine them).
"""


from pytamaro.graphic import Compose, Graphic, Pin, Rotate
from pytamaro.utils import export


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
def compose(foreground_graphic: Graphic, background_graphic: Graphic) \
        -> Graphic:
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
def pin(horizontal_place: str, vertical_place: str, graphic: Graphic) \
        -> Graphic:
    """
    Changes the pinning position of a graphic, returning a new graphic with
    the same content but with an updated pinning position.

    The new pinning position is determined by the parameters `horizontal_place`
    and `vertical_place`.

    :param horizontal_place: one of "left", "middle" or "right" that
           respectively indicate to move the new pinning positon to the left
           border, the (horizontal) center, or the right border of the graphic
    :param vertical_place: one of "top", "middle" or "bottom" that
           respectively indicate to move the new pinning positon to the top
           border, the (vertical) center, or the bottom border of the graphic
    :param graphic: original graphic
    :returns: a new graphic with an updated pinning position
    """
    return Pin(graphic, horizontal_place, vertical_place)


@export
def overlay(foreground_graphic: Graphic, background_graphic: Graphic) \
        -> Graphic:
    """
    Overlays two graphics keeping the first one in the foreground and the
    second one in background, aligning them on their centers.

    :param foreground_graphic: graphic to keep in the foreground
    :param background_graphic: graphic to keep in the background
    :returns: the resulting graphic after overlaying the two provided ones
    """
    return compose(
        pin("middle", "middle", foreground_graphic),
        pin("middle", "middle", background_graphic))


@export
def beside(left_graphic: Graphic, right_graphic: Graphic) -> Graphic:
    """
    Composes two graphics placing the first on the left and the second on the
    right.  The two graphics are aligned vertically on their centers.

    :param left_graphic: graphic to place on the left
    :param right_graphic: graphic to place on the right
    :returns: the resulting graphic after placing the two graphics one besides
              the other
    """
    return compose(
        pin("right", "middle", left_graphic),
        pin("left", "middle", right_graphic))


@export
def above(top_graphic: Graphic, bottom_graphic: Graphic) -> Graphic:
    """
    Composes two graphics placing the first on the top and the second on the
    bottom.
    The two graphics are aligned horizontally on their centers.

    :param top_graphic: graphic to place on the top
    :param bottom_graphic: graphic to place on the bottom
    :returns: the resulting graphic after placing the two graphics one above
              the other
    """
    return compose(
        pin("middle", "bottom", top_graphic),
        pin("middle", "top", bottom_graphic))


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
