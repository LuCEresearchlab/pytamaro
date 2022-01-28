"""
General utils.
"""

import sys


def export(fn):  # pylint: disable=invalid-name
    """
    Use a decorator to avoid retyping function/class names.
    """
    mod = sys.modules[fn.__module__]
    if hasattr(mod, '__all__'):
        name = fn.__name__
        all_ = mod.__all__
        if name not in all_:
            all_.append(name)
    else:
        setattr(mod, '__all__', [fn.__name__])
    return fn
