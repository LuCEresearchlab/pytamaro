from typing import Any

from pytamaro.utils import Size


def js_graphic_size(specs: list[dict[str, Any]]) -> Size: ...


def js_render_graphic(specs: list[dict[str, Any]], scaling_factor: int, debug: bool) -> str: ...


def js_save_graphic(filename: str, specs: list[dict[str, Any]], scaling_factor: int, debug: bool) -> None: ...
