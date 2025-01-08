# Einrichten einer Virtual Machine (VM) unter Rocky Linux

## Beschreibung
In diesem Projekt wird eine Virtual Machine (VM) unter Rocky Linux eingerichtet. Es werden verschiedene Benutzer angelegt, die Partitionierung vorgenommen und verschiedene Programme installiert.

## Anleitung
Folge der Anleitung in der KnowledgeBase, um eine VM einzurichten. Stelle sicher, dass du die Scaltel Repos für den Packetmanager hinterlegst.

### Benutzer anlegen
- `root`: Der Hauptbenutzer mit vollständigen administrativen Rechten.
- `admin`: Ein Benutzer mit sudo-Berechtigungen.
- `entwickler`: Ein Benutzer ohne sudo-Berechtigungen.

### Partitionierung
- `/`: Das Stammverzeichnis.
- `/var/`: Das Verzeichnis für variable Daten.
- `/home/`: Das Verzeichnis für Benutzerdaten.

### Installierte Programme
a) GUI  
b) IDE  
c) Git  
d) Docker  
e) Python  
f) Docker-compose  

## Fragen und Antworten
- Was ist Linux und wie unterscheidet es sich von anderen Betriebssystemen wie Windows oder macOS?
    Linux ist als einziges Betriebssystem OpenSource

- Was sind die Vorteile der Verwendung von Linux im Vergleich zu anderen Betriebssystemen?
    Abhängig von Einsatzgebiet gibt es unterschiedliche Vorteile:
    Als Server:
        -   Linux ist sehr Resourcen sparend
        -   Linux kann als Server fungieren, ohne zu zahlen
    Als Betriebssystem:
        -   Von Grund auf konfigurierbar.
        -   Eigenet sich für schwächere Rechner.
        -   Bietet kostenlose Verschlüsselung wie Bitlocker.
        -   Kann  vom USB-Stick gebooted werden.
        
- Was ist Virtualisierung und welche Vorteile bieten VMs?
    -   Effiziente Nutzung von Ressourcen 
        -   Statt einzelner Server, ein großer Server mit mehreren VMs.
    -   Reduzierung der IT-kosten
        -   durch optimierungen können einzelne Server voll ausgelastet werden, worduch andere Server für weitere Anwendungen frei werden oder komplett eingespart werden können.
    -   Einfache Verwaltung
        -   Da IT-Infrastruktur größtenteils virtuell ist können Prozesse komplett automatisiert werden.
        -   Über bestimmte Programme lassen sich standardtisierte VMs komplett automatisch erstellen, reduziert kosten.
    -   Sicherheit
        -   Virtuelle MAschinen können leicht isoliert und abgeschaltet werden, wenn Redundant, dann auch ohne Störung möglich.
        -   Können anhand von Snapshots wiederhergestellt werden. 
        -   erhöht generell die Ausfallsischerheit und senkt das Betriebsrisiko
        
- Was sind yum und dnf?
    -    beides sind Programme die die Verwaltung von Pakten vereinfachen sollen.
    -    DNF ist die aktuelleste Version von Yum und bietet einen größeren Funktionsumfang

- Was ist eine IDE und wie unterscheidet sie sich von einem Texteditor?
    -   Eine IDE (integrated Development Enviroment) bietet im vergleich zu einem Texteditor einen weitreichenderen Umfang bei er Programmierung und deren Bearbeitung.
        Wie z.B. eine Syntax Analyse, Verbesserungsvorschläge, Autovervollständigung, Fehlercodeanalyse,  einen Compiler/Interpreter und die Möglichkeit extensions, die wiederum den Funktionsumfang erweitern, installieren zu können.

- Was ist der Unterschied zwischen einem LSP und einem Texteditor?
    -   Ein Texteditor kann mit einem LSP (Language Server Protocol) erweitert werden um unabhängig von der Programmiersprache Funktionen wie z.B., Syntaxprüfung und             
        Code-Vervollständigung zu implementieren.

- Wie kann man Programme im Hintergrund laufen lassen und Prozesse verwalten?
    -   "&"         am Ende eines Befehls, kann dieser im Hintergrund ausgeführt werden.
    -   "nohup"     sorgt dafür das das Programm weiterläuft selbst wenn die Verbindung zum Terminal oder der Sitzung beendet wird.
    -   "disown"    sorgt dafür das Przesse selbst dann weiterlaufen, wenn du dich abmeldest.
    -   "jobs"      zeigt aktuelle Hintergrundprozesse an. 
    -   "fg Job-ID" zieht Hintergrundprozesse wieder in den Vordergrund, die ID kann durch den Befehl "jobs" ausgelesen werden.

