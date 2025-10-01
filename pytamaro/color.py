"""
`Color` type, functions to produce colors, and constants for important colors.
"""

from dataclasses import dataclass

from pytamaro.localization import translate
from pytamaro.utils import has_skia


@dataclass(frozen=True)
class Color:
    """
    Represents a color.
    A color also has a degree of opacity,
    from completely transparent (like the color `transparent`)
    to completely opaque (like the color `red`).
    """
    red: int      # [0-255]
    green: int    # [0-255]
    blue: int     # [0-255]
    alpha: float  # [0-1]

    def __init__(self, red: int, green: int, blue: int, alpha: float):
        object.__setattr__(self, "red", red)
        object.__setattr__(self, "green", green)
        object.__setattr__(self, "blue", blue)
        object.__setattr__(self, "alpha", alpha)

        if has_skia():
            # Dynamically load the conversion method that depends on skia iff
            # skia is available
            # pylint: disable=import-outside-toplevel, cyclic-import
            from pytamaro.impl.skia.color import skia_color
            object.__setattr__(self, "skia_color", skia_color(self))

    def __repr__(self) -> str:
        from pytamaro.color_names import \
            _known_colors  # pylint: disable=cyclic-import,import-outside-toplevel
        maybe_known_color = _known_colors.get(self)
        if maybe_known_color:
            return translate(maybe_known_color)
        alpha_repr = "" if self.alpha == 1 else f", {self.alpha}"
        return f"{translate('rgb_color')}({self.red}, {self.green}, {self.blue}{alpha_repr})"
