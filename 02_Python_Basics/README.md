## Aufgabenbeschreibung

### 1. Erstellen eines UML-Klassendiagramms basierend auf den gegebenen Daten:
- **Analysiere die Struktur des JSON-Dokuments** und identifiziere die relevanten Klassen und ihre Attribute sowie Beziehungen zueinander.
- **Zeichne ein UML-Klassendiagramm**, das die Klassen, ihre Attribute und Methoden sowie die Beziehungen zwischen den Klassen (z.B. Assoziationen, Vererbungen) darstellt.

### 2. Implementierung der Klasse in Python:
- **Erstelle eine Python-Klasse oder Klassen**, die die Struktur des UML-Klassendiagramms widerspiegeln.
- **Definiere die Attribute und Methoden** entsprechend den Daten und Anforderungen aus dem JSON-Dokument.

### 3. Einlesen der JSON-Daten als Objekte der erstellten Klasse(n):
- **Schreibe ein Python-Skript**, das die JSON-Daten einliest.
- **Erstelle Instanzen der zuvor definierten Klasse(n)** und initialisiere sie mit den Daten aus dem JSON-Dokument.

### 4. Methode zum Hinzufügen eines Members:
- **Implementiere eine Methode in der entsprechenden Klasse**, die ein neues Mitglied zum Team hinzufügt.
- Die Methode sollte die benötigten Informationen (z.B. Name, ID) als Parameter entgegennehmen und ein neues Mitgliedsobjekt erstellen und zur entsprechenden Liste hinzufügen.

### 5. Methode zur Ausgabe des Teams mit den jeweiligen Mitgliedern:
- **Implementiere eine Methode in der entsprechenden Klasse**, die das gesamte Team und deren Mitglieder auf eine lesbare Weise ausgibt.
- Die Methode sollte durch die Mitglieder des Teams iterieren und deren Details anzeigen.

### 6. Methode zum Löschen eines Members anhand der ID:
- **Implementiere eine Methode in der entsprechenden Klasse**, die ein Mitglied anhand seiner ID löscht.
- Die Methode sollte die Liste der Mitglieder durchsuchen, das Mitglied mit der passenden ID finden und es aus der Liste entfernen.




## Fragen zur Objektorientierung

1. Warum verwendet man Objektorientierung?
   - Es macht Code und Anwendungen robuster, weniger Fehleranfällig und einfacher zu warten!
2. Welche weiteren Vorgehensweisen gibt es?
   - Funktionale Programmierung!
3. Was ist ein Objekt und was eine Klasse?
   - Eine Klasse sind die Variablen, Eigenschaften und Ereignisse eines Objekts, Objekte sind die Instanzen von Klassen 
4. Was versteht man unter Kapselung?
   - Es ist eine Konzept der objektorientierten Programmierung , bei dem Daten und Methoden, die auf diese Daten zugreifen, in einer einzelnen Einheit, genannt Objekt, zusammengefasst werden
8. Was ist Vererbung?
   - Aufbauend auf bereits existierende Klassen neue erstellen 
6. Was versteht man unter Refactoring?
    - Die Umstrukturierung von Code ohne die Funktionalität zu verändern 
7. Welche Rolle spielt das Refactoring bzgl. der Wiederverwendung von Code?
    - es wird verwendet um z.B. bei der Wiederverwendung doppelte Funktionen zu verhindern 
8. Für was gibt es die `__init__`-Funktion in einer Klasse?
    - Die Methode kann dafür genutzt werden ein Objekt zu initialisieren 
9. Für was braucht man den `self` Parameter?
    - Es repräsentiert die Instanz
10. Wie schreibt man einzeilige und mehrzeilige Kommentare in Python?
    - Mehrzeilige Kommentare mit jeweils 3 Anführungsstrichen vor und nach dem Kommentar. Einzeilige Kommentare mit einem # davor 
11. Welche weiteren objektorientierten Programmiersprachen neben Python gibt es? (3 Beispiele)
    - Es gibt Java C++ und C#
12. Korrigiere die Fehlerhaften Skripte.

### Code 1
```python
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")

obj = MyClass("Alice")
obj.greet()
```


### Code 2
```python
def say_hello():
    print("Hello, World!")  

say_hello()
```


### Code 3 
```python
x = 10
if x == 5:   
    print("x is 5")
```


### Code 4
```python
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
```


### Code 5
```python
values = [1, 2, 3, 4, 5]
a = values
```
