"""Localization utilities to translate error messages"""
# pylint: disable=line-too-long

import sys

translations = {
    # Error messages
    "INVALID_LENGTH": {
        "en": "Invalid length for parameter {}",
        "it": "Lunghezza non valida per il parametro {}",
        "de": "Ungültige Länge für den Parameter {}",
    },
    "INVALID_TYPE": {
        "en": "Invalid type for parameter {}: expected {}, got {}",
        "it": "Tipo non valido per il parametro {}: previsto {}, ottenuto {}",
        "de": "Ungültiger Typ für den Parameter {}: erwartet {}, erhalten {}",
    },
    "INVALID_RANGE": {
        "en": "Value for parameter {} out of the allowed range [{}, {}]",
        "it": "Valore per il parametro {} fuori dall'intervallo consentito [{}, {}]",
        "de": "Wert für den Parameter {} außerhalb des zulässigen Bereichs [{}, {}]",
    },
    "INVALID_FILENAME_EXTENSION": {
        "en": "Invalid or missing extension for filename: only .png and .svg are supported",
        "it": "Estensione non valida o mancante per il nome del file: sono supportati solo .png e .svg",
        "de": "Ungültige oder fehlende Dateinamenerweiterung: Nur .png und .svg werden unterstützt",
    },
    "INVALID_FILENAME_GIF": {
        "en": "Invalid or missing extension for a GIF file: needs to end with `.gif`",
        "it": "Estensione non valida o mancante per un file GIF: deve terminare con `.gif`",
        "de": "Ungültige oder fehlende Dateinamenerweiterung für eine GIF-Datei: muss mit `.gif` enden",
    },
    "EMPTY_GRAPHICS_LIST": {
        "en": "The list of graphics cannot be empty",
        "it": "La lista delle grafiche non può essere vuota",
        "de": "Die Liste der Grafiken darf nicht leer sein",
    },
    "EMPTY_AREA_OUTPUT": {
        "en": "Cannot show/save a graphic of size {} as it has no area",
        "it": "Impossibile mostrare/salvare una grafica di dimensione {} poiché non ha area",
        "de": "Kann eine Grafik der Größe {} nicht anzeigen/speichern, da sie keine Fläche hat",
    },
    # Parameter names
    "width": {
        "en": "width",
        "it": "larghezza",
        "de": "breite",
    },
    "height": {
        "en": "height",
        "it": "altezza",
        "de": "hoehe",
    },
    "radius": {
        "en": "radius",
        "it": "raggio",
        "de": "radius",
    },
    "red": {
        "en": "red",
        "it": "rosso",
        "de": "rot",
    },
    "green": {
        "en": "green",
        "it": "verde",
        "de": "gruen",
    },
    "blue": {
        "en": "blue",
        "it": "blu",
        "de": "blau",
    },
    "opacity": {
        "en": "opacity",
        "it": "opacita",
        "de": "opazitaet",
    },
    "hue": {
        "en": "hue",
        "it": "tonalita",
        "de": "farbton",
    },
    "saturation": {
        "en": "saturation",
        "it": "saturazione",
        "de": "saettigung",
    },
    "value": {
        "en": "value",
        "it": "valore",
        "de": "hellwert",
    },
    "lightness": {
        "en": "lightness",
        "it": "luce",
        "de": "helligkeit",
    },
    "angle": {
        "en": "angle",
        "it": "angolo",
        "de": "winkel",
    },
    "side1": {
        "en": "side1",
        "it": "lato1",
        "de": "seite1",
    },
    "side2": {
        "en": "side2",
        "it": "lato2",
        "de": "seite2",
    },
    "content": {
        "en": "content",
        "it": "contenuto",
        "de": "inhalt",
    },
    "foreground_graphic": {
        "en": "foreground_graphic",
        "it": "grafica_primopiano",
        "de": "vordere_grafik",
    },
    "background_graphic": {
        "en": "background_graphic",
        "it": "grafica_secondopiano",
        "de": "hintere_grafik",
    },
    "left_graphic": {
        "en": "left_graphic",
        "it": "grafica_sinistra",
        "de": "linke_grafik",
    },
    "right_graphic": {
        "en": "right_graphic",
        "it": "grafica_destra",
        "de": "rechte_grafik",
    },
    "top_graphic": {
        "en": "top_graphic",
        "it": "grafica_alto",
        "de": "obere_grafik",
    },
    "bottom_graphic": {
        "en": "bottom_graphic",
        "it": "grafica_basso",
        "de": "untere_grafik",
    },
    "filename": {
        "en": "filename",
        "it": "nome_file",
        "de": "datei_name",
    },
    "graphics": {
        "en": "graphics",
        "it": "grafiche",
        "de": "grafiken",
    },
    "graphic": {
        "en": "graphic",
        "it": "grafica",
        "de": "grafiken",
    },
    "color": {
        "en": "color",
        "it": "colore",
        "de": "farbe",
    },
    "point": {
        "en": "point",
        "it": "punto",
        "de": "punkt",
    },
    "font": {
        "en": "font",
        "it": "font",
        "de": "schriftart",
    },
    "points": {
        "en": "points",
        "it": "punti",
        "de": "punkte",
    },
    # Types
    "Graphic": {
        "en": "Graphic",
        "it": "Grafica",
        "de": "Grafik",
    },
    "Color": {
        "en": "Color",
        "it": "Colore",
        "de": "Farbe",
    },
    "Point": {
        "en": "Point",
        "it": "Punto",
        "de": "Punkt",
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
