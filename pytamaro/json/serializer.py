import pytamaro.visitor as visitor

from pytamaro import json

from pytamaro import Color, Point

from pytamaro import (
    Graphic,
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
    Triangle,
)

from pytamaro.json import (
    JSONGraphicVisitor,
    Color as JSONColor,
    Point as JSONPoint,
    Graphic as JSONGraphic,
    GraphicAbove as JSONGraphicAbove,
    GraphicBeside as JSONGraphicBeside,
    GraphicCircularSector as JSONGraphicCircularSector,
    GraphicCompose as JSONGraphicCompose,
    GraphicEllipse as JSONGraphicEllipse,
    GraphicEmpty as JSONGraphicEmpty,
    GraphicOverlay as JSONGraphicOverlay,
    GraphicPin as JSONGraphicPin,
    GraphicRectangle as JSONGraphicRectangle,
    GraphicRotate as JSONGraphicRotate,
    GraphicText as JSONGraphicText,
    GraphicTriangle as JSONGraphicTriangle,
)


class JSONSerializer(visitor.GraphicVisitor[JSONGraphic]):

    @classmethod
    def color(cls, v: Color) -> JSONColor:
        return JSONColor(alpha=v.alpha, red=v.red, green=v.green, blue=v.blue)

    @classmethod
    def point(cls, v: Point) -> JSONPoint:
        return JSONPoint(x=v.x, y=v.y)

    def visitRectangle(self, v: Rectangle) -> JSONGraphicRectangle:
        return JSONGraphicRectangle(
            "rectangle",
            color=JSONSerializer.color(v.color),
            width=v.width,
            height=v.height,
        )

    def visitEllipse(self, v: Ellipse) -> JSONGraphicEllipse:
        return JSONGraphicEllipse(
            "ellipse",
            color=JSONSerializer.color(v.color),
            width=v.width,
            height=v.height,
        )

    def visitText(self, v: Text) -> JSONGraphicText:
        print(v.color, JSONSerializer.color(v.color))
        return JSONGraphicText(
            "text",
            color=JSONSerializer.color(v.color),
            text=v.text,
            font_name=v.font_name,
            text_size=v.text_size,
        )

    def visitEmpty(self, v: Empty) -> JSONGraphicEmpty:
        return JSONGraphicEmpty("empty")

    def visitAbove(self, v: Above) -> JSONGraphicAbove:
        return JSONGraphicAbove(
            "above",
            bottom_graphic=self.visit(v.bottom_graphic),
            top_graphic=self.visit(v.top_graphic),
        )

    def visitBeside(self, v: Beside) -> JSONGraphicBeside:
        return JSONGraphicBeside(
            "beside",
            left_graphic=self.visit(v.left_graphic),
            right_graphic=self.visit(v.right_graphic),
        )

    def visitCircularSector(self, v: CircularSector) -> JSONGraphicCircularSector:
        return JSONGraphicCircularSector(
            "circular_sector",
            angle=v.angle,
            color=JSONSerializer.color(v.color),
            radius=v.radius,
        )

    def visitCompose(self, v: Compose) -> JSONGraphicCompose:
        return JSONGraphicCompose(
            "compose",
            background=self.visit(v.background),
            foreground=self.visit(v.foreground),
        )

    def visitOverlay(self, v: Overlay) -> JSONGraphicOverlay:
        return JSONGraphicOverlay(
            "overlay",
            back_graphic=self.visit(v.back_graphic),
            front_graphic=self.visit(v.front_graphic),
        )

    def visitPin(self, v: Pin) -> JSONGraphicPin:
        return JSONGraphicPin(
            "pin",
            graphic=self.visit(v.graphic),
            pinning_point=JSONSerializer.point(v.pin_position),
        )

    def visitRotate(self, v: Rotate) -> JSONGraphicRotate:
        return JSONGraphicRotate("rotate", angle=v.angle, graphic=self.visit(v.graphic))

    def visitTriangle(self, v: Triangle) -> JSONGraphicTriangle:
        return JSONGraphicTriangle(
            "triangle",
            angle=v.angle,
            color=JSONSerializer.color(v.color),
            side1=v.side1,
            side2=v.side2,
        )

    def serialize(self, v: Graphic) -> JSONGraphic:
        return self.visit(v)


class JSONDeserializer(JSONGraphicVisitor[Graphic]):
    @classmethod
    def color(cls, v: JSONColor) -> Color:
        return Color(red=v.red, green=v.green, blue=v.blue, alpha=v.alpha)

    @classmethod
    def point(cls, v: JSONPoint) -> Point:
        return Point(x=v.x, y=v.y)

    def visitRectangle(self, v: JSONGraphicRectangle) -> Rectangle:
        return Rectangle(
            width=v.width, height=v.height, color=JSONDeserializer.color(v.color)
        )

    def visitEllipse(self, v: JSONGraphicEllipse) -> Ellipse:
        return Ellipse(
            width=v.width, height=v.height, color=JSONDeserializer.color(v.color)
        )

    def visitText(self, v: JSONGraphicText) -> Text:
        return Text(
            text=v.text,
            font_name=v.font_name,
            text_size=v.text_size,
            color=JSONDeserializer.color(v.color),
        )

    def visitEmpty(self, v: JSONGraphicEmpty) -> Empty:
        return Empty()

    def visitAbove(self, v: JSONGraphicAbove) -> Above:
        return Above(
            bottom_graphic=self.visit(v.bottom_graphic),
            top_graphic=self.visit(v.top_graphic),
        )

    def visitBeside(self, v: JSONGraphicBeside) -> Beside:
        return Beside(
            left_graphic=self.visit(v.left_graphic),
            right_graphic=self.visit(v.right_graphic),
        )

    def visitCircularSector(self, v: JSONGraphicCircularSector) -> CircularSector:
        return CircularSector(
            radius=v.radius, angle=v.angle, color=JSONDeserializer.color(v.color)
        )

    def visitCompose(self, v: JSONGraphicCompose) -> Compose:
        return Compose(
            background=self.visit(v.background), foreground=self.visit(v.foreground)
        )

    def visitOverlay(self, v: JSONGraphicOverlay) -> Overlay:
        return Overlay(
            back_graphic=self.visit(v.back_graphic),
            front_graphic=self.visit(v.front_graphic),
        )

    def visitPin(self, v: JSONGraphicPin) -> Pin:
        return Pin(
            graphic=self.visit(v.graphic),
            pinning_point=JSONDeserializer.point(v.pinning_point),
        )

    def visitRotate(self, v: JSONGraphicRotate) -> Rotate:
        return Rotate(graphic=self.visit(v.graphic), angle=v.angle)

    def visitTriangle(self, v: JSONGraphicTriangle) -> Triangle:
        return Triangle(
            side1=v.side1,
            side2=v.side2,
            angle=v.angle,
            color=JSONDeserializer.color(v.color),
        )

    def deserialize(self, v: JSONGraphic) -> Graphic:
        return self.visit(v)
