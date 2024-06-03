"""
Type `Graphic`, that includes a graphic with a pinning position.
"""

import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass

from skia import (Canvas, Font, FontMgr, Matrix, Paint, Path, Point, Rect,
                  Size, Typeface)

from pytamaro.color import Color
from pytamaro.localization import translate
from pytamaro.point import Point as PyTamaroPoint
from pytamaro.point_names import (bottom_center, center, center_left,
                                  center_right, top_center)


@dataclass(frozen=True, eq=False)
class Graphic(ABC):
    """
    A graphic (image) with a position for pinning.

    The pinning position is used in the following operations:

    - rotation (to determine the center of rotation)
    - graphic composition (two graphics get composed aligning their pinning
      position).
    """
    pin_position: Point
    path: Path

    def size(self) -> Size:
        """
        Computes the size of this graphic (x and y axes spanning),
        using the bounds computed by bounds().

        :returns: graphic's size
        """
        bounds = self.bounds()
        return Size(bounds.width(), bounds.height())

    def bounds(self) -> Rect:
        """
        Computes the (tight) bounds for the path (outline) of this graphic.

        :returns: a rectangle that indicates the bounds of the graphic in the 2D
                  space
        """
        return self.path.computeTightBounds()

    @abstractmethod
    def draw(self, canvas: Canvas):
        """
        Draws the current graphic onto the provided canvas.

        :param canvas: canvas onto which to draw
        """

    def empty_area(self) -> bool:
        """
        Returns whether this graphic has an empty area (width or height 0) or
        not.

        :returns: True if the graphic has an empty area, False otherwise
        """
        return self.size().isEmpty()

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
class Primitive(Graphic):
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
        paint = Paint(Color=color.skia_color, AntiAlias=True)
        object.__setattr__(self, "paint", paint)

    def draw(self, canvas: Canvas):
        canvas.drawPath(self.path, self.paint)  # type: ignore  # pylint: disable=no-member

    def _key(self):
        return super()._key(), self.color


@dataclass(frozen=True, eq=False)
class Empty(Graphic):
    """
    An empty graphic.
    """

    def __init__(self):
        super().__init__(Point(0, 0), Path())

    def draw(self, canvas: Canvas):
        pass

    def __repr__(self) -> str:
        return f"{translate('empty_graphic')}()"


@dataclass(frozen=True, eq=False)
class Rectangle(Primitive):
    """
    A rectangle.
    """
    width: float
    height: float

    def __init__(self, width: float, height: float, color: Color):
        object.__setattr__(self, "width", width)
        object.__setattr__(self, "height", height)
        path = Path().addRect(Rect.MakeWH(width, height))
        super().__init__(path, color)

    def __repr__(self) -> str:
        return f"{translate('rectangle')}({self.width}, {self.height}, {self.color})"


@dataclass(frozen=True, eq=False)
class Ellipse(Primitive):
    """
    An ellipse.
    """
    width: float
    height: float

    def __init__(self, width: float, height: float, color: Color):
        object.__setattr__(self, "width", width)
        object.__setattr__(self, "height", height)
        path = Path().addOval(Rect.MakeWH(width, height))
        super().__init__(path, color)

    def __repr__(self) -> str:
        return f"{translate('ellipse')}({self.width}, {self.height}, {self.color})"


@dataclass(frozen=True, eq=False)
class CircularSector(Primitive):
    """
    A circular sector (with an angle between 0 and 360).
    Its pinning position is the center of the circle from which it is taken.
    """
    radius: float
    angle: float

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
        return f"{translate('circular_sector')}({self.radius}, {self.angle}, {self.color})"


@dataclass(frozen=True, eq=False)
class Triangle(Primitive):
    """
    A triangle specified using two sides and the angle between them.
    The first side extends horizontally to the right.
    The second side is rotated counterclockwise by the specified angle.

    Its pinning position is the centroid of the triangle.
    """
    side1: float
    side2: float
    angle: float

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
        return f"{translate('triangle')}({self.side1}, {self.side2}, {self.angle}, {self.color})"


@dataclass(frozen=True, eq=False)
class Text(Primitive):
    """
    Graphic containing text, using a given font with a given typographic size.
    Its pinning position is horizontally aligned on the left and vertically on
    the baseline of the text.
    """
    text: str
    font_name: str
    text_size: float

    def __init__(self, text: str, font_name: str, text_size: float, color: Color):
        object.__setattr__(self, "text", text)
        object.__setattr__(self, "font_name", font_name)
        object.__setattr__(self, "text_size", text_size)
        if FontMgr().matchFamily(font_name).count() == 0:
            print(translate("FONT_NOT_FOUND", font_name), file=sys.stderr)
        font = Font(Typeface(font_name), text_size)
        glyphs = font.textToGlyphs(text)
        offsets = font.getXPos(glyphs)
        text_path = Path()
        for glyph, x_offset in zip(glyphs, offsets):
            path = font.getPath(glyph)
            # Some glyphs (e.g., the space) have no outline
            if path is not None:
                path.offset(x_offset, 0)
                text_path.addPath(path)

        # The pinning position is at baseline level (0) on the very left (which
        # might be slightly after 0, given that the bounding box is computed
        # very tightly around the glyphs, cutting some space before the first
        # one).
        bounds = text_path.computeTightBounds()
        super().__init__(text_path, color, Point(bounds.left(), 0))

    def __repr__(self) -> str:
        return f"{translate('text')}({self.text!r}, {self.font_name!r}, {self.text_size}, {self.color})"  # pylint: disable=line-too-long


