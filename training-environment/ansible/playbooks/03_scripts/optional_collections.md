# Vom Python-Skript zum Ansible-Modul

Unser Python-Skript `simple_pong.py` ist sehr einfach:

```python
#!/usr/bin/env python3

print("pong")
```

Ansible kopiert dieses Skript auf den Managed Node, führt es dort aus und liest die Ausgabe wieder ein.

Damit haben wir bereits einen wichtigen Grundgedanken eines Ansible-Moduls kennengelernt:

> Ein Ansible-Modul ist letztlich ein Programm, das von Ansible aufgerufen wird und ein Ergebnis an Ansible zurückliefert.

## Unser Skript und das ping-Modul

Unser Skript liefert:

```text
pong
```

Auch das bereits verwendete Modul

```yaml
ansible.builtin.ping:
```

liefert als Ergebnis ein `pong`.

Das echte `ping`-Modul ist natürlich etwas mehr als unser `simple_pong.py`. Es verwendet die von Ansible bereitgestellte Python-Infrastruktur und liefert sein Ergebnis in einer für Ansible definierten Form zurück.

Sehr stark vereinfacht kann man sich den entscheidenden Teil ungefähr so vorstellen:

```python
from ansible.module_utils.basic import AnsibleModule

module = AnsibleModule(
    argument_spec={}
)

module.exit_json(
    changed=False,
    ping="pong"
)
```

`exit_json()` beendet das Modul erfolgreich und gibt strukturierte Ergebnisdaten an Ansible zurück.

Deshalb sieht das Ergebnis des `ping`-Moduls beispielsweise so aus:

```text
"changed": false,
"ping": "pong"
```

Unser eigenes Skript schreibt dagegen lediglich Text nach `stdout`:

```python
print("pong")
```

Das Ansible-Modul verwendet bereits die Ansible-Infrastruktur, um ein strukturiertes Ergebnis zurückzugeben.

## Woher kommt `ansible.builtin.ping`?

Der vollständige Name

```text
ansible.builtin.ping
```

besteht aus mehreren Teilen:

```text
ansible . builtin . ping
   │        │        │
Namespace Collection Modul
```

`ansible.builtin` ist eine **Collection**.

Collections sind eine Möglichkeit, zusammengehörige Ansible-Inhalte zu organisieren. Sie können unter anderem Module enthalten.

Eine Collection kann beispielsweise folgende Struktur besitzen:

```text
Collection
│
├── plugins/
│   └── modules/
│       ├── ping.py
│       ├── command.py
│       └── ...
│
├── roles/
├── playbooks/
└── ...
```

Das Python-Programm hinter einem Modul liegt innerhalb einer Collection typischerweise im Bereich `plugins/modules`.

Für den Moment reicht daher folgende Vorstellung:

```text
Python-Skript
     │
     ▼
Ansible-Modul
     │
     ▼
Collection
```

Unser `simple_pong.py` zeigt bereits den grundlegenden Mechanismus. Ein richtiges Ansible-Modul ergänzt diesen um eine definierte Schnittstelle für Parameter und strukturierte Rückgabewerte.
