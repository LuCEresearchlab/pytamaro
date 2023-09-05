"""
`Color` type, functions to produce colors, and constants for important colors.
"""

from dataclasses import dataclass
from typing import Tuple

from skia import Color4f


@dataclass
class Color:
    """
    Represents a color.
    A color also has a degree of opacity,
    from completely transparent (like the color `transparent`)
    to completely opaque (like the color `red`).
    """

    color: Color4f

    def __init__(self, red: int, green: int, blue: int, alpha: float):
        self.color = Color4f(red / 255, green / 255, blue / 255, alpha)

    def as_tuple(self) -> Tuple[int, int, int, float]:
        """
        Returns the current color as an RGBA tuple.

        :meta private:
        :returns: a tuple with four components. The first three [0-255] identify the
                  color, the last one [0-1] identifies the transparency
        """
        return self.color[0] * 255, self.color[1] * 255, self.color[2] * 255, self.color[3]
