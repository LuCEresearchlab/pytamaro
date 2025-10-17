"""
FFI-based implementation of I/O functions.

:meta private:
"""
import sys
from io import UnsupportedOperation
from typing import List

# pylint: disable=missing-function-docstring

import pytamaro_ffi as __impl  # pylint: disable=import-error # type: ignore

from pytamaro.checks import check_graphic, check_type
from pytamaro.graphic import Graphic
from pytamaro.localization import translate


def show_graphic(graphic: Graphic, debug: bool):
    check_graphic(graphic)
    check_type(debug, bool, "debug")

    graphic_dict = graphic.asdict()
    # Check for empty graphics
    size = __impl.graphic_size(graphic_dict)
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
    b64_str = __impl.show_graphic(graphic_dict, debug)
    prefix = "@@@PYTAMARO_DATA_URI_BEGIN@@@"
    suffix = "@@@PYTAMARO_DATA_URI_END@@@"
    print(f"{prefix}{b64_str}{suffix}", end="")
    try:
        sys.stdout.flush()
    except AttributeError:
        # https://docs.python.org/3/library/sys.html#sys.stdout
        # > Under some conditions stdin, stdout and stderr as well as the
        # > original values __stdin__, __stdout__ and __stderr__ can be None
        pass


def save_graphic(filename: str, graphic: Graphic, debug: bool):
    raise UnsupportedOperation(f"save_graphic({filename}, {graphic}, {debug})")


def save_animation(filename: str, graphics: List[Graphic],
                   duration: int, loop: bool):
    raise UnsupportedOperation(
        f"save_animation({filename}, [{', '.join(list(map(str, graphics)))}, {duration}, {loop})")


def show_animation(graphics: List[Graphic], duration: int, loop: bool):
    raise UnsupportedOperation(
        f"show_animation([{', '.join(list(map(str, graphics)))}], {duration}, {loop})")
