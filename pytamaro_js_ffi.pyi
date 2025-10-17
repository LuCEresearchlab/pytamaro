from typing import Any


class Size:
    width: float
    height: float

def graphic_size(graphic_dict: dict[str, Any]) -> Size: ...

def render_graphic(graphic_dict: dict[str, Any], debug: bool) -> str: ...