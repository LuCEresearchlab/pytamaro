"""
Names of notable colors because they are at the vertices of the RGB cube,
plus the fully-transparent one.
"""

from pytamaro.color import Color
from pytamaro.color_functions import rgb_color

black: Color = rgb_color(0, 0, 0)
"""Black color

:meta hide-value:
"""

red: Color = rgb_color(255, 0, 0)
"""Red color

:meta hide-value:
"""

green: Color = rgb_color(0, 255, 0)
"""Green color

:meta hide-value:
"""

blue: Color = rgb_color(0, 0, 255)
"""Blue color

:meta hide-value:
"""

yellow: Color = rgb_color(255, 255, 0)
"""Yellow color

:meta hide-value:
"""

magenta: Color = rgb_color(255, 0, 255)
"""Magenta color

:meta hide-value:
"""

cyan: Color = rgb_color(0, 255, 255)
"""Cyan color

:meta hide-value:
"""

white: Color = rgb_color(255, 255, 255)
"""White color

:meta hide-value:
"""

transparent: Color = rgb_color(0, 0, 0, 0)
"""Fully-transparent color

:meta hide-value:
"""

_known_colors = {
    black: "black",
    red: "red",
    green: "green",
    blue: "blue",
    yellow: "yellow",
    magenta: "magenta",
    cyan: "cyan",
    white: "white",
    transparent: "transparent",
}
