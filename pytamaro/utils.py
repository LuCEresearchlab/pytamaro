"""General utility functions and shared datatypes."""

import importlib.util
import sys
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def export(fn: F) -> F:
    """Use a decorator to avoid retyping function/class names."""
    mod = sys.modules[fn.__module__]
    if hasattr(mod, "__all__"):
        name = fn.__name__
        all_ = mod.__all__
        if name not in all_:
            all_.append(name)
    else:
        mod.__all__ = [fn.__name__]  # type: ignore
    return fn


def is_notebook() -> bool:
    """Checks whether we are running inside a Jupyter notebook.

    Adapted from
    https://stackoverflow.com/questions/15411967/how-can-i-check-if-code-is-executed-in-the-ipython-notebook/24937408

    :returns: True if running inside a notebook, False otherwise
    """
    try:
        from IPython import get_ipython  # type: ignore[import]  # noqa: PLC0415

        if "IPKernelApp" not in get_ipython().config:
            return False
    except ImportError:
        return False
    except AttributeError:
        return False
    return True


__has_skia: bool | None = None


def has_skia() -> bool:
    """Check whether the skia module is available.

    :meta private:
    :returns: True if the "skia" python package is available
    """
    # Use global to cache the __has_skia value
    global __has_skia  # noqa: PLW0603
    if __has_skia is None:
        __has_skia = importlib.util.find_spec("skia") is not None
    return __has_skia


@dataclass
class ISize:
    """Version of Size but with integer values."""

    width: int
    height: int

    def empty_area(self) -> bool:
        """Check if the size represents an empty area (zero width or height)."""
        return self.width * self.height == 0

    def too_large_area(self) -> bool:
        """Check if the size is too large to fit in a 4GB surface,
        assuming 4 bytes per pixel.
        """
        sk_maxs32 = 2**31 - 1
        bytes_per_pixel = 4
        surface_size = self.width * self.height * bytes_per_pixel
        return surface_size > sk_maxs32


@dataclass
class Size:
    """Size representation for the dimensions of a graphic."""

    width: float
    height: float

    def to_round(self) -> ISize:
        """Round the size dimensions to the nearest integer values.

        :returns: ISize with the rounded dimensions
        """
        return ISize(round(self.width), round(self.height))


# A specification (Spec) of a graphic is a key-value mapping of its properties.
Spec = dict[str, Any]
