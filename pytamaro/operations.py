"""
Functions to do operations on graphics (mainly, to combine them).
"""

from math import cos, radians, sin
from operator import itemgetter
from typing import Callable, Tuple

from PIL import Image as ImageMod
from PIL.Image import Image as PILImage

from pytamaro.color_names import transparent
from pytamaro.graphic import Graphic
from pytamaro.graphic_utils import (canvas, crop_to_bounding_box,
                                    half_position, translate_position)
from pytamaro.utils import export


@export
def graphic_width(graphic: Graphic) -> int:
    """
    Returns the width of a graphic, in pixel.

    :param graphic: graphic to calculate the width of
    :returns: width of the graphic
    """
    return graphic.get_image().width


@export
def graphic_height(graphic: Graphic) -> int:
    """
    Returns the height of a graphic, in pixel.

    :param graphic: graphic to calculate the height of
    :returns: height of the graphic
    """
    return graphic.get_image().height


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
    fg_pin = foreground_graphic.get_pin_position()
    bg_pin = background_graphic.get_pin_position()
    left = max(fg_pin[0], bg_pin[0])
    right = max(graphic_width(foreground_graphic) - fg_pin[0],
                graphic_width(background_graphic) - bg_pin[0])
    top = max(fg_pin[1], bg_pin[1])
    bottom = max(graphic_height(foreground_graphic) - fg_pin[1],
                 graphic_height(background_graphic) - bg_pin[1])
    result, _ = canvas((left + right, top + bottom))
    result.paste(background_graphic.get_image(),
                 (left - bg_pin[0], top - bg_pin[1]))
    result.alpha_composite(foreground_graphic.get_image(),
                           (left - fg_pin[0], top - fg_pin[1]))
    return Graphic(result, (left, top))


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
    width = graphic_width(graphic)
    height = graphic_height(graphic)
    h_mapping = {
        "left": 0,
        "middle": half_position(width - 1),
        "right": width
    }
    v_mapping = {
        "top": 0,
        "middle": half_position(height - 1),
        "bottom": height
    }
    return graphic.change_pin_position(
        (h_mapping[horizontal_place], v_mapping[vertical_place]))


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
def rotate(degrees: int, graphic: Graphic) -> Graphic:
    """
    Rotates an graphic by a given amount of degrees counterclockwise around
    its pinning position.

    Small rounding errors (due to approximations to the nearest pixel) may
    occur.

    :param degrees: amount of degrees the graphic needs to be rotated
    :param graphic: the graphic to rotate
    :returns: the original graphic rotated around its pinning position
    """

    # When the rotation is not around the center, Pillow does not properly
    # expand the graphic.  More specifically, Pillow would also support the
    # rotation around an arbitrary point, but then the `expand=True` flag gets
    # ignored.
    # To overcome this limitation, we reposition the graphic adding padding
    # so that the pinning position becomes the center of the graphic.
    # At that point we can use `PILImage.rotate()` with `expand=True`,
    # deferring the required computations to Pillow.

    padding_top, padding_bottom, padding_left, padding_right = \
        _padding_center_pin(graphic)

    # Affine transformation to create a new graphic having the size of the old
    # one plus padding. The original graphics is translated by (padding_left,
    # padding_top) wrt the origin (0, 0) of the resulting graphic.

    graphic_center_pin = graphic.get_image().transform(
        (graphic_width(graphic) + padding_left + padding_right,
         graphic_height(graphic) + padding_top + padding_bottom),
        ImageMod.AFFINE,
        (1, 0, -padding_left, 0, 1, -padding_top),
        fillcolor=transparent.as_tuple())

    # Manually rotate the original pixels. We only care about the alpha
    # channel, because it determines which fully transparent pixels will be
    # removed when cropping to the new bounding box.
    # The new ("rotated") pinning position is obtained by rotating the original
    # one after padding and translating it by (min_x, min_y) to account for the
    # implicit "repositioning" after cropping and due to the fact that every
    # graphic in Pillow has a local origin (0, 0) and there are no global
    # absolute coordinates.

    min_x, min_y = _offset_after_rotate(degrees, graphic_center_pin)
    pin_pos = graphic.get_pin_position()
    rotated_pin = _rotate_point_by(degrees)(
        translate_position(pin_pos, (padding_left, padding_top)))
    new_pin_pos = translate_position(rotated_pin, (-min_x, -min_y))

    rotated_graphic = graphic_center_pin.rotate(
        degrees,
        expand=True,
        fillcolor=transparent.as_tuple())

    return Graphic(crop_to_bounding_box(rotated_graphic), new_pin_pos)


def _padding_center_pin(graphic: Graphic) -> Tuple[int, int, int, int]:
    """
    Computes how much padding to add to the four sides of an graphic so that
    its pinning position is at the center of the padded graphic.

    :param graphic: graphic to compute the padding for
    :returns: padding to add to the four sides (top, bottom, left, right)
    """
    pos = graphic.get_pin_position()

    pos_to_left = pos[0]
    pos_to_top = pos[1]
    pos_to_right = graphic_width(graphic) - 1 - pos[0]
    pos_to_bottom = graphic_height(graphic) - 1 - pos[1]

    padding_top = max(0, pos_to_bottom - pos_to_top)
    padding_bottom = max(0, pos_to_top - pos_to_bottom)
    padding_left = max(0, pos_to_right - pos_to_left)
    padding_right = max(0, pos_to_left - pos_to_right)

    return (padding_top, padding_bottom, padding_left, padding_right)


def _rotate_point_by(degrees: int) \
        -> Callable[[Tuple[int, int]], Tuple[int, int]]:
    """
    Rotates a 2D point counterclockwise by `degrees`.

    We use the rotation matrix, but we negate the angle because we are in a
    left-handed cartesian coordinate system (y grows going down), thus the
    classical rotation matrix would produce a clockwise rotation.

    Given that this function is expected to be called several times with the
    same angle, we "curry" it and return a function that rotates a point by a
    fixed angle.

    :param degrees: angle of rotation
    :returns: a function that rotates a point by `degrees`
    """
    theta = radians(-degrees)
    cosine = cos(theta)
    sine = sin(theta)

    def rotate_point(point: Tuple[int, int]) -> Tuple[int, int]:
        """
        :param point: 2D point to rotate
        :returns: the coordinates of the rotated point
        """
        x, y = point  # pylint: disable=invalid-name
        return (round(x * cosine - y * sine),
                round(x * sine + y * cosine))
    return rotate_point


def _offset_after_rotate(degrees: int, graphic: PILImage) -> Tuple[int, int]:
    """
    Computes the offset of the left and the top-most non-trasparent pixel after
    rotating `graphic` by `degrees`.

    We want to know this because transparent pixels get removed after cropping
    to the bouding box.

    :param degrees: angle of rotation
    :param graphic: graphic to rotate
    :returns: absolute global coordinates (x, y) of the the left and the
              top-most non-trasparent pixel after the rotation

    """
    rot = _rotate_point_by(degrees)
    rotated_coords = (rot((x, y))
                      for y in range(graphic.height)
                      for x in range(graphic.width))
    # In RGBA mode, A is the fourth band
    alpha_values = graphic.getdata(3)
    filled_coords = list(
        map(itemgetter(0),
            filter(lambda alpha_c: alpha_c[1] != 0,
                   zip(rotated_coords, alpha_values))))
    min_x = min(map(itemgetter(0), filled_coords))
    min_y = min(map(itemgetter(1), filled_coords))
    return (min_x, min_y)
