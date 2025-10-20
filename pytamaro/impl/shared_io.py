""""Shared io functions between impl
    (that cannot be placed in the main io module to avoid circular dependencies)."""

import sys
from pytamaro.localization import translate


def area_message(error_message_key: str, width: float, height: float) -> str:
    """
    Emits a warning indicating that the graphic cannot be shown or saved
    because of a problem with its area.

    :param error_message_key: key for the error message
    :param graphic: graphic that cannot be shown or saved
    :returns: translated error message
    """
    return translate(error_message_key, f"{round(width)}x{round(height)}")


def print_data_uri(mime_type: str, b64_content: str):
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
    try:
        sys.stdout.flush()
    except AttributeError:
        # https://docs.python.org/3/library/sys.html#sys.stdout
        # > Under some conditions stdin, stdout and stderr as well as the
        # > original values __stdin__, __stdout__ and __stderr__ can be None
        pass
