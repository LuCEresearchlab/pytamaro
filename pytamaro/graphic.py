"""
Type `Graphic`, that includes a graphic with a pinning position.
"""

from abc import ABC
from dataclasses import dataclass, field

from pytamaro.color import Color
from pytamaro.localization import translate
from pytamaro.point import Point


@dataclass(frozen=True, eq=False)
class Graphic(ABC):
    """
    A graphic (image) with a position for pinning.

    The pinning position is used in the following operations:

    - rotation (to determine the center of rotation)
    - graphic composition (two graphics get composed aligning their pinning
      position).
    """

    type: str = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, "type", self.__class__.__name__)


@dataclass(frozen=True, eq=False)
class Empty(Graphic):
    """
    An empty graphic.
    """

    def __repr__(self) -> str:
        return f"{translate('empty_graphic')}()"


@dataclass(frozen=True, eq=False)
class Rectangle(Graphic):
    """
    A rectangle.
    """
    width: float
    height: float
    color: Color

    def __repr__(self) -> str:
        return f"{translate('rectangle')}({self.width}, {self.height}, {self.color})"


@dataclass(frozen=True, eq=False)
class Ellipse(Graphic):
    """
    An ellipse.
    """
    width: float
    height: float
    color: Color

    def __repr__(self) -> str:
        return f"{translate('ellipse')}({self.width}, {self.height}, {self.color})"


@dataclass(frozen=True, eq=False)
class CircularSector(Graphic):
    """
    A circular sector (with an angle between 0 and 360).
    Its pinning position is the center of the circle from which it is taken.
    """
    radius: float
    angle: float
    color: Color

    def __repr__(self) -> str:
        return f"{translate('circular_sector')}({self.radius}, {self.angle}, {self.color})"


@dataclass(frozen=True, eq=False)
class Triangle(Graphic):
    """
    A triangle specified using two sides and the angle between them.
    The first side extends horizontally to the right.
    The second side is rotated counterclockwise by the specified angle.

    Its pinning position is the centroid of the triangle.
    """
    side1: float
    side2: float
    angle: float
    color: Color

    def __repr__(self) -> str:
        return f"{translate('triangle')}({self.side1}, {self.side2}, {self.angle}, {self.color})"


@dataclass(frozen=True, eq=False)
class Text(Graphic):
    """
    Graphic containing text, using a given font with a given typographic size.
    Its pinning position is horizontally aligned on the left and vertically on
    the baseline of the text.
    """
    text: str
    font_name: str
    text_size: float
    color: Color

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

    def __repr__(self) -> str:
        return f"{translate('compose')}({self.foreground}, {self.background})"


@dataclass(frozen=True, eq=False)
class Pin(Graphic):
    """
    Represents the pinning of a graphic in a certain position on its bounds.
    """
    graphic: Graphic
    pinning_point: Point

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

    def __repr__(self) -> str:
        return f"{translate('rotate')}({self.angle}, {self.graphic})"


@dataclass(frozen=True, eq=False)
class Beside(Graphic):
    """
    Represents the composition of two graphics one beside the other,
    vertically centered.
    """
    left_graphic: Graphic
    right_graphic: Graphic

    def __repr__(self) -> str:
        return f"{translate('beside')}({self.left_graphic}, {self.right_graphic})"


@dataclass(frozen=True, eq=False)
class Above(Graphic):
    """
    Represents the composition of two graphics one above the other,
    horizontally centered.
    """
    top_graphic: Graphic
    bottom_graphic: Graphic

    def __repr__(self) -> str:
        return f"{translate('above')}({self.top_graphic}, {self.bottom_graphic})"


@dataclass(frozen=True, eq=False)
class Overlay(Graphic):
    """
    Represents the composition of two graphics that one overlay other,
    the center of the two graphics are at the same position
    """
    front_graphic: Graphic
    back_graphic: Graphic

    def __repr__(self) -> str:
        return f"{translate('overlay')}({self.front_graphic}, {self.back_graphic})"
