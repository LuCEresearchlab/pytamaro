import json
import subprocess
from pathlib import Path

import lxml.etree as ET
import xmltodict

OUTPUT_DIR = Path("_build/judicious")
subprocess.run(["make", "xml"])
subprocess.run(["rm", "-rf", str(OUTPUT_DIR)])
subprocess.run(["mkdir", str(OUTPUT_DIR)])


xslt_transform = ET.XSLT(ET.parse("judicious.xslt"))


def plural(element_type):
    return element_type + "s"


def postprocessor(path, key, value):
    if key == "parameter":
        return plural(key), value
    if key == "sideEffects":
        return key, True if value == "true" else False
    return key, value


def pytamaro_module(folder_name):
    if folder_name == "English":
        return "pytamaro"
    elif folder_name == "French":
        return "pytamaro.fr"
    elif folder_name == "German":
        return "pytamaro.de"
    elif folder_name == "Italian":
        return "pytamaro.it"


for languagedir in [el for el in Path("_build/xml").iterdir() if el.is_dir()]:
    module_name = pytamaro_module(languagedir.name)
    docs = {"module": module_name, "elements": []}
    for filename in languagedir.glob("*.xml"):
        xml = ET.parse(filename)
        new_xml = xslt_transform(xml)
        new_xml_as_dict = xmltodict.parse(ET.tostring(new_xml, encoding='unicode'), force_list=['element', 'p'], postprocessor=postprocessor)
        docs["elements"].extend(new_xml_as_dict['elements']["element"])
    output_path = OUTPUT_DIR / (module_name + ".json")
    with open(output_path, "w") as f:
        f.write(json.dumps(docs, indent=4))
    print("Wrote", output_path)
