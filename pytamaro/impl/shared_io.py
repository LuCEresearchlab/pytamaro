"""Shared io functions between impl
   (that cannot be placed in the main io module to avoid circular dependencies)."""

import sys
from pytamaro.utils import ISize


def print_data_uri(mime_type: str, b64_content: str):
    """
    Prints a data URI to standard output with a special prefix and suffix so
    that it can be recognized in the context of a larger output.

    :param mime_type: MIME type of the data (e.g., "image/png")
    :param b64_content: base64-encoded content
    """
    prefix = "@@@PYTAMARO_DATA_URI_BEGIN@@@"
    suffix = "@@@PYTAMARO_DATA_URI_END@@@"
    print(f"{prefix}data:{mime_type};base64,{b64_content}{suffix}", end="")
    try:
        sys.stdout.flush()
    except AttributeError:
        # https://docs.python.org/3/library/sys.html#sys.stdout
        # > Under some conditions stdin, stdout and stderr as well as the
        # > original values __stdin__, __stdout__ and __stderr__ can be None
        pass


def guess_scaling_factor(rounded_size: ISize) -> int:
    """
    Makes an educated guess for a reasonable scaling factor (for super-sampling),
    based on the area of the graphic.
    """
    pixels = rounded_size.width * rounded_size.height
    if pixels <= 300 * 300:
        return 3
    if pixels <= 3_000 * 3_000:
        return 2
    # No scaling
    return 1
