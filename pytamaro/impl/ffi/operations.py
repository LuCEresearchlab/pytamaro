"""FFI-based implementation of graphic operations.

:meta private:
"""

from pytamaro.graphic import Above, Beside, Compose, Graphic, Overlay, Pin, Rotate
from pytamaro.impl.ffi.specs import to_specs
from pytamaro.point import Point
from pytamaro_js_ffi import js_graphic_size  # type: ignore

# ruff: noqa: D103


def graphic_width(graphic: Graphic) -> int:
    return round(js_graphic_size(to_specs(graphic)).width)


def graphic_height(graphic: Graphic) -> int:
    return round(js_graphic_size(to_specs(graphic)).height)


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
