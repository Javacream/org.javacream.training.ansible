# Lernpfad – Linux, Python und Ansible

## Block 1: Linux-Grundlagen I – Arbeiten mit Linux

- Aufbau eines Linux-Systems
  - Dateisystem und Verzeichnisstruktur
  - Wichtige Verzeichnisse wie `/etc`, `/home`, `/var`, `/tmp`
- Terminal und Shell
- Navigation im Dateisystem
- Wichtige Shell-Befehle
  - `ls`, `cd`, `pwd`
  - `cp`, `mv`, `rm`, `mkdir`
  - `cat`, `less`, `grep`
- Arbeiten mit einem Texteditor
- Ein- und Ausgabeumleitung sowie einfache Pipes
- Benutzer und Gruppen
- Linux-Rechtekonzept
  - Besitzer, Gruppe und Andere
  - Lesen, Schreiben und Ausführen
  - `chmod`, `chown`
- Administrative Rechte
  - `root`
  - `sudo`

### Ziel des Blocks

Die Teilnehmenden können sich auf einem Linux-System orientieren, Dateien und Verzeichnisse bearbeiten und verstehen die grundlegenden Benutzer- und Berechtigungskonzepte.

---

## Block 2: Linux-Grundlagen II – Administration und einfache Automatisierung

- Paketmanagement
  - Grundprinzip von Paketmanagern
  - `apt`
  - Überblick über `yum` und `dnf`
- Prozesse
  - Prozesse anzeigen und identifizieren
  - `ps`
  - Prozesse beenden
- Dienste
  - Grundprinzip von `systemd`
  - Dienste mit `systemctl` starten, stoppen und überprüfen
- Netzwerkgrundlagen
  - IP-Adressen und Hostnamen
  - Erreichbarkeit mit `ping`
  - grundlegende Netzwerkdiagnose
- SSH
  - Remote-Zugriff
  - Benutzer und Zielsystem
  - SSH-Keys
  - Public-Key-Authentifizierung
- Grundlagen einfacher Shell-Skripte
  - Shebang
  - Befehlssequenzen
  - einfache Variablen
  - Exit Codes
  - einfache Bedingungen
- Shell-Skripte zur Orchestrierung vorhandener Programme

### Ziel des Blocks

Die Teilnehmenden können grundlegende administrative Aufgaben unter Linux durchführen und verstehen, wie mehrere Programme und Kommandos mit einfachen Shell-Skripten zu einem automatisierten Ablauf verbunden werden.

---

## Block 3: Einführung in Ansible – Vom manuellen zum automatisierten Systemmanagement

- Ausgangssituation: wiederkehrende Administration mehrerer Linux-Systeme
- Was ist Ansible?
- Typische Anwendungsfälle
  - Configuration Management
  - Provisionierung
  - Deployment
  - wiederkehrende administrative Aufgaben
- Architektur von Ansible
- Control Node und Managed Nodes
- Agentenloses Konzept
- Kommunikation über SSH
- Grundidee von Inventory, Hosts und Gruppen
- Ansible-Module als ausführbare Aktionen
- Abgrenzung der Automatisierungswerkzeuge
  - Shell zur einfachen Orchestrierung
  - Python für eigene Programmlogik
  - Ansible für automatisierte Systemkonfiguration und gewünschte Systemzustände
- Ansible kann ohne selbst geschriebene Python-Skripte eingesetzt werden
- Rolle von Python innerhalb der technischen Ansible-Architektur

### Ziel des Blocks

Die Teilnehmenden verstehen, welches Problem Ansible löst, wie eine Ansible-Umgebung grundsätzlich aufgebaut ist und wie sich Ansible von Shell- und Python-Automatisierung unterscheidet.

---

## Block 4: Ansible – Installation, Setup und erste Automatisierung

- Installation von Ansible
- Überprüfung der Installation
- Aufbau einer einfachen Arbeitsumgebung
- Anlegen eines ersten Inventories
- Verbindung zu Managed Nodes
- Zusammenspiel mit SSH und SSH-Keys
- Erster Verbindungstest
- Einführung in Ad-hoc Commands
- Aufbau eines Ad-hoc Commands
  - Host bzw. Gruppe
  - Modul
  - Modulargumente
