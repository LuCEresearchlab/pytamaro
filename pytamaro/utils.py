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


def is_notebook() -> bool:
    """
    Checks whether we are running inside a Jupyter notebook.
    Adapted from
    https://stackoverflow.com/questions/15411967/how-can-i-check-if-code-is-executed-in-the-ipython-notebook/24937408

    :returns: True if running inside a notebook, False otherwise
    """
    try:
        shell = get_ipython().__class__.__name__  # type: ignore[name-defined]
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        if shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter
