# Trainerleitfaden – Block 9: Templates, Bedingungen und Handler

## 1. Zielsetzung

Block 9 macht Playbooks dynamisch. Die Teilnehmenden erzeugen Konfigurationsdateien aus Templates, verwenden Bedingungen und Schleifen und reagieren über Handler nur dann auf Änderungen, wenn dies erforderlich ist.

## 2. Lernziele

Die Teilnehmenden können:

- Jinja2-Templates erstellen,
- Variablen und Facts in Templates verwenden,
- Bedingungen in Tasks einsetzen,
- einfache Bedingungen und Schleifen in Templates formulieren,
- Loops in Playbooks verwenden,
- Handler definieren und mit `notify` auslösen,
- Zusammenhang von Konfigurationsänderung, Handler und Idempotenz erklären.

## 3. Jinja2

- Template als Quelldatei
- `{{ variable }}`
- einfache Filter nur bei Bedarf

## 4. Template-Modul

- `template`
- `src`
- `dest`
- Dateirechte optional

## 5. Bedingungen

- `when`
- host- oder factabhängige Ausführung

## 6. Schleifen

- `loop`
- `item`
- Listen verarbeiten
- Bezug zu Python-Listen

## 7. Bedingungen und Schleifen in Templates

Nur grundlegende Jinja2-Syntax. Komplexe Template-Logik vermeiden.

## 8. Handler

- eigener Abschnitt
- `notify`
- Ausführung nur bei Änderung
- typischer Einsatz: Reload oder Restart eines Dienstes

## 9. Idempotenz vertiefen

Eine unveränderte Template-Datei löst keinen Handler aus.

## 10. Abschlussübung

Eine Dienstkonfiguration wird aus Variablen und Facts erzeugt, bei Änderung wird ein Handler ausgelöst, und zusätzliche Ressourcen werden über eine Schleife angelegt.

## 11. Überleitung zu Block 10

Das Playbook besitzt nun viele Bestandteile. Block 10 strukturiert diese in wiederverwendbare Rollen.
