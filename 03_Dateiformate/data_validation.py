"""Bearbeitung Aufgabe 03"""

import xml.etree.ElementTree as ET
import json
import yaml
from validator import validate

with open("base1.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

yaml_data = yaml.dump(data, allow_unicode=True)
with open("base.yaml", "w", encoding="utf-8") as yaml_file:
    yaml_file.write(yaml_data)


def dict_to_xml(tag, d):
    """Erstellt aus dem dict eine XML Datei"""
    elem = ET.Element(tag)
    if isinstance(d, dict):
        for key, val in d.items():
            child = dict_to_xml(key, val)
            elem.append(child)
    elif isinstance(d, list):
        for item in d:
            child = dict_to_xml(tag, item)
            elem.append(child)
    else:
        elem.text = str(d)
    return elem


root = ET.Element("root")
for entry in data:
    squad = dict_to_xml("squad", entry)
    root.append(squad)

tree = ET.ElementTree(root)
tree.write("base.xml", xml_declaration=True, encoding="utf-8", method="xml")

if validate(
    "/home/yw/einarbeitung/03_Dateiformate/base.xml",
    "/home/yw/einarbeitung/03_Dateiformate/base1.xml",
):
    print("Valid")
else:
    print("Not valid")
