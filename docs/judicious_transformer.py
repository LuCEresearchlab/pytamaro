# /// script
# dependencies = [
#   "lxml",
#   "xmltodict",
#   "pytamaro==1.1.3",
# ]
# ///


"""
Run this script with:
> uv run --prerelease=allow judicious_transformer.py
"""
import ast
import json
import os
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

import lxml.etree as ET
import xmltodict

OUTPUT_DIR = Path("_build/judicious")
EXAMPLES_EXECUTION_DIR = TemporaryDirectory()
subprocess.run(["make", "xml"])
subprocess.run(["rm", "-rf", str(OUTPUT_DIR)])
subprocess.run(["mkdir", str(OUTPUT_DIR)])


xslt_transform = ET.XSLT(ET.parse("judicious.xslt"))


def plural(element_type):
    return element_type + "s"


def postprocessor(path, key, value):
    if key == "parameters":
        return key, value["parameter"] if value is not None else []
    if key == "sideEffects":
        return key, True if value == "true" else False
    return key, value


def pytamaro_module(folder_name):
    if folder_name == "English":
        return "pytamaro", "en"
    elif folder_name == "French":
        return "pytamaro.fr", "fr"
    elif folder_name == "German":
        return "pytamaro.de", "de"
    elif folder_name == "Italian":
        return "pytamaro.it", "it"


def localize_code(code, lang):
    sys.path.append(os.path.join(os.path.dirname(__file__), '../pytamaro'))
    from localization import translations
    tree = ast.parse(code)
    # Replace all names in the tree with their localized version
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if node.id in translations:
                node.id = translations[node.id][lang]
    code = ast.unparse(tree)
    return code


for languagedir in [el for el in Path("_build/xml").iterdir() if el.is_dir()]:
    module_name = pytamaro_module(languagedir.name)[0]
    print("Processing", languagedir)
    docs = {"module": module_name, "summary": f"PyTamaro graphics ({languagedir.name} API)", "elements": []}
    for filename in languagedir.glob("*.xml"):
        xml = ET.parse(filename)
        new_xml = xslt_transform(xml)
        new_xml_as_dict = xmltodict.parse(ET.tostring(new_xml, encoding='unicode'), force_list=['element', 'p', 'parameter'], postprocessor=postprocessor)
        maybe_elements = new_xml_as_dict["elements"]
        new_elements = maybe_elements["element"] if maybe_elements is not None else []
        docs["elements"].extend(new_elements)

    # Execute code examples for PyTamaro (localizing names) and add the output to the docs
    with open("examples-pytamaro.json", "r") as f:
        examples_dict = json.load(f)
    for element in examples_dict["elements"]:
        lang_code = pytamaro_module(languagedir.name)[1]
        element["name"] = localize_code(element["name"], lang_code)
        if "examples" in element:
            for example in element["examples"]:
                example["code"] = localize_code(example["code"], lang_code)
                output = subprocess.run([sys.executable, "-c", f'import os; os.chdir("{EXAMPLES_EXECUTION_DIR.name}"); from {module_name} import *; {example["code"]}'],
                                        capture_output=True, text=True, env={"PYTAMARO_OUTPUT_DATA_URI": "1"}, check=True)
                example["stdout"] = output.stdout
            for el in docs["elements"]:
                if el["name"] == element["name"]:
                    el["examples"] = element["examples"]

    output_path = OUTPUT_DIR / (module_name + ".json")
    with open(output_path, "w") as f:
        f.write(json.dumps(docs, indent=4))
    print("Wrote", output_path)
