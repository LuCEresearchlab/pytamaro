"""
Visitor type for Graphic instances
"""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from pytamaro.graphic import (Graphic, Empty,
                              Rectangle, Ellipse, CircularSector, Triangle, Text,
                              Compose, Pin, Rotate, Beside, Above, Overlay)

# Needed by Python < 3.12
T = TypeVar('T')


class Visitor(ABC, Generic[T]):
    """
    Abstract class that allows to implement a visitor object
    to traverse a graphic tree.
    """

    def visit(self, graphic: Graphic) -> T:
        """
        Visit a graphic instance
        """
        # noinspection PyProtectedMember
        # pylint: disable=protected-access
        return graphic.accept(self)

    @abstractmethod
    def visit_empty(self, graphic: Empty) -> T:
        """
        Visit an empty graphic instance
        """

    # Primitives

    @abstractmethod
    def visit_rectangle(self, graphic: Rectangle) -> T:
        """
        Visit a rectangle graphic instance
        """

    @abstractmethod
    def visit_ellipse(self, graphic: Ellipse) -> T:
        """
        Visit an ellipse graphic instance
        """

    @abstractmethod
    def visit_circular_sector(self, graphic: CircularSector) -> T:
        """
        Visit a circular sector graphic instance
        """

    @abstractmethod
    def visit_triangle(self, graphic: Triangle) -> T:
        """
        Visit a triangle graphic instance
        """

    @abstractmethod
    def visit_text(self, graphic: Text) -> T:
        """
        Visit a text graphic instance
        """

    # Transformations

    @abstractmethod
    def visit_compose(self, graphic: Compose) -> T:
        """
        Visit a compose graphic instance
        """

    @abstractmethod
    def visit_pin(self, graphic: Pin) -> T:
        """
        Visit a pin graphic instance
        """

    @abstractmethod
    def visit_rotate(self, graphic: Rotate) -> T:
        """
        Visit a rotate graphic instance
        """

    @abstractmethod
    def visit_beside(self, graphic: Beside) -> T:
        """
        Visit a beside graphic instance
        """

    @abstractmethod
    def visit_above(self, graphic: Above) -> T:
        """
        Visit an above graphic instance
        """

    @abstractmethod
    def visit_overlay(self, graphic: Overlay) -> T:
        """
        Visit an overlay graphic instance
        """
