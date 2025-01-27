## Aufgabenbeschreibung
Die Daten sollen in einer Datenbank gespeichert werden.

1. **DB aufsetzen**: Die Datenbank wird eingerichtet, um Daten zu speichern.
2. **Struktur der Datenbank mittels semantisches ER-Diagramm**: Das semantische ER-Diagramm wird erstellt, um die Struktur der Datenbank zu visualisieren.
3. **Datenbank aufsetzen und Daten einfügen**: Die Datenbank wird erstellt und Daten werden eingefügt.
4. **Daten mittels SQL-Querys bearbeiten (nicht über xampp-oberfläche)**:
   a) **Hinzufügen**: Neue Daten werden der Datenbank hinzugefügt.
   b) **Löschen**: Daten werden aus der Datenbank gelöscht.
   c) **Bearbeiten**: Bestehende Daten werden in der Datenbank bearbeitet.
   d) **Auslesen**: Daten werden aus der Datenbank abgerufen.

### Fragen:

### **Welche Datenbanken gibt es?**  
- **SQL-Datenbanken** (z.B. MySQL, PostgreSQL, Microsoft SQL Server).  
- **SQLite** (eine leichtgewichtige SQL-basierte Datenbank).  

---

### **Wann macht welcher Typ Sinn?**  
- **SQL**: Sinnvoll bei großen Datenmengen und gleichbleibenden Attributen, z.B. für Unternehmenssysteme.  
- **SQLite**: Ideal für kleine Projekte und lokale Anwendungen, z. B. mobile Apps.  

---

### **Was ist ein Primary Key und was ein Foreign Key?**  
- **Primary Key**: Eindeutiger Identifikator für eine Zeile in einer Tabelle.  
- **Foreign Key**: Ein Attribut, das auf einen Primary Key in einer anderen Tabelle verweist.  

---

### **Was ist ein nativer und was ein künstlicher Primary Key?**  
- **Nativer Primary Key**: Ein existierendes Attribut, z.B. "Personalausweisnummer".  
- **Künstlicher Primary Key**: Ein neu generiertes Attribut, z.B. eine automatische ID.  

---

### **Welche Beziehungstypen zwischen Tabellen gibt es?**  
1. **1:1**: Eine Zeile in Tabelle A entspricht genau einer Zeile in Tabelle B.  
2. **1:n**: Eine Zeile in Tabelle A ist mit mehreren Zeilen in Tabelle B verbunden.  
3. **n:m**: Mehrere Zeilen aus Tabelle A können mit mehreren Zeilen aus Tabelle B verknüpft sein.  

---

### **Welche Wildcards gibt es in MySQL und was bedeuten sie?**  
- **%**: Platzhalter für beliebig viele Zeichen (z.B. `LIKE 'A%', '%A'` findet alles, was mit A beginnt oder alles was ein A am ende hat).  
- **_**: Platzhalter für genau ein Zeichen (z.B. `LIKE '_b'` findet alles, wo der zweite Buchstabe "b" ist).  

---

### **Was ist ein Join?**  
Ein Join verknüpft zwei Tabellen basierend auf einem gemeinsamen Attribut.  

---

### **Was ist ein left- und was ein right-Join?**  
- **Left Join**: Gibt alle Zeilen der linken Tabelle aus, auch wenn es keine Übereinstimmungen in der rechten Tabelle gibt.  
- **Right Join**: Gibt alle Zeilen der rechten Tabelle aus, auch wenn es keine Übereinstimmungen in der linken Tabelle gibt.  

---

### **Was ist das kartesische Produkt zweier Tabellen?**  
Das Ergebnis einer Verknüpfung ohne Bedingung, bei der jede Zeile der ersten Tabelle mit jeder Zeile der zweiten Tabelle kombiniert wird.  

---

### **Was ist Kaskadierung?**  
Eine Regel, die festlegt, wie verbundene Daten behandelt werden:  
- **On Delete Cascade**: Löscht verbundene Daten automatisch, wenn eine Referenz gelöscht wird.  
- **On Update Cascade**: Aktualisiert verbundene Daten automatisch, wenn eine Referenz geändert wird.  

---

### **Wann werden Gruppierungen benötigt?**  
Wenn Daten nach bestimmten Kriterien zusammengefasst werden sollen, z.B. zur Summen- oder Durchschnittsberechnung (`GROUP BY`).  

---

### **Was ist ein DBMS?**  
Ein **Datenbankmanagementsystem (DBMS)** ist Software, die die Speicherung, Abfrage und Verwaltung von Datenbanken ermöglicht (z.B. MySQL, SQLite).  

---

### **Was versteht man unter Datenintegrität?**  
Datenintegrität stellt sicher, dass Daten korrekt, konsistent und fehlerfrei sind, z.B. durch Constraints wie PRIMARY KEY oder UNIQUE.  

---

### **Was ist Normalisierung?**  
Normalisierung ist der Prozess, Daten zu strukturieren, um Redundanzen zu vermeiden und Konsistenz zu gewährleisten.  

---

### **Was sind Aggregationsfunktionen und welche gibt es?**  
Aggregationsfunktionen fassen Werte aus mehreren Zeilen zusammen:  
1. **SUM()**: Addiert Werte.  
2. **AVG()**: Berechnet den Durchschnitt.  
3. **COUNT()**: Zählt Einträge.  