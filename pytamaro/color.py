"""
`Color` type, functions to produce colors, and constants for important colors.
"""

from dataclasses import dataclass

from pytamaro.localization import translate


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

    def __repr__(self) -> str:
        from pytamaro.color_names import \
            _known_colors  # pylint: disable=cyclic-import,import-outside-toplevel
        maybe_known_color = _known_colors.get(self)
        if maybe_known_color:
            return translate(maybe_known_color)
        alpha_repr = "" if self.alpha == 1 else f", {self.alpha}"
        return f"{translate('rgb_color')}({self.red}, {self.green}, {self.blue}{alpha_repr})"
