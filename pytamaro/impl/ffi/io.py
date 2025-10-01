"""
FFI-based implementation of I/O functions.

:meta private:
"""
# pylint: disable=import-error, missing-function-docstring
import asyncio
import sys
from typing import List

import pytamaro_ffi as __impl  # type: ignore

from pytamaro.graphic import Graphic


def show_graphic(graphic: Graphic, debug: bool):
    b64_str = asyncio.run(__impl.show_graphic(graphic.as_dict(), debug))
    prefix = "@@@PYTAMARO_DATA_URI_BEGIN@@@"
    suffix = "@@@PYTAMARO_DATA_URI_END@@@"
    print(f"{prefix}{b64_str}{suffix}", end="")
    sys.stdout.flush()


def save_graphic(filename: str, graphic: Graphic, debug: bool):
    asyncio.run(__impl.save_graphic(filename, graphic.as_dict(), debug))


def save_animation(filename: str, graphics: List[Graphic],
                   duration: int, loop: bool):
    asyncio.run(__impl.save_animation(filename, [g.as_dict() for g in graphics], duration, loop))


def show_animation(graphics: List[Graphic], duration: int, loop: bool):
    asyncio.run(__impl.show_animation([g.as_dict() for g in graphics], duration, loop))
