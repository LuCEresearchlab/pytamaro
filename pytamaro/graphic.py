"""
Graphic class, which wraps a Pillow image with a position for pinning.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from itertools import accumulate
from math import sqrt
from typing import List

from skia import (Canvas, Font, Image, Matrix, Paint, Path, Point, Rect, Size,
                  Surface, Typeface)

from pytamaro.color import Color
from pytamaro.color_names import black

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
    def render(self, canvas: Canvas):
        """
        Renders the current graphic onto the provided canvas.

        :param canvas: canvas onto which to render
        """

    def is_empty_graphic(self) -> bool:  # pylint: disable=no-self-use
        """
        Returns whether this graphic is empty or not.

        :returns: True if the graphic is empty, False otherwise
        """
        return False

    def as_image(self) -> Image:
        """
        Renders this graphic as an image.

        The image has the minimal size required to fit the graphic.

        :returns: an image with the rendered graphic
        """
        int_size = self.size().toCeil()
        surface = Surface(int_size.width(), int_size.height())
        with surface as canvas:
            bounds = self.bounds()
            canvas.translate(-bounds.left(), -bounds.top())
            self.render(canvas)
        return surface.makeImageSnapshot()

    def _key(self) -> List:
        """
        Returns the fields relevant for __eq__ and __hash__ as a list.
        The resulting list must contain comparable and hashable values.
        For this reason, we carefully manage the case with the empty image.

        :returns: a list with values relevant for equality
        """
        if self.is_empty_graphic():
            return [None]

        bitmap = self.as_image().bitmap()
        pixels = [bitmap.getColor(x, y)
                  for y in range(bitmap.height()) for x in range(bitmap.width())]
        return [tuple(pixels)]

    def __eq__(self, other: object) -> bool:
        """
        Compares a graphic with another graphic.
        Two graphics are considered equal if they are both empty or if they
        have exactly the same content when rendered (pixel by pixel)/

        :returns: True if the two graphics are considered equal, False
                  otherwise
        """
        if not isinstance(other, Graphic):
            return NotImplemented
        return self._key() == other._key()

    def __hash__(self) -> int:
        """
        Computes the hash of this graphic, relying on _key() and the built-in
        hash().

        :returns hash for this graphic
        """
        return hash(tuple(self._key()))


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

    def render(self, canvas: Canvas):
        canvas.drawPath(self.path, self.paint)


class Empty(Primitive):
    """
    An empty graphic.
    """
    def __init__(self):
        super().__init__(Path(), black)

    def is_empty_graphic(self) -> bool:
        return True


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
    A circular sector (with an angle between 1 and 359).
    """
    def __init__(self, radius: float, angle: float, color: Color):
        circle = Rect.MakeWH(2 * radius, 2 * radius)
        path = Path()
        path.moveTo(radius, radius)
        path.arcTo(circle, 0, angle, False)
        path.close()
        super().__init__(path, color)


class Triangle(Primitive):
    """
    An upwards-pointing equilateral triangle.
    """
    def __init__(self, side: float, color: Color):
        height = side * sqrt(3) / 2
        points = [Point(0, 0), Point(-side/2, height), Point(side/2, height)]
        path = Path().addPoly(points, close=True)
        super().__init__(path, color)


class Text(Primitive):
    """
    Graphic containing text, using a given font with a given typographic size.
    """
    def __init__(self, text: str, font_name: str, size: float, color: Color):
        font = Font(Typeface(font_name), size)
        glyphs = font.textToGlyphs(text)
        paths = font.getPaths(glyphs)
        offsets = [0] + list(accumulate(font.getWidths(glyphs)))
        text_path = Path()
        for path, x_offset in zip(paths, offsets):
            path.offset(x_offset, 0)
            text_path.addPath(path)
        super().__init__(text_path, color)


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

    def render(self, canvas: Canvas):
        canvas.save()
        self.background.render(canvas)
        canvas.translate(self.background.pin_position.x() - self.foreground.pin_position.x(),
                         self.background.pin_position.y() - self.foreground.pin_position.y())
        self.foreground.render(canvas)
        canvas.restore()


class Pin(Graphic):
    """
    Represents the pinning of a graphic in a certain position on its bounds.
    """
    def __init__(self, graphic: Graphic, horizontal_place: str, vertical_place: str):
        self.graphic = graphic
        bounds = self.graphic.bounds()
        h_mapping = {
            "left": bounds.left(),
            "middle": bounds.centerX(),
            "right": bounds.right()
        }
        v_mapping = {
            "top": bounds.top(),
            "middle": bounds.centerY(),
            "bottom": bounds.bottom()
        }
        self.set_pin_position(
            h_mapping[horizontal_place], v_mapping[vertical_place])
        self.path = Path(self.graphic.path)

    def render(self, canvas: Canvas):
        self.graphic.render(canvas)


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

    def render(self, canvas: Canvas):
        canvas.save()
        canvas.concat(self.rot_matrix)
        self.graphic.render(canvas)
        canvas.restore()
