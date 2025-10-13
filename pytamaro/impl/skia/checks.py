"""
Skia-specific type check utils.

:meta private:
"""
from typing import Any

from pytamaro.checks import check_type
from pytamaro.impl.skia.graphic import SkiaGraphic


def ensure_skia_graphic(graphic: Any, parameter_name: str = "graphic") -> SkiaGraphic:
    """
    Raises an exception when the provided value is not valid for a
    graphic, not being of type SkiaGraphic.

    :param graphic: the value for a (skia) graphic to be checked
    :returns: the validated graphic as a SkiaGraphic
    """
    check_type(graphic, SkiaGraphic, parameter_name)
    return graphic
