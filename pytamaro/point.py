"""
`Point` type and functions to represent a point int he 2 dimensional space.
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass
class Point:
    """
    Represents a point in 2-dimensional space.
    """
    x: float    # pylint: disable=invalid-name
    y: float    # pylint: disable=invalid-name

    def __init__(self, x: float, y: float):  # pylint: disable=invalid-name
        self.x = x
        self.y = y

    def as_tuple(self) -> Tuple[float, float]:
        """
        Returns the current point as a tuple of two floating point values

        :meta private:
        :returns: a tuple with 2 float components that represent a point in the 2-dimensional space
        """
        return self.x, self.y


@dataclass
class Vector:
    """
    Represents a vector in 2-dimensional space storing its terminal point.
    """
    terminal_point: Point

    def __init__(self, terminal_point: Point):
        self.terminal_point = terminal_point

    def __add__(self, other):
        """
        Returns the vector obtained by adding `other` to the current one

        :param other: the vector added to the current one
        :returns: a vector that represent the sum of the current one and `other`.
        """
        return Vector(Point(self.terminal_point.x + other.terminal_point.x,
                            self.terminal_point.y + other.terminal_point.y))

    def __mul__(self, other):
        """
        Applies vector scalar multiplication

        :param other: scalar used in the multiplication
        :returns: a new vector, the result of scalar-vector multiplication
        """
        return Vector(Point(self.terminal_point.x * other, self.terminal_point.y * other))

    def as_tuple(self) -> Tuple[float, float]:
        """
        Returns the current vector as a tuple of two floating point values

        :meta private:
        :returns: a tuple with 2 float components that represent a vector in the 2-dimensional space
        """
        return self.terminal_point.x, self.terminal_point.y


def point(x: float, y: float) -> Point:  # pylint: disable=invalid-name
    """
    Returns a 2-dimensional point given its coordinates

    :param x: coordinate along the x-axis
    :param y: coordinate along the y-axis
    """
    return Point(x, y)


def vector(current_point: Point) -> Vector:
    """
    Returns a 2-dimensional vector given the terminal point

    :param current_point: terminal point of the vector
    :returns: a vector given the terminal point
    """
    return Vector(current_point)


def translate(current_point: Point, current_vector: Vector) -> Point:
    """
    Returns a point obtained by translating `current_point` using `current_vector`

    :param current_point: the point to be translated
    :param current_vector: the vector used for translation
    :returns: a new point, the result of the translation
    """
    return point(current_point.x + current_vector.terminal_point.x,
                 current_point.y + current_vector.terminal_point.y)


i_hat = vector(Point(1.0, 0.0))
j_hat = vector(Point(0.0, 1.0))
