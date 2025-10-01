"""
Functions for output (show or save) of graphics.
"""
from typing import List

from pytamaro.graphic import Graphic
from pytamaro.utils import export, has_skia

if has_skia():
    import pytamaro.impl.skia.io as __impl
else:
    import pytamaro.impl.ffi.io as __impl


@export
def show_graphic(graphic: Graphic, debug: bool = False):
    """
    Show a graphic. Graphics with no area cannot be shown.

    When `debug` is `True`, adorns the visualization with useful information
    for debugging: a red border around the bounding box and a yellowish cross
    around the pinning position.

    :param graphic: graphic to be shown
    :param debug: can be optionally set to `True` to overlay debugging
           information
    """
    __impl.show_graphic(graphic, debug)


@export
def save_graphic(filename: str, graphic: Graphic, debug: bool = False):
    """
    Save a graphic to a file.
    Two file formats are supported: PNG (raster graphics) and SVG (vector graphics).
    The extension of the filename (either ".png" or ".svg") determines the format.

    Graphics with no area cannot be saved in the PNG format.

    When `debug` is `True`, adorns the visualization with useful information
    for debugging: a red border around the bounding box and a yellowish cross
    around the pinning position.

    :param filename: name of the file to create (with the extension)
    :param graphic: graphic to be saved
    :param debug: can be optionally set to `True` to overlay debugging
           information
    """
    __impl.save_graphic(filename, graphic, debug)


@export
def save_animation(filename: str, graphics: List[Graphic], duration: int = 40, loop: bool = True):
    """
    Save a sequence of graphics as an animation (GIF).

    Graphics are sequentially reproduced (normally at 25 frames per second) in
    a loop (unless specificied otherwise).

    :param filename: name of the file to create, including the extension '.gif'
    :param graphics: list of graphics to be saved as an animation
    :param duration: duration in milliseconds for each frame
           (defaults to 40 milliseconds, which leads to 25 frames per second)
    :param loop: whether the GIF should loop indefinitely (defaults to true)
    """
    __impl.save_animation(filename, graphics, duration, loop)


@export
def show_animation(graphics: List[Graphic], duration: int = 40, loop: bool = True):
    """
    Show a sequence of graphics as an animation (GIF).

    Graphics are sequentially reproduced (normally at 25 frames per second) in
    a loop (unless specificied otherwise).

    :param graphics: list of graphics to be shown as an animation
    :param duration: duration in milliseconds for each frame
           (defaults to 40 milliseconds, which leads to 25 frames per second)
    :param loop: whether the animation should loop indefinitely (defaults to true)
    """
    __impl.show_animation(graphics, duration, loop)
