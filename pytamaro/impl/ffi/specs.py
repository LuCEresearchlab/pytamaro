"""
Graphic tree to specs sequence.

A sequence of specs can be used to draw a graphic without having to perform a
recursive traversal of the graphic tree. This is useful in scenarios where we
are constrained by a small stack that cannot host many stack frames.

:meta private:
"""
# pylint: disable=missing-function-docstring
from typing import Any

from pytamaro.graphic import Graphic

type _Cons[T] = tuple[T, _Cons[T] | None] | None


def to_specs(graphic: Graphic) -> list[dict[str, Any]]:
    to_process_stack: _Cons[Graphic] = (graphic, None)
    specs_stack: _Cons[dict[str, Any]] = None

    while to_process_stack is not None:
        curr, to_process_stack = to_process_stack
        deps, frame = curr.deps_and_spec()
        # Add deps to queue
        for dep in reversed(deps):
            to_process_stack = (dep, to_process_stack)
        # Add current frame to specs stack
        specs_stack = (frame, specs_stack)

    result = []
    while specs_stack is not None:
        it, specs_stack = specs_stack
        result.append(it)

    return result
