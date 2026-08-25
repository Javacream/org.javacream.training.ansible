# Trainerleitfaden – Block 10: Rollen und Strukturierung größerer Ansible-Projekte

## 1. Zielsetzung

Block 10 führt Rollen als Strukturierungs- und Wiederverwendungskonzept ein. Ausgangspunkt ist ein bereits gewachsenes Playbook aus den vorherigen Blöcken.

## 2. Lernziele

Die Teilnehmenden können:

- Motivation und Nutzen von Rollen erklären,
- die Standardverzeichnisstruktur einer Rolle einordnen,
- Tasks, Handler, Templates, Files, Defaults und Vars sinnvoll zuordnen,
- bestehende Tasks in eine Rolle überführen,
- Rollen aus einem Playbook aufrufen,
- Daten und Implementierung besser trennen,
- einfache Best Practices für Projektorganisation anwenden.

## 3. Warum Rollen?

- große Playbooks werden unübersichtlich
- Wiederverwendung
- Trennung von Verantwortlichkeiten
- standardisierte Struktur

## 4. Rollenstruktur

- `tasks/main.yml`
- `handlers/main.yml`
- `templates/`
- `files/`
- `defaults/main.yml`
- `vars/main.yml`

## 5. Defaults vs. Vars

- Defaults als leicht überschreibbare Standardwerte
- Vars mit höherer Priorität
- im Einsteigerkontext bevorzugt Defaults für konfigurierbare Rollenparameter

## 6. Rolle erzeugen

- manuell oder mit `ansible-galaxy role init`
- Struktur lesen und reduzieren

## 7. Bestehende Automatisierung überführen

Der Trainer nimmt ein bekanntes Playbook aus Block 9 und verschiebt:

- Tasks
- Handler
- Template
- Defaultvariablen

in eine Rolle.

## 8. Rolle verwenden

- `roles`
- Rolle aus Play aufrufen
- Variablen überschreiben

## 9. Best Practices

- sprechende Rollennamen
- eine klare Verantwortung pro Rolle
- keine unnötige Komplexität
- Defaults dokumentieren
- wiederverwendbare Ressourcen in Rolle halten

## 10. Abschlussübung

Ein bestehendes Playbook wird in mindestens eine Rolle überführt und mit unterschiedlichen Variablen auf zwei Hostgruppen angewendet.

## 11. Überleitung zu Block 11

Die Projektstruktur ist nun sauber. Als Nächstes geht es darum, Fehler gezielt zu analysieren und Automatisierungen reproduzierbar zu testen.
