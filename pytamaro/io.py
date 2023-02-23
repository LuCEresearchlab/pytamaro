"""
Functions to do I/O with graphics, such as showing or saving them.
"""

import base64
import io
import os
from pathlib import Path
from typing import List

from PIL import Image as PILImageMod
from PIL.Image import Image as PILImage
from skia import Canvas, FILEWStream, Image, Rect, Surface, SVGCanvas, kPNG

from pytamaro.checks import check_graphic, check_type
from pytamaro.debug import add_debug_info
from pytamaro.graphic import Graphic
from pytamaro.localization import translate
from pytamaro.utils import export, is_notebook


def _warning_no_area(graphic: Graphic):
    """
    Emits a warning indicating that the graphic cannot be shown or saved
    because it has no area.

    :param graphic: graphic that cannot be shown or saved
    """
    size = graphic.bounds().round()
    # pylint: disable-next=line-too-long
    print(translate("EMPTY_AREA_OUTPUT", f"{size.width()}x{size.height()}"))


def _draw_to_canvas(canvas: Canvas, graphic: Graphic):
    """
    Draws a graphic to a canvas, correcting for the top-left position.

    :param canvas: canvas onto which to draw
    :param graphic: graphic to be drawn
    """
    bounds = graphic.bounds()
    canvas.translate(-bounds.left(), -bounds.top())
    graphic.draw(canvas)


# pylint: disable-next=invalid-name
def _save_as_SVG(filename: str, graphic: Graphic):
    """
    Save a graphic to an SVG file.

    :param filename: name of the file to be created, ending in ".svg"
    :param graphic: graphic to be saved
    """
    size = graphic.size()
    stream = FILEWStream(filename)
    canvas = SVGCanvas.Make(Rect.MakeSize(size), stream)
    _draw_to_canvas(canvas, graphic)
    del canvas
    stream.flush()


def graphic_to_image(graphic: Graphic) -> Image:
    """
    Renders a graphic into a Skia image.

    :param graphic: graphic to be rendered
    :returns: rendered graphic as a Skia image
    """
    int_size = graphic.size().toCeil()
    surface = Surface(int_size.width(), int_size.height())
    _draw_to_canvas(surface.getCanvas(), graphic)
    return surface.makeImageSnapshot()


def graphic_to_pillow_image(graphic: Graphic) -> PILImage:
    """
    Renders a graphic and converts it into a Pillow image.

    :param graphic: graphic to be rendered and converted
    :returns: rendered graphic as a Pillow image
    """
    with io.BytesIO(graphic_to_image(graphic).encodeToData()) as stream:
        pil_image = PILImageMod.open(stream)
        pil_image.load()  # Ensure to make a copy of buffer
        return pil_image


# pylint: disable-next=invalid-name
def _save_as_PNG(filename: str, graphic: Graphic):
    """
    Save a graphic to a PNG file.

    :param filename: name of the file to be created, ending in ".png"
    :param graphic: graphic to be saved
    """
    graphic_to_image(graphic).save(filename, kPNG)


@export
def show_graphic(graphic: Graphic, debug: bool = False):
    """
    Show a graphic in a window. Graphics with no area cannot be shown.

    When `debug` is `True`, adorns the visualization with useful information
    for debugging: a red border around the bounding box and a yellowish cross
    around the pinning position.

    :param graphic: graphic to be shown
    :param debug: can be optionally set to `True` to overlay debugging
           information
    """
    check_graphic(graphic)
    if graphic.empty_area():
        _warning_no_area(graphic)
    else:
        to_show = add_debug_info(graphic) if debug else graphic
        pil_image = graphic_to_pillow_image(to_show)
        if is_notebook():
            # pylint: disable=undefined-variable
            display(pil_image)  # type: ignore[name-defined]
        elif "PYTAMARO_OUTPUT_DATA_URI" in os.environ:
            buffer = io.BytesIO()
            pil_image.save(buffer, format="PNG")
            b64_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
            print(f"data:image/png;base64,{b64_str}", end="")
        else:
            pil_image.show()


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
    to_show = add_debug_info(graphic) if debug else graphic
    extension = Path(filename).suffix
    if extension == ".png":
        if graphic.empty_area():
            _warning_no_area(graphic)
        else:
            _save_as_PNG(filename, to_show)
    elif extension == ".svg":
        _save_as_SVG(filename, to_show)
    else:
        raise ValueError(translate("INVALID_FILENAME_EXTENSION"))


@export
def save_gif(filename: str, graphics: List[Graphic], duration: int = 40, loop: bool = True):
    """
    Save a sequence of graphics as an animated GIF.

    Graphics are sequentially reproduced (normally at 25 frames per second) in
    a loop (unless specificied otherwise).

    :param filename: name of the file to create, including the extension '.gif'
    :param graphics: list of graphics to be saved as a GIF
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
    pil_images = list(map(graphic_to_pillow_image, graphics))
    pil_images[0].save(
        filename,
        save_all=True,
        append_images=pil_images[1:],
        duration=duration,
        loop=0 if loop else 1,  # loop 0 means "indefinitely", 1 means "once"
    )
