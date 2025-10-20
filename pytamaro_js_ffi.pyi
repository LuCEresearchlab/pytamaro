from typing import Any

from pytamaro.utils import Size



def graphic_size(graphic_dict: dict[str, Any]) -> Size: ...

def render_graphic(graphic_dict: dict[str, Any], debug: bool) -> str: ...