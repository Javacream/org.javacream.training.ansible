# Trainerleitfaden – Block 5: Python-Grundlagen I – Python verstehen

## 1. Zielsetzung des Blocks

Block 5 vermittelt die Python-Grundlagen, die für einfache Automatisierungsaufgaben und für das Verständnis späterer Ansible-Datenstrukturen benötigt werden.

Python wird als eigenständiges Werkzeug eingeführt. Die Teilnehmenden sollen nicht den Eindruck gewinnen, Python sei nur eine Voraussetzung für Ansible.

## 2. Lernziele

Nach Abschluss können die Teilnehmenden:

- Python-Programme ausführen,
- grundlegende Syntax lesen,
- Variablen und elementare Datentypen verwenden,
- Listen und Dictionaries aufbauen und auslesen,
- einfache Ein- und Ausgaben verarbeiten,
- einfache Python-Skripte lesen und erklären,
- Parallelen zwischen Python-Datenstrukturen und späteren YAML-Strukturen erkennen.

## 3. Python ausführen

### Inhalt

- `python3`
- interaktiver Interpreter
- Skriptdateien
- Dateiendung `.py`

### Demonstration

Ein Ausdruck wird zunächst interaktiv, danach aus einer Datei ausgeführt.

## 4. Syntax und Variablen

### Inhalt

- Zuweisung
- Namen
- Kommentare
- Einrückung als syntaktisches Element
- dynamische Typisierung

## 5. Grundlegende Datentypen

- `str`
- `int`
- `float`
- `bool`
- `None`

### Demonstration

Werte erzeugen, Typen mit `type()` untersuchen und einfache Umwandlungen zeigen.

## 6. Operatoren

- arithmetische Operatoren
- Vergleiche
- logische Operatoren
- String-Verkettung bzw. f-Strings

## 7. Listen

### Inhalt

- geordnete Sammlung
- Indexzugriff
- Länge
- Elemente ergänzen
- Elemente verändern

### Bezug zu Ansible

Listen tauchen später in YAML und bei Loops wieder auf.

## 8. Dictionaries

### Inhalt

- Schlüssel-Wert-Paare
- Zugriff per Schlüssel
- verschachtelte Datenstrukturen

### Bezug zu Ansible

Dictionaries entsprechen strukturell vielen YAML-Mappings und Variablenstrukturen.

## 9. Ein- und Ausgabe

- `print`
- `input`
- einfache Typkonvertierung

## 10. Code lesen

Die Teilnehmenden sollen bewusst kurze Programme lesen und vorhersagen, was sie ausgeben.

## 11. Abschlussübung

Ein kleines Python-Programm verwaltet eine Liste von Servern und zugehörige Eigenschaften in Dictionaries und gibt strukturierte Informationen aus.

## 12. Überleitung zu Block 6

Block 5 behandelt Daten und einfache Ausdrücke. Block 6 ergänzt Kontrollfluss, Funktionen, Module, Dateioperationen und Fehlerbehandlung und macht daraus echte Automatisierungsskripte.
