"""
Graphic tree to specs sequence.

A sequence of specs can be used to draw a graphic without having to perform a
recursive traversal of the graphic tree. This is useful in scenarios where we
are constrained by a small stack that cannot host many stack frames.

:meta private:
"""
from pytamaro.graphic import Graphic
from pytamaro.utils import Spec


def to_specs(graphic: Graphic) -> list[Spec]:
    """
    Turn a graphic into a list of specs,
    processing (without recursion) the recursive dependencies.
    """
    graphics_to_process: list[Graphic] = [graphic]
    specs: list[Spec] = []

    while len(graphics_to_process) > 0:
        graphic = graphics_to_process.pop()
        spec, deps = graphic.spec_with_deps()
        graphics_to_process.extend(reversed(deps))
        specs.append(spec)

    specs.reverse()
    return specs
