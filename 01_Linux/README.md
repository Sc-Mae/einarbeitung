### Aufsetzen einer VM (Empfohlen: Rocky Linux) 

Folge der Anleitung in der KnowledgeBase, um eine VM einzurichten. Stelle sicher, dass du die Scaltel Repos für den Packetmanager hinterlegst. Lege verschiedene Benutzer an:

- `root`
- `admin` mit sudo-Berechtigung
- `entwickler` ohne sudo-Berechtigung

### Partitionierung:

- `/`
- `/var/`
- `/home/`

### Installierte Programme:

a) GUI  
b) IDE  
c) Git  
d) Docker  
e) Python  
f) Docker-compose  

### Fragen:

1. Was ist Linux und wie unterscheidet es sich von anderen Betriebssystemen wie Windows oder macOS?
2. Was sind die Vorteile der Verwendung von Linux im Vergleich zu anderen Betriebssystemen?
3. Was ist Virtualisierung und welche Vorteile bieten VMs?
4. Was sind `yum` und `dnf`?
5. Was ist eine IDE und wie unterscheidet sie sich von einem Texteditor?
6. Was ist der Unterschied zwischen einem LSP und einem Texteditor?
7. Wie kann man Programme im Hintergrund laufen lassen und Prozesse verwalten?
8. Wie kann man Skripte unter Linux erstellen und ausführen?
9. Was ist ein Linux-Kernel und wie kann man ihn aktualisieren?
10. Was sind symbolische Links und wie unterscheiden sie sich von Hardlinks?
11. Welche Vorteile bietet die Nutzung von LTS (Long Term Support) Versionen einer Linux-Distribution?
12. Wie schreibt man Kommentare in Bash?
13. Was ist `vim`?

### Linux-Befehle:

a) `history` - Zeigt die Liste der bereits ausgeführten Befehle an  
b) `chmod` - Ändert die Dateiberechtigungen  
c) `chown` - Ändert den Eigentümer einer Datei oder eines Verzeichnisses  
d) `mv test.txt abc` - Verschiebt oder benennt die Datei `test.txt` in `abc` um  
e) `ll | grep test` - Listet Dateien im aktuellen Verzeichnis auf, die "test" im Namen enthalten  
f) `find . -name cisco` - Sucht nach Dateien mit dem Namen "cisco" im aktuellen Verzeichnis und seinen Unterverzeichnissen  
g) `find / -name cisco` - Sucht nach Dateien mit dem Namen "cisco" im gesamten Dateisystem
