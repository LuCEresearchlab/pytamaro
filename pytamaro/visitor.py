from pytamaro import (
    Rectangle,
    Ellipse,
    Text,
    Empty,
    Above,
    Beside,
    CircularSector,
    Compose,
    Overlay,
    Pin,
    Rotate,
    SimpleCompose,
    Triangle,
    Graphic,
)
import pytamaro
from typing import TypeVar, Generic

T = TypeVar("T")


class GraphicVisitor(Generic[T]):

    def visitRectangle(self, v: Rectangle) -> T:
        return self.visitChildren(v)

    def visitEllipse(self, v: Ellipse) -> T:
        return self.visitChildren(v)

    def visitText(self, v: Text) -> T:
        return self.visitChildren(v)

    def visitEmpty(self, v: Empty) -> T:
        return self.visitChildren(v)

    def visitAbove(self, v: Above) -> T:
        return self.visitChildren(v)

    def visitBeside(self, v: Beside) -> T:
        return self.visitChildren(v)

    def visitCircularSector(self, v: CircularSector) -> T:
        return self.visitChildren(v)

    def visitCompose(self, v: Compose) -> T:
        return self.visitChildren(v)

    def visitOverlay(self, v: Overlay) -> T:
        return self.visitChildren(v)

    def visitPin(self, v: Pin) -> T:
        return self.visitChildren(v)

    def visitRotate(self, v: Rotate) -> T:
        return self.visitChildren(v)

    def visitSimpleCompose(self, v: SimpleCompose) -> T:
        return self.visitChildren(v)

    def visitTriangle(self, v: Triangle) -> T:
        return self.visitChildren(v)

    def visit(self, v: Graphic) -> T:
        match v.__class__:
            case pytamaro.Rectangle:
                return self.visitRectangle(v)  # type: ignore
            case pytamaro.Ellipse:
                return self.visitEllipse(v)  # type: ignore
            case pytamaro.Text:
                return self.visitText(v)  # type: ignore
            case pytamaro.Empty:
                return self.visitEmpty(v)  # type: ignore
            case pytamaro.Above:
                return self.visitAbove(v)  # type: ignore
            case pytamaro.Beside:
                return self.visitBeside(v)  # type: ignore
            case pytamaro.CircularSector:
                return self.visitCircularSector(v)  # type: ignore
            case pytamaro.Compose:
                return self.visitCompose(v)  # type: ignore
            case pytamaro.Overlay:
                return self.visitOverlay(v)  # type: ignore
            case pytamaro.Pin:
                return self.visitPin(v)  # type: ignore
            case pytamaro.Rotate:
                return self.visitRotate(v)  # type: ignore
            case pytamaro.SimpleCompose:
                raise RuntimeError(
                    "Known type but child class should be used", v.__class__
                )
            case pytamaro.Triangle:
                return self.visitTriangle(v)  # type: ignore
            case _:
                raise RuntimeError("Type", v.__class__, "is unknown")

    def visitChildren(self, v) -> T:
        graphics_children = [o for o in v.__dict__.values() if isinstance(o, Graphic)]

        el = None
        for o in graphics_children:
            if el is None:
                el = self.visit(o)
            else:
                el = self.reduce(el, self.visit(o))

        return el  # type: ignore

    def reduce(self, v1: T, v2: T) -> T:
        """Reduce the graphics object to a single value."""
        return v1
