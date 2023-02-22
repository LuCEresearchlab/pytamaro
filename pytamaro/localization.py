"""Localization utilities to translate error messages"""
# pylint: disable=line-too-long

import sys

translations = {
    # Error messages
    "INVALID_LENGTH": {
        "en": "Invalid length for parameter {}",
        "it": "Lunghezza non valida per il parametro {}",
        "de": "",
    },
    "INVALID_TYPE": {
        "en": "Invalid type for parameter {}: expected {}, got {}",
        "it": "Tipo non valido per il parametro {}: previsto {}, ottenuto {}",
        "de": "",
    },
    "INVALID_RANGE": {
        "en": "Value for parameter {} out of the allowed range [{}, {}]",
        "it": "Valore per il parametro {} fuori dall'intervallo consentito [{}, {}]",
        "de": "",
    },
    "INVALID_FILENAME_EXTENSION": {
        "en": "Invalid or missing extension for filename: only .png and .svg are supported",
        "it": "Estensione non valida o mancante per il nome del file: sono supportati solo .png e .svg",
        "de": "",
    },
    "INVALID_FILENAME_GIF": {
        "en": "Invalid or missing extension for a GIF file: needs to end with `.gif`",
        "it": "Estensione non valida o mancante per un file GIF: deve terminare con `.gif`",
        "de": "",
    },
    "EMPTY_GRAPHICS_LIST": {
        "en": "The list of graphics cannot be empty",
        "it": "La lista delle grafiche non può essere vuota",
        "de": "",
    },
    "EMPTY_AREA_OUTPUT": {
        "en": "Cannot show/save a graphic of size {} as it has no area",
        "it": "Impossibile mostrare/salvare una grafica di dimensione {} poiché non ha area",
        "de": "",
    },
    # Parameter names
    "width": {
        "en": "width",
        "it": "larghezza",
        "de": "",
    },
    "height": {
        "en": "height",
        "it": "altezza",
        "de": "",
    },
    "radius": {
        "en": "radius",
        "it": "raggio",
        "de": "",
    },
    "red": {
        "en": "red",
        "it": "rosso",
        "de": "",
    },
    "green": {
        "en": "green",
        "it": "verde",
        "de": "",
    },
    "blue": {
        "en": "blue",
        "it": "blu",
        "de": "",
    },
    "opacity": {
        "en": "opacity",
        "it": "opacita",
        "de": "",
    },
    "hue": {
        "en": "hue",
        "it": "tonalita",
        "de": "",
    },
    "saturation": {
        "en": "saturation",
        "it": "saturazione",
        "de": "",
    },
    "value": {
        "en": "value",
        "it": "valore",
        "de": "",
    },
    "lightness": {
        "en": "lightness",
        "it": "luce",
        "de": "",
    },
    "angle": {
        "en": "angle",
        "it": "angolo",
        "de": "",
    },
    "side1": {
        "en": "side1",
        "it": "lato1",
        "de": "",
    },
    "side2": {
        "en": "side2",
        "it": "lato2",
        "de": "",
    },
    "content": {
        "en": "content",
        "it": "contenuto",
        "de": "",
    },
    "foreground_graphic": {
        "en": "foreground_graphic",
        "it": "grafica_primopiano",
        "de": "",
    },
    "background_graphic": {
        "en": "background_graphic",
        "it": "grafica_secondopiano",
        "de": "",
    },
    "left_graphic": {
        "en": "left_graphic",
        "it": "grafica_sinistra",
        "de": "",
    },
    "right_graphic": {
        "en": "right_graphic",
        "it": "grafica_destra",
        "de": "",
    },
    "top_graphic": {
        "en": "top_graphic",
        "it": "grafica_alto",
        "de": "",
    },
    "bottom_graphic": {
        "en": "bottom_graphic",
        "it": "grafica_basso",
        "de": "",
    },
    "filename": {
        "en": "filename",
        "it": "nome_file",
        "de": "",
    },
    "graphics": {
        "en": "graphics",
        "it": "grafiche",
        "de": "",
    },
    "graphic": {
        "en": "graphic",
        "it": "grafica",
        "de": "",
    },
    "color": {
        "en": "color",
        "it": "colore",
        "de": "",
    },
    "point": {
        "en": "point",
        "it": "punto",
        "de": "",
    },
    "font": {
        "en": "font",
        "it": "font",
        "de": "",
    },
    "points": {
        "en": "points",
        "it": "punti",
        "de": "",
    },
    # Types
    "Graphic": {
        "en": "Graphic",
        "it": "Grafica",
        "de": "",
    },
    "Color": {
        "en": "Color",
        "it": "Colore",
        "de": "",
    },
    "Point": {
        "en": "Point",
        "it": "Punto",
        "de": "",
    },
}


def translate(key: str, *args) -> str:
    """Looks up an error message by `key` and returns the localized version.

    :param key: error message key
    :param args: optional arguments to be formatted into the localized message
    :returns: locale-specific descriptive error message
    """
    lang = sys.modules["pytamaro"].LANGUAGE
    if key not in translations:
        return key
    localized = translations[key][lang]
    if len(localized) == 0:
        localized = translations[key]["en"]
    return localized.format(*args)
