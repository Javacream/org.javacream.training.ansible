# Trainerleitfaden -- Block 1: Linux-Grundlagen I -- Arbeiten mit Linux

## 1. Zielsetzung des Blocks

Block 1 schafft die Linux-Grundlage für alle weiteren Seminarinhalte.
Die Teilnehmenden sollen Linux nicht umfassend administrieren können,
sondern sicher genug mit einem Linux-System umgehen können, um die
späteren Automatisierungsaufgaben mit Shell, Python und Ansible
nachvollziehen und selbst durchführen zu können.

Im Vordergrund steht das Verständnis dafür, wie ein Linux-System
organisiert ist, wie über die Shell mit ihm gearbeitet wird und wie
Dateien, Benutzer und Berechtigungen zusammenwirken.

Ein wichtiger didaktischer Grundsatz lautet: Die verwendeten
Shell-Befehle werden nicht als isolierte Befehlsliste vermittelt. Sie
werden unmittelbar für konkrete Aufgaben auf dem Linux-System
eingesetzt.

------------------------------------------------------------------------

## 2. Lernziele

Nach Abschluss des Blocks können die Teilnehmenden:

-   die grundlegende Struktur des Linux-Dateisystems erklären,
-   sich im Dateisystem mit absoluten und relativen Pfaden orientieren,
-   grundlegende Datei- und Verzeichnisoperationen über die Shell
    durchführen,
-   Textdateien anzeigen, durchsuchen und bearbeiten,
-   einfache Ein- und Ausgabeumleitungen sowie Pipes verwenden,
-   Benutzer und Gruppen als Grundlage des Linux-Rechtesystems
    verstehen,
-   Datei- und Verzeichnisrechte lesen und verändern,
-   den Unterschied zwischen normalen Benutzern und `root` erklären,
-   administrative Befehle gezielt mit `sudo` ausführen.

------------------------------------------------------------------------

## 3. Einstieg: Orientierung auf einem Linux-System

### Inhalt

Zu Beginn sollte zunächst das System betrachtet werden, bevor einzelne
Befehle eingeführt werden.

Zu erläutern sind:

-   Linux als Mehrbenutzersystem
-   Shell als textbasierte Schnittstelle zum Betriebssystem
-   hierarchisches Dateisystem
-   Wurzelverzeichnis `/`
-   Unterschied zu Laufwerksbuchstaben unter Windows

Wichtige Verzeichnisse:

-   `/etc` -- systemweite Konfiguration
-   `/home` -- Home-Verzeichnisse der Benutzer
-   `/var` -- veränderliche Daten
-   `/tmp` -- temporäre Dateien
-   `/usr` -- Programme und weitere Systemressourcen

Weitere Verzeichnisse können erwähnt werden, eine vollständige
Behandlung des Filesystem Hierarchy Standard ist jedoch nicht
erforderlich.

### Demonstration

Der Trainer bewegt sich zunächst selbst durch das System und zeigt die
Verzeichnisstruktur.

Dabei sollten bereits `pwd`, `ls` und `cd` verwendet werden, ohne alle
Optionen dieser Befehle systematisch zu behandeln.

### Didaktischer Hinweis

Die Verzeichnisse sollten immer mit ihrem späteren Nutzen verbunden
werden. Insbesondere `/etc` ist für das Seminar wichtig, da die
Teilnehmenden später mit Ansible Konfigurationsdateien verwalten werden.

------------------------------------------------------------------------

## 4. Terminal und Shell

### Inhalt

Zu unterscheiden sind:

-   Terminal
-   Shell
-   Kommando
-   Kommandoargumente
-   Kommandooptionen

Grundlegender Aufbau eines Shell-Kommandos:

`kommando [optionen] [argumente]`

Einführung in die Hilfe:

-   `man`
-   `--help`

### Trainerhinweis

Es geht nicht darum, zahlreiche Optionen einzelner Programme auswendig
zu lernen. Die Teilnehmenden sollen vielmehr lernen, unbekannte oder
vergessene Optionen selbst nachzuschlagen.

------------------------------------------------------------------------

## 5. Navigation im Dateisystem

### Inhalt

Behandelt werden:

-   aktuelles Arbeitsverzeichnis
-   `pwd`
-   `cd`
-   `ls`
-   absolute Pfade
-   relative Pfade
-   `.`
-   `..`
-   Home-Verzeichnis und `~`

### Demonstration

Der Trainer navigiert zunächst ausschließlich mit absoluten Pfaden und
löst anschließend dieselben Navigationsaufgaben mit relativen Pfaden.

### Übung

Die Teilnehmenden erhalten mehrere Zielverzeichnisse und wechseln
zunächst über absolute und anschließend über relative Pfade zwischen
diesen.

Sie sollen jeweils mit `pwd` kontrollieren, wo sie sich befinden.

### Typische Schwierigkeiten

Besonders bei Teilnehmenden mit überwiegender Windows-Erfahrung sollte
auf folgende Unterschiede geachtet werden:

