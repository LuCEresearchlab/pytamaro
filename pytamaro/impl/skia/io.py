"""Skia-based implementation of I/O functions.

:meta private:
"""

import base64
import io
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import cast

from PIL import Image as PILImageMod
from PIL.Image import Image as PILImage
from skia import (
    Canvas,
    FILEWStream,
    FilterMode,
    Image,
    MipmapMode,
    Rect,
    SamplingOptions,
    Surface,
    SVGCanvas,
    kPNG,
    kRGBA_8888_ColorType,
    kUnpremul_AlphaType,
)

from pytamaro.checks import area_message, check_graphic_size
from pytamaro.graphic import Graphic
from pytamaro.impl.shared_io import guess_scaling_factor, print_data_uri
from pytamaro.impl.skia.debug import add_debug_info
from pytamaro.impl.skia.graphic import SkiaGraphic
from pytamaro.localization import translate
from pytamaro.utils import ISize, Size, is_notebook

# ruff: noqa: D103


def graphic_size(graphic: Graphic) -> Size:
    graphic = cast(SkiaGraphic, graphic)
    skia_size = graphic.size()
    return Size(skia_size.width(), skia_size.height())


def _draw_to_canvas(canvas: Canvas, graphic: SkiaGraphic):
    """Draw a graphic to a canvas, correcting for the top-left position.

    :param canvas: canvas onto which to draw
    :param graphic: graphic to be drawn
    """
    bounds = graphic.bounds
    canvas.translate(-bounds.left(), -bounds.top())
    # Temporarily set the recursion limit to a high value so that we can
    # traverse the (potentially deeply nested) tree that represents the graphic.
    current_recursion_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(100000)
    graphic.draw(canvas)
    sys.setrecursionlimit(current_recursion_limit)


def _save_as_SVG(filename: str, graphic: SkiaGraphic):
    """Save a graphic to an SVG file.

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
    with open(filename, encoding="utf-8") as file:
        content = file.read()
    # `svg` tag may be self-closing
    new_content = re.sub("<svg(.*?)(/?)>", r'<svg\1 shape-rendering="crispEdges"\2>', content)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(new_content)


def graphic_to_image(graphic: SkiaGraphic) -> Image:
    """Render a graphic into a Skia image.

    :param graphic: graphic to be rendered
    :returns: rendered graphic as a Skia image
    """
    skia_size = graphic.size()
    width, height = skia_size.toRound()
    rounded_size = ISize(width, height)
    if rounded_size.too_large_area():
        raise ValueError(
            area_message("TOO_LARGE_AREA_OUTPUT", skia_size.width(), skia_size.height())
        )
    scaling_factor = guess_scaling_factor(rounded_size)
    surface = Surface(width * scaling_factor, height * scaling_factor)
    surface.getCanvas().scale(scaling_factor, scaling_factor)
    _draw_to_canvas(surface.getCanvas(), graphic)
    return surface.makeImageSnapshot().resize(
        width, height, SamplingOptions(FilterMode.kLinear, MipmapMode.kNearest)
    )


def graphic_to_pillow_image(graphic: Graphic) -> PILImage:
    """Render a graphic and converts it into a Pillow image.

    :param graphic: graphic to be rendered and converted
    :returns: rendered graphic as a Pillow image
    """
    rounded_size = graphic_size(graphic).to_round()
    check_graphic_size(rounded_size)
    graphic = cast(SkiaGraphic, graphic)
    return PILImageMod.fromarray(
        graphic_to_image(graphic).convert(
            alphaType=kUnpremul_AlphaType, colorType=kRGBA_8888_ColorType
        )
    )


def _save_as_PNG(filename: str, graphic: SkiaGraphic):
    """Save a graphic to a PNG file.

    :param filename: name of the file to be created, ending in ".png"
    :param graphic: graphic to be saved
    """
    graphic_to_image(graphic).save(filename, kPNG)


def show_graphic(graphic: Graphic, debug: bool):
    graphic = cast(SkiaGraphic, graphic)
    rounded_size = graphic_size(graphic).to_round()
    check_graphic_size(rounded_size)
    to_show = add_debug_info(graphic) if debug else graphic
    pil_image = graphic_to_pillow_image(to_show)
    if is_notebook():
        display(pil_image)  # type: ignore[name-defined]  # noqa: F821
    elif "PYTAMARO_OUTPUT_DATA_URI" in os.environ:
        buffer = io.BytesIO()
        pil_image.save(buffer, format="PNG")
        b64_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
        print_data_uri("image/png", b64_str)
    else:
        pil_image.show()


def save_graphic(filename: str, graphic: Graphic, debug: bool):
    graphic = cast(SkiaGraphic, graphic)
    to_show = add_debug_info(graphic) if debug else graphic
    extension = Path(filename).suffix
    if extension == ".png":
        rounded_size = graphic_size(graphic).to_round()
        check_graphic_size(rounded_size)
        _save_as_PNG(filename, to_show)
    elif extension == ".svg":
        _save_as_SVG(filename, to_show)
    else:
        raise ValueError(translate("INVALID_FILENAME_EXTENSION"))


def show_animation(filename: str):
    if is_notebook():
        from IPython.display import Image as IPythonImage  # type: ignore[import]

        with open(filename, "rb") as stream:
            display(IPythonImage(stream.read()))  # type: ignore[name-defined]  # noqa: F821
    elif "PYTAMARO_OUTPUT_DATA_URI" in os.environ:
        with open(filename, "rb") as stream:
            b64_str = base64.b64encode(stream.read()).decode("utf-8")
            print_data_uri("image/gif", b64_str)
    elif sys.platform == "win32":
        os.startfile(filename)
    elif sys.platform == "darwin":
        subprocess.call(["open", "-a", "Safari", filename])
    else:
        subprocess.call(["xdg-open", filename])


def save_animation_extra(filename: str):
    # No need to do anything else for the skia implementation
    pass
