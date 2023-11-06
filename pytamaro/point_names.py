"""
Names of notable points, that can be used as pinning positions for a graphic.
"""

from pytamaro.point import Point, i_hat, j_hat, zero

center: Point = zero
"""The center point of the bounding box

:meta hide-value:
"""


top_center: Point = center.translate(j_hat)
"""The middle point of the top edge of the bounding box

:meta hide-value:
"""

bottom_center: Point = center.translate(j_hat * -1)
"""The middle point of the bottom edge of the bounding box

:meta hide-value:
"""

center_left: Point = center.translate(i_hat * -1)
"""The middle point of the left edge of the bounding box

:meta hide-value:
"""


center_right: Point = center.translate(i_hat)
"""The middle point of the right edge of the bounding box

:meta hide-value:
"""


top_left: Point = center_left.translate(j_hat)
"""The top left corner of the bounding box

:meta hide-value:
"""

top_right: Point = center_right.translate(j_hat)
"""The top right corner of the bounding box

:meta hide-value:
"""


bottom_left: Point = center_left.translate(j_hat * -1)
"""The bottom left corner of the bounding box

:meta hide-value:
"""


bottom_right: Point = center_right.translate(j_hat * -1)
"""The bottom right corner of the bounding box

:meta hide-value:
"""

_known_points = {
    center: "center",
    top_center: "top_center",
    bottom_center: "bottom_center",
    center_left: "center_left",
    center_right: "center_right",
    top_left: "top_left",
    top_right: "top_right",
    bottom_left: "bottom_left",
    bottom_right: "bottom_right",
}
