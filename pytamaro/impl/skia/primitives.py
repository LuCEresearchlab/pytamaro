"""
FFI-based implementation of graphic primitives.

:meta private:
"""
# pylint: disable=missing-function-docstring
from pytamaro.graphic import Graphic
from pytamaro.color import Color
from pytamaro.impl.skia.graphic import (SkiaRectangle, SkiaEmpty, SkiaEllipse,
                                        SkiaCircularSector, SkiaTriangle, SkiaText)


def rectangle(width: float, height: float, color: Color) -> Graphic:
    return SkiaRectangle(width, height, color)


def empty_graphic() -> Graphic:
    return SkiaEmpty()


def ellipse(width: float, height: float, color: Color) -> Graphic:
    return SkiaEllipse(width, height, color)


def circular_sector(radius: float, angle: float, color: Color) -> Graphic:
    return SkiaCircularSector(radius, angle, color)


def triangle(side1: float, side2: float, angle: float, color: Color) -> Graphic:
    return SkiaTriangle(side1, side2, angle, color)


def text(content: str, font: str, points: float, color: Color) -> Graphic:
    return SkiaText(content, font, points, color)
