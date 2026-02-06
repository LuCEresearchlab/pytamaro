from typing import Any

from pytamaro.utils import Size


def graphic_size(specs: list[dict[str, Any]]) -> Size: ...


def render_graphic(specs: list[dict[str, Any]], scaling_factor: int, debug: bool) -> str: ...
