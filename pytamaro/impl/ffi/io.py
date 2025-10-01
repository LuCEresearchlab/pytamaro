"""
FFI-based implementation of I/O functions.

:meta private:
"""
# pylint: disable=import-error, missing-function-docstring
import sys
from io import UnsupportedOperation
from typing import List

import pytamaro_ffi as __impl  # type: ignore

from pytamaro.checks import check_graphic, check_type
from pytamaro.graphic import Graphic
from pytamaro.localization import translate


def show_graphic(graphic: Graphic, debug: bool):
    check_graphic(graphic)
    check_type(debug, bool, "debug")

    # Check for empty graphics
    size = __impl.graphic_size(graphic.as_dict())
    rounded_size = {
        "width": round(size.width),
        "height": round(size.height),
    }
    if rounded_size["width"] == 0 or rounded_size["height"] == 0:
        raise ValueError(translate(
            "EMPTY_AREA_OUTPUT",
            f"{rounded_size["width"]}x{rounded_size["height"]}"
        ))

    # Render and print data uri
    b64_str = __impl.show_graphic(graphic.as_dict(), debug)
    prefix = "@@@PYTAMARO_DATA_URI_BEGIN@@@"
    suffix = "@@@PYTAMARO_DATA_URI_END@@@"
    print(f"{prefix}{b64_str}{suffix}", end="")
    sys.stdout.flush()


def save_graphic(filename: str, graphic: Graphic, debug: bool):
    raise UnsupportedOperation(f"save_graphic({filename}, {graphic}, {debug})")


def save_animation(filename: str, graphics: List[Graphic],
                   duration: int, loop: bool):
    raise UnsupportedOperation(
        f"save_animation({filename}, [{', '.join(list(map(str, graphics)))}, {duration}, {loop})")


def show_animation(graphics: List[Graphic], duration: int, loop: bool):
    raise UnsupportedOperation(
        f"show_animation([{', '.join(list(map(str, graphics)))}], {duration}, {loop})")