- Wie kann man Skripte unter Linux erstellen und ausführen?
    -   Skript erstellen 
        "nano mein_skript.sh" im Texeditor nano oder vim
    -   Skript-Inhalt
        soll mit Bash ausgeführt werden -> "#!/bin/bash"   Inhalt -> "echo "Hallo, Welt!""   Echo= gibt in der Kommandozeile aus.
    -   Skript ausführbar machen
        "chmod +x mein_skript.sh"
    -   Skript ausführen
        "./mein_skript.sh" oder mit "bash mein_skript.sh" oder mit "sh mein_skript.sh"
    -   Skript im Hintergrund ausführen
        "./mein_skript.sh &"
    -   Prozesse überwachen
        "ps aux | grep mein_skript.sh"

- Was ist ein Linux-Kernel und wie kann man ihn aktualisieren?
    -   Er ermöglicht die Kommunikation zwischen Hardware und Software und verwaltet wichtige Ressourcen wie Prozessoren, Speicher und Geräte.
            Prozessmanagement:          Verwaltung von Prozessen und deren Prioritäten.
            Speicherverwaltung:         Verwaltung von physischen und virtuellen Speichern.
            Hardwaresteuerung:          Bereitstellung von Treibern und Schnittstellen für Geräte.
            Dateisystemmanagement:      Verwaltung von Dateisystemen zur Speicherung und Abruf von Daten.

    -   Update
            Systemupdate mit            "sudo dnf update"
            Kernel Installieren mit     "sudo dnf install kernel"
            Reboot                      "sudo reboot"

- Was sind symbolische Links und wie unterscheiden sie sich von Hardlinks?
    -   Symlinks können auf Dateien oder Verzeichnisse in unterschiedlichen Dateisystemen zeigen, Hardlinks nur innerhalb des gleichen Dateisystems.
    -   Symlinks können auf nicht existierende Dateien zeigen (broken links), Hardlinks nicht.

- Welche Vorteile bietet die Nutzung von LTS (Long Term Support) Versionen einer Linux-Distribution?
    -   Langfristige Sicherheit:    LTS-Versionen erhalten über mehrere Jahre regelmäßige Sicherheitsupdates und Bugfixes.
    -   Stabilität:                 Da LTS-Versionen gründlich getestet werden, bieten sie eine stabile und zuverlässige Plattform für den Einsatz in Produktionsumgebungen.
    -   Weniger häufige Upgrades:   Benutzer müssen nicht ständig auf neue Versionen aktualisieren, was den Wartungsaufwand reduziert.
    -   Kompatibilität:             LTS-Versionen bieten längere Unterstützung für Software und Treiber, was die Integration und Nutzung vereinfacht.
- Wie schreibt man Kommentare in Bash?
    -   mit "#" z.B #hier wird erklärt wie man Kommentare in Bash schreibt.

- Was ist vim?
    -   Vim ist ein Texteditor, der oft von Programmierern verwendet wird, da er eine Vielzahl von Funktionen wie Syntaxhervorhebung, Autovervollständigung (muss seperat konfiguriert werden) und eine effiziente Navigation bietet. Er basiert auf dem alten Vi-Editor. Vim hat drei Hauptmodi:

        Normalmodus: Zum Navigieren und Bearbeiten von Text.
        Einfügemodus: Zum Tippen von Text.
        Befehlmodus: Zum Ausführen von Befehlen (z. B. Speichern oder Schließen).

### Linux-Befehle
Was bewirken folgende Befehle:
-   history:                    Zeigt die Liste der zuletzt verwendeten Befehle an.
-   chmod:                      Ändert die Berechtigungen von Dateien oder Verzeichnissen.
-   chown:                      Ändert den Besitzer und/oder die Gruppe einer Datei oder eines Verzeichnisses.
-   mv test.txt abc:            Verschiebt oder benennt die Datei test.txt in abc um.
-   ll | grep test:             Es zeigt eine ausführliche Liste der Dateien und Verzeichnisse im aktuellen Verzeichnis an, einschließlich Berechtigungen, Eigentümer,              Größe                             Änderungszeit und filtert nach dem Wort "test".
-   find . -name cisco:         Sucht nach Dateien mit dem Namen "cisco" im aktuellen Verzeichnis und Unterverzeichnissen.
-   find / -name cisco:         Sucht nach Dateien mit dem Namen "cisco" im gesamten Dateisystem.
-   tar -xvf archive.tar.gz:    Entpackt das Archiv archive.tar.gz.
-   df -h:                      Zeigt die verfügbaren und verwendeten Festplattenspeichergrößen in menschenlesbarem Format.
-   du -sh directory:           Zeigt die Gesamtgröße eines Verzeichnisses.
-   ps aux:                     Zeigt eine Liste aller laufenden Prozesse.
-   grep pattern file:          Sucht nach dem Muster "pattern" in der Datei "file".
-   top:                        Zeigt eine Echtzeitübersicht der Systemressourcen und laufenden Prozesse.
-   netstat -tuln:              Zeigt alle aktiven Netzwerkverbindungen und offenen Ports an.
-   ifconfig:                   Zeigt die Netzwerkschnittstellen und deren Status.
-   ping host:                  Sendet Ping-Anfragen an einen Host, um die Erreichbarkeit zu testen.


