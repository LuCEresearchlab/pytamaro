"""
Functions for output (show or save) of graphics.
"""

import base64
import io
import os
import re
import subprocess
import sys
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import List

from PIL import Image as PILImageMod
from PIL.Image import Image as PILImage
from skia import (Canvas, FILEWStream, Image, Rect, Surface, SVGCanvas, kPNG,
                  kRGBA_8888_ColorType, kUnpremul_AlphaType)

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
    # Temporarily set the recursion limit to a high value so that we can
    # traverse the (potentially deeply nested) tree that represents the graphic.
    current_recursion_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(100000)
    graphic.draw(canvas)
    sys.setrecursionlimit(current_recursion_limit)


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
    stream.fsync()
    # Manually add shape-rendering="crispEdges" to the SVG file.
    # We don't use the XML parser from the standard library because,
    # among other aspects, it does not properly maintain the doctype.
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    # `svg` tag may be self-closing
    new_content = re.sub("<svg(.*?)(/?)>",
                         r'<svg\1 shape-rendering="crispEdges"\2>',
                         content)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(new_content)


def graphic_to_image(graphic: Graphic) -> Image:
    """
    Renders a graphic into a Skia image.

    :param graphic: graphic to be rendered
    :returns: rendered graphic as a Skia image
    """
    int_size = graphic.size().toRound()
    surface = Surface(int_size.width(), int_size.height())
    _draw_to_canvas(surface.getCanvas(), graphic)
    return surface.makeImageSnapshot()


def graphic_to_pillow_image(graphic: Graphic) -> PILImage:
    """
    Renders a graphic and converts it into a Pillow image.

    :param graphic: graphic to be rendered and converted
    :returns: rendered graphic as a Pillow image
    """
    return PILImageMod.fromarray(graphic_to_image(graphic).convert(
        alphaType=kUnpremul_AlphaType, colorType=kRGBA_8888_ColorType)
    )


# pylint: disable-next=invalid-name
def _save_as_PNG(filename: str, graphic: Graphic):
    """
    Save a graphic to a PNG file.

    :param filename: name of the file to be created, ending in ".png"
    :param graphic: graphic to be saved
    """
    graphic_to_image(graphic).save(filename, kPNG)


def _print_data_uri(mime_type: str, b64_content: str):
    """
    Prints a data URI to standard output with a special prefix and suffix so
    that it can be recognized in the context of a larger output.

    :param mime_type: MIME type of the data (e.g., "image/png")
    :param b64_content: base64-encoded content
    """
    prefix = "@@@PYTAMARO_DATA_URI_BEGIN@@@"
    suffix = "@@@PYTAMARO_DATA_URI_END@@@"
    uri = f"data:{mime_type};base64,{b64_content}"
    print(f"{prefix}{uri}{suffix}", end="")


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
    if graphic.empty_area():
        _warning_no_area(graphic)
    else:
        to_show = add_debug_info(graphic) if debug else graphic
        pil_image = graphic_to_pillow_image(to_show)
        if is_notebook():
            # pylint: disable-next=undefined-variable
            display(pil_image)  # type: ignore[name-defined]
        elif "PYTAMARO_OUTPUT_DATA_URI" in os.environ:
            buffer = io.BytesIO()
            pil_image.save(buffer, format="PNG")
            b64_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
            _print_data_uri("image/png", b64_str)
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
    check_type(debug, bool, "debug")
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
    pil_images = list(map(graphic_to_pillow_image, graphics))
    if len(set(image.size for image in pil_images)) != 1:
        raise ValueError(translate("DIFFERENT_SIZES"))
    check_type(duration, int, "duration")
    check_type(loop, bool, "loop")
    pil_images[0].save(
        filename,
        save_all=True,
        append_images=pil_images[1:],
        duration=duration,
        loop=0 if loop else 1,  # loop 0 means "indefinitely", 1 means "once"
        disposal=2,  # 2 means "after showing the frame, clear to background"
    )


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
        save_animation(file.name, graphics, duration, loop)
        if is_notebook():
            # pylint: disable-next=import-outside-toplevel, import-error
            from IPython.display import Image as IPythonImage  # type: ignore[import]
            with open(file.name, "rb") as stream:
                # pylint: disable-next=undefined-variable
                display(IPythonImage(stream.read()))  # type: ignore[name-defined]
        elif "PYTAMARO_OUTPUT_DATA_URI" in os.environ:
            with open(file.name, "rb") as stream:
                b64_str = base64.b64encode(stream.read()).decode("utf-8")
                _print_data_uri("image/gif", b64_str)
        elif sys.platform == "win32":
            os.startfile(file.name)
        elif sys.platform == "darwin":
            subprocess.call(["open", "-a", "Safari", file.name])
        else:
            subprocess.call(["xdg-open", file.name])
