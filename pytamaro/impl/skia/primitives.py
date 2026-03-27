"""
Skia-based implementation of graphic primitives.

:meta private:
"""
# pylint: disable=missing-function-docstring
from pytamaro.color import Color
from pytamaro.impl.skia.graphic import (SkiaRectangle, SkiaEmpty, SkiaEllipse,
                                        SkiaCircularSector, SkiaTriangle, SkiaText, SkiaGraphic)


def rectangle(width: float, height: float, color: Color) -> SkiaGraphic:
    return SkiaRectangle(width, height, color)


def empty_graphic() -> SkiaGraphic:
    return SkiaEmpty()


def ellipse(width: float, height: float, color: Color) -> SkiaGraphic:
    return SkiaEllipse(width, height, color)


def circular_sector(radius: float, angle: float, color: Color) -> SkiaGraphic:
    return SkiaCircularSector(radius, angle, color)


def triangle(side1: float, side2: float, angle: float, color: Color) -> SkiaGraphic:
    return SkiaTriangle(side1, side2, angle, color)


def text(content: str, font: str, points: float, color: Color) -> SkiaGraphic:
    return SkiaText(content, font, points, color)