@dataclass(frozen=True, eq=False)
class Compose(Graphic):
    """
    Represents the composition of two graphics, one in the foreground and the
    other in the background, joined on their pinning positions.
    """
    foreground: Graphic
    background: Graphic

    def __init__(self, foreground: Graphic, background: Graphic):
        object.__setattr__(self, "foreground", foreground)
        object.__setattr__(self, "background", background)
        fg_pin = self.foreground.pin_position
        bg_pin = self.background.pin_position
        pin = Point(bg_pin.x(), bg_pin.y())
        path = Path(self.background.path)
        path.addPath(self.foreground.path,
                     bg_pin.x() - fg_pin.x(), bg_pin.y() - fg_pin.y())
        super().__init__(pin, path)

    def draw(self, canvas: Canvas):
        canvas.save()
        self.background.draw(canvas)
        canvas.translate(self.background.pin_position.x() - self.foreground.pin_position.x(),
                         self.background.pin_position.y() - self.foreground.pin_position.y())
        self.foreground.draw(canvas)
        canvas.restore()

    def __repr__(self) -> str:
        return f"{translate('compose')}({self.foreground}, {self.background})"


@dataclass(frozen=True, eq=False)
class Pin(Graphic):
    """
    Represents the pinning of a graphic in a certain position on its bounds.
    """
    graphic: Graphic
    pinning_point: PyTamaroPoint

    def __init__(self, graphic: Graphic, pinning_point: PyTamaroPoint):
        object.__setattr__(self, "graphic", graphic)
        object.__setattr__(self, "pinning_point", pinning_point)
        bounds = graphic.bounds()
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

    def draw(self, canvas: Canvas):
        self.graphic.draw(canvas)

    def __repr__(self) -> str:
        return f"{translate('pin')}({self.pinning_point}, {self.graphic})"


@dataclass(frozen=True, eq=False)
class Rotate(Graphic):
    """
    Represents the counterclockwise rotation of a graphic
    by a certain angle around the pinning position.
    The angle is expressed in degrees.
    """
    graphic: Graphic
    angle: float

    def __init__(self, graphic: Graphic, angle: float):
        object.__setattr__(self, "graphic", graphic)
        object.__setattr__(self, "angle", angle)
        # Negated angle because RotateDeg works clockwise.
        object.__setattr__(self, "rot_matrix", Matrix.RotateDeg(-angle, graphic.pin_position))
        path = Path()
        # transform() mutates the path provided as the second argument
        graphic.path.transform(self.rot_matrix, path)  # type: ignore  # pylint: disable=no-member
        super().__init__(graphic.pin_position, path)

    def draw(self, canvas: Canvas):
        canvas.save()
        canvas.concat(self.rot_matrix)  # type: ignore  # pylint: disable=no-member
        self.graphic.draw(canvas)
        canvas.restore()

    def __repr__(self) -> str:
        return f"{translate('rotate')}({self.angle}, {self.graphic})"


@dataclass(frozen=True, eq=False)
class SimpleCompose(Graphic):
    """
    Represents a simple composition operation between two graphics
    (i.e., beside, above, or overlay).
    These simple compositions pin the two graphics appropriately,
    compose them normally, and then pin the result on its center.
    """

    def __init__(self, graphic1: Graphic, graphic2: Graphic,
                 point1: PyTamaroPoint, point2: PyTamaroPoint):
        composed_graphic = Pin(Compose(Pin(graphic1, point1),
                                       Pin(graphic2, point2)), center)
        object.__setattr__(self, "composed_graphic", composed_graphic)
        super().__init__(composed_graphic.pin_position, composed_graphic.path)

    def draw(self, canvas: Canvas):
        self.composed_graphic.draw(canvas)  # type: ignore  # pylint: disable=no-member


@dataclass(frozen=True, eq=False)
class Beside(SimpleCompose):
    """
    Represents the composition of two graphics one beside the other,
    vertically centered.
    """
    left_graphic: Graphic
    right_graphic: Graphic

    def __init__(self, left_graphic: Graphic, right_graphic: Graphic):
        object.__setattr__(self, "left_graphic", left_graphic)
        object.__setattr__(self, "right_graphic", right_graphic)
        super().__init__(left_graphic, right_graphic, center_right, center_left)

    def __repr__(self) -> str:
        return f"{translate('beside')}({self.left_graphic}, {self.right_graphic})"


@dataclass(frozen=True, eq=False)
class Above(SimpleCompose):
    """
    Represents the composition of two graphics one above the other,
    horizontally centered.
    """
    top_graphic: Graphic
    bottom_graphic: Graphic

    def __init__(self, top_graphic: Graphic, bottom_graphic: Graphic):
        object.__setattr__(self, "top_graphic", top_graphic)
        object.__setattr__(self, "bottom_graphic", bottom_graphic)
        super().__init__(top_graphic, bottom_graphic, bottom_center, top_center)

    def __repr__(self) -> str:
        return f"{translate('above')}({self.top_graphic}, {self.bottom_graphic})"


@dataclass(frozen=True, eq=False)
class Overlay(SimpleCompose):
    """
    Represents the composition of two graphics that one overlay other,
    the center of the two graphics are at the same position
    """
    front_graphic: Graphic
    back_graphic: Graphic

    def __init__(self, front_graphic: Graphic, back_graphic: Graphic):
        object.__setattr__(self, "front_graphic", front_graphic)
        object.__setattr__(self, "back_graphic", back_graphic)
        super().__init__(front_graphic, back_graphic, center, center)

    def __repr__(self) -> str:
        return f"{translate('overlay')}({self.front_graphic}, {self.back_graphic})"
