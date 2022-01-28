"""
Names of notable colors because they are at the vertices of the RGB cube,
plus the fully-transparent one.
"""

from pytamaro.color import rgb_color, rgba_color

black = rgb_color(0, 0, 0)
"""Black color"""

red = rgb_color(255, 0, 0)
"""Red color"""

green = rgb_color(0, 255, 0)
"""Green color"""

blue = rgb_color(0, 0, 255)
"""Blue color"""

yellow = rgb_color(255, 255, 0)
"""Yellow color"""

magenta = rgb_color(255, 0, 255)
"""Magenta color"""

cyan = rgb_color(0, 255, 255)
"""Cyan color"""

white = rgb_color(255, 255, 255)
"""White color"""

transparent = rgba_color(0, 0, 0, 0)
"""Fully-transparent color"""
