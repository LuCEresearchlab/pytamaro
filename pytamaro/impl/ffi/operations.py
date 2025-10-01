"""
FFI-based implementation of graphic operations.

:meta private:
"""
# pylint: disable=import-error. missing-function-docstring
from pytamaro_ffi import graphic_size  # type: ignore

from pytamaro.graphic import Graphic, Compose, Point, Pin, Overlay, Beside, Above, Rotate


def graphic_width(graphic: Graphic) -> int:
    return graphic_size(graphic.as_dict()).width


def graphic_height(graphic: Graphic) -> int:
    return graphic_size(graphic.as_dict()).height


def compose(foreground_graphic: Graphic, background_graphic: Graphic) -> Graphic:
    return Compose(foreground_graphic, background_graphic)


def pin(point: Point, graphic: Graphic) -> Graphic:
    return Pin(graphic, point)


def overlay(foreground_graphic: Graphic, background_graphic: Graphic) -> Graphic:
    return Overlay(foreground_graphic, background_graphic)


def beside(left_graphic: Graphic, right_graphic: Graphic) -> Graphic:
    return Beside(left_graphic, right_graphic)


def above(top_graphic: Graphic, bottom_graphic: Graphic) -> Graphic:
    return Above(top_graphic, bottom_graphic)


def rotate(angle: float, graphic: Graphic) -> Graphic:
    return Rotate(graphic, angle)
