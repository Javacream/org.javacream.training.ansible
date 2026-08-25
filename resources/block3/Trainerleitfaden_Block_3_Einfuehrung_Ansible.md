# Trainerleitfaden – Block 3: Einführung in Ansible – Vom manuellen zum automatisierten Systemmanagement

## 1. Zielsetzung des Blocks

Block 3 führt Ansible zunächst als Konzept und Werkzeug zur zentralen Automatisierung von Linux-Systemen ein. Die Teilnehmenden sollen verstehen, welches Problem Ansible löst und wie es sich in die bisher behandelten Automatisierungsformen einordnet.

Der Block ist bewusst vor den Python-Grundlagen positioniert. Die Teilnehmenden erhalten dadurch früh ein Zielbild für die spätere Automatisierung und können Python anschließend im Kontext von Linux und Ansible einordnen.

Ansible wird in diesem Block noch nicht systematisch praktisch eingesetzt. Installation, Aufbau einer konkreten Arbeitsumgebung, Inventory-Dateien und Ad-hoc Commands werden in Block 4 praktisch vertieft.

---

## 2. Lernziele

Nach Abschluss des Blocks können die Teilnehmenden:

- typische Probleme manueller Administration mehrerer Linux-Systeme beschreiben,
- Zweck und grundlegende Einsatzgebiete von Ansible erklären,
- Control Node und Managed Nodes unterscheiden,
- das agentenlose Architekturprinzip von Ansible erklären,
- SSH als wesentlichen Transportmechanismus einordnen,
- die Grundidee von Inventory, Hosts und Gruppen erklären,
- den Zweck von Ansible-Modulen beschreiben,
- imperative und deklarative Automatisierung grundsätzlich unterscheiden,
- Shell, Python und Ansible hinsichtlich ihrer Rolle in einer Automatisierung einordnen,
- erklären, dass für die Nutzung von Ansible keine selbst geschriebenen Python-Skripte erforderlich sind,
- die technische Rolle von Python innerhalb von Ansible grundsätzlich einordnen.

---

## 3. Ausgangssituation: Manuelle Administration mehrerer Systeme

### Inhalt

Ausgangspunkt sind die Aufgaben aus Block 2:

- Pakete installieren
- Dienste verwalten
- Konfigurationen bearbeiten
- Erreichbarkeit prüfen
- per SSH auf entfernten Systemen arbeiten
- einfache Abläufe über Shell-Skripte automatisieren

Die Fragestellung wird nun auf mehrere Systeme erweitert.

Typische Probleme:

- derselbe Arbeitsschritt muss auf mehreren Hosts wiederholt werden,
- Systeme können unterschiedliche Ausgangszustände besitzen,
- manuelle Änderungen sind fehleranfällig,
- Änderungen müssen nachvollziehbar und reproduzierbar sein,
- Fehler auf einzelnen Hosts müssen erkannt werden,
- Konfigurationen sollen zentral verwaltet werden.

### Didaktischer Einstieg

Der Trainer entwickelt zunächst ein Szenario mit mehreren Linux-Servern und fragt, wie eine bereits bekannte administrative Aufgabe auf zehn, fünfzig oder hundert Hosts ausgeführt werden könnte.

Mögliche Antworten wie manuelle SSH-Sitzungen, Shell-Schleifen oder eigene Skripte werden aufgenommen und hinsichtlich ihrer Grenzen diskutiert.

### Ziel

Die Notwendigkeit eines Configuration-Management- bzw. Automatisierungswerkzeugs soll aus einem bekannten Problem entstehen, bevor Ansible als Lösung vorgestellt wird.

---

## 4. Was ist Ansible?

### Inhalt

Ansible ist ein Werkzeug zur Automatisierung von IT-Aufgaben.

Typische Einsatzgebiete:

- Configuration Management
- Provisionierung
- Software-Deployment
- wiederkehrende administrative Aufgaben
- Orchestrierung von Abläufen

Wichtige Eigenschaften:

- zentrale Steuerung
- Automatisierung mehrerer Zielsysteme
- wiederholbare Abläufe
- deklarative Beschreibung gewünschter Zustände
- Automatisierung über vorhandene Schnittstellen und Module

### Trainerhinweis

Ansible sollte nicht ausschließlich als "Tool zum Ausführen von Befehlen über SSH" eingeführt werden. Das würde das spätere Verständnis von Modulen, Zuständen und Idempotenz erschweren.

Ebenso sollte Ansible nicht als Ersatz für jede Form von Shell- oder Python-Automatisierung dargestellt werden.

---

## 5. Architektur: Control Node und Managed Nodes

### Inhalt

Grundmodell:

- Control Node
- Managed Nodes
- Netzwerkverbindung zwischen den Systemen
- Ansible wird vom Control Node aus gestartet

Der Control Node enthält typischerweise:

- Ansible
- Inventory
- Automatisierungsdefinitionen
- benötigte Konfigurationen und Templates

Managed Nodes sind die Systeme, deren Zustand verwaltet wird.

