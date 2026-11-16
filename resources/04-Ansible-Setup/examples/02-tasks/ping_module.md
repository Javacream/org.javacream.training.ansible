# Das Modul `ansible.builtin.ping`

Das Modul `ansible.builtin.ping` dient dazu, die Ansible-Verbindung zu einem Managed Node zu testen.

Dabei handelt es sich **nicht um einen ICMP-Ping** wie beim Betriebssystemkommando `ping`. Das Modul prüft vielmehr, ob Ansible den Managed Node erreichen, sich dort anmelden und eine verwendbare Python-Umgebung nutzen kann.

Bei erfolgreicher Ausführung liefert das Modul standardmäßig den Wert:

```text
pong
```

## Verwendung ohne Parameter

```yaml
- name: Verbindung testen
  ansible.builtin.ping:
```

Für den normalen Verbindungstest müssen keine Parameter angegeben werden.

## Parameter `data`

Das Modul besitzt den Parameter `data`.

Mit `data` kann festgelegt werden, welcher Wert anstelle des standardmäßigen `pong` zurückgegeben werden soll.

Beispiel:

```yaml
- name: Verbindung mit eigener Antwort testen
  ansible.builtin.ping:
    data: hallo
```

Die Antwort enthält dann:

```text
"ping": "hallo"
```

Der Standardwert von `data` ist:

```text
pong
```

Wird als Wert von `data` der besondere Wert `crash` angegeben, erzeugt das Modul absichtlich eine Exception. Dies kann beispielsweise zum Testen des Fehlerverhaltens verwendet werden:

```yaml
- name: Fehler provozieren
  ansible.builtin.ping:
    data: crash
```

## Parameterübersicht

| Parameter | Typ | Standard | Bedeutung |
| --- | --- | --- | --- |
| `data` | String | `pong` | Legt den zurückgegebenen Wert fest. Der besondere Wert `crash` löst eine Exception aus. |

`data` ist der einzige modulspezifische Parameter von `ansible.builtin.ping`.

## Dokumentation auf dem Control Node

Die Dokumentation eines installierten Ansible-Moduls kann auch direkt auf der Kommandozeile angezeigt werden:

```bash
ansible-doc ansible.builtin.ping
```

## Offizielle Dokumentation

Die vollständige und aktuelle Beschreibung des Moduls befindet sich in der offiziellen Ansible-Dokumentation:

https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/ping_module.html
