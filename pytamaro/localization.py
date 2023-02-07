"""Localization utilities to translate error messages"""

import sys

translations = {
    "INVALID_SIZE": {
        "en": "Invalid size (must be a positive number)",
        "it": "Dimensione non valida (deve essere un numero positivo)",
        "de": ""
    },
    "EMPTY_GRAPHICS_LIST": {
        "en": "The list of graphics cannot be empty",
        "it": "La lista delle grafiche non può essere vuota",
        "de": ""
    },
    "EMPTY_AREA_OUTPUT_PREFIX": {
        "en": "Cannot show/save a graphic of size",
        "it": "Impossibile mostrare/salvare una grafica di dimensione",
        "de": ""
    },
    "EMPTY_AREA_OUTPUT_SUFFIX": {
        "en": "as it has no area",
        "it": "poiché non ha area",
        "de": ""
    },
}


def translate(key: str) -> str:
    """Looks up an error message by `key` and returns the localized version.

    :param key: error message key
    :returns: locale-specific descriptive error message
    """
    lang = sys.modules["pytamaro"].LANGUAGE
    return translations[key][lang]
