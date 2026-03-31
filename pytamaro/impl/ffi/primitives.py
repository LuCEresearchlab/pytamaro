"""FFI-based implementation of graphic primitives.

:meta private:
"""

from pytamaro.color import Color
from pytamaro.graphic import CircularSector, Ellipse, Empty, Graphic, Rectangle, Text, Triangle

# ruff: noqa: D103


def rectangle(width: float, height: float, color: Color) -> Graphic:
    return Rectangle(width, height, color)


def empty_graphic() -> Graphic:
    return Empty()


def ellipse(width: float, height: float, color: Color) -> Graphic:
    return Ellipse(width, height, color)


def circular_sector(radius: float, angle: float, color: Color) -> Graphic:
    return CircularSector(radius, angle, color)


def triangle(side1: float, side2: float, angle: float, color: Color) -> Graphic:
    return Triangle(side1, side2, angle, color)


def text(content: str, font: str, points: float, color: Color) -> Graphic:
    return Text(content, font, points, color)
