"""
Graphic class, which wraps a Pillow image with a position for pinning.
"""

from dataclasses import dataclass
from typing import List, Tuple

from PIL.Image import Image as PILImage

from pytamaro.graphic_utils import half_position


@dataclass
class Graphic:
    """
    A graphic (image) with a position for pinning.

    The pinning position is used in the following operations:

    - rotation (to determine the center of rotation)
    - graphic composition (two graphics get composed aligning their pinning
      position).
    """
    img: PILImage
    pin_position: Tuple[int, int]

    def __init__(self, img: PILImage, pin_position: Tuple[int, int] = None):
        self.img = img
        self.pin_position = pin_position if pin_position is not None \
            else self._default_pin_position()

    def _default_pin_position(self) -> Tuple[int, int]:
        # The default pin position is at the center of the graphic,
        # approximated to the nearest pixel.
        return (half_position(self.width() - 1),
                half_position(self.height() - 1))

    def get_image(self) -> PILImage:
        """
        Returns the Pillow image.

        :returns: an instance of Pillow's Image class
        :meta private:
        """
        return self.img

    def get_pin_position(self) -> Tuple[int, int]:
        """
        Returns the pin position of this graphic, as a pair of coordinates
        (x, y).

        :returns: the pin position
        :meta private:
        """
        return self.pin_position

    def width(self) -> int:
        """
        Returns the width of the graphic.

        :meta private:
        :returns: width in pixels
        """
        return self.get_image().width

    def height(self) -> int:
        """
        Returns the height of the graphic.

        :meta private:
        :returns: height in pixels
        """
        return self.get_image().height

    def change_pin_position(self, position: Tuple[int, int]):
        """
        Returns a new graphic with an updated pin position.

        :param position: the new position for the pin
        :returns: a new graphic with the same content and the new pin position
        :meta private:
        """
        return Graphic(self.get_image(), position)

    def is_empty_graphic(self) -> bool:
        """
        Checks whether this is an empty graphic (size 0 by 0 pixels).

        :returns: True if the graphic is empty, False otherwise
        :meta private:
        """
        return self.get_image().size == (0, 0)

    def _key(self) -> List:
        """
        Returns the fields relevant for __eq__ and __hash__ as a list.

        The resulting list must contain comparable and hashable values.
        For this reason, we carefully manage the case with the empty image
        (on which invoking .tobytes() raises an exception).

        :returns: a list with values relevant for equality
        """
        return [self.get_image().tobytes() if not self.is_empty_graphic()
                else None,
                self.get_pin_position()]

    def __eq__(self, other: object) -> bool:
        """
        Compares a graphic with another graphic.
        Two graphics are considered equal if they are both empty or if they
        have exactly the same content (pixel by pixel) and the same pinning
        position.

        :returns: True if the two graphics are considered equal, False
                  otherwise
        """
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._key() == other._key()

    def __hash__(self) -> int:
        """
        Computes the hash of this graphic, relying on _key() and the built-in
        hash().

        :returns hash for this graphic
        """
        return hash(tuple(self._key()))
