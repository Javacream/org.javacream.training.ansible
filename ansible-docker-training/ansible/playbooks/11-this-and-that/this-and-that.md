# Weitere Ansible-Konzepte

Der bisherige Lernpfad behandelt die wichtigsten Grundlagen für die praktische Arbeit mit Ansible. Darüber hinaus gibt es weitere Konzepte, die je nach Einsatzgebiet wichtig werden können.

Dieses Kapitel dient als Überblick. Die Themen werden bewusst nur kurz angerissen.

## `delegate_to`

Normalerweise wird ein Task auf dem Host ausgeführt, der durch `hosts` ausgewählt wurde.

Mit `delegate_to` kann ein einzelner Task stattdessen auf einem anderen Host ausgeführt werden:

```yaml
- name: Aktion auf dem Control Node ausführen
  ansible.builtin.debug:
    msg: "Dieser Task läuft auf dem Control Node"
  delegate_to: localhost
```

Das ist beispielsweise nützlich, wenn während einer Konfiguration zusätzlich eine Aktion auf einem zentralen System ausgeführt werden soll.

## `run_once`

Ein Play kann viele Hosts betreffen. Manche Tasks sollen trotzdem nur einmal ausgeführt werden.

Dafür gibt es:

```yaml
run_once: true
```

Typische Anwendungsfälle sind einmalige Initialisierungen oder zentrale Aktionen.

## `serial`

Normalerweise bearbeitet Ansible mehrere Hosts eines Plays parallel.

Mit `serial` kann festgelegt werden, wie viele Hosts gleichzeitig bearbeitet werden:

```yaml
- name: Server schrittweise aktualisieren
  hosts: webservers
  serial: 1
```

Damit können beispielsweise Webserver nacheinander aktualisiert werden.

Das ist eine Grundlage für Rolling Updates.

## `block`, `rescue` und `always`

Mehrere Tasks können mit `block` zusammengefasst werden.

Tritt innerhalb des Blocks ein Fehler auf, können mit `rescue` Fehlerbehandlungen definiert werden. Tasks unter `always` werden unabhängig vom Ergebnis ausgeführt.

Das Konzept ähnelt `try`, `except` und `finally` aus anderen Programmiersprachen.

## `failed_when`

Ansible entscheidet normalerweise anhand des Return Codes, ob ein Kommando erfolgreich war.

Mit `failed_when` kann diese Entscheidung angepasst werden:

```yaml
failed_when: command_result.rc > 1
```

Damit können auch programmspezifische Return Codes ausgewertet werden.

## `changed_when`

Bei `command` und `shell` kann Ansible häufig nicht erkennen, ob tatsächlich etwas verändert wurde.

Mit `changed_when` kann der Status selbst festgelegt werden:

```yaml
changed_when: false
```

Das kann insbesondere bei reinen Prüfkommandos sinnvoll sein.

## `assert`

Mit `ansible.builtin.assert` können Voraussetzungen geprüft werden:

```yaml
- name: Port prüfen
  ansible.builtin.assert:
    that:
      - application_port > 0
```

Ein Playbook kann damit frühzeitig abbrechen, wenn notwendige Bedingungen nicht erfüllt sind.

## `fail`

Mit `ansible.builtin.fail` kann ein Playbook gezielt mit einer eigenen Fehlermeldung beendet werden.

```yaml
- name: Ausführung abbrechen
  ansible.builtin.fail:
    msg: "Konfiguration ist ungültig"
```

## Magic Variables

Ansible stellt neben Facts weitere spezielle Variablen bereit.

Beispiele sind:

```text
inventory_hostname
groups
hostvars
playbook_dir
```

Damit kann unter anderem auf Inventory-Informationen oder Variablen anderer Hosts zugegriffen werden.

## Variable Precedence

Variablen können in Ansible an vielen Stellen definiert werden:

```text
Role Defaults
Inventory
group_vars
host_vars
Playbook
Role
Kommandozeile
```

Wenn dieselbe Variable mehrfach definiert ist, entscheidet die sogenannte **Variable Precedence**, welcher Wert verwendet wird.

Für komplexere Projekte sollte diese Rangfolge bekannt sein. In einfachen Playbooks ist es meist besser, Variablen möglichst eindeutig zu definieren.

## Weitere Plugins

Ansible kann über Plugins erweitert werden.

Dazu gehören beispielsweise:

- Callback-Plugins
- Lookup-Plugins
- Filter-Plugins
- Connection-Plugins
- Inventory-Plugins

Für die tägliche Arbeit mit einfachen Playbooks ist ein tieferes Verständnis dieser Plugin-Typen zunächst nicht notwendig.

## Event-Driven Ansible

Event-Driven Ansible ermöglicht es, auf externe Ereignisse zu reagieren und daraus automatisierte Aktionen abzuleiten.

Das geht über den klassischen Ablauf

```text
Playbook starten → Tasks ausführen → Playbook beenden
```

hinaus und bildet ein eigenes weiterführendes Themengebiet.

## Dynamic Inventory

Inventories müssen nicht ausschließlich statische Dateien sein.

Inventory-Plugins können Hosts beispielsweise dynamisch aus Cloud- oder Virtualisierungsumgebungen ermitteln.

Das ist insbesondere bei Infrastrukturen interessant, deren Systeme häufig erzeugt und entfernt werden.

## Eigene Module und Collections

Wenn vorhandene Module nicht ausreichen, können eigene Ansible-Module entwickelt werden.

Mehrere Module, Plugins und Roles können anschließend in einer eigenen Collection zusammengefasst und verteilt werden.

Für den Einstieg sollte jedoch möglichst auf vorhandene Module zurückgegriffen werden.
