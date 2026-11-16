# Trainerleitfaden – Block 4: Ansible – Installation, Setup und erste Automatisierung

## 1. Zielsetzung des Blocks

Block 4 setzt das in Block 3 entwickelte Architekturmodell praktisch um. Die Teilnehmenden installieren Ansible auf dem Control Node, richten eine einfache Arbeitsumgebung ein, erstellen ein erstes Inventory und testen die Kommunikation zu Managed Nodes.

Anschließend führen sie erste Ad-hoc Commands aus. Im Mittelpunkt steht dabei noch nicht die Playbook-Syntax, sondern das Grundmuster aus Zielhost bzw. Hostgruppe, Modul, Modulparametern und Ergebnis.

## 2. Lernziele

Nach Abschluss des Blocks können die Teilnehmenden:

- Ansible auf einem Control Node installieren und die Installation prüfen,
- ein einfaches Projektverzeichnis aufbauen,
- ein erstes Inventory anlegen,
- Managed Nodes über SSH erreichen,
- die Verbindung mit dem Ansible-Ping-Modul testen,
- Ad-hoc Commands syntaktisch einordnen,
- einfache Module wie `ping`, `command`, `copy` und `package` verwenden,
- administrative Aktionen mit `become` ausführen,
- Rückgabewerte wie `SUCCESS`, `CHANGED` oder Fehlerausgaben interpretieren.

## 3. Installation von Ansible

### Inhalt

- Installation über den Paketmanager oder eine Python-basierte Umgebung
- Unterschied zwischen `ansible` und `ansible-core`
- Versionsprüfung mit `ansible --version`
- Bedeutung von Python auf dem Control Node

### Demonstration

Der Trainer installiert Ansible in der vorgesehenen Schulungsumgebung und zeigt anschließend die Versionsausgabe.

### Trainerhinweis

Die Installation sollte auf genau einem standardisierten Weg erfolgen. Mehrere alternative Installationsvarianten können erwähnt werden, sollten aber nicht parallel praktisch durchgeführt werden.

## 4. Aufbau der Arbeitsumgebung

### Inhalt

Ein einfaches Projektverzeichnis enthält zunächst:

- Inventory
- optionale `ansible.cfg`
- später Playbooks und weitere Dateien

### Demonstration

Der Trainer erzeugt ein minimales Arbeitsverzeichnis und führt alle weiteren Schritte daraus aus.

## 5. Erstes Inventory

### Inhalt

- Hosteinträge
- Gruppen
- Hostnamen bzw. IP-Adressen
- Verbindungsparameter nur soweit nötig
- Prüfung mit `ansible-inventory`

### Übung

Die Teilnehmenden erstellen ein kleines Inventory mit mindestens zwei Hostgruppen.

### Typische Fehler

- falsche Gruppenbezeichnung
- Tippfehler bei Hostnamen
- nicht erreichbare IP-Adresse
- falscher SSH-Benutzer

## 6. Verbindung zu Managed Nodes

### Inhalt

- SSH als Transportmechanismus
- Wiederverwendung vorhandener SSH-Keys
- Host-Key-Prüfung
- Benutzerzuordnung
- Rechteerhöhung erst bei Bedarf

### Demonstration

Zuerst erfolgt ein direkter SSH-Test, anschließend der gleiche Verbindungsweg über Ansible.

## 7. Ad-hoc Commands

### Inhalt

Grundmuster:

`ansible <pattern> -m <module> -a "<argumente>"`

Zu erläutern sind:

- Host Pattern
- Modul
- Modulargumente
- Ausgabe pro Host

### Didaktischer Hinweis

Ad-hoc Commands dienen in diesem Block vor allem dazu, das Ansible-Ausführungsmodell zu verstehen. Sie ersetzen noch keine Playbooks.

## 8. Erste Module

### `ping`

- testet die grundsätzliche Ansible-Kommunikation
- ist kein ICMP-Ping

### `command`

- führt ein Kommando auf dem Managed Node aus
- dient als Brücke zur bekannten Shell-Administration

### `copy`

- überträgt Dateien auf Managed Nodes
- führt bereits an Zustandsverwaltung heran

### `package`

- verwaltet Pakete
- abstrahiert den Paketmanager des Zielsystems

## 9. `become`

### Inhalt

- Verbindung als normaler Benutzer
- administrative Task
- Privilege Escalation
- Bezug zu `sudo` aus Block 1 und 2

### Typische Fehler

- `become` mit SSH-Anmeldung als `root` gleichsetzen
- fehlende sudo-Berechtigung
- Passwortabfrage ohne passende Konfiguration

## 10. Ergebnisse und Statusausgaben

Zu unterscheiden sind insbesondere:

- `SUCCESS`
- `CHANGED`
- `FAILED`
- `UNREACHABLE`

Die Teilnehmenden sollen erkennen, ob ein Fehler aus der Verbindung, aus fehlenden Rechten oder aus der ausgeführten Aufgabe selbst stammt.

## 11. Abschlussübung

Die Teilnehmenden:

- prüfen ihr Inventory,
- testen alle Hosts mit dem Ping-Modul,
- führen einen Diagnosebefehl remote aus,
- kopieren eine Testdatei auf eine Hostgruppe,
- installieren ein freigegebenes Paket mit `become`,
- interpretieren die Ergebnisse.

## 12. Überleitung zu Block 5

Ansible funktioniert nun praktisch. Die Teilnehmenden haben aber noch kein eigenes Automatisierungsprogramm geschrieben.

Block 5 führt Python als eigenständiges Werkzeug ein und schafft zugleich Verständnis für Datenstrukturen, die später in YAML und Ansible wieder auftauchen.
