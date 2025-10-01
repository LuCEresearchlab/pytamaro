"""
Skia-specific color utils.

:meta private:
"""
# pylint: disable=too-few-public-methods
from typing import Protocol

from skia import Color4f


class ColorLikeType(Protocol):
    """
    Protocol for objects that represent colors and have RGBA fields.

    We need this to avoid a circular dependency with pytamaro.color
    :meta private:
    """
    red: int
    green: int
    blue: int
    alpha: float


def skia_color(color: ColorLikeType) -> Color4f:
    """
    Returns the current color as a Skia color.

    :meta private:
    :returns: a Skia color
    """
    return Color4f(color.red / 255,
                   color.green / 255,
                   color.blue / 255,
                   color.alpha)
