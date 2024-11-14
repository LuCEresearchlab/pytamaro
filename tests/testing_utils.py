import importlib
import xml.etree.ElementTree as ET
from dataclasses import astuple
from typing import List, Tuple

from PIL import ImageChops, ImageFilter
from PIL.Image import Image

from pytamaro.color import Color
from pytamaro.color_names import transparent
from pytamaro.graphic import Graphic
from pytamaro.io import graphic_to_image, graphic_to_pillow_image
from pytamaro.operations import graphic_height, graphic_width
from pytamaro.point import Point

WIDTH = 10
HEIGHT = 20
RADIUS = 20


def pixels_colors(g: Graphic) -> List[int]:
    bitmap = graphic_to_image(g).bitmap()
    return [bitmap.getColor(x, y)
            for y in range(bitmap.height()) for x in range(bitmap.width())]


def assert_unique_color(g: Graphic,
                        color: Color):
    all_colors = pixels_colors(g)
    colors = set(filter(lambda c: c != int(transparent.skia_color), all_colors))
    assert len(colors) == 1
    assert int(color.skia_color) in colors


def assert_color(g: Graphic, color: Color):
    assert int(color.skia_color) in pixels_colors(g)


def assert_size(g: Graphic, expected_size: Tuple[int, int]):
    assert_size_tolerance(g, expected_size, tolerance=0)


def assert_value_tolerance(actual_value: float, expected_value: float, tolerance: float):
    assert expected_value * (1 - tolerance) <= actual_value <= expected_value * (1 + tolerance)


def assert_size_tolerance(g: Graphic, expected_size: Tuple[int, int],
                          tolerance: float = 0.02):
    # 2% of tolerance by default
    assert_value_tolerance(graphic_width(g), expected_size[0], tolerance)
    assert_value_tolerance(graphic_height(g), expected_size[1], tolerance)


def assert_graphics_equals_tolerance(g1: Graphic, g2: Graphic):
    diff = ImageChops.difference(graphic_to_pillow_image(g1), graphic_to_pillow_image(g2))
    filtered_diff = diff.filter(ImageFilter.MinFilter())
    colors = filtered_diff.getcolors() or []
    assert len(colors) == 1
    assert colors[0][1] == astuple(transparent)


def assert_pin_tolerance(g: Graphic, expected_pin: Tuple[int, int]):
    x_pin, y_pin = g.pin_position
    assert expected_pin[0] - 1 <= x_pin <= expected_pin[0] + 1
    assert expected_pin[1] - 1 <= y_pin <= expected_pin[1] + 1


def assert_equals_rendered(g1: Graphic, g2: Graphic):
    assert graphic_to_image(g1).tobytes() == graphic_to_image(g2).tobytes()


def assert_SVG_file_width_height(filename: str, width: float, height: float):
    tree = ET.parse(filename)
    root = tree.getroot()
    assert root.attrib["width"] == str(width)
    assert root.attrib["height"] == str(height)
    assert root.attrib["shape-rendering"] == "crispEdges"


def assert_repr(obj: Graphic | Point | Color, language: str):
    # Import all the names from pytamaro.{language}, so that eval can work.
    import importlib
    module = importlib.import_module("." if language == "en" else f".{language}", "pytamaro")
    names = [n for n in module.__dict__ if not n.startswith("_")]
    globals().update({n: getattr(module, n) for n in names})
    # Set LANGUAGE so that repr produces a localized string.
    import sys
    sys.modules["pytamaro"].LANGUAGE = language  # type: ignore
    # Assert that evaluating the repr yields the same graphic.
    assert eval(repr(obj)) == obj


def assert_frames_count(im: Image, n_frames: int):
    assert getattr(im, "n_frames", 1) == n_frames