### Demonstration

Der Trainer zeigt eine einfache vorbereitete Architektur mit einem Control Node und mehreren Managed Nodes.

Noch werden keine Installationsschritte durchgeführt.

### Didaktischer Hinweis

Die Begriffe sollten konsequent verwendet werden. Insbesondere sollte vermieden werden, Managed Nodes als "Ansible-Server" zu bezeichnen.

---

## 6. Agentenloses Konzept

### Inhalt

Ansible benötigt für typische Linux-Verwaltung keinen dauerhaft laufenden Ansible-Agenten auf den Managed Nodes.

Zu erläutern sind:

- Steuerung vom Control Node
- Nutzung vorhandener Remote-Zugänge
- kein eigener dauerhaft laufender Ansible-Dienst auf den Zielsystemen
- Vorteile für Installation und Betrieb

### Abgrenzung

"Agentenlos" bedeutet nicht, dass auf einem Managed Node keinerlei Voraussetzungen bestehen.

Je nach verwendetem Modul und Zielsystem können beispielsweise benötigt werden:

- SSH-Zugang
- geeigneter Benutzer
- Rechteerhöhung
- Python-Laufzeit oder andere vom Modul benötigte Komponenten

### Trainerhinweis

Diese Differenzierung ist wichtig, damit aus "agentless" nicht fälschlicherweise "Managed Nodes benötigen überhaupt nichts" wird.

---

## 7. Kommunikation über SSH

### Inhalt

Der Bezug zu Block 2 wird hergestellt:

- SSH-Verbindung
- Benutzer
- Hostname bzw. IP-Adresse
- SSH-Key
- Public-Key-Authentifizierung
- Host-Key-Prüfung

Ansible kann diese bereits bekannte Infrastruktur für die Kommunikation mit Linux-Managed-Nodes nutzen.

### Didaktischer Hinweis

Dieser Abschnitt sollte bewusst kurz bleiben. SSH wurde bereits praktisch behandelt. Hier geht es um dessen Rolle innerhalb der Ansible-Architektur.

### Ausblick

Administrative Aufgaben benötigen häufig erhöhte Rechte. Das bereits bekannte `sudo` wird später in Ansible über Privilege Escalation bzw. `become` aufgegriffen.

---

## 8. Inventory, Hosts und Gruppen – Grundidee

### Inhalt

Das Inventory beschreibt, welche Zielsysteme Ansible verwalten soll.

Grundbegriffe:

- Host
- Gruppe
- Zuordnung mehrerer Hosts zu einer Gruppe
- logische Gruppierung nach Aufgabe oder Umgebung

Mögliche Gruppierung:

- Webserver
- Datenbankserver
- Testsysteme
- Produktionssysteme

### Trainerhinweis

Syntax und unterschiedliche Inventory-Formate werden noch nicht vertieft. Die Teilnehmenden sollen zunächst das Modell verstehen.

### Demonstration

Der Trainer zeigt ein vorbereitetes kleines Inventory und erläutert ausschließlich:

- einzelne Hosts
- Gruppen
- Beziehung zwischen Gruppe und Hosts

Die praktische Erstellung folgt in Block 4.

---

## 9. Ansible-Module – Aktionen auf Managed Nodes

### Inhalt

Ansible verwendet Module für konkrete Aufgaben.

Beispiele für Aufgabenklassen:

- Paket verwalten
- Datei kopieren
- Datei oder Verzeichnis verwalten
- Dienst verwalten
- Kommando ausführen

Grundidee:

**Zielsystem + Modul + Parameter → Ergebnis**

### Wichtige Abgrenzung

Ein Modul ist nicht gleichbedeutend mit einem selbst geschriebenen Python-Skript.

Ansible stellt eine große Zahl vorhandener Module bereit. Anwender können diese verwenden, ohne selbst Python-Code zu schreiben.

### Didaktischer Hinweis

Konkrete Modulsyntax wird noch nicht vermittelt. Einige Modulnamen können zur Orientierung genannt werden, die praktische Verwendung folgt in Block 4.

---

## 10. Imperative und deklarative Automatisierung

### Inhalt

Ein zentraler konzeptioneller Unterschied wird eingeführt.

Imperativ:

- führe konkrete Schritte bzw. Kommandos aus

Deklarativ:

- stelle einen gewünschten Zustand her

Beispielhafte Fragestellung ohne konkrete Ansible-Syntax:

Imperativ:

- Installiere Paket X.
- Starte Dienst Y.

Deklarativ:

- Paket X soll installiert sein.
- Dienst Y soll laufen.

### Bezug zur Idempotenz

Der Begriff Idempotenz kann als Ausblick eingeführt werden:

Wird derselbe gewünschte Zustand erneut angefordert und ist er bereits erreicht, sollte keine unnötige Änderung erfolgen.

Die systematische Behandlung erfolgt erst bei den Playbooks.

### Trainerhinweis

