"""
Names of notable points (point of interest) that can be used as pinning positions of a graphic
"""

from pytamaro.point import point, translate, i_hat, j_hat


center = point(0.0, 0.0)
"""The center point of the bounding box

:meta hide-value:
"""


top_center = translate(center, j_hat)
"""The middle point of the top edge of the bounding box

:meta hide-value:
"""

bottom_center = translate(center, j_hat * -1)
"""The middle point of the bottom edge of the bounding box

:meta hide-value:
"""

center_left = translate(center, i_hat * -1)
"""The middle point of the left edge of the bounding box

:meta hide-value:
"""


center_right = translate(center, i_hat)
"""The middle point of the right edge of the bounding box

:meta hide-value:
"""


top_left = translate(center, (i_hat * -1) + j_hat)
"""The top left corner of the bounding box

:meta hide-value:
"""

top_right = translate(center, i_hat + j_hat)
"""The top right corner of the bounding box

:meta hide-value:
"""

bottom_left = translate(center, (i_hat + j_hat) * -1)
"""The bottom left corner of the bounding box

:meta hide-value:
"""

bottom_right = translate(center, i_hat + (j_hat * -1))
"""The bottom right corner of the bounding box

:meta hide-value:
"""
