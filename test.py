import xmlschema

xsd_path = "valid.xsd"
xml_path = "squads.xml"

schema = xmlschema.XMLSchema(xsd_path)
print(schema.is_valid(xml_path))




# import json
# from json2xml import json2xml


# with open("base.json", "r") as j:
#     inhalt = j.read()

# data = json.loads(inhalt)
# xml_data = json2xml.Json2xml(data).to_xml()

# with open("squads.xml", "w") as f:
#     f.write(xml_data)





# data = json2xml.Json2xml(j).to_xml()
# j.write(data)


# import json
# import xml.etree.ElementTree as ET

# with open('base.json', 'r') as f:
#     squads = json.load(f)

# root = ET.Element('squads')

# for squad in squads:
#     squad_elem = ET.SubElement(root, 'squad')
#     for key in ['squadName', 'homeTown', 'formed', 'status', 'secretBase', 'active']:
#         child = ET.SubElement(squad_elem, key)
#         child.text = str(squad[key])

#     members_elem = ET.SubElement(squad_elem, 'members')
#     for member in squad['members']:
#         member_elem = ET.SubElement(members_elem, 'member')
#         for mkey in ['name', 'age', 'secretIdentity']:
#             child = ET.SubElement(member_elem, mkey)
#             child.text = str(member[mkey])

#         powers_elem = ET.SubElement(member_elem, 'powers')
#         for power in member['powers']:
#             power_elem = ET.SubElement(powers_elem, 'power')
#             power_elem.text = power

# tree = ET.ElementTree(root)
# tree.write('base.xml', encoding='utf-8', xml_declaration=True)

# print("XML-Datei wurde erfolgreich erstellt: base.xml")



# import yaml

# with open("03_Dateiformate/README.md", "r") as f:
#     inhalt_1 = f.read()


# with open('Dateiformate.yaml', 'w') as file_1:
#     yaml.dump(inhalt_1, file)




# import xml
# import json
# import xml.etree.ElementTree as ET

# root = ET.Element("")

# with open("base.json","r") as j:
#     data = json.load(j)

# root = ET.Element("base")

# Maths = ET.SubElement(root, "squad")

# tree = ET.ElementTree(root)

# tree.write("squads.xml")

# with open("Dateiformate.XML","w") as file_2:
#     ET.Element(data, file_2)



# import json
# from dicttoxml import dicttoxml

# with open('base.json', 'r') as j:
#     data = json.load(j)

# xml_bytes = dicttoxml(data, custom_root='root', attr_type=False)
# xml_str = xml_bytes.decode('utf-8')

# with open('daten.xml', 'w') as j:
#     j.write(xml_str)

# print("Umwandlung abgeschlossen.")
