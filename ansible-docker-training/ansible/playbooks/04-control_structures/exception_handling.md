# Fehlerbehandlung bei Tasks

Ein Task kann bei seiner Ausführung fehlschlagen. Standardmäßig behandelt Ansible einen solchen Fehler als Abbruch für den betroffenen Host.

In unserem Beispiel wird absichtlich ein nicht existierendes Kommando ausgeführt:

```yaml
- name: Nicht existierendes Kommando ausführen
  ansible.builtin.shell:
    cmd: non_existent
```

Da die Shell das Kommando `non_existent` nicht finden kann, schlägt der Task fehl.

## Fehler ignorieren mit `ignore_errors`

Soll Ansible trotz eines fehlgeschlagenen Tasks mit den folgenden Tasks fortfahren, kann

```yaml
ignore_errors: true
```

verwendet werden:

```yaml
- name: Nicht existierendes Kommando ausführen
  ansible.builtin.shell:
    cmd: non_existent
  register: command_result
  ignore_errors: true
```

Der Fehler verschwindet dadurch nicht. Der Task wird weiterhin als fehlgeschlagen erkannt und der Fehler wird von Ansible angezeigt.

`ignore_errors: true` bedeutet lediglich:

> Trotz dieses Fehlers soll die Verarbeitung mit den folgenden Tasks fortgesetzt werden.

Dadurch können wir den Fehler anschließend selbst auswerten.

## Das Ergebnis mit `register` speichern

Mit

```yaml
register: command_result
```

wird das Ergebnis des Tasks in der Variablen `command_result` gespeichert.

Diese Variable enthält verschiedene Informationen über die Ausführung, unter anderem:

```text
command_result.stdout
command_result.stderr
command_result.rc
```

`stdout` enthält die normale Ausgabe des Kommandos.

`stderr` enthält die Fehlerausgabe.

`rc` steht für **Return Code** und enthält den Exit Code des ausgeführten Kommandos.

## Der Return Code `rc`

Shell-Kommandos liefern beim Beenden einen Exit Code zurück.

Üblicherweise bedeutet:

```text
rc = 0     Kommando wurde erfolgreich ausgeführt
rc != 0    Kommando ist fehlgeschlagen
```

Ansible stellt diesen Wert über

```text
command_result.rc
```

zur Verfügung.

Damit können Bedingungen formuliert werden.

Bei erfolgreicher Ausführung:

```yaml
- name: Erfolgsmeldung ausgeben
  ansible.builtin.debug:
    msg: "command non_existent executed successfully"
  when: command_result.rc == 0
```

Bei fehlgeschlagener Ausführung:

```yaml
- name: Fehlermeldung ausgeben
  ansible.builtin.debug:
    msg: "command non_existent failed, cause is {{ command_result.stderr }}"
  when: command_result.rc != 0
```

Damit ergibt sich folgender Ablauf:

```text
Shell-Kommando
      │
      ▼
 command_result
      │
      ├── stdout   normale Ausgabe
      ├── stderr   Fehlerausgabe
      └── rc       Return Code
                    │
                    ├── 0    → erfolgreich
                    └── != 0 → fehlgeschlagen
```

Durch `ignore_errors: true` kann Ansible nach einem Fehler weiterarbeiten. Mit `command_result.rc` kann anschließend entschieden werden, welche weiteren Tasks ausgeführt werden sollen.

## Werte in Text einsetzen: `{{ ... }}`

In der Fehlermeldung verwenden wir:

```yaml
msg: "command non_existent failed, cause is {{ command_result.stderr }}"
```

Die Schreibweise

```text
{{ command_result.stderr }}
```

bedeutet: An dieser Stelle soll Ansible den Wert von `command_result.stderr` einsetzen.

Das Prinzip kennen wir bereits aus Python. Dort kann mit einem f-String ein Wert in einen Text eingesetzt werden:

```python
cause = "command not found"

print(f"command non_existent failed, cause is {cause}")
```

In einem Ansible-Playbook sieht das vergleichbare Prinzip so aus:

```yaml
msg: "command non_existent failed, cause is {{ command_result.stderr }}"
```

Vereinfacht gegenübergestellt:

```text
Python                         Ansible

f"... {cause} ..."             "... {{ command_result.stderr }} ..."
       │                                   │
       ▼                                   ▼
 Wert einsetzen                        Wert einsetzen
```

Die Schreibweise `{{ ... }}` stammt aus der von Ansible verwendeten Template-Sprache **Jinja**.

Für den Moment reicht es, sich zu merken:

> Mit `{{ ... }}` können Werte in einen Text oder an eine andere Stelle im Playbook eingesetzt werden.

