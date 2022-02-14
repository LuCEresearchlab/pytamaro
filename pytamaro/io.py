"""
Functions to do I/O with graphics, such as showing or saving them.
"""

from typing import List

from skia import kPNG

from pytamaro.debug import add_debug_info
from pytamaro.graphic import Graphic
from pytamaro.graphic_utils import graphic_to_image
from pytamaro.localization import translate
from pytamaro.utils import export, is_notebook


@export
def show_graphic(graphic: Graphic, debug: bool = False):
    """
    Show a graphic in a window. Empty graphics cannot be shown and produce no
    effect when shown using this function.

    When `debug` is `True`, adorns the visualization with useful information
    for debugging: a red border around the bounding box and a yellowish cross
    around the pinning position.

    :param graphic: graphic to be shown
    :param debug: can be optionally set to `True` to overlay debugging
           information
    """
    if not graphic.is_empty_graphic():
        to_show = add_debug_info(graphic) if debug else graphic
        pil_image = graphic_to_image(to_show)
        if is_notebook():
            # pylint: disable=undefined-variable
            display(pil_image)  # type: ignore[name-defined]
        else:
            pil_image.show()


@export
def save_graphic(filename: str, graphic: Graphic, debug: bool = False):
    """
    Save a graphic as a PNG file. Empty graphics cannot be saved and produce no
    effect when saved using this function.

    When `debug` is `True`, adorns the visualization with useful information
    for debugging: a red border around the bounding box and a yellowish cross
    around the pinning position.

    :param filename: name of the file to create (without the extension)
    :param graphic: graphic to be saved
    :param debug: can be optionally set to `True` to overlay debugging
           information
    """
    if not graphic.is_empty_graphic():
        to_show = add_debug_info(graphic) if debug else graphic
        image = to_show.as_image()
        image.save(f'{filename}.png', kPNG)


@export
def save_gif(filename: str, graphics: List[Graphic], duration: int = 40):
    """
    Save a sequence of graphics as an aminated GIF.

    Graphics are sequentially reproduced (normally at 25 frames per second) in
    a loop.

    :param filename: name of the file to create (without the extension)
    :param graphics: list of graphics to be saved as a GIF
    :param duration: duration in milliseconds for each frame
           (defaults to 40 milliseconds, which leads to 25 frames per second)
    """
    if len(graphics) == 0:
        raise ValueError(translate("EMPTY_GRAPHICS_LIST"))
    pil_images = list(map(graphic_to_image, graphics))
    pil_images[0].save(f"{filename}.gif", save_all=True,
                       append_images=pil_images[1:],
                       duration=duration,
                       loop=0)  # loop 0 means "loop indefinitely"
