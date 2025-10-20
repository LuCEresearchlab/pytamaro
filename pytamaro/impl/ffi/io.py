"""
FFI-based implementation of I/O functions.

:meta private:
"""
import base64
from dataclasses import asdict
from io import BytesIO, UnsupportedOperation
from PIL import Image
from PIL.Image import Image as PILImage

from pytamaro_js_ffi import graphic_size as js_graphic_size, render_graphic  # pylint: disable=import-error # type: ignore

from pytamaro.impl.shared_io import area_message, print_data_uri
from pytamaro.utils import Size

from pytamaro.checks import check_graphic, check_type
from pytamaro.graphic import Graphic

# pylint: disable=missing-function-docstring


def extract_base64_image_data(data_uri: str) -> str:
    return data_uri.split(",")[1]


def graphic_size(graphic: Graphic):
    js_size = js_graphic_size(asdict(graphic))
    return Size(js_size.width, js_size.height)


def show_graphic(graphic: Graphic, debug: bool):
    check_graphic(graphic)
    check_type(debug, bool, "debug")
    graphic_dict = asdict(graphic)
    size = js_graphic_size(graphic_dict)
    if size.to_round().empty_area():
        raise ValueError(area_message("EMPTY_AREA_OUTPUT", size.width, size.height))
    b64_str = render_graphic(graphic_dict, debug)
    print_data_uri("image/png", extract_base64_image_data(b64_str))


def graphic_to_pillow_image(graphic: Graphic) -> PILImage:
    data_uri = render_graphic(asdict(graphic), False)
    data = BytesIO(base64.b64decode(extract_base64_image_data(data_uri)))
    return Image.open(data)


def save_graphic(filename: str, graphic: Graphic, debug: bool):
    raise UnsupportedOperation(f"save_graphic({filename}, {graphic}, {debug})")


def show_animation(filename: str):
    with open(filename, "rb") as stream:
        b64_str = base64.b64encode(stream.read()).decode("utf-8")
        print_data_uri("image/gif", b64_str)
