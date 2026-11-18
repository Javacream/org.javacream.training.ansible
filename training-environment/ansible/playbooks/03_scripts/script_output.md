# Ausgaben von Skripten: stdout und stderr

Ein Skript, das Ansible auf einem Managed Node ausführt, kann Ausgaben erzeugen.

Dabei sind insbesondere zwei Ausgabekanäle wichtig:

- `stdout` – Standardausgabe
- `stderr` – Standardfehlerausgabe

## Standardausgabe mit `print`

Unser Python-Skript enthält:

```python
#!/usr/bin/env python3

print("pong")
```

`print("pong")` schreibt den Text `pong` auf die Standardausgabe des Python-Prozesses.

Diese Standardausgabe wird als `stdout` bezeichnet.

Ansible führt das Skript auf dem Managed Node aus und erfasst dessen Standardausgabe.

```text
Python-Skript
     │
     │ print("pong")
     ▼
   stdout
     │
     ▼
   Ansible
```

## Warum nicht `return "pong"`?

`return` hat in Python eine andere Bedeutung.

Ein `return` gibt einen Wert aus einer Funktion an deren Aufrufer zurück:

```python
def ping():
    return "pong"
```

Dieser Wert wird jedoch nicht automatisch auf die Standardausgabe geschrieben.

Außerdem kann `return` nicht einfach auf der obersten Ebene eines Python-Skripts verwendet werden.

Wenn Ansible die Ausgabe eines Skripts erfassen soll, muss das Skript daher etwas auf einen Ausgabekanal schreiben.

Für die normale Ausgabe verwenden wir:

```python
print("pong")
```

## Ausgabe mit `register` speichern

Im Playbook wird das Python-Skript mit dem `command`-Modul ausgeführt:

```yaml
- name: Python-Skript ausführen
  ansible.builtin.command:
    cmd: /tmp/simple_pong.py
  register: script_result
```

Mit `register` speichert Ansible das Ergebnis des Tasks in der Variablen `script_result`.

Die Standardausgabe des ausgeführten Programms befindet sich anschließend in:

```text
script_result.stdout
```

Sie kann mit `debug` angezeigt werden:

```yaml
- name: Ausgabe des Python-Skripts anzeigen
  ansible.builtin.debug:
    var: script_result.stdout
```

Auf der Control Node erscheint damit die Ausgabe des Python-Skripts:

```text
"script_result.stdout": "pong"
```

## Standardfehlerausgabe: stderr

Neben `stdout` besitzt ein Prozess eine Standardfehlerausgabe.

Diese wird als `stderr` bezeichnet.

Programme können darüber Fehlermeldungen oder Diagnoseinformationen ausgeben.

Ansible erfasst auch diesen Ausgabekanal. Er steht im registrierten Task-Ergebnis unter:

```text
script_result.stderr
```

Die Fehlerausgabe kann ebenfalls mit `debug` angezeigt werden:

```yaml
- name: Fehlerausgabe anzeigen
  ansible.builtin.debug:
    var: script_result.stderr
```

Damit stehen bei einem mit `register` gespeicherten Task beide wichtigen Ausgabekanäle zur Verfügung:

```text
Skript auf dem Managed Node
        │
        ├── stdout ──► script_result.stdout
        │
        └── stderr ──► script_result.stderr
```

`stdout` enthält die normale Programmausgabe, während `stderr` für Fehler- und Diagnoseausgaben vorgesehen ist.
