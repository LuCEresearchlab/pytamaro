"""
Type `Graphic`, that includes a graphic with a pinning position.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from typing import override, Any

from pytamaro.color import Color
from pytamaro.localization import translate
from pytamaro.point import Point
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

    @abstractmethod
    def as_dict(self) -> dict[str, int | float | dict[str, Any] | str]:
        """
        Produce a dictionary-based representation of this graphic.

        :meta private:
        """


@dataclass(frozen=True, eq=False)
class Empty(Graphic):
    """
    An empty graphic.
    """

    @override
    def as_dict(self) -> dict[str, str]:
        return {
            "type": "empty",
        }

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

    @override
    def as_dict(self) -> dict[str, float | str | dict[str, int | float]]:
        return {
            "type": "rectangle",
            "width": self.width,
            "height": self.height,
            "color": asdict(self.color),
        }

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

    @override
    def as_dict(self) -> dict[str, float | str | dict[str, int | float]]:
        return {
            "type": "ellipse",
            "width": self.width,
            "height": self.height,
            "color": asdict(self.color),
        }

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

    @override
    def as_dict(self) -> dict[str, float | str | dict[str, int | float]]:
        return {
            "type": "circular_sector",
            "radius": self.radius,
            "angle": self.angle,
            "color": asdict(self.color),
        }

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

    def as_dict(self) -> dict[str, str | float | dict[str, int | float]]:
        return {
            "type": "triangle",
            "side1": self.side1,
            "side2": self.side2,
            "angle": self.angle,
            "color": asdict(self.color),
        }

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

    def as_dict(self) -> dict[str, str | float | dict[str, int | float]]:
        return {
            "type": "text",
            "text": self.text,
            "font_name": self.font_name,
            "text_size": self.text_size,
            "color": asdict(self.color),
        }

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

    def as_dict(self) -> dict[str, str | dict[str, Any]]:
        return {
            "type": "compose",
            "foreground": self.foreground.as_dict(),
            "background": self.background.as_dict(),
        }

    def __repr__(self) -> str:
        return f"{translate('compose')}({self.foreground}, {self.background})"


@dataclass(frozen=True, eq=False)
class Pin(Graphic):
    """
    Represents the pinning of a graphic in a certain position on its bounds.
    """
    graphic: Graphic
    pinning_point: Point

    def as_dict(self) -> dict[str, str | dict[str, Any]]:
        return {
            "type": "pin",
            "graphic": self.graphic.as_dict(),
            "pinning_point": asdict(self.pinning_point),
        }

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

    def as_dict(self) -> dict[str, str | dict[str, Any] | float]:
        return {
            "type": "rotate",
            "graphic": self.graphic.as_dict(),
            "angle": self.angle,
        }

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

    def as_dict(self) -> dict[str, str | dict[str, Any]]:
        return Pin(
            Compose(Pin(self.left_graphic, center_right),
                    Pin(self.right_graphic, center_left)),
            center
        ).as_dict()

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

    def as_dict(self) -> dict[str, str | dict[str, Any]]:
        return Pin(
            Compose(Pin(self.top_graphic, bottom_center),
                    Pin(self.bottom_graphic, top_center)),
            center
        ).as_dict()

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

    def as_dict(self) -> dict[str, str | dict[str, Any]]:
        return Pin(
            Compose(Pin(self.front_graphic, center),
                    Pin(self.back_graphic, center)),
            center
        ).as_dict()

    def __repr__(self) -> str:
        return f"{translate('overlay')}({self.front_graphic}, {self.back_graphic})"
