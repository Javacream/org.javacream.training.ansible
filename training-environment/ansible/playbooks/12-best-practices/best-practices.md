# Best Practices

Zum Abschluss werden einige Regeln zusammengefasst, die Ansible-Playbooks übersichtlicher, zuverlässiger und leichter wartbar machen.

## Deklarative Module bevorzugen

Wenn ein passendes Ansible-Modul existiert, sollte es gegenüber `command` oder `shell` bevorzugt werden.

Statt:

```yaml
ansible.builtin.command:
  cmd: mkdir -p /tmp/demo
```

besser:

```yaml
ansible.builtin.file:
  path: /tmp/demo
  state: directory
```

Ansible kann dadurch den aktuellen Zustand erkennen und nur notwendige Änderungen durchführen.

## Idempotenz beachten

Ein Playbook sollte möglichst mehrfach ausgeführt werden können, ohne bei jedem Lauf unnötige Änderungen zu verursachen.

Ein zweiter Lauf sollte deshalb häufig überwiegend

```text
ok
```

statt

```text
changed
```

melden.

## Fully Qualified Collection Names verwenden

Module sollten eindeutig benannt werden:

```yaml
ansible.builtin.copy:
```

statt nur:

```yaml
copy:
```

Dadurch ist unmittelbar erkennbar, aus welcher Collection ein Modul stammt.

## Aussagekräftige Namen verwenden

Plays und Tasks sollten beschreiben, was erreicht werden soll:

```yaml
- name: nginx installieren
```

ist besser als:

```yaml
- name: Paket
```

Gute Namen helfen sowohl beim Lesen des Playbooks als auch bei der Interpretation der Ansible-Ausgabe.

## Variablen statt Wiederholungen

Werte, die mehrfach verwendet oder je nach Umgebung geändert werden, sollten als Variablen definiert werden.

```yaml
webserver_port: 8080
```

Dadurch werden Playbooks leichter anpassbar.

## Secrets nicht im Klartext speichern

Passwörter, Tokens und andere geheime Werte gehören nicht direkt in Playbooks oder unverschlüsselte Variablendateien.

Dafür kann beispielsweise Ansible Vault verwendet werden.

## Roles für größere Aufgaben verwenden

Kleine Playbooks dürfen klein bleiben.

Wenn jedoch Tasks, Handler, Templates und Variablen zu einer gemeinsamen Aufgabe gehören, bietet sich eine Role an.

Damit wird aus einem großen Playbook eine strukturierte und wiederverwendbare Einheit.

## Handler für Folgeaktionen verwenden

Ein Dienst sollte nicht nach jedem Lauf unnötig neu gestartet werden.

Stattdessen sollte eine Konfigurationsänderung über `notify` einen Handler auslösen.

So erfolgt der Neustart nur, wenn tatsächlich eine Änderung stattgefunden hat.

## Änderungen vorab prüfen

Vor wichtigen Änderungen können Check Mode und Diff Mode helfen:

```bash
ansible-playbook site.yml --check --diff
```

Die Ausgabe sollte trotzdem kritisch geprüft werden, da nicht jedes Modul den Check Mode vollständig unterstützt.

## Versionskontrolle verwenden

Playbooks, Roles, Templates und Inventory-Strukturen sollten in einem Versionskontrollsystem wie Git verwaltet werden.

Damit sind Änderungen nachvollziehbar und können gemeinsam entwickelt und geprüft werden.

Secrets gehören dabei nicht unverschlüsselt in das Repository.

## Kleine, nachvollziehbare Änderungen bevorzugen

Playbooks sollten schrittweise entwickelt werden.

Nach einer Änderung kann zunächst die Syntax geprüft werden:

```bash
ansible-playbook site.yml --syntax-check
```

Anschließend kann das Playbook gegen eine Testumgebung ausgeführt werden.

## Ausgaben zur Fehlersuche erhöhen

Für die Fehlersuche kann die Ausführlichkeit der Ausgabe erhöht werden:

```bash
ansible-playbook site.yml -v
```

Weitere Stufen sind beispielsweise:

```bash
ansible-playbook site.yml -vv
ansible-playbook site.yml -vvv
```

Je mehr `v` angegeben werden, desto detaillierter wird die Ausgabe.

## Voraussetzungen explizit prüfen

Mit `ansible.builtin.assert` können Annahmen eines Playbooks geprüft werden.

Dadurch entsteht eine verständliche Fehlermeldung möglichst früh, statt dass ein späterer Task aus einem schwer erkennbaren Grund fehlschlägt.

## ansible-lint

`ansible-lint` untersucht Ansible-Inhalte auf typische Probleme und Verstöße gegen empfohlene Konventionen.

Ein Playbook kann beispielsweise geprüft werden mit:

```bash
ansible-lint site.yml
```

Der Linter ersetzt keine Tests, hilft aber dabei, problematische Muster frühzeitig zu erkennen.

## Dokumentation verwenden

Bei Unsicherheit über Parameter und Verhalten eines Moduls sollte die Moduldokumentation verwendet werden.

Direkt auf der Kommandozeile:

```bash
ansible-doc ansible.builtin.file
```

oder für ein anderes Modul:

```bash
ansible-doc ansible.builtin.template
```

Gerade bei `state`, Check-Mode-Unterstützung und modulspezifischen Parametern ist die Dokumentation die maßgebliche Referenz.

## Zusammenfassung

Ein gutes Ansible-Projekt versucht insbesondere:

```text
deklarativ statt imperativ
idempotent statt wiederholter unnötiger Änderungen
Module statt Shell-Kommandos
Variablen statt duplizierter Werte
Handler statt unnötiger Neustarts
Roles statt großer unstrukturierter Playbooks
Vault statt Secrets im Klartext
Check und Diff vor kritischen Änderungen
Versionskontrolle für Nachvollziehbarkeit
Linting und Tests für Qualität
```