- Erste Module
  - `ping`
  - `command`
  - `copy`
  - `package`
- Administrative Aktionen mit `become`
- Rückgabewerte und Statusausgaben verstehen

### Ziel des Blocks

Die Teilnehmenden können eine einfache Ansible-Umgebung einrichten, Managed Nodes erreichen und erste administrative Aufgaben mit Ad-hoc Commands durchführen.

---

## Block 5: Python-Grundlagen I – Python verstehen

- Einordnung von Python als Automatisierungswerkzeug
- Rolle von Python im Umfeld von Linux und Ansible
- Ausführen von Python-Programmen
- Grundsyntax
- Variablen
- grundlegende Datentypen
  - Strings
  - Integer und Float
  - Boolean
- Operatoren und einfache Ausdrücke
- wichtige Datenstrukturen
  - Listen
  - Dictionaries
- Zugriff auf Elemente und Werte
- Ein- und Ausgabe
- Lesen und Verstehen einfacher Python-Skripte
- Parallelen zwischen Python-Datenstrukturen und später verwendeten YAML-Strukturen

### Ziel des Blocks

Die Teilnehmenden verstehen grundlegenden Python-Code und können einfache Daten und Datenstrukturen in Python verarbeiten.

---

## Block 6: Python-Grundlagen II – Eigene Automatisierungsskripte

- Kontrollstrukturen
  - `if` / `elif` / `else`
- Schleifen
  - insbesondere `for`
- Iteration über Listen und Dictionaries
- Funktionen
  - Parameter
  - Rückgabewerte
- Verwendung von Modulen
- grundlegende Fehlerbehandlung
  - Exceptions
  - `try` / `except`
- Arbeiten mit Dateien
- Ausführen externer Programme
- Schreiben einfacher Automatisierungsskripte
- Zusammenspiel von Shell und Python
- Zusammenhang zwischen Python und Ansible-Modulen
- Abgrenzung
  - eigenes Python-Skript
  - vorhandenes Ansible-Modul

### Ziel des Blocks

Die Teilnehmenden können überschaubare Automatisierungsaufgaben selbstständig mit Python implementieren und verstehen, wann ein Python-Skript und wann Ansible das geeignetere Werkzeug ist.

---

## Block 7: Ansible Playbooks – Deklarative Automatisierung

- Vom Ad-hoc Command zum Playbook
- Einführung in YAML
  - Einrückung
  - Listen
  - Dictionaries
  - Schlüssel und Werte
- Aufbau eines Playbooks
- Plays
- Hosts
- Tasks
- Module und Modulparameter
- Einsatz bekannter Module in Playbooks
  - `copy`
  - `file`
  - `package`
  - `service`
- `become` in Playbooks
- Ausführen von Playbooks
- Ausgaben und Status
  - `ok`
  - `changed`
  - `failed`
- Einführung in das Konzept der Idempotenz
- Imperatives Kommando gegenüber gewünschtem Systemzustand

### Ziel des Blocks

Die Teilnehmenden können einfache Playbooks erstellen und verstehen den Wechsel von einzelnen Aktionen hin zur deklarativen Beschreibung gewünschter Systemzustände.

---

## Block 8: Inventories, Variablen und Facts

- Vertiefung von Inventories
- Inventory-Formate
  - INI
  - YAML
- Hosts und Gruppen
- Variablen definieren und verwenden
- Playbook-Variablen
- Host-Variablen
- Gruppenvariablen
- `host_vars`
- `group_vars`
- zusätzliche Variablen
- Grundprinzip der Variablen-Priorität
- keine vollständige Vertiefung der Ansible Variable Precedence
- Ansible Facts
- Ermitteln von Systeminformationen
- Verwendung von Facts in Tasks
- Verbindung von Facts, Variablen und Systemkonfiguration

### Ziel des Blocks

