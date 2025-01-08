## Aufgabenbeschreibung

### 1. Erstellen eines UML-Klassendiagramms basierend auf den gegebenen Daten:
- **Analysiere die Struktur des JSON-Dokuments** und identifiziere die relevanten Klassen und ihre Attribute sowie Beziehungen zueinander.
- **Zeichne ein UML-Klassendiagramm**, das die Klassen, ihre Attribute und Methoden sowie die Beziehungen zwischen den Klassen (z.B. Assoziationen, Vererbungen) darstellt.
Squad
--
+	squadName: String
-	homeTown: String
+	formed: int
+	status: String
-   secretBase: String
+	active: Bolean
+	members: Array <String, int>
--
+	searchSquadName()
-	searchHomeTown()
+	whenFormed()
+	areTheyActive()
+	heroNameSquad()


Members
--
+	name: String
+	age: int
-	secretIdentity: String
-	powers: Arrey <String>



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
Die OOP ermöglicht es Code wiederverwendbar zu machen, indem bestimmte Abläufe standartisiert werden und allgemein gehalten werden.
Wie z.B die Print Funktion, diese kann in jedem Code unabhängig von der Funktion des Codes genutzt werden. 

2. Welche weiteren Vorgehensweisen gibt es?
Prozedurale Programmierung, Funktionale und Logische 

3. Was ist ein Objekt und was eine Klasse?
Eine Klasse ist ist ein abstraktes Modell, welches Baupläne und Atribute für eine Klasse bereitstellt.
Anhand dieser Klasse kann man wiederum beliebig viele Objekte instanzieren.

4. Was versteht man unter Kapselung?
Kapselung ermöglicht kontrollierten Zugriff auf Klassendaten, schützt vor versehentlichen Änderungen und sorgt für sauberen, lesbaren Code.

5. Was ist Vererbung?
Vererbung ermöglicht einer Klasse, Eigenschaften und Methoden einer anderen Klasse zu übernehmen.

6. Was versteht man unter Refactoring?
Refactoring ist der Prozess, den Code zu verbessern, ohne dessen Funktionalität zu ändern. Ziel ist es, den Code lesbarer, wartbarer und effizienter zu machen.

7. Welche Rolle spielt das Refactoring bzgl. der Wiederverwendung von Code?
Refactoring verbessert die Struktur des Codes, wodurch er modularer und flexibler wird. Das erleichtert wiederum die Wiederverwendung von Code, da er klarer und besser organisiert ist.

8. Für was gibt es die `__init__`-Funktion in einer Klasse?
Der Konstruktor einer Klasse ist notwendig um die Anfangswerte für die Eigenschaften des Objekts festzulegen.

9. Für was braucht man den `self` Parameter?
self zeigt auf das aktuelle Objekt der Klasse und muss am Anfang stehen um, auf dessen Eigenschaften und Methoden zuzugreifen zu können.

10. Wie schreibt man einzeilige und mehrzeilige Kommentare in Python?
Einzeilig mit "#"
Mehrzeilig mit >""" oder '''<

11. Welche weiteren objektorientierten Programmiersprachen neben Python gibt es? (3 Beispiele)
Java, C++, C#

12. Korrigiere die Fehlerhaften Skripte.

### Code 1
```python

class MyClass:
    def __init__(self, name):   #self hat gefehlt
        self.name = name

    def greet():
        print(f"Hello, {self.name}")

obj = MyClass("Alice")
obj.greet()

```


### Code 2
```python

def say_hello():
    print("Hello, World!") #Einrückung beachten 

say_hello()

```


### Code 3 
```python

x = 10
if x == 5:  #Vergleichsoperator == und nicht =
    print("x is 5")

```


### Code 4
```python

numbers = (1, 2, 3, 4, 5) #Ein Tuple ist nicht veränderbar, am besten umwandeln in einen veränderbaren Datentyp
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

```


### Code 5
```python

values = [1, 2, 3, 4, 5]
a, b, c = values #man kann hier [:3] eingeben um die ersten drei values abzufragen oder man nimmt einfach 5 Variabeln 

```
