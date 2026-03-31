"""Type `Graphic`, that includes a graphic with a pinning position."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from pytamaro.color import Color
from pytamaro.localization import translate
from pytamaro.point import Point
from pytamaro.point_names import bottom_center, center, center_left, center_right, top_center
from pytamaro.utils import Spec

# ruff: noqa: D105


@dataclass(frozen=True)
class Graphic(ABC):
    """A graphic (image) with a position for pinning.

    The pinning position is used in the following operations:

    - rotation (to determine the center of rotation)
    - graphic composition (two graphics get composed aligning their pinning
      position).
    """

    @abstractmethod
    def spec_with_deps(self) -> tuple[Spec, list]:
        """Return a tuple that "declaratively specifies" this graphic.

        The first is a dictionary with this graphic's properties.
        The second member is a list of Graphics that this graphic depends on.
        See :file:`impl/ffi/specs.py` for more information.
        """


@dataclass(frozen=True)
class Empty(Graphic):
    """An empty graphic."""

    def __repr__(self) -> str:
        return f"{translate('empty_graphic')}()"

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:  # noqa: D102
        return {
            "t": "Empty",
        }, []


@dataclass(frozen=True)
class Rectangle(Graphic):
    """A rectangle."""

    width: float
    height: float
    color: Color

    def __repr__(self) -> str:
        return f"{translate('rectangle')}({self.width}, {self.height}, {self.color})"

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:  # noqa: D102
        return {
            "t": "Rectangle",
            "width": self.width,
            "height": self.height,
            "color": self.color.value_for_spec,
        }, []


@dataclass(frozen=True)
class Ellipse(Graphic):
    """An ellipse."""

    width: float
    height: float
    color: Color

    def __repr__(self) -> str:
        return f"{translate('ellipse')}({self.width}, {self.height}, {self.color})"

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:  # noqa: D102
        return {
            "t": "Ellipse",
            "width": self.width,
            "height": self.height,
            "color": self.color.value_for_spec,
        }, []


@dataclass(frozen=True)
class CircularSector(Graphic):
    """A circular sector (with an angle between 0 and 360).
    Its pinning position is the center of the circle from which it is taken.
    """  # noqa: D205

    radius: float
    angle: float
    color: Color

    def __repr__(self) -> str:
        return f"{translate('circular_sector')}({self.radius}, {self.angle}, {self.color})"

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:  # noqa: D102
        return {
            "t": "CircularSector",
            "radius": self.radius,
            "angle": self.angle,
            "color": self.color.value_for_spec,
        }, []


@dataclass(frozen=True)
class Triangle(Graphic):
    """A triangle specified using two sides and the angle between them.
    The first side extends horizontally to the right.
    The second side is rotated counterclockwise by the specified angle.

    Its pinning position is the centroid of the triangle.
    """  # noqa: D205

    side1: float
    side2: float
    angle: float
    color: Color

    def __repr__(self) -> str:
        return f"{translate('triangle')}({self.side1}, {self.side2}, {self.angle}, {self.color})"

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:  # noqa: D102
        return {
            "t": "Triangle",
            "side1": self.side1,
            "side2": self.side2,
            "angle": self.angle,
            "color": self.color.value_for_spec,
        }, []


@dataclass(frozen=True)
class Text(Graphic):
    """Graphic containing text, using a given font with a given typographic size.
    Its pinning position is horizontally aligned on the left and vertically on
    the baseline of the text.
    """  # noqa: D205

    text: str
    font_name: str
    text_size: float
    color: Color

    def __repr__(self) -> str:
        return f"{translate('text')}({self.text!r}, {self.font_name!r}, {self.text_size}, {self.color})"  # noqa: E501

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:  # noqa: D102
        return {
            "t": "Text",
            "text": self.text,
            "font_name": self.font_name,
            "text_size": self.text_size,
            "color": self.color.value_for_spec,
        }, []


@dataclass(frozen=True)
class Compose(Graphic):
    """Represents the composition of two graphics, one in the foreground and the
    other in the background, joined on their pinning positions.
    """  # noqa: D205

    foreground: Graphic
    background: Graphic

    def __repr__(self) -> str:
        return f"{translate('compose')}({self.foreground}, {self.background})"

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:  # noqa: D102
        spec: Spec = {"t": "Compose"}
        deps: list[Graphic] = []

        def optimize_child_pin(child: Graphic, key_prefix: str):
            """Optimization:
            If `child` is a `Pin`, directly add the pinning position to the spec
            of the current graphic, to skip one level in the tree.
            """  # noqa: D205
            if isinstance(child, Pin):
                spec[f"{key_prefix}_pin"] = child.pinning_point.value_for_spec
                deps.append(child.graphic)
            else:
                deps.append(child)

        optimize_child_pin(self.foreground, "fg")
        optimize_child_pin(self.background, "bg")

        return spec, deps


@dataclass(frozen=True)
class Pin(Graphic):
    """Represents the pinning of a graphic in a certain position on its bounds."""

    graphic: Graphic
    pinning_point: Point

    def __repr__(self) -> str:
        return f"{translate('pin')}({self.pinning_point}, {self.graphic})"

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:  # noqa: D102
        if isinstance(self.graphic, Compose):
            # Optimization: if our direct child is a Compose,
            # we can directly add the pinning position to the spec of the Compose,
            # to skip one level in the tree.
            child_spec, child_deps = self.graphic.spec_with_deps()
            child_spec["pin"] = self.pinning_point.value_for_spec
            return child_spec, child_deps

        # Regular case
        return {
            "t": "Pin",
            "pin": self.pinning_point.value_for_spec,
        }, [self.graphic]


@dataclass(frozen=True)
class Rotate(Graphic):
    """Represents the counterclockwise rotation of a graphic
    by a certain angle around the pinning position.
    The angle is expressed in degrees.
    """  # noqa: D205

    graphic: Graphic
    angle: float

    def __repr__(self) -> str:
        return f"{translate('rotate')}({self.angle}, {self.graphic})"

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:  # noqa: D102
        # Optimization: skip rotations by multiples of 360 degrees
        if (
            (isinstance(self.angle, float) and self.angle.is_integer())
            or isinstance(self.angle, int)
        ) and int(self.angle) % 360 == 0:
            return self.graphic.spec_with_deps()
        return {
            "t": "Rotate",
            "angle": self.angle,
        }, [self.graphic]


@dataclass(frozen=True)
class Beside(Graphic):
    """Represents the composition of two graphics one beside the other,
    vertically centered.
    """  # noqa: D205

    left_graphic: Graphic
    right_graphic: Graphic

    def __repr__(self) -> str:
        return f"{translate('beside')}({self.left_graphic}, {self.right_graphic})"

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:  # noqa: D102
        return {
            "t": "Compose",
            "fg_pin": center_right.value_for_spec,
            "bg_pin": center_left.value_for_spec,
            "pin": center.value_for_spec,
        }, [self.left_graphic, self.right_graphic]


@dataclass(frozen=True)
class Above(Graphic):
    """Represents the composition of two graphics one above the other,
    horizontally centered.
    """  # noqa: D205

    top_graphic: Graphic
    bottom_graphic: Graphic

    def __repr__(self) -> str:
        return f"{translate('above')}({self.top_graphic}, {self.bottom_graphic})"

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:  # noqa: D102
        return {
            "t": "Compose",
            "fg_pin": bottom_center.value_for_spec,
            "bg_pin": top_center.value_for_spec,
            "pin": center.value_for_spec,
        }, [self.top_graphic, self.bottom_graphic]


@dataclass(frozen=True)
class Overlay(Graphic):
    """Represents the composition of two graphics that one overlay other,
    the center of the two graphics are at the same position.
    """  # noqa: D205

    front_graphic: Graphic
    back_graphic: Graphic

    def __repr__(self) -> str:
        return f"{translate('overlay')}({self.front_graphic}, {self.back_graphic})"

    def spec_with_deps(self) -> tuple[Spec, list[Graphic]]:  # noqa: D102
        return {
            "t": "Compose",
            "fg_pin": center.value_for_spec,
            "bg_pin": center.value_for_spec,
            # When `pin` is absent, it defaults to `bg_pin`.
            # We omit it here as an optimization.
            # 'pin': center.spec,
        }, [self.front_graphic, self.back_graphic]
