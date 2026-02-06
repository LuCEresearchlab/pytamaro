"""
Type `Graphic`, that includes a graphic with a pinning position.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Self

from pytamaro.color import Color
from pytamaro.localization import translate
from pytamaro.point import Point
from pytamaro.point_names import center, center_left, center_right, bottom_center, top_center
from pytamaro.utils import Spec


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
    def spec_with_deps(self) -> tuple[Spec, list[Self]]:
        """
        Returns a tuple that "declaratively specifies" this graphic.
        The first is a dictionary with this graphic's properties.
        The second member is a list of Graphics that this graphic depends on.
        See :file:`impl/ffi/specs.py` for more information.
        """


@dataclass(frozen=True, eq=False)
class Empty(Graphic):
    """
    An empty graphic.
    """

    def __repr__(self) -> str:
        return f"{translate('empty_graphic')}()"

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:
        return {
            't': 'Empty',
        }, []


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

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:
        return {
            't': 'Rectangle',
            'width': self.width,
            'height': self.height,
            'color': self.color.spec,
        }, []


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

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:
        return {
            't': 'Ellipse',
            'width': self.width,
            'height': self.height,
            'color': self.color.spec,
        }, []


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

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:
        return {
            't': 'CircularSector',
            'radius': self.radius,
            'angle': self.angle,
            'color': self.color.spec,
        }, []


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

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:
        return {
            't': 'Triangle',
            'side1': self.side1,
            'side2': self.side2,
            'angle': self.angle,
            'color': self.color.spec
        }, []


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

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:
        return {
            't': 'Text',
            'text': self.text,
            'font_name': self.font_name,
            'text_size': self.text_size,
            'color': self.color.spec,
        }, []


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

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:
        spec: Spec = {'t': 'Compose'}
        deps: list[Graphic] = []

        def optimize_child_pin(child: Graphic, key_prefix: str):
            """
            Optimization:
            If `child` is a `Pin`, directly add the pinning position to the spec
            of the current graphic, to skip one level in the tree.
            """
            if isinstance(child, Pin):
                spec[f'{key_prefix}_pin'] = child.pinning_point.spec
                deps.append(child.graphic)
            else:
                deps.append(child)

        optimize_child_pin(self.foreground, 'fg')
        optimize_child_pin(self.background, 'bg')

        return spec, deps


@dataclass(frozen=True, eq=False)
class Pin(Graphic):
    """
    Represents the pinning of a graphic in a certain position on its bounds.
    """
    graphic: Graphic
    pinning_point: Point

    def __repr__(self) -> str:
        return f"{translate('pin')}({self.pinning_point}, {self.graphic})"

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:
        return {
            't': 'Pin',
            'pin': self.pinning_point.spec,
        }, [self.graphic]


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

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:
        # Optimization: skip rotations by multiples of 360 degrees
        if self.angle.is_integer() and int(self.angle) % 360 == 0:
            return self.graphic.spec_with_deps()
        return {
            't': 'Rotate',
            'angle': self.angle,
        }, [self.graphic]


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

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:
        return {
            't': 'Compose',
            'fg_pin': center_right.spec,
            'bg_pin': center_left.spec,
            'pin': center.spec,
        }, [self.left_graphic, self.right_graphic]


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

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:
        return {
            't': 'Compose',
            'fg_pin': bottom_center.spec,
            'bg_pin': top_center.spec,
            'pin': center.spec,
        }, [self.top_graphic, self.bottom_graphic]


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

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:
        return {
            't': 'Compose',
            'fg_pin': center.spec,
            'bg_pin': center.spec,
            # When `pin` is absent, it defaults to `bg_pin`.
            # We omit it here as an optimization.
            # 'pin': center.spec,
        }, [self.front_graphic, self.back_graphic]
