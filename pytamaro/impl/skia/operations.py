"""Skia-based implementation of graphic operations.

:meta private:
"""

# ruff: noqa: D103
from typing import cast

from pytamaro.graphic import Graphic
from pytamaro.impl.skia.graphic import (
    SkiaAbove,
    SkiaBeside,
    SkiaCompose,
    SkiaGraphic,
    SkiaOverlay,
    SkiaPin,
    SkiaRotate,
)
from pytamaro.point import Point


def graphic_width(graphic: Graphic) -> int:
    graphic = cast(SkiaGraphic, graphic)
    return graphic.size().toRound().width()


def graphic_height(graphic: Graphic) -> int:
    graphic = cast(SkiaGraphic, graphic)
    return graphic.size().toRound().height()


def compose(foreground_graphic: Graphic, background_graphic: Graphic) -> SkiaGraphic:
    foreground_graphic = cast(SkiaGraphic, foreground_graphic)
    background_graphic = cast(SkiaGraphic, background_graphic)
    return SkiaCompose(foreground_graphic, background_graphic)


def pin(point: Point, graphic: Graphic) -> SkiaGraphic:
    graphic = cast(SkiaGraphic, graphic)
    return SkiaPin(graphic, point)


def overlay(foreground_graphic: Graphic, background_graphic: Graphic) -> SkiaGraphic:
    foreground_graphic = cast(SkiaGraphic, foreground_graphic)
    background_graphic = cast(SkiaGraphic, background_graphic)
    return SkiaOverlay(foreground_graphic, background_graphic)


def beside(left_graphic: Graphic, right_graphic: Graphic) -> SkiaGraphic:
    left_graphic = cast(SkiaGraphic, left_graphic)
    right_graphic = cast(SkiaGraphic, right_graphic)
    return SkiaBeside(left_graphic, right_graphic)


def above(top_graphic: Graphic, bottom_graphic: Graphic) -> SkiaGraphic:
    top_graphic = cast(SkiaGraphic, top_graphic)
    bottom_graphic = cast(SkiaGraphic, bottom_graphic)
    return SkiaAbove(top_graphic, bottom_graphic)


def rotate(angle: float, graphic: Graphic) -> SkiaGraphic:
    graphic = cast(SkiaGraphic, graphic)
    return SkiaRotate(graphic, angle)