Die Teilnehmenden können Playbooks für unterschiedliche Hosts und Gruppen parametrisieren und Informationen der Managed Nodes in ihre Automatisierung einbeziehen.

---

## Block 9: Templates, Bedingungen und Handler

- Einführung in Jinja2
- Erstellen dynamischer Konfigurationsdateien
- Verwendung von Variablen in Templates
- Verwendung von Facts in Templates
- Bedingungen in Playbooks
- Bedingungen in Templates
- Schleifen in Playbooks und Templates
- Übertragen generierter Konfigurationen
- Handler
- `notify`
- Handler nur bei tatsächlichen Änderungen ausführen
- Zusammenhang zwischen Template, Konfigurationsänderung, `notify`, Handler und Neustart bzw. Reload eines Dienstes
- Zusammenhang mit Idempotenz

### Ziel des Blocks

Die Teilnehmenden können systemabhängige Konfigurationen erzeugen und Aktionen gezielt von Änderungen und Systemzuständen abhängig machen.

---

## Block 10: Rollen und Strukturierung größerer Ansible-Projekte

- Grenzen umfangreicher einzelner Playbooks
- Motivation für Rollen
- Wiederverwendbarkeit
- Aufbau einer Rolle
- Verzeichnisstruktur
  - `tasks`
  - `handlers`
  - `templates`
  - `files`
  - `defaults`
  - `vars`
- Überführung bestehender Tasks in eine Rolle
- Verwendung von Rollen in Playbooks
- Trennung von Daten, Logik und Templates
- Best Practices für die Projektorganisation
- übersichtliche und wartbare Ansible-Projekte

### Ziel des Blocks

Die Teilnehmenden können umfangreichere Ansible-Automatisierungen sinnvoll strukturieren und wiederverwendbare Bestandteile in Rollen organisieren.

---

## Block 11: Fehlerbehandlung, Debugging und Tests

- Fehler in Ansible verstehen
- Interpretation der Ansible-Ausgabe
- Debugging mit dem `debug`-Modul
- Variablen und Facts zur Laufzeit untersuchen
- Umgang mit Fehlern
  - `ignore_errors`
  - `failed_when`
- sinnvolle Fehlerbedingungen
- Logging und Verbosity
- Idempotenz überprüfen
- Playbooks mehrfach ausführen
- Unterschied zwischen
  - `ok`
  - `changed`
  - `failed`
- saubere und reproduzierbare Runs
- grundlegende Strategien zum Testen von Automatisierungen

### Ziel des Blocks

Die Teilnehmenden können typische Fehler in Ansible-Automatisierungen analysieren und beurteilen, ob Playbooks reproduzierbar und idempotent arbeiten.

---

## Block 12: Praxisprojekt – Linux, Python und Ansible im Zusammenspiel

- Umsetzung eines durchgängigen Automatisierungsszenarios
- Ausgangspunkt ist eine administrative Aufgabe auf Linux-Systemen
- Einbindung eines Python-Skripts für eigene Verarbeitungslogik
- optionaler Einsatz eines einfachen Shell-Skripts zur Ablaufsteuerung
- Verwaltung mehrerer Managed Nodes mit Ansible
- Verwendung eines Inventories
- Variablen und Facts
- Installation und Konfiguration eines Dienstes
- Erzeugen einer Konfigurationsdatei über ein Template
- Reaktion auf Änderungen über Handler
- Strukturierung über eine Rolle
- Überprüfung der Idempotenz
- Fehleranalyse und Debugging
- gemeinsame Betrachtung der eingesetzten Werkzeuge
  - Was übernimmt Linux?
  - Was übernimmt die Shell?
  - Was übernimmt Python?
  - Was übernimmt Ansible?
- Zusammenfassung
- Q&A

### Ziel des Blocks

Die Teilnehmenden führen die Inhalte des Seminars in einem zusammenhängenden Szenario zusammen und können begründet entscheiden, welches Werkzeug für welchen Teil einer Automatisierungsaufgabe eingesetzt werden sollte.