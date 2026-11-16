# Trainerleitfaden – Block 11: Fehlerbehandlung, Debugging und Tests

## 1. Zielsetzung

Block 11 vermittelt einen systematischen Umgang mit fehlerhaften oder unerwarteten Ansible-Runs. Die Teilnehmenden lernen, Ausgaben zu interpretieren, Variablen sichtbar zu machen, Fehlerbedingungen gezielt zu formulieren und Idempotenz zu prüfen.

## 2. Lernziele

Die Teilnehmenden können:

- Verbindungs- und Taskfehler unterscheiden,
- Verbosity gezielt erhöhen,
- `debug` zum Untersuchen von Variablen und Facts verwenden,
- `ignore_errors` einordnen und vorsichtig einsetzen,
- eigene Fehlerbedingungen mit `failed_when` formulieren,
- Idempotenz durch wiederholte Runs prüfen,
- einfache Testszenarien für Playbooks entwickeln.

## 3. Fehlerklassen

- `UNREACHABLE`
- `FAILED`
- Syntaxfehler
- Variablenfehler
- Berechtigungsfehler
- Modulfehler

## 4. Verbosity

- `-v`, `-vv`, `-vvv`
- nur bei Bedarf erhöhen
- sensible Daten beachten

## 5. `debug`

- feste Meldung
- Variable
- zusammengesetzte Diagnoseausgabe

## 6. `ignore_errors`

Nur für bewusst tolerierte Fehler. Nicht als generelle Methode zum „Grünmachen“ eines Playbooks.

## 7. `failed_when`

Eigene fachliche Fehlerbedingungen auf Rückgabewerte oder Ausgaben anwenden.

## 8. Register als notwendige Ergänzung

Für `failed_when` und Debugging wird das Ergebnis eines Tasks häufig mit `register` gespeichert.

## 9. Idempotenz testen

- Playbook mehrfach ausführen
- `changed=0` als typisches Ziel bei unverändertem System
- Ausnahmen begründen

## 10. Grundlegende Teststrategien

- Syntaxcheck
- begrenzte Testgruppe
- Check Mode soweit geeignet
- wiederholter Run
- erwartete Zielzustände kontrollieren

## 11. Abschlussübung

Ein absichtlich fehlerhaftes Playbook wird analysiert, korrigiert und anschließend auf Idempotenz geprüft.

## 12. Überleitung zu Block 12

Im letzten Block werden Linux, Shell, Python und Ansible in einem gemeinsamen Praxisprojekt zusammengeführt.
