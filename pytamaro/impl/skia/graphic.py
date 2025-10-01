"""
Skia-based implementation of graphics.

:meta private:
"""
# pylint: disable=missing-class-docstring
import sys
from abc import abstractmethod, ABC
from dataclasses import dataclass
from functools import cached_property
from typing import override

from skia import (Canvas, Paint, Path, Point, Rect, Size, Matrix, FontMgr, Font, Typeface)

from pytamaro.color import Color
from pytamaro.graphic import (Graphic, Empty, Rectangle, Ellipse, CircularSector,
                              Text, Compose, Pin, Rotate, Beside, Above,
                              Overlay, Triangle)
from pytamaro.localization import translate
from pytamaro.point import Point as PyTamaroPoint
from pytamaro.point_names import center, center_right, center_left, bottom_center, top_center


@dataclass(frozen=True, eq=False)
class SkiaGraphic(Graphic, ABC):
    pin_position: Point
    path: Path

    def size(self) -> Size:
        """
        Computes the size of this graphic (x and y axes spanning),
        using the bounds computed by bounds().

        :returns: graphic's size
        """
        return Size(self.bounds.width(), self.bounds.height())

    @cached_property
    def bounds(self) -> Rect:
        """
        Computes the (tight) bounds for the path (outline) of this graphic.

        :returns: a rectangle that indicates the bounds of the graphic in the 2D
                  space
        """
        return self.path.computeTightBounds()

    def zero_pixels(self) -> bool:
        """
        Returns whether this graphic has no pixels to render, because its (rounded) area is 0.

        :returns: True if the graphic has no pixels, False otherwise
        """
        return self.size().toRound().isEmpty()

    @abstractmethod
    def draw(self, canvas: Canvas):
        """
        Draws the current graphic onto the provided canvas.

        :param canvas: canvas onto which to draw
        """

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Graphic):
            return self.__hash__() == other.__hash__()
        return False

    def __hash__(self) -> int:
        return hash(self._key())

    def _key(self):
        return ((self.pin_position.fX, self.pin_position.fY),
                self.path.serialize().bytes())


@dataclass(frozen=True, eq=False)
class SkiaPrimitive(SkiaGraphic):
    """
    Represents a primitive graphic, which has a uniform color.
    Geometric shapes and text are primitive graphics.
    """
    color: Color

    def __init__(self, path: Path, color: Color, pin_position: Point = None):
        object.__setattr__(self, "color", color)
        if pin_position is None:
            bounds = path.computeTightBounds()
            pin_position = Point(bounds.width() / 2, bounds.height() / 2)
        super().__init__(pin_position, path)

    @cached_property
    def antialias(self) -> bool:
        """
        Whether the graphic should be drawn with antialiasing.
        """
        return False

    @override
    def draw(self, canvas: Canvas):
        # pylint: disable=no-member
        canvas.drawPath(self.path, Paint(Color=self.color.skia_color, AntiAlias=self.antialias))

    @override
    def _key(self):
        return super()._key(), self.color


@dataclass(frozen=True, eq=False)
class SkiaEmpty(SkiaGraphic, Empty):

    def __init__(self):
        super().__init__(Point(0, 0), Path())

    @override
    def draw(self, canvas: Canvas):
        pass

    def __repr__(self) -> str:
        return Empty.__repr__(self)


@dataclass(frozen=True, eq=False)
class SkiaRectangle(SkiaPrimitive, Rectangle):

    def __init__(self, width: float, height: float, color: Color):
        object.__setattr__(self, "width", width)
        object.__setattr__(self, "height", height)
        path = Path().addRect(Rect.MakeWH(width, height))
        super().__init__(path, color)

    def __repr__(self) -> str:
        return Rectangle.__repr__(self)


@dataclass(frozen=True, eq=False)
class SkiaEllipse(SkiaPrimitive, Ellipse):

    def __init__(self, width: float, height: float, color: Color):
        object.__setattr__(self, "width", width)
        object.__setattr__(self, "height", height)
        path = Path().addOval(Rect.MakeWH(width, height))
        super().__init__(path, color)

    def __repr__(self) -> str:
        return Ellipse.__repr__(self)


