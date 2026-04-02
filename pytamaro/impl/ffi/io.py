"""FFI-based implementation of I/O functions.

:meta private:
"""

import base64
from io import BytesIO

from PIL import Image
from PIL.Image import Image as PILImage

from pytamaro.checks import check_graphic, check_graphic_size, check_type
from pytamaro.graphic import Graphic
from pytamaro.impl.ffi.specs import to_specs
from pytamaro.impl.shared_io import guess_scaling_factor, print_data_uri
from pytamaro.utils import Size, Spec
from pytamaro_js_ffi import (  # type: ignore
    js_graphic_size,
    js_render_graphic,
    js_save,
)


# ruff: noqa: D103
def _render_graphic_base64(graphic: Graphic, debug: bool) -> str:
    specs = to_specs(graphic)
    rounded_size = graphic_size(specs).to_round()
    check_graphic_size(rounded_size)
    scaling_factor = guess_scaling_factor(rounded_size)
    return js_render_graphic(specs, scaling_factor, debug)


def extract_base64_image_data(data_uri: str) -> str:
    return data_uri.split(",")[1]


def graphic_size(specs: list[Spec]):
    js_size = js_graphic_size(specs)
    return Size(js_size.width, js_size.height)


def show_graphic(graphic: Graphic, debug: bool):
    check_graphic(graphic)
    check_type(debug, bool, "debug")
    b64_str = _render_graphic_base64(graphic, debug)
    print_data_uri("image/png", extract_base64_image_data(b64_str))


def graphic_to_pillow_image(graphic: Graphic) -> PILImage:
    specs = to_specs(graphic)
    rounded_size = graphic_size(specs).to_round()
    check_graphic_size(rounded_size)
    scaling_factor = guess_scaling_factor(rounded_size)
    data_uri = js_render_graphic(specs, scaling_factor, False)
    data = BytesIO(base64.b64decode(extract_base64_image_data(data_uri)))
    return Image.open(data)


def save_graphic(filename: str, graphic: Graphic, debug: bool):
    check_type(filename, str, "filename")
    check_graphic(graphic)
    check_type(debug, bool, "debug")
    b64_str = _render_graphic_base64(graphic, debug)
    js_save(filename, b64_str)


def show_animation(filename: str):
    with open(filename, "rb") as stream:
        b64_str = base64.b64encode(stream.read()).decode("utf-8")
        print_data_uri("image/gif", b64_str)


def save_animation_extra(filename: str):
    with open(filename, "rb") as stream:
        b64_str = f"data:image/gif;base64,{base64.b64encode(stream.read()).decode('utf-8')}"
        js_save(filename, b64_str)
