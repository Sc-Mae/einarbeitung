## Aufgabenbeschreibung

1. Erstelle aus den Daten eine YAML-Datei.

```python
import yaml

with open("03_Dateiformate/README.md", "r") as f:
    inhalt_1 = f.read()


with open('Dateiformate.yaml', 'w') as file_1:
    yaml.dump(inhalt_1, file)

```
2. Erstelle ein XML-File aus der JSON.

```python 
import json
from json2xml import json2xml


with open("base.json", "r") as j:
    inhalt = j.read()

data = json.loads(inhalt)
xml_data = json2xml.Json2xml(data).to_xml()

with open("squads.xml", "w") as f:
    f.write(xml_data)
```

3. Validiere das XML-File mittels XSD.

```python 
import xmlschema

xsd_path = "valid.xsd"
xml_path = "squads.xml"

schema = xmlschema.XMLSchema(xsd_path)
print(schema.is_valid(xml_path))

```

### Fragen:

1. Was sind die Unterschiede der Datentypen?
-Die Unterschiede bestehen in der formatierung der inhalte der dateien und in welcher form sie in dei jeweiligen datentypen gespechert werden dürfen
2. Was sind Vor- und Nachteile der jeweiligen Dateiformate?
-mit yaml kann man eine einfach lesbarkeit herstellen aber ist allerdings auch weniger leistungsfähig bei großen dateien
-mit xml kann man die daten einfacher einlesen und bearbeiten allerdings ist es weniger lesbarer
-json ist sehr effizient aber hat keine integrierte schema-validierung
3. Wofür wird XML verwendet?
-oft in der webentwicklung
4. Unterstützt XML benutzerdefinierte Tags?
-ja
5. Wann ist welcher Datentyp von Vorteil?
-JSON ist ideal für schnelle, einfache Datenaustauschformate in z.b Web-Anwendungen, YAML eignet sich hervorragend für Konfigurationsdateien und das menschenlesbare Management, und XML ist vorteilhaft für strukturierte Dokumente mit Validierungsanforderungen
6. Was ist eine XSD-Datei?
-eine XSD datei ist quasi eine vorlagen datei für eine xml datei bzw. ein gerüst einer xml datei, damit man überprüfen kann ob die xml datei regelkonform formatiert ist
7. Was versteht man unter Validierung?
-validierung ist eine überfrüfung, in dem fall wird überprüft ob die xml datei der xsd "vorlage" entspricht
8. An was erinnert eine XML-Datei bzgl. ihres Aufbaus?
-an HTML
9. Was bedeutet Parsen?
parsen ist das zerlegen von daten oder code in kleinere teile
