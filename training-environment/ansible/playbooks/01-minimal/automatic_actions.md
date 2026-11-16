# Automatische Aktionen bei der Ausführung eines Playbooks

Auch ein minimales Playbook ohne selbst definierte Tasks erzeugt bei der Ausführung bereits mehrere Ausgaben.

Beispiel:

```yaml
---
- name: Minimales Play
  hosts: all
```

Bei der Ausführung mit

```bash
ansible-playbook minimal.yml
```

sind insbesondere zwei Bereiche interessant:

- `Gathering Facts`
- `PLAY RECAP`

## Gathering Facts

Zu Beginn eines Plays sammelt Ansible standardmäßig Informationen über die angesprochenen Managed Nodes.

In der Ausgabe erscheint deshalb beispielsweise:

```text
TASK [Gathering Facts] ************************************************
ok: [db1]
```

Für das Sammeln dieser Informationen verwendet Ansible das Modul `ansible.builtin.setup`.

Die ermittelten Informationen werden als **Facts** bezeichnet. Dazu gehören beispielsweise Angaben über das Betriebssystem, den Hostnamen, Netzwerkinterfaces oder die Prozessorarchitektur.

Das Gathering Facts geschieht automatisch, auch wenn im Playbook noch keine eigenen Tasks definiert wurden.

## PLAY RECAP

Am Ende der Ausführung zeigt Ansible eine Zusammenfassung an:

```text
PLAY RECAP ************************************************************
db1 : ok=1 changed=0 unreachable=0 failed=0 skipped=0 rescued=0 ignored=0
```

Der `PLAY RECAP` zeigt für jeden beteiligten Managed Node, was während der Ausführung des Playbooks passiert ist.

Die Angaben haben folgende Bedeutung:

| Angabe | Bedeutung |
| --- | --- |
| `ok` | Anzahl der erfolgreich ausgeführten Aktionen |
| `changed` | Anzahl der Aktionen, die auf dem Managed Node eine Änderung vorgenommen haben |
| `unreachable` | Anzahl der Aktionen, bei denen der Managed Node nicht erreichbar war |
| `failed` | Anzahl der fehlgeschlagenen Aktionen |
| `skipped` | Anzahl der übersprungenen Aktionen |
| `rescued` | Anzahl der fehlgeschlagenen Aktionen, deren Fehler durch einen `rescue`-Block behandelt wurde |
| `ignored` | Anzahl der fehlgeschlagenen Aktionen, deren Fehler ignoriert wurde |

Bei unserem minimalen Playbook kann beispielsweise

```text
ok=1 changed=0
```

erscheinen, obwohl wir selbst noch keinen Task definiert haben.

Der Grund ist das automatische `Gathering Facts`: Dieses wurde erfolgreich ausgeführt und wird deshalb bei `ok` mitgezählt. Da dabei lediglich Informationen über den Managed Node ermittelt und keine Konfiguration verändert wurde, bleibt `changed` auf `0`.

## Zwei automatische Bestandteile der Ausgabe

Bei unserem minimalen Playbook können wir damit bereits zwei Dinge beobachten, die wir nicht selbst als Tasks definiert haben:

1. **Gathering Facts** findet zu Beginn eines Plays statt und sammelt Informationen über die Managed Nodes.
2. **PLAY RECAP** wird am Ende ausgegeben und fasst das Ergebnis der Ausführung für jeden Managed Node zusammen.

Der `PLAY RECAP` führt selbst keine Aktion auf den Managed Nodes aus. Er ist eine von Ansible erzeugte Zusammenfassung der vorherigen Ausführung.
