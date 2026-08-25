# Trainerleitfaden – Block 8: Inventories, Variablen und Facts

## 1. Zielsetzung

Block 8 löst feste Werte aus den bisherigen Playbooks heraus und macht Automatisierungen für unterschiedliche Hosts, Gruppen und Umgebungen parametrisierbar.

## 2. Lernziele

Die Teilnehmenden können:

- Inventory-Dateien in INI und YAML einordnen,
- Hosts und Gruppen strukturieren,
- Variablen in Playbooks verwenden,
- Host- und Gruppenvariablen einsetzen,
- `host_vars` und `group_vars` verwenden,
- zusätzliche Variablen einordnen,
- das Grundprinzip der Variablenpriorität erklären,
- Facts anzeigen und in Tasks verwenden.

## 3. Inventory vertiefen

- Gruppen
- Gruppen von Gruppen nur bei Bedarf
- Hostvariablen
- YAML- vs. INI-Format

## 4. Variablen

- Definition
- Verwendung mit Jinja-Ausdrücken
- Datentypen
- Bezug zu Python-Listen und Dictionaries

## 5. `group_vars` und `host_vars`

- Trennung von Struktur und Daten
- gruppenweite Werte
- hostspezifische Überschreibungen

## 6. Zusätzliche Variablen

- `--extra-vars`
- bewusst nur als Konzept
- hohe Priorität als Merksatz

## 7. Variablenpriorität

Keine vollständige Precedence-Tabelle. Wichtig ist nur: Variablen können aus mehreren Quellen stammen und näher bzw. expliziter gesetzte Werte können andere übersteuern.

## 8. Facts

- automatische Systeminformationen
- `gather_facts`
- typische Facts wie Distribution, Hostname, IPv4-Daten
- Anzeige mit `debug`

## 9. Abschlussübung

Ein Playbook installiert bzw. konfiguriert einen Dienst unterschiedlich für mehrere Hostgruppen und verwendet zusätzlich mindestens einen Fact.

## 10. Überleitung zu Block 9

Variablen und Facts liefern Daten. Block 9 nutzt diese Daten in Templates, Bedingungen, Schleifen und Handlern.