@dataclass(frozen=True, eq=False)
class SkiaCircularSector(SkiaPrimitive, CircularSector):

    def __init__(self, radius: float, angle: float, color: Color):
        object.__setattr__(self, "radius", radius)
        object.__setattr__(self, "angle", angle)
        if angle == 360:
            path = Path.Circle(radius, radius, radius)
        else:
            diameter = 2 * radius
            path = Path()
            path.moveTo(radius, radius)
            path.arcTo(Rect.MakeWH(diameter, diameter), 0, -angle, False)
            path.close()
        super().__init__(path, color, Point(radius, radius))

    def __repr__(self) -> str:
        return CircularSector.__repr__(self)


@dataclass(frozen=True, eq=False)
class SkiaTriangle(SkiaPrimitive, Triangle):

    def __init__(self, side1: float, side2: float, angle: float, color: Color):
        object.__setattr__(self, "side1", side1)
        object.__setattr__(self, "side2", side2)
        object.__setattr__(self, "angle", angle)
        third_point = Matrix.RotateDeg(-angle).mapXY(side2, 0)
        path = Path.Polygon([Point(0, 0), Point(side1, 0), third_point], isClosed=True)
        # The centroid is the average of the three vertices
        centroid = Point((side1 + third_point.x()) / 3, third_point.y() / 3)
        super().__init__(path, color, centroid)

    def __repr__(self) -> str:
        return Triangle.__repr__(self)


@dataclass(frozen=True, eq=False)
class SkiaText(SkiaPrimitive, Text):

    def __init__(self, text: str, font_name: str, text_size: float, color: Color):
        object.__setattr__(self, "text", text)
        object.__setattr__(self, "font_name", font_name)
        object.__setattr__(self, "text_size", text_size)
        if FontMgr().matchFamily(font_name).count() == 0:
            print(translate("FONT_NOT_FOUND", font_name), file=sys.stderr)
        glyphs = self.font.textToGlyphs(text)
        offsets = self.font.getXPos(glyphs)
        text_path = Path()
        for glyph, x_offset in zip(glyphs, offsets):
            path = self.font.getPath(glyph)
            if path is not None:  # some glyphs (e.g., a space) have no outline
                path.offset(x_offset, 0)
                text_path.addPath(path)
        # The pinning position is on the left (0) on the baseline (0).
        super().__init__(text_path, color, Point(0, 0))

    @cached_property
    @override
    def antialias(self) -> bool:
        return True

    @cached_property
    def font(self) -> Font:
        """
        The Skia Font used to render the text.
        """
        return Font(Typeface(self.font_name), self.text_size)

    @cached_property
    @override
    def bounds(self) -> Rect:
        """
        Computes the bounding box of the text, whose width is determined by
        Font.measureText() to account for leading and trailing glyphs with no outline.
        """
        path_bounds = super().bounds
        text_length = self.font.measureText(self.text)
        return Rect.MakeLTRB(0, path_bounds.top(), text_length, path_bounds.bottom())

    def __repr__(self) -> str:
        return Text.__repr__(self)


@dataclass(frozen=True, eq=False)
class SkiaCompose(SkiaGraphic, Compose):
    foreground: SkiaGraphic
    background: SkiaGraphic

    def __init__(self, foreground: SkiaGraphic, background: SkiaGraphic):
        object.__setattr__(self, "foreground", foreground)
        object.__setattr__(self, "background", background)
        fg_pin = self.foreground.pin_position
        bg_pin = self.background.pin_position
        pin = Point(bg_pin.x(), bg_pin.y())
        path = Path(self.background.path)
        path.addPath(self.foreground.path,
                     bg_pin.x() - fg_pin.x(), bg_pin.y() - fg_pin.y())
        super().__init__(pin, path)

    @override
    def draw(self, canvas: Canvas):
        canvas.save()
        self.background.draw(canvas)
        canvas.translate(self.background.pin_position.x() - self.foreground.pin_position.x(),
                         self.background.pin_position.y() - self.foreground.pin_position.y())
        self.foreground.draw(canvas)
        canvas.restore()

    def __repr__(self) -> str:
        return Compose.__repr__(self)


