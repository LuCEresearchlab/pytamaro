"""
Various small utilities to deal with a Pillow image and coordinates.
"""

from math import ceil
from typing import Tuple

from PIL import Image as PILImageMod
from PIL import ImageDraw as ImageDrawMod
from PIL.Image import Image as PILImage
from PIL.ImageDraw import ImageDraw as PILImageDraw

from pytamaro.color_names import transparent
from pytamaro.localization import translate

IMAGE_MODE = "RGBA"  # RGB + Alpha channel


def canvas(size: Tuple[int, int]) -> Tuple[PILImage, PILImageDraw]:
    """
    Returns an empty "canvas" (transparent rectangle) with an instance
    of ImageDraw ready to use to draw onto the canvas.

    :param size: width and height of the canvas, in pixel
    :returns: a tuple containing an image of the requested size and
              an ImageDraw instance to draw onto it.
    """
    image = PILImageMod.new(IMAGE_MODE, size, transparent.as_tuple())
    return (image, ImageDrawMod.Draw(image))


def half_position(pos: float) -> int:
    """
    Halves a position, rounding up to the nearest pixel.

    Using the built-in round() function would lead to undesirable
    results due to the floating-point representation;
    e.g., round(11/2) = 6 but round(9/2) = 4.

    :param pos: the position of the pixel to be halved
    :returns the position of the pixel in the middle
    """
    return ceil(pos / 2)


def ensure_size(value: int):
    """
    Raises an exception when the provided value is not valid for a
    size in pixel, being negative or equal to zero.

    :param value: the value (in pixel) to be checked
    """
    if value <= 0:
        raise ValueError(translate("INVALID_SIZE"))


def translate_position(position: Tuple[int, int],
                       delta: Tuple[int, int]) -> Tuple[int, int]:
    """
    Translates a given 2D point by a certain delta.

    :param position: the original position
    :param delta: the translation vector
    :returns: the translated position
    """
    return (position[0] + delta[0], position[1] + delta[1])


def crop_to_bounding_box(image: PILImage) -> PILImage:
    """
    Crop (cut) the image so that the new size just fits the bounding box.
    As an effect, potential transparent borders get eliminated.

    :param image: the image to crop
    :returns: a new cropped image
    """
    return image.crop(image.getbbox())
