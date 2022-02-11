"""
Small functions used in various places to deal with graphics.
"""


import io

from PIL import Image as PILImageMod
from PIL.Image import Image as PILImage

from pytamaro.graphic import Graphic
from pytamaro.localization import translate


def ensure_size(value: float):
    """
    Raises an exception when the provided value is not valid for a
    size in pixel, being negative or equal to zero.

    :param value: the value (in pixel) to be checked
    """
    if value <= 0:
        raise ValueError(translate("INVALID_SIZE"))


def graphic_to_image(graphic: Graphic) -> PILImage:
    """
    Renders a graphic and converts it into a Pillow image.

    :param graphic: graphic to be rendered and converted
    :returns: an equivalent Pillow image
    """
    with io.BytesIO(graphic.as_image().encodeToData()) as stream:
        pil_image = PILImageMod.open(stream)
        pil_image.load()  # Ensure to make a copy of buffer
        return pil_image
