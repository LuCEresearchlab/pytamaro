from pytamaro import json
from typing import TypeVar, Generic

T = TypeVar("T")


class JSONGraphicVisitor(Generic[T]):

    def visit(self, v: json.Graphic) -> T:
        match v.__class__:
            case json.GraphicAbove:
                return self.visitAbove(v)  # type: ignore
            case json.GraphicAbove:
                return self.visitAbove(v)  # type: ignore
            case json.GraphicBeside:
                return self.visitBeside(v)  # type: ignore
            case json.GraphicCircularSector:
                return self.visitCircularSector(v)  # type: ignore
            case json.GraphicCompose:
                return self.visitCompose(v)  # type: ignore
            case json.GraphicEllipse:
                return self.visitEllipse(v)  # type: ignore
            case json.GraphicEmpty:
                return self.visitEmpty(v)  # type: ignore
            case json.GraphicOverlay:
                return self.visitOverlay(v)  # type: ignore
            case json.GraphicPin:
                return self.visitPin(v)  # type: ignore
            case json.GraphicRectangle:
                return self.visitRectangle(v)  # type: ignore
            case json.GraphicRotate:
                return self.visitRotate(v)  # type: ignore
            case json.GraphicText:
                return self.visitText(v)  # type: ignore
            case json.GraphicTriangle:
                return self.visitTriangle(v)  # type: ignore
            case _:
                raise RuntimeError("Type", v.__class__, "is unknown")

    def visitAbove(self, v: json.GraphicAbove) -> T:
        return self.visitChildren(v)

    def visitBeside(self, v: json.GraphicBeside) -> T:
        return self.visitChildren(v)

    def visitCircularSector(self, v: json.GraphicCircularSector) -> T:
        return self.visitChildren(v)

    def visitCompose(self, v: json.GraphicCompose) -> T:
        return self.visitChildren(v)

    def visitEllipse(self, v: json.GraphicEllipse) -> T:
        return self.visitChildren(v)

    def visitEmpty(self, v: json.GraphicEmpty) -> T:
        return self.visitChildren(v)

    def visitOverlay(self, v: json.GraphicOverlay) -> T:
        return self.visitChildren(v)

    def visitPin(self, v: json.GraphicPin) -> T:
        return self.visitChildren(v)

    def visitRectangle(self, v: json.GraphicRectangle) -> T:
        return self.visitChildren(v)

    def visitRotate(self, v: json.GraphicRotate) -> T:
        return self.visitChildren(v)

    def visitText(self, v: json.GraphicText) -> T:
        return self.visitChildren(v)

    def visitTriangle(self, v: json.GraphicTriangle) -> T:
        return self.visitChildren(v)

    def visitChildren(self, v: json.Graphic) -> T:

        Graphic_children = [
            o for o in v.__dict__.values() if isinstance(o, json.Graphic)
        ]

        el = None
        for o in Graphic_children:
            if el is None:
                el = self.visit(o)
            else:
                el = self.reduce(el, self.visit(o))

        return el  # type: ignore

    def reduce(self, v1: T, v2: T) -> T:
        """Reduce the Graphic object to a single value."""
        return v1
