"""Localization utilities to translate error messages"""
# pylint: disable=line-too-long

import sys

translations = {
    # Error messages
    "INVALID_LENGTH": {
        "en": "Invalid length for parameter {}",
        "it": "Lunghezza non valida per il parametro {}",
        "de": "Ungültige Länge für den Parameter {}",
        "fr": "Longeur invalide pour paramètre {}",
    },
    "INVALID_TYPE": {
        "en": "Invalid type for parameter {}: expected {}, got {}",
        "it": "Tipo non valido per il parametro {}: previsto {}, ottenuto {}",
        "de": "Ungültiger Typ für den Parameter {}: erwartet {}, erhalten {}",
        "fr": "Type invalid pour le paramètre {}: attendu {}, eu {}"
    },
    "INVALID_RANGE": {
        "en": "Value for parameter {} out of the allowed range [{}, {}]",
        "it": "Valore per il parametro {} fuori dall'intervallo consentito [{}, {}]",
        "de": "Wert für den Parameter {} außerhalb des zulässigen Bereichs [{}, {}]",
        "fr": "Valeur pour le paramètre {} est hors de l'interval autorisé [{}, {}]",
    },
    "INVALID_FILENAME_EXTENSION": {
        "en": "Invalid or missing extension for filename: only .png and .svg are supported",
        "it": "Estensione non valida o mancante per il nome del file: sono supportati solo .png e .svg",
        "de": "Ungültige oder fehlende Dateinamenerweiterung: Nur .png und .svg werden unterstützt",
        "fr": "Extension non-valid ou mancante pour le nom du fichier: sont supportées seulement .png et .svg",
    },
    "INVALID_FILENAME_GIF": {
        "en": "Invalid or missing extension for a GIF file: needs to end with `.gif`",
        "it": "Estensione non valida o mancante per un file GIF: deve terminare con `.gif`",
        "de": "Ungültige oder fehlende Dateinamenerweiterung für eine GIF-Datei: muss mit `.gif` enden",
        "fr": "Extension invalide ou manquante pour un fichier GIF: doit terminer en `.gif`",
    },
    "EMPTY_GRAPHICS_LIST": {
        "en": "The list of graphics cannot be empty",
        "it": "La lista delle grafiche non può essere vuota",
        "de": "Die Liste der Grafiken darf nicht leer sein",
        "fr": "La list de graphiques ne peut pas être vide",
    },
    "EMPTY_AREA_OUTPUT": {
        "en": "Cannot show/save a graphic of size {} as it has no area",
        "it": "Impossibile mostrare/salvare una grafica di dimensione {} poiché non ha area",
        "de": "Kann eine Grafik der Größe {} nicht anzeigen/speichern, da sie keine Fläche hat",
        "fr": "Impossible de montrer/sauvegarder un graphiqye de dimensions {} vu qu'il ne possède pas de surface",
    },
    "FONT_NOT_FOUND": {
        "en": "Cannot find font '{}', another font used as fallback",
        "it": "Impossibile trovare il font '{}', un altro font è stato usato come alternativa",
        "de": "Schriftart '{}' nicht gefunden, eine andere Schriftart wird als Fallback verwendet",
        "fr": "Impossible de trouver la police '{}', une autre police est utilisée comme alternative",
    },
    "DIFFERENT_SIZES": {
        "en": "All graphics in the list must have the same size",
        "it": "Tutte le grafiche nella lista devono avere le stesse dimensioni",
        "de": "Alle Grafiken in der Liste müssen die gleiche Größe haben",
        "fr": "Tous les graphiques dans la liste doivent avoir la même taille",
    },
    # Function names
    "compose": {
        "en": "compose",
        "it": "componi",
        "de": "kombiniere",
        "fr": "compose",
    },
    "pin": {
        "en": "pin",
        "it": "fissa",
        "de": "fixiere",
        "fr": "ancre",
    },
    "overlay": {
        "en": "overlay",
        "it": "sovrapponi",
        "de": "ueberlagere",
        "fr": "superpose",
    },
    "beside": {
        "en": "beside",
        "it": "accanto",
        "de": "neben",
        "fr": "cote_a_cote",
    },
    "above": {
        "en": "above",
        "it": "sopra",
        "de": "ueber",
        "fr": "au_dessus",
    },
    "rotate": {
        "en": "rotate",
        "it": "ruota",
        "de": "drehe",
        "fr": "pivote",
    },
    "rgb_color": {
        "en": "rgb_color",
        "it": "colore_rgb",
        "de": "rgb_farbe",
        "fr": "couleur_rgb",
    },
    "rectangle": {
        "en": "rectangle",
        "it": "rettangolo",
        "de": "rechteck",
        "fr": "rectangle",
    },
    "empty_graphic": {
        "en": "empty_graphic",
        "it": "grafica_vuota",
        "de": "leere_grafik",
        "fr": "graphique_vide",
    },
    "ellipse": {
        "en": "ellipse",
        "it": "ellisse",
        "de": "ellipse",
        "fr": "ellipse",
    },
    "text": {
        "en": "text",
        "it": "testo",
        "de": "text",
        "fr": "text",
    },
    "circular_sector": {
        "en": "circular_sector",
        "it": "settore_circolare",
        "de": "kreissektor",
        "fr": "secteur_circulaire",
    },
    "triangle": {
        "en": "triangle",
        "it": "triangolo",
        "de": "dreieck",
        "fr": "triangle",
    },
    # Parameter names
    "width": {
        "en": "width",
        "it": "larghezza",
        "de": "breite",
        "fr": "largeur",
    },
    "height": {
        "en": "height",
        "it": "altezza",
        "de": "hoehe",
        "fr": "hauteur",
    },
    "radius": {
        "en": "radius",
        "it": "raggio",
        "de": "radius",
        "fr": "rayon",
    },
    "opacity": {
        "en": "opacity",
        "it": "opacita",
        "de": "opazitaet",
        "fr": "opacite",
    },
    "hue": {
        "en": "hue",
        "it": "tonalita",
        "de": "farbton",
        "fr": "teinte",
    },
    "saturation": {
        "en": "saturation",
        "it": "saturazione",
        "de": "saettigung",
        "fr": "saturation",
    },
    "value": {
        "en": "value",
        "it": "valore",
        "de": "hellwert",
        "fr": "valeur",
    },
    "lightness": {
        "en": "lightness",
        "it": "luce",
        "de": "helligkeit",
        "fr": "luminosite",
    },
    "angle": {
        "en": "angle",
        "it": "angolo",
        "de": "winkel",
        "fr": "angle",
    },
    "side1": {
        "en": "side1",
        "it": "lato1",
        "de": "seite1",
        "fr": "cote1",
    },
    "side2": {
        "en": "side2",
        "it": "lato2",
        "de": "seite2",
        "fr": "cote2",
    },
    "content": {
        "en": "content",
        "it": "contenuto",
        "de": "inhalt",
        "fr": "contenu",
    },
    "foreground_graphic": {
        "en": "foreground_graphic",
        "it": "grafica_primopiano",
        "de": "vordere_grafik",
        "fr": "graphique_premier_plan",
    },
    "background_graphic": {
        "en": "background_graphic",
        "it": "grafica_secondopiano",
        "de": "hintere_grafik",
        "fr": "graphique_arriere_plan",
    },
    "left_graphic": {
        "en": "left_graphic",
        "it": "grafica_sinistra",
        "de": "linke_grafik",
        "fr": "graphique_gauche",
    },
    "right_graphic": {
        "en": "right_graphic",
        "it": "grafica_destra",
        "de": "rechte_grafik",
        "fr": "graphique_droite",
    },
    "top_graphic": {
        "en": "top_graphic",
        "it": "grafica_alto",
        "de": "obere_grafik",
        "fr": "graphique_haut",
    },
    "bottom_graphic": {
        "en": "bottom_graphic",
        "it": "grafica_basso",
        "de": "untere_grafik",
        "fr": "graphique_bas",
    },
    "filename": {
        "en": "filename",
        "it": "nome_file",
        "de": "datei_name",
        "fr": "nom_fichier",
    },
    "graphics": {
        "en": "graphics",
        "it": "grafiche",
        "de": "grafiken",
        "fr": "graphiques",
    },
    "graphic": {
        "en": "graphic",
        "it": "grafica",
        "de": "grafiken",
        "fr": "graphique",
    },
    "color": {
        "en": "color",
        "it": "colore",
        "de": "farbe",
        "fr": "couleur",
    },
    "point": {
        "en": "point",
        "it": "punto",
        "de": "punkt",
        "fr": "point",
    },
    "font": {
        "en": "font",
        "it": "font",
        "de": "schriftart",
        "fr": "police",
    },
    "points": {
        "en": "points",
        "it": "punti",
        "de": "punkte",
        "fr": "points",
    },
    "debug": {
        "en": "debug",
        "it": "debug",
        "de": "debug",
        "fr": "debug",
    },
    "duration": {
        "en": "duration",
        "it": "durata",
        "de": "dauer",
        "fr": "duree",
    },
    "loop": {
        "en": "loop",
        "it": "loop",
        "de": "loop",
        "fr": "en_boucle",
    },
    # Types
    "Graphic": {
        "en": "Graphic",
        "it": "Grafica",
        "de": "Grafik",
        "fr": "Graphique",
    },
    "Color": {
        "en": "Color",
        "it": "Colore",
        "de": "Farbe",
        "fr": "Couleur",
    },
    "Point": {
        "en": "Point",
        "it": "Punto",
        "de": "Punkt",
        "fr": "Point",
    },
    # Known Points
    "center": {
        "en": "center",
        "it": "centro",
        "de": "mitte",
        "fr": "centre",
    },
    "top_center": {
        "en": "top_center",
        "it": "alto_centro",
        "de": "oben_mitte",
        "fr": "haut_centre",
    },
    "bottom_center": {
        "en": "bottom_center",
        "it": "basso_centro",
        "de": "unten_mitte",
        "fr": "bas_centre",
    },
    "center_left": {
        "en": "center_left",
        "it": "centro_sinistra",
        "de": "mitte_links",
        "fr": "centre_gauche",
    },
    "center_right": {
        "en": "center_right",
        "it": "centro_destra",
        "de": "mitte_rechts",
        "fr": "centre_droite",
    },
    "top_left": {
        "en": "top_left",
        "it": "alto_sinistra",
        "de": "oben_links",
        "fr": "haut_gauche",
    },
    "top_right": {
        "en": "top_right",
        "it": "alto_destra",
        "de": "oben_rechts",
        "fr": "haut_droite",
    },
    "bottom_left": {
        "en": "bottom_left",
        "it": "basso_sinistra",
        "de": "unten_links",
        "fr": "bas_gauche",
    },
    "bottom_right": {
        "en": "bottom_right",
        "it": "basso_destra",
        "de": "unten_rechts",
        "fr": "bas_droite",
    },
    # Known Colors
    "black": {
        "en": "black",
        "it": "nero",
        "de": "schwarz",
        "fr": "noir",
    },
    "red": {
        "en": "red",
        "it": "rosso",
        "de": "rot",
        "fr": "rouge",
    },
    "green": {
        "en": "green",
        "it": "verde",
        "de": "gruen",
        "fr": "vert",
    },
    "blue": {
        "en": "blue",
        "it": "blu",
        "de": "blau",
        "fr": "bleu",
    },
    "yellow": {
        "en": "yellow",
        "it": "giallo",
        "de": "gelb",
        "fr": "jaune",
    },
    "magenta": {
        "en": "magenta",
        "it": "magenta",
        "de": "magenta",
        "fr": "magenta",
    },
    "cyan": {
        "en": "cyan",
        "it": "ciano",
        "de": "cyan",
        "fr": "cyan",
    },
    "white": {
        "en": "white",
        "it": "bianco",
        "de": "weiss",
        "fr": "blanc",
    },
    "transparent": {
        "en": "transparent",
        "it": "trasparente",
        "de": "transparent",
        "fr": "transparent",
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
