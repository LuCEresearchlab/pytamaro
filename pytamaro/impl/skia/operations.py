"""
Skia-based implementation of graphic operations.

:meta private:
"""
# pylint: disable=missing-function-docstring
from pytamaro.graphic import Graphic
from pytamaro.point import Point
from pytamaro.impl.skia.checks import ensure_skia_graphic
from pytamaro.impl.skia.graphic import (SkiaGraphic, SkiaCompose, SkiaPin, SkiaOverlay,
                                        SkiaBeside, SkiaAbove, SkiaRotate)


def graphic_width(graphic: Graphic) -> int:
    graphic = ensure_skia_graphic(graphic)
    return graphic.size().toRound().width()


def graphic_height(graphic: Graphic) -> int:
    graphic = ensure_skia_graphic(graphic)
    return graphic.size().toRound().height()


def compose(foreground_graphic: Graphic,
            background_graphic: Graphic) -> SkiaGraphic:
    foreground_graphic = ensure_skia_graphic(foreground_graphic, "foreground_graphic")
    background_graphic = ensure_skia_graphic(background_graphic, "background_graphic")
    return SkiaCompose(foreground_graphic, background_graphic)


def pin(point: Point, graphic: Graphic) -> SkiaGraphic:
    graphic = ensure_skia_graphic(graphic)
    return SkiaPin(graphic, point)


def overlay(foreground_graphic: Graphic,
            background_graphic: Graphic) -> SkiaGraphic:
    foreground_graphic = ensure_skia_graphic(foreground_graphic, "foreground_graphic")
    background_graphic = ensure_skia_graphic(background_graphic, "background_graphic")
    return SkiaOverlay(foreground_graphic, background_graphic)


def beside(left_graphic: Graphic,
           right_graphic: Graphic) -> SkiaGraphic:
    left_graphic = ensure_skia_graphic(left_graphic, "left_graphic")
    right_graphic = ensure_skia_graphic(right_graphic, "right_graphic")
    return SkiaBeside(left_graphic, right_graphic)


def above(top_graphic: Graphic,
          bottom_graphic: Graphic) -> SkiaGraphic:
    top_graphic = ensure_skia_graphic(top_graphic, "top_graphic")
    bottom_graphic = ensure_skia_graphic(bottom_graphic, "bottom_graphic")
    return SkiaAbove(top_graphic, bottom_graphic)


def rotate(angle: float, graphic: Graphic) -> SkiaGraphic:
    graphic = ensure_skia_graphic(graphic)
    return SkiaRotate(graphic, angle)
