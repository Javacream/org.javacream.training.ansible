# Trainerleitfaden – Block 12: Praxisprojekt – Linux, Python und Ansible im Zusammenspiel

## 1. Zielsetzung

Block 12 führt die Inhalte des gesamten Seminars in einem zusammenhängenden Praxisprojekt zusammen. Der Schwerpunkt liegt nicht mehr auf neuen Einzeltechniken, sondern auf Auswahl, Kombination und Begründung geeigneter Werkzeuge.

## 2. Lernziele

Die Teilnehmenden können:

- eine Automatisierungsaufgabe in Teilprobleme zerlegen,
- Linux-, Shell-, Python- und Ansible-Anteile sinnvoll voneinander abgrenzen,
- einen kleinen automatisierten Gesamtprozess entwerfen,
- Python für eigene Verarbeitungslogik einsetzen,
- Ansible für Hostgruppen und Systemzustände verwenden,
- Variablen, Facts, Templates, Handler und Rollen kombinieren,
- Idempotenz und Fehlerverhalten prüfen,
- ihre Werkzeugwahl begründen.

## 3. Projektszenario

Eine kleine Serverlandschaft soll standardisiert vorbereitet werden.

Anforderungen können sein:

- mehrere Linux-Hosts
- mindestens zwei Hostgruppen
- ein Dienst bzw. Paket
- eine Konfigurationsdatei
- host- oder gruppenspezifische Werte
- ein Python-Schritt zur Berechnung oder Aufbereitung von Daten
- optional ein einfaches Shell-Skript zur Ablaufsteuerung

## 4. Phase 1: Aufgabe analysieren

Die Teilnehmenden bestimmen:

- welche Schritte reine Linux-Administration darstellen,
- welche Logik in Python gehört,
- welche Zustände Ansible verwalten soll,
- ob eine Shell-Sequenz als übergeordnete Orchestrierung sinnvoll ist.

## 5. Phase 2: Python-Komponente

Das Python-Programm übernimmt eine klar abgegrenzte eigene Logik, zum Beispiel:

- Einlesen strukturierter Eingangsdaten
- Validierung
- Ableitung bzw. Berechnung von Konfigurationswerten
- Ausgabe als JSON oder YAML-nahe Datenquelle

## 6. Phase 3: Ansible-Projekt

Das Projekt enthält mindestens:

- Inventory
- Hostgruppen
- `group_vars` bzw. `host_vars`
- Rolle
- Tasks
- Template
- Handler
- Verwendung mindestens eines Facts

## 7. Phase 4: Integration

Die erzeugten bzw. berechneten Werte werden in den Automatisierungsprozess eingebunden.

Wichtig ist die klare Abgrenzung:

Python erzeugt oder verarbeitet Daten; Ansible verwaltet die Zielsysteme.

## 8. Phase 5: Test

- Connectivity
- korrekte Variablen
- erfolgreicher erster Run
- zweiter Run zur Idempotenzprüfung
- absichtlicher Fehlerfall
- verständliche Diagnose

## 9. Reflexion

Die Teilnehmenden beantworten:

- Warum wurde welcher Schritt mit welchem Werkzeug umgesetzt?
- Welche Alternative wäre technisch möglich?
- Welche Lösung wäre bei 100 statt 3 Hosts noch tragfähig?
- Wo liegen Grenzen der gewählten Umsetzung?

## 10. Abschluss

Der Trainer greift den gesamten Lernpfad nochmals auf:

- Linux: System und Administration
- Shell: einfache Orchestrierung
- Python: eigene Programmlogik
- Ansible: deklarative Systemautomatisierung

Das zentrale Abschlussziel lautet: Nicht ein Werkzeug für alles verwenden, sondern die geeignete Abstraktionsebene wählen.
