"""
Type `Graphic`, that includes a graphic with a pinning position.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Self

from pytamaro.color import Color
from pytamaro.localization import translate
from pytamaro.point import Point
from pytamaro.point_names import center, center_left, center_right, bottom_center, top_center


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
    def deps_and_spec(self) -> tuple[list[Self], dict[str, Any]]:
        """
        Create specs to render this graphic
        """


@dataclass(frozen=True, eq=False)
class Empty(Graphic):
    """
    An empty graphic.
    """

    def __repr__(self) -> str:
        return f"{translate('empty_graphic')}()"

    def deps_and_spec(self) -> tuple[list[Graphic], dict[str, Any]]:
        return [], {
            'type': 'Empty',
        }


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

    def deps_and_spec(self) -> tuple[list[Graphic], dict[str, Any]]:
        return [], {
            'type': 'Rectangle',
            'width': self.width,
            'height': self.height,
            'color': self.color.as_dict,
        }


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

    def deps_and_spec(self) -> tuple[list[Graphic], dict[str, Any]]:
        return [], {
            'type': 'Ellipse',
            'width': self.width,
            'height': self.height,
            'color': self.color.as_dict,
        }


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

    def deps_and_spec(self) -> tuple[list[Graphic], dict[str, Any]]:
        return [], {
            'type': 'CircularSector',
            'radius': self.radius,
            'angle': self.angle,
            'color': self.color.as_dict,
        }


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

    def deps_and_spec(self) -> tuple[list[Graphic], dict[str, Any]]:
        return [], {
            'type': 'Triangle',
            'side1': self.side1,
            'side2': self.side2,
            'angle': self.angle,
            'color': self.color.as_dict
        }


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

    def deps_and_spec(self) -> tuple[list[Graphic], dict[str, Any]]:
        return [], {
            'type': 'Text',
            'text': self.text,
            'font_name': self.font_name,
            'text_size': self.text_size,
            'color': self.color.as_dict
        }


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

    def deps_and_spec(self) -> tuple[list[Graphic], dict[str, Any]]:
        deps: list[Graphic] = []
        spec: dict[str, Any] = {'type': 'Compose'}

        def flat_child(child: Graphic, key: str):
            """
            Inline pinning position of children of type Pin to flatten the tree.
            """
            if isinstance(child, Pin):
                spec[f'{key}_pin'] = child.pinning_point.as_dict
                # Also flatten nested pins
                while isinstance(child, Pin):
                    child = child.graphic
            deps.append(child)

        flat_child(self.foreground, 'foreground')
        flat_child(self.background, 'background')

        return deps, spec


@dataclass(frozen=True, eq=False)
class Pin(Graphic):
    """
    Represents the pinning of a graphic in a certain position on its bounds.
    """
    graphic: Graphic
    pinning_point: Point

    def __repr__(self) -> str:
        return f"{translate('pin')}({self.pinning_point}, {self.graphic})"

    def deps_and_spec(self) -> tuple[list[Graphic], dict[str, Any]]:
        # Flatten pin(pin(...))
        child_graphic = self.graphic
        while isinstance(child_graphic, Pin):
            # pylint: disable=no-member
            child_graphic = child_graphic.graphic
        return (
            [child_graphic],
            {
                'type': 'Pin',
                'pinning_point': self.pinning_point.as_dict,
            }
        )


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

    def deps_and_spec(self) -> tuple[list[Graphic], dict[str, Any]]:
        # Optimize away %360-deg rotations
        if self.angle.is_integer() and int(self.angle) % 360 == 0:
            return self.graphic.deps_and_spec()
        return [self.graphic], {
            'type': 'Rotate',
            'angle': self.angle,
        }


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

    def deps_and_spec(self) -> tuple[list[Graphic], dict[str, Any]]:
        return (
            [self.left_graphic, self.right_graphic],
            {
                'type': 'Compose',
                'foreground_pin': center_right.as_dict,
                'background_pin': center_left.as_dict,
                'own_pin': center.as_dict,
            },
        )


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

    def deps_and_spec(self) -> tuple[list[Graphic], dict[str, Any]]:
        return (
            [self.top_graphic, self.bottom_graphic],
            {
                'type': 'Compose',
                'foreground_pin': bottom_center.as_dict,
                'background_pin': top_center.as_dict,
                'own_pin': center.as_dict,
            },
        )


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

    def deps_and_spec(self) -> tuple[list[Graphic], dict[str, Any]]:
        return (
            [self.front_graphic, self.back_graphic],
            {
                'type': 'Compose',
                'foreground_pin': center.as_dict,
                'background_pin': center.as_dict,
            },
        )
