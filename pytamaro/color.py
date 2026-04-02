"""`Color` type, functions to produce colors, and constants for important colors."""

from dataclasses import dataclass

from pytamaro.localization import translate


@dataclass(frozen=True)
class Color:
    """Represents a color.
    A color also has a degree of opacity,
    from completely transparent (like the color `transparent`)
    to completely opaque (like the color `red`).
    """

    red: int  # [0-255]
    green: int  # [0-255]
    blue: int  # [0-255]
    alpha: float  # [0-1]

    def __repr__(self) -> str:  # noqa: D105
        from pytamaro.color_names import (  # noqa: PLC0415
            _known_colors,
        )

        maybe_known_color = _known_colors.get(self)
        if maybe_known_color:
            return translate(maybe_known_color)
        alpha_repr = "" if self.alpha == 1 else f", {self.alpha}"
        return f"{translate('rgb_color')}({self.red}, {self.green}, {self.blue}{alpha_repr})"

    @property
    def value_for_spec(self) -> int:
        """ARGB 32-bit word, to be used in a spec.

        :meta private:
        """
        a = int(self.alpha * 255) & 0xFF
        r = self.red & 0xFF
        g = self.green & 0xFF
        b = self.blue & 0xFF
        return (a << 24) | (r << 16) | (g << 8) | b
