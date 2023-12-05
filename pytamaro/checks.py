"""
Checks to be performed on the parameters of user-facing functions.
"""

from math import inf
from numbers import Number
from typing import Any

from pytamaro.color import Color
from pytamaro.graphic import Graphic
from pytamaro.localization import translate
from pytamaro.point import Point


def check_angle(angle: Any, lower_bound: float = -inf, upper_bound: float = inf):
    """
    Raises an exception when the provided value is not valid for a
    angle, being outside the specified range or not a numeric type.

    :param angle: the value for an angle to be checked
    """
    check_range(angle, lower_bound, upper_bound, "angle")


def check_length(length: Any, parameter_name: str):
    """
    Raises an exception when the provided value is not valid for a
    length, being negative or not a numeric type.

    :param length: the value for a length to be checked
    """
    check_number(length, parameter_name)
    localized_parameter_name = translate(parameter_name)
    if length < 0:
        raise ValueError(translate("INVALID_LENGTH", localized_parameter_name))


def check_type(value: Any, expected_type: type, parameter_name: str):
    """
    Raises an exception when the provided value is not valid for a
    given type.

    Subclasses of Graphic are opaquely reported as Graphic.

    :param value: the value to be checked
    :param expected_type: the expected type for the value
    :param parameter_name: original parameter name, to be used in the error message
    """
    if not isinstance(value, expected_type):
        expected_type_name: str = expected_type.__name__
        actual_type = type(value)
        actual_public_type = Graphic if issubclass(actual_type, Graphic) else actual_type
        actual_type_name: str = actual_public_type.__name__
        raise TypeError(translate("INVALID_TYPE",
                                  translate(parameter_name),
                                  translate(expected_type_name),
                                  translate(actual_type_name)))


def check_color(color: Any):
    """
    Raises an exception when the provided value is not valid for a
    color, not being of type Color.

    :param color: the value for a color to be checked
    """
    check_type(color, Color, "color")


def check_graphic(graphic: Any, parameter_name: str = "graphic"):
    """
    Raises an exception when the provided value is not valid for a
    graphic, not being of type Graphic.

    :param color: the value for a color to be checked
    """
    check_type(graphic, Graphic, parameter_name)


def check_point(point: Any):
    """
    Raises an exception when the provided value is not valid for a
    point, not being of type Point.

    :param point: the value for a point to be checked
    """
    check_type(point, Point, "point")


def check_number(value: Any, parameter_name: str):
    """
    Raises an exception when the provided value is not valid for a
    number, not being of type Number.

    :param value: the value to be checked
    :param parameter_name: original parameter name, to be used in the error message
    """
    check_type(value, Number, parameter_name)


def check_range(value: Any, lower_bound: float, upper_bound: float, parameter_name: str):
    """
    Raises an exception when the provided value is not valid for a
    range, being outside the specified range or not a numeric type.

    :param value: the value to be checked
    :param lower_bound: the lower bound of the range
    :param upper_bound: the upper bound of the range
    """
    check_number(value, parameter_name)
    if value < lower_bound or value > upper_bound:
        raise ValueError(translate("INVALID_RANGE",
                                   translate(parameter_name),
                                   lower_bound,
                                   upper_bound))
