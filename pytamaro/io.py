"""
Functions for output (show or save) of graphics.
"""
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import List

from pytamaro.checks import check_graphic, check_type
from pytamaro.graphic import Graphic
from pytamaro.impl.shared_io import area_message
from pytamaro.localization import translate
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
    check_graphic(graphic)
    check_type(debug, bool, "debug")
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
    check_type(filename, str, "filename")
    check_graphic(graphic)
    check_type(debug, bool, "debug")
    __impl.save_graphic(filename, graphic, debug)


def _save_animation(filename: str, graphics: List[Graphic],
                    duration: int, loop: bool):
    """
    Try to save a sequence of graphics as an animation (GIF).

    :param filename: name of the file to create, including the extension '.gif'
    :param graphics: list of graphics to be saved as an animation
    :param duration: duration in milliseconds for each frame
    :param loop: whether the GIF should loop indefinitely
    :returns: whether the animation was successfully saved
    """
    for idx, graphic in enumerate(graphics):
        check_type(graphic, Graphic, "graphics", idx)
        size = __impl.graphic_size(graphic)
        if size.to_round().empty_area():
            raise ValueError(area_message("EMPTY_AREA_OUTPUT", size.width, size.height))
    pil_images = list(map(__impl.graphic_to_pillow_image, graphics))
    if len(set(image.size for image in pil_images)) != 1:
        raise ValueError(translate("DIFFERENT_SIZES"))
    check_type(duration, int, "duration")
    check_type(loop, bool, "loop")
    pil_images[0].save(
        filename,
        save_all=True,
        append_images=pil_images[1:],
        duration=duration,
        loop=0 if loop else None,  # loop 0 means "indefinitely", None means "once"
        disposal=2,  # 2 means "after showing the frame, clear to background"
    )


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
    check_type(filename, str, "filename")
    if Path(filename).suffix != ".gif":
        raise ValueError(translate("INVALID_FILENAME_GIF"))
    check_type(graphics, list, "graphics")
    if len(graphics) == 0:
        raise ValueError(translate("EMPTY_GRAPHICS_LIST"))
    _save_animation(filename, graphics, duration, loop)


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
    with NamedTemporaryFile(suffix=".gif", delete=False) as file:
        _save_animation(file.name, graphics, duration, loop)
    __impl.show_animation(file.name)
