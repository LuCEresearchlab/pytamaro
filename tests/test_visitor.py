from typing import List

from pytamaro import black
from pytamaro.graphic import *
from pytamaro.visitor import Visitor


class _DummyVisitor(Visitor[List[str]]):

    def visit_empty(self, graphic: Empty) -> List[str]:
        return ['empty']

    def visit_rectangle(self, graphic: Rectangle) -> List[str]:
        return ['rectangle']

    def visit_ellipse(self, graphic: Ellipse) -> List[str]:
        return ['ellipse']

    def visit_circular_sector(self, graphic: CircularSector) -> List[str]:
        return ['circular_sector']

    def visit_triangle(self, graphic: Triangle) -> List[str]:
        return ['triangle']

    def visit_text(self, graphic: Text) -> List[str]:
        return ['text']

    def visit_compose(self, graphic: Compose) -> List[str]:
        return ['compose'] + self.visit(graphic.foreground) + self.visit(graphic.background)

    def visit_pin(self, graphic: Pin) -> List[str]:
        return ['pin'] + self.visit(graphic.graphic)

    def visit_rotate(self, graphic: Rotate) -> List[str]:
        return ['rotate'] + self.visit(graphic.graphic)

    def visit_beside(self, graphic: Beside) -> List[str]:
        return ['beside'] + self.visit(graphic.left_graphic) + self.visit(graphic.right_graphic)

    def visit_above(self, graphic: Above) -> List[str]:
        return ['above'] + self.visit(graphic.top_graphic) + self.visit(graphic.bottom_graphic)

    def visit_overlay(self, graphic: Overlay) -> List[str]:
        return ['overlay'] + self.visit(graphic.front_graphic) + self.visit(graphic.back_graphic)


def test_visitor():
    g = Overlay(
        Above(
            Beside(
                Pin(
                    Compose(
                        Compose(
                            Text('Test', 'sans-serif', 10, black),
                            Triangle(10, 10, 60, black),
                        ),
                        CircularSector(10, 30, black),
                    ),
                    center
                ),
                Ellipse(10, 10, black),
            ),
            Rectangle(10, 20, black),
        ),
        Empty()
    )

    visitor = _DummyVisitor()
    result = ' '.join(visitor.visit(g))
    # pylint: disable: line-too-long
    assert 'overlay above beside pin compose compose text triangle circular_sector ellipse rectangle empty' == result