-   `/` statt `\`
-   keine Laufwerksbuchstaben
-   Groß-/Kleinschreibung ist relevant
-   relative Pfade beziehen sich auf das aktuelle Arbeitsverzeichnis

------------------------------------------------------------------------

## 6. Dateien und Verzeichnisse verwalten

### Inhalt

Grundlegende Befehle:

-   `mkdir`
-   `cp`
-   `mv`
-   `rm`

Dabei werden die Konzepte hinter den Befehlen behandelt:

-   Verzeichnisse anlegen
-   Dateien kopieren
-   Dateien und Verzeichnisse verschieben
-   Dateien umbenennen
-   Dateien und Verzeichnisse löschen

### Demonstration

Der Trainer baut schrittweise eine kleine Arbeitsstruktur auf, kopiert
und verschiebt Dateien und entfernt anschließend einzelne Bestandteile
wieder.

### Übung

Die Teilnehmenden erstellen selbstständig eine vorgegebene
Verzeichnisstruktur und führen darin verschiedene Dateioperationen aus.

Die Aufgabe sollte bewusst mehrere Schritte enthalten, sodass Navigation
und Dateioperationen miteinander kombiniert werden.

### Trainerhinweis

Bei `rm` sollte bereits auf die grundsätzliche Bedeutung destruktiver
Shell-Kommandos hingewiesen werden. Eine ausführliche Behandlung von
Sicherheitsmechanismen ist an dieser Stelle nicht notwendig.

------------------------------------------------------------------------

## 7. Textdateien anzeigen und durchsuchen

### Inhalt

Behandelt werden:

-   `cat`
-   `less`
-   `grep`

Dabei sollte insbesondere der Unterschied zwischen dem vollständigen
Ausgeben einer Datei und dem interaktiven Betrachten größerer Dateien
deutlich werden.

`grep` wird zunächst nur für einfache Textsuche verwendet. Reguläre
Ausdrücke sind nicht Bestandteil dieses Blocks.

### Demonstration

Der Trainer verwendet geeignete vorhandene Systemdateien oder
vorbereitete Beispieldateien und zeigt:

-   vollständige Ausgabe,
-   seitenweises Betrachten,
-   Suche nach bestimmten Textinhalten.

### Übung

Die Teilnehmenden suchen bestimmte Informationen in mehreren
bereitgestellten Textdateien.

Ziel ist nicht die Beherrschung von `grep`-Optionen, sondern die
Erkenntnis, dass Informationen auf Linux-Systemen häufig direkt über
Textwerkzeuge ermittelt werden können.

------------------------------------------------------------------------

## 8. Textdateien bearbeiten

### Inhalt

Ein einfacher Terminaleditor wird eingeführt.

Ziel ist lediglich:

-   Datei öffnen,
-   Text ändern,
-   speichern,
-   Editor verlassen.

### Trainerhinweis

Die Editorauswahl sollte sich an der Seminarumgebung orientieren. Der
Block sollte nicht zu einer Schulung für `vi` oder `vim` werden.

Die Teilnehmenden benötigen lediglich genügend Sicherheit, um später
beispielsweise YAML-, Inventory- und Konfigurationsdateien bearbeiten zu
können.

------------------------------------------------------------------------

## 9. Ein- und Ausgabe sowie Pipes

### Inhalt

Grundmodell eines Shell-Programms:

-   Standard Input
-   Standard Output
-   Standard Error

Praktisch behandelt werden:

-   `>`
-   `>>`
-   `|`

Die Umleitung von Standard Error kann bei Bedarf gezeigt werden, muss
aber noch nicht vertieft werden.

### Demonstration

Ausgaben werden zunächst auf dem Terminal erzeugt, anschließend in
Dateien umgeleitet und schließlich über Pipes an ein weiteres Kommando
weitergegeben.

### Übung

Die Teilnehmenden sollen vorhandene Kommandos miteinander kombinieren,
um:

-   eine Ausgabe in einer Datei zu speichern,
-   eine Ausgabe an eine vorhandene Datei anzuhängen,
-   eine Ausgabe nach einem bestimmten Inhalt zu filtern.

### Didaktischer Hinweis

Dieser Abschnitt bereitet bereits Block 2 vor. Die Teilnehmenden sollen
erkennen, dass kleine Linux-Werkzeuge miteinander kombiniert werden
können. Die eigentliche Automatisierung über Shell-Skripte folgt erst
dort.

------------------------------------------------------------------------

## 10. Benutzer und Gruppen

### Inhalt

Linux als Mehrbenutzersystem:

-   Benutzer
-   Benutzer-ID
-   Gruppen
-   Gruppen-ID
-   primäre und weitere Gruppen
-   Eigentümer von Dateien

Nützliche Befehle:

-   `whoami`
-   `id`

Systemdateien wie `/etc/passwd` können zur Veranschaulichung gezeigt
werden.

### Trainerhinweis

Benutzerverwaltung selbst ist nicht Schwerpunkt dieses Blocks.
Entscheidend ist das Verständnis von Benutzern und Gruppen als
Voraussetzung für das nachfolgende Rechtekonzept.

------------------------------------------------------------------------

## 11. Datei- und Verzeichnisrechte

### Inhalt

Das Linux-Rechtesystem wird zunächst anhand der Ausgabe von `ls -l`
entwickelt.

Zu behandeln sind:

-   Eigentümer
-   Gruppe
-   Andere
-   `r` -- read
-   `w` -- write
-   `x` -- execute

Anschließend:

-   `chmod`
-   `chown`

Symbolische und numerische Rechte können beide erläutert werden.
Entscheidend ist, dass die Teilnehmenden die Darstellung beispielsweise
als `rwxr-xr--` lesen können.

Bei Verzeichnissen sollte auf die besondere Bedeutung von `r`, `w` und
`x` hingewiesen werden.

### Demonstration

Der Trainer erzeugt eine Datei und verändert gezielt deren Rechte.
Anschließend wird überprüft, welche Operationen noch möglich sind.

### Übung

Die Teilnehmenden erhalten mehrere Anforderungen an Dateien und
Verzeichnisse und müssen passende Berechtigungen setzen.

Anschließend kontrollieren sie das Ergebnis mit `ls -l`.

### Typische Schwierigkeiten

Besonders zu beachten sind:

-   Unterschied zwischen Datei- und Verzeichnisrechten
-   Verwechslung von Eigentümer und Gruppe
-   Bedeutung des Execute-Bits
-   Umrechnung zwischen symbolischer und numerischer Schreibweise

------------------------------------------------------------------------

## 12. `root` und `sudo`

### Inhalt

Behandelt werden:

-   normaler Benutzer
-   Superuser `root`
-   administrative Operationen
-   `sudo`
-   gezielte Rechteerhöhung

Die Teilnehmenden sollen insbesondere verstehen, warum nicht dauerhaft
als `root` gearbeitet werden sollte.

### Demonstration

Ein administrativer Zugriff wird zunächst als normaler Benutzer versucht
und schlägt aufgrund fehlender Berechtigung fehl.

Anschließend wird derselbe Vorgang mit `sudo` durchgeführt.

### Ausblick auf Ansible

Dieser Zusammenhang wird später bei Ansible wieder aufgegriffen:

Ein Managed Node kann mit einem normalen Benutzer angesprochen werden,
während für administrative Tasks eine Rechteerhöhung erforderlich ist.

Der Begriff `become` kann als Ausblick genannt werden, sollte aber noch
nicht erläutert werden.

------------------------------------------------------------------------

## 13. Abschlussübung

Zum Abschluss bearbeiten die Teilnehmenden eine zusammenhängende
Aufgabe, die mehrere Inhalte des Blocks kombiniert.

Die Aufgabe sollte enthalten:

-   Navigation im Dateisystem
-   Anlegen einer Verzeichnisstruktur
-   Kopieren oder Verschieben von Dateien
-   Anzeigen und Suchen von Dateiinhalten
-   Bearbeiten einer Textdatei
-   Umleitung oder Pipe
-   Setzen von Datei- bzw. Verzeichnisrechten
-   Kontrolle der Ergebnisse

Die Übung sollte möglichst wenig konkrete Befehle vorgeben. Statt
"Führen Sie `mkdir ...` aus" sollte beispielsweise die Anforderung
lauten: "Legen Sie folgende Verzeichnisstruktur an."

Damit wird überprüft, ob die Teilnehmenden bereits selbstständig das
passende Werkzeug auswählen können.

------------------------------------------------------------------------

## 14. Typische Fragen und Fehler

Der Trainer sollte insbesondere mit folgenden Punkten rechnen:

-   Verwechslung absoluter und relativer Pfade
-   falsche Groß-/Kleinschreibung
-   Verwechslung von `/` und `\`
-   Unsicherheit beim aktuellen Arbeitsverzeichnis
-   fehlende Berechtigungen
-   falsche Verwendung von `sudo`
-   Schwierigkeiten beim Lesen von `ls -l`
-   Unsicherheit bei numerischen Dateirechten
-   unbeabsichtigtes Überschreiben von Dateien mit `>`
-   Verwechslung von `>` und `>>`
-   Schwierigkeiten beim Beenden des verwendeten Editors oder von `less`

------------------------------------------------------------------------

## 15. Überleitung zu Block 2

Am Ende sollte der Trainer den Übergang von der grundlegenden Bedienung
zur Administration herstellen.

Die Teilnehmenden haben bisher einzelne Operationen auf einem
Linux-System durchgeführt. Im nächsten Block kommen Aufgaben hinzu, die
für Administration und Automatisierung besonders relevant sind:

-   Software installieren,
-   Prozesse und Dienste verwalten,
-   Netzwerkverbindungen überprüfen,
-   entfernte Systeme über SSH erreichen,
-   mehrere Kommandos zu einfachen automatisierten Abläufen verbinden.

Damit verschiebt sich die Fragestellung von "Wie arbeite ich mit einem
Linux-System?" zu "Wie administriere und automatisiere ich ein
Linux-System?".