@dataclass(frozen=True, eq=False)
class SkiaPin(SkiaGraphic, Pin):
    """
    Represents the pinning of a graphic in a certain position on its bounds.
    """
    graphic: SkiaGraphic
    pinning_point: PyTamaroPoint

    def __init__(self, graphic: SkiaGraphic, pinning_point: PyTamaroPoint):
        object.__setattr__(self, "graphic", graphic)
        object.__setattr__(self, "pinning_point", pinning_point)
        bounds = graphic.bounds
        h_mapping = {
            -1.0: bounds.left(),
            0.0: bounds.centerX(),
            1.0: bounds.right()
        }
        v_mapping = {
            1.0: bounds.top(),
            0.0: bounds.centerY(),
            -1.0: bounds.bottom()
        }
        pin = Point(h_mapping[pinning_point.x], v_mapping[pinning_point.y])
        super().__init__(pin, graphic.path)

    @override
    def draw(self, canvas: Canvas):
        self.graphic.draw(canvas)

    def __repr__(self) -> str:
        return Pin.__repr__(self)


@dataclass(frozen=True, eq=False)
class SkiaRotate(SkiaGraphic, Rotate):
    graphic: SkiaGraphic

    def __init__(self, graphic: SkiaGraphic, angle: float):
        object.__setattr__(self, "graphic", graphic)
        object.__setattr__(self, "angle", angle)
        # Negated angle because RotateDeg works clockwise.
        object.__setattr__(self, "rot_matrix", Matrix.RotateDeg(-angle, graphic.pin_position))
        path = Path()
        # transform() mutates the path provided as the second argument
        graphic.path.transform(self.rot_matrix, path)  # type: ignore  # pylint: disable=no-member
        super().__init__(graphic.pin_position, path)

    @override
    def draw(self, canvas: Canvas):
        canvas.save()
        canvas.concat(self.rot_matrix)  # type: ignore  # pylint: disable=no-member
        self.graphic.draw(canvas)
        canvas.restore()

    def __repr__(self) -> str:
        return Rotate.__repr__(self)


@dataclass(frozen=True, eq=False)
class SkiaSimpleCompose(SkiaGraphic, ABC):
    """
    Represents a simple composition operation between two graphics
    (i.e., beside, above, or overlay).
    These simple compositions pin the two graphics appropriately,
    compose them normally, and then pin the result on its center.
    """

    def __init__(self, graphic1: SkiaGraphic, graphic2: SkiaGraphic,
                 point1: PyTamaroPoint, point2: PyTamaroPoint):
        composed_graphic = SkiaPin(SkiaCompose(SkiaPin(graphic1, point1),
                                               SkiaPin(graphic2, point2)), center)
        object.__setattr__(self, "composed_graphic", composed_graphic)
        super().__init__(composed_graphic.pin_position, composed_graphic.path)

    @override
    def draw(self, canvas: Canvas):
        self.composed_graphic.draw(canvas)  # type: ignore  # pylint: disable=no-member


@dataclass(frozen=True, eq=False)
class SkiaBeside(SkiaSimpleCompose, Beside):

    def __init__(self, left_graphic: SkiaGraphic, right_graphic: SkiaGraphic):
        object.__setattr__(self, "left_graphic", left_graphic)
        object.__setattr__(self, "right_graphic", right_graphic)
        super().__init__(left_graphic, right_graphic, center_right, center_left)

    def __repr__(self) -> str:
        return Beside.__repr__(self)


@dataclass(frozen=True, eq=False)
class SkiaAbove(SkiaSimpleCompose, Above):

    def __init__(self, top_graphic: SkiaGraphic, bottom_graphic: SkiaGraphic):
        object.__setattr__(self, "top_graphic", top_graphic)
        object.__setattr__(self, "bottom_graphic", bottom_graphic)
        super().__init__(top_graphic, bottom_graphic, bottom_center, top_center)

    def __repr__(self) -> str:
        return Above.__repr__(self)


@dataclass(frozen=True, eq=False)
class SkiaOverlay(SkiaSimpleCompose, Overlay):

    def __init__(self, front_graphic: SkiaGraphic, back_graphic: SkiaGraphic):
        object.__setattr__(self, "front_graphic", front_graphic)
        object.__setattr__(self, "back_graphic", back_graphic)
        super().__init__(front_graphic, back_graphic, center, center)

    def __repr__(self) -> str:
        return Overlay.__repr__(self)