Nicht jedes Ansible-Modul arbeitet ausschließlich deklarativ. Module zum direkten Ausführen von Kommandos existieren ebenfalls. Ansible unterstützt beide Arbeitsweisen, fördert aber bei Configuration Management die Beschreibung gewünschter Zustände.

---

## 11. Shell, Python und Ansible im Vergleich

### Inhalt

Die drei Werkzeuge erhalten klar unterscheidbare Rollen.

### Shell

Geeignet für:

- Aufruf vorhandener Programme
- einfache Befehlssequenzen
- einfache lokale Orchestrierung
- Pipeline-artige Abläufe

### Python

Geeignet für:

- eigene Programmlogik
- Datenverarbeitung
- komplexere Entscheidungen und Abläufe
- eigene Automatisierungsprogramme

Die praktische Einführung folgt in Block 5 und 6.

### Ansible

Geeignet für:

- zentrale Verwaltung mehrerer Systeme
- Configuration Management
- reproduzierbare Systemzustände
- Remote-Automatisierung
- Orchestrierung über mehrere Systeme

### Didaktischer Hinweis

Die Abgrenzung ist keine harte technische Grenze. Alle drei Werkzeuge können sich funktional überschneiden.

Ziel ist, den Teilnehmenden ein sinnvolles Entscheidungsmodell zu geben und nicht künstliche Verbote zu formulieren.

---

## 12. Die Rolle von Python in Ansible

### Inhalt

Zu unterscheiden sind zwei Aussagen:

1. Ansible selbst und viele seiner Module basieren technisch auf Python bzw. nutzen Python.
2. Anwender müssen deshalb nicht selbst Python-Skripte schreiben, um Ansible verwenden zu können.

### Wichtige Aussage

**Ansible verwenden** und **eigene Ansible-Module in Python entwickeln** sind unterschiedliche Dinge.

Im Seminar werden zunächst vorhandene Ansible-Module verwendet.

### Ausblick auf Python

Die folgenden Python-Blöcke vermitteln Python als eigenständiges Automatisierungswerkzeug. Dadurch können die Teilnehmenden später auch besser verstehen, wie Python und Ansible technisch zusammenspielen.

---

## 13. Konzeptübung: Das passende Werkzeug wählen

### Ziel

Die Teilnehmenden ordnen unterschiedliche Automatisierungsaufgaben Shell, Python oder Ansible zu und begründen ihre Entscheidung.

Dabei sollte ausdrücklich erlaubt sein, dass mehrere Werkzeuge technisch möglich sind.

Entscheidend ist die Begründung anhand von Kriterien wie:

- ein oder viele Systeme
- vorhandenes Programm oder eigene Logik
- gewünschter Zustand oder konkrete Befehlssequenz
- Wiederholbarkeit
- Komplexität der Datenverarbeitung

### Trainerhinweis

Die Übung dient nicht dazu, eine starre Zuordnung auswendig zu lernen. Sie soll die unterschiedlichen Rollen der Werkzeuge diskutierbar machen.

---

## 14. Architekturübung

### Ziel

Die Teilnehmenden erhalten ein Szenario mit:

- einem Administrationssystem,
- mehreren Linux-Servern,
- verschiedenen Servergruppen,
- SSH-Zugängen.

Sie identifizieren:

- Control Node
- Managed Nodes
- mögliche Inventory-Gruppen
- Kommunikationsweg
- notwendige grundlegende Voraussetzungen

Die Übung bleibt konzeptionell und benötigt noch keine funktionsfähige Ansible-Installation.

---

## 15. Typische Fragen und Missverständnisse

Der Trainer sollte insbesondere mit folgenden Punkten rechnen:

- "Ansible ist nur SSH für viele Server."
- "Auf jedem Managed Node muss Ansible installiert werden."
- "Agentenlos bedeutet, dass der Zielhost keinerlei Voraussetzungen benötigt."
- "Für Ansible muss ich Python programmieren können."
- "Ansible ersetzt Shell und Python."
- "Ein Inventory ist nur eine Liste von IP-Adressen."
- "Deklarativ bedeutet, dass Ansible niemals Kommandos ausführt."
- "Control Node" und "Managed Node" werden verwechselt.
- SSH-Key und Ansible-Konfiguration werden als dasselbe Konzept betrachtet.
- Idempotenz wird mit bloßer Wiederholbarkeit verwechselt.

---

## 16. Überleitung zu Block 4

Die Teilnehmenden kennen nun das Grundmodell:

- ein Control Node,
- mehrere Managed Nodes,
- Kommunikation über SSH,
- ein Inventory zur Beschreibung der Zielsysteme,
- Module zur Durchführung von Aufgaben.

Block 4 setzt dieses Modell praktisch um.

Die Leitfrage lautet:

**Wie wird aus dieser Architektur eine tatsächlich funktionierende Ansible-Arbeitsumgebung?**

Dazu werden Ansible installiert, ein erstes Inventory erstellt, die Verbindung zu Managed Nodes getestet und erste Ad-hoc Commands ausgeführt.
