# Trainerleitfaden – Block 6: Python-Grundlagen II – Eigene Automatisierungsskripte

## 1. Zielsetzung

Block 6 erweitert die Daten- und Syntaxgrundlagen aus Block 5 zu eigenständigen Automatisierungsskripten. Die Teilnehmenden lernen Kontrollstrukturen, Schleifen, Funktionen, Module, Dateien, externe Programme und grundlegende Fehlerbehandlung.

## 2. Lernziele

Nach Abschluss können die Teilnehmenden:

- Entscheidungen mit `if` formulieren,
- Listen und Dictionaries mit Schleifen verarbeiten,
- Funktionen mit Parametern und Rückgabewerten erstellen,
- Standardmodule importieren und verwenden,
- Dateien lesen und schreiben,
- externe Programme kontrolliert aufrufen,
- einfache Exceptions behandeln,
- kleine Automatisierungsprogramme strukturieren,
- Python-Skript und Ansible-Modul sinnvoll unterscheiden.

## 3. Bedingungen

- `if`, `elif`, `else`
- Vergleichsoperatoren
- Wahrheitswerte

## 4. Schleifen

- `for`
- Iteration über Listen
- Iteration über Dictionaries
- `range` nur bei Bedarf

## 5. Funktionen

- `def`
- Parameter
- Rückgabewerte
- lokale Variablen
- Nutzen für Wiederverwendung und Testbarkeit

## 6. Module

- `import`
- Standardbibliothek
- Beispielmodule wie `pathlib`, `json`, `subprocess`

## 7. Dateien

- Lesen
- Schreiben
- `with open(...)`
- Textdateien als typische Automatisierungsquelle

## 8. Fehlerbehandlung

- Exceptions
- `try` / `except`
- sinnvolle Fehlerbehandlung statt pauschalem Unterdrücken

## 9. Externe Programme

- `subprocess.run`
- Exit Code
- Standardausgabe
- Bezug zu Shell-Skripten aus Block 2

## 10. Python und Ansible

Python eignet sich für eigene Programmlogik. Ansible bietet für viele Administrationsaufgaben bereits fertige Module. Eigener Python-Code ist sinnvoll, wenn die benötigte Logik über vorhandene Ansible-Funktionalität hinausgeht.

## 11. Abschlussübung

Ein Python-Skript liest eine einfache Serverdefinition aus einer Datei, prüft die Daten und führt für ausgewählte Einträge eine lokale Testaktion aus.

## 12. Überleitung zu Block 7

Nach Linux, erster Ansible-Erfahrung und Python-Grundlagen folgt nun die systematische Automatisierung mit Playbooks.
