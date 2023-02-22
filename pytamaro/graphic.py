"""
Type `Graphic`, that includes a graphic with a pinning position.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from skia import (Canvas, Font, Matrix, Paint, Path, Point, Rect, Size,
                  Typeface)

from pytamaro.color import Color
from pytamaro.point import Point as PyTamaroPoint

# pylint: disable=super-init-not-called


@dataclass
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

    def set_pin_position(self, x: float, y: float):  # pylint: disable=invalid-name
        """
        Changes the pinning position of this graphic.

        :param x: x coordinate
        :param y: y coordinate
        """
        self.pin_position = Point(x, y)

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

    def __hash__(self) -> int:
        return hash(self._key())

    def _key(self):
        return ((self.pin_position.fX, self.pin_position.fY),
                self.path.serialize().bytes())


class Primitive(Graphic):
    """
    Represents a primitive graphic, which has a path and a uniform color.
    Geometric shapes and text are primitive graphics.
    """
    def __init__(self, path: Path, color: Color):
        self.path = path
        self.paint = Paint(color.color)
        bounds = self.path.computeTightBounds()
        self.set_pin_position(bounds.width() / 2, bounds.height() / 2)

    def draw(self, canvas: Canvas):
        canvas.drawPath(self.path, self.paint)

    def _key(self):
        return (super()._key(), self.paint.getHash())


class Empty(Graphic):
    """
    An empty graphic.
    """
    def __init__(self):
        super().__init__(Point(0, 0), Path())

    def draw(self, canvas: Canvas):
        pass


class Rectangle(Primitive):
    """
    A rectangle.
    """
    def __init__(self, width: float, height: float, color: Color):
        path = Path().addRect(Rect.MakeWH(width, height))
        super().__init__(path, color)


class Ellipse(Primitive):
    """
    An ellipse.
    """
    def __init__(self, width: float, height: float, color: Color):
        path = Path().addOval(Rect.MakeWH(width, height))
        super().__init__(path, color)


class CircularSector(Primitive):
    """
    A circular sector (with an angle between 0 and 360).
    Its pinning position is the center of the circle from which it is taken.
    """
    def __init__(self, radius: float, angle: float, color: Color):
        if angle == 360:
            path = Path.Circle(0, 0, radius)
        else:
            diameter = 2 * radius
            path = Path()
            path.moveTo(radius, radius)
            path.arcTo(Rect.MakeWH(diameter, diameter), 0, -angle, False)
            path.close()
        super().__init__(path, color)
        self.set_pin_position(radius, radius)


class Triangle(Primitive):
    """
    A triangle specified using two sides and the angle between them.
    The first side extends horizontally to the right.
    The second side is rotated counterclockwise by the specified angle.

    Its pinning position is the centroid of the triangle.
    """
    def __init__(self, side1: float, side2: float, angle: float, color: Color):
        third_point = Matrix.RotateDeg(-angle).mapXY(side2, 0)
        path = Path.Polygon([Point(0, 0), Point(side1, 0), third_point], isClosed=True)
        super().__init__(path, color)
        # The centroid is the average of the three vertices
        centroid = Point((side1 + third_point.x()) / 3, third_point.y() / 3)
        self.pin_position = centroid


class Text(Primitive):
    """
    Graphic containing text, using a given font with a given typographic size.
    Its pinning position is horizontally aligned on the left and vertically on
    the baseline of the text.
    """
    def __init__(self, text: str, font_name: str, size: float, color: Color):
        font = Font(Typeface(font_name), size)
        glyphs = font.textToGlyphs(text)
        offsets = font.getXPos(glyphs)
        text_path = Path()
        for glyph, x_offset in zip(glyphs, offsets):
            path = font.getPath(glyph)
            # Some glyphs (e.g., the space) have no outline
            if path is not None:
                path.offset(x_offset, 0)
                text_path.addPath(path)

        super().__init__(text_path, color)
        # Set the pinning position at baseline level (0) on the very left (which
        # might be slightly after 0, given that the bounding box is computed
        # very tightly around the glyphs, cutting some space before the first
        # one).
        self.set_pin_position(self.bounds().left(), 0)


class Compose(Graphic):
    """
    Represents the composition of two graphics, one in the foreground and the
    other in the background, joined on their pinning positions.
    """
    def __init__(self, foreground: Graphic, background: Graphic):
        self.foreground = foreground
        self.background = background
        fg_pin = self.foreground.pin_position
        bg_pin = self.background.pin_position
        self.set_pin_position(bg_pin.x(), bg_pin.y())
        self.path = Path(self.background.path)
        self.path.addPath(self.foreground.path,
                          bg_pin.x() - fg_pin.x(), bg_pin.y() - fg_pin.y())

    def draw(self, canvas: Canvas):
        canvas.save()
        self.background.draw(canvas)
        canvas.translate(self.background.pin_position.x() - self.foreground.pin_position.x(),
                         self.background.pin_position.y() - self.foreground.pin_position.y())
        self.foreground.draw(canvas)
        canvas.restore()


class Pin(Graphic):
    """
    Represents the pinning of a graphic in a certain position on its bounds.
    """
    def __init__(self, graphic: Graphic, pinning_point: PyTamaroPoint):
        self.graphic = graphic
        bounds = self.graphic.bounds()
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
        self.set_pin_position(
            h_mapping[pinning_point.x], v_mapping[pinning_point.y])
        self.path = Path(self.graphic.path)

    def draw(self, canvas: Canvas):
        self.graphic.draw(canvas)


class Rotate(Graphic):
    """
    Represents the rotation of a graphic by a certain angle clockwise.
    """
    def __init__(self, graphic: Graphic, deg: float):
        self.graphic = graphic
        self.rot_matrix = Matrix.RotateDeg(deg, self.graphic.pin_position)
        self.path = Path()
        self.graphic.path.transform(self.rot_matrix, self.path)  # updates self.path
        self.pin_position = graphic.pin_position

    def draw(self, canvas: Canvas):
        canvas.save()
        canvas.concat(self.rot_matrix)
        self.graphic.draw(canvas)
        canvas.restore()
