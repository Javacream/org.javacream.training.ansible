# Trainerleitfaden – Block 7: Ansible Playbooks – Deklarative Automatisierung

## 1. Zielsetzung

Block 7 führt von Ad-hoc Commands zu wiederverwendbaren Playbooks. Dabei werden die notwendigen YAML-Grundlagen, die Struktur aus Plays und Tasks, Modulaufrufe, `become` und die zentrale Idee der Idempotenz vermittelt.

## 2. Lernziele

Nach Abschluss können die Teilnehmenden:

- einfache YAML-Strukturen lesen und schreiben,
- ein Ansible-Playbook strukturieren,
- Hosts und Tasks definieren,
- Module mit Parametern verwenden,
- Playbooks ausführen und deren Ausgabe interpretieren,
- `become` in Playbooks verwenden,
- `ok`, `changed` und `failed` unterscheiden,
- imperative Kommandos von deklarativer Zustandsbeschreibung unterscheiden,
- Idempotenz praktisch überprüfen.

## 3. YAML-Grundlagen

- Schlüssel/Wert
- Listen
- Mappings
- Einrückung
- Strings, Booleans, Zahlen
- typische Syntaxfehler

## 4. Aufbau eines Playbooks

- Play
- `hosts`
- `become`
- `tasks`
- Task-Name
- Modulname
- Modulparameter

## 5. Bekannte Module in Playbooks

- `copy`
- `file`
- `package`
- `service`

## 6. Ausführung

- `ansible-playbook`
- Inventory angeben
- Syntaxprüfung
- optional `--check` als Ausblick

## 7. Statusausgaben

- `ok`
- `changed`
- `failed`
- Zusammenfassung im Recap

## 8. Idempotenz

Ein Playbook wird mehrfach ausgeführt. Beim zweiten Lauf sollte ein bereits erreichter Zustand keine unnötige Änderung erzeugen.

## 9. Command vs. zustandsorientiertes Modul

Der Trainer zeigt denselben fachlichen Zweck einmal über `command` und einmal über ein passendes Modul und diskutiert die Unterschiede.

## 10. Abschlussübung

Ein Playbook richtet einen einfachen Dienst ein, legt ein Verzeichnis und eine Datei an und stellt sicher, dass der Dienst läuft.

## 11. Überleitung zu Block 8

Die Playbooks funktionieren, enthalten aber noch feste Werte. Block 8 parametrisiert sie mit Inventories, Variablen und Facts.
