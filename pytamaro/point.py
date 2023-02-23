"""
`Point` type.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Point:
    """
    Represents a point on a plane.
    """
    x: float    # pylint: disable=invalid-name
    y: float    # pylint: disable=invalid-name

    def translate(self, current_vector: Vector) -> Point:
        """
        Returns a point obtained by translating `current_point` using `current_vector`

        :meta private:
        :param current_point: the point to be translated
        :param current_vector: the vector used for translation
        :returns: a new point, the result of the translation
        """
        return Point(self.x + current_vector.terminal_point.x,
                     self.y + current_vector.terminal_point.y)


# Center of the 2-dimensional space
zero = Point(0.0, 0.0)


@dataclass
class Vector:
    """
    Represents a vector in 2-dimensional space storing its terminal point,
    assuming it starts at the origin (0, 0).

    :meta private:
    """
    terminal_point: Point

    def __add__(self, other: Vector):
        """
        Returns the vector obtained by adding `other` to the current one

        :param other: the vector added to the current one
        :returns: a vector that represent the sum of the current one and `other`.
        """
        return Vector(Point(self.terminal_point.x + other.terminal_point.x,
                            self.terminal_point.y + other.terminal_point.y))

    def __mul__(self, factor: float):
        """
        Returns this vector multiplied by a given scalar

        :param factor: scalar used in the multiplication
        :returns: a new vector, the result of scalar-vector multiplication
        """
        return Vector(Point(self.terminal_point.x * factor, self.terminal_point.y * factor))


# Canonical basis of R2
i_hat = Vector(Point(1.0, 0.0))
j_hat = Vector(Point(0.0, 1.0))
