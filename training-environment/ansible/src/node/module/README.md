# Eigenes Ansible-Modul: node_executor

Das Modul `node_executor.py` ermittelt Hostname und Prozess-ID des Managed Nodes, wartet 30 Sekunden und gibt die Werte strukturiert an Ansible zurück. Anders als beim `script`-Modul nutzt es dafür `AnsibleModule` und `exit_json()`.

## Modul installieren

Auf dem **Ansible Controller** im Verzeichnis `/training`:

```bash
mkdir -p library
cp src/node/module/node_executor.py library/
```

Ansible findet eigene Module im Verzeichnis `library`, wenn dieses über die Konfiguration eingebunden ist. Dazu in `ansible.cfg` unter `[defaults]` ergänzen:

```ini
library = ./library
```

Alternativ lässt sich das Modul **ohne Installation** direkt mit `-M` laden:

```bash
ansible web1 -M src/node/module -m node_executor
```

## Modul ausführen

Nach dem Kopieren und Konfigurieren:

```bash
ansible web1 -m node_executor
```

Ansible überträgt den Modulcode auf `web1`, führt ihn dort mit Python aus und liefert `hostname`, `pid` und `message` zurück.

## Übertragung beobachten

```bash
ANSIBLE_KEEP_REMOTE_FILES=1 ansible web1 -m node_executor -vvv
```

Während der 30 Sekunden auf dem Managed Node:

```bash
ps -ef | grep '[A]nsiballZ'
find ~/.ansible/tmp -name 'AnsiballZ_node_executor.py'
```

Die temporäre Datei `AnsiballZ_node_executor.py` enthält einen von Ansible erzeugten Wrapper mit dem Modulcode. `ANSIBLE_KEEP_REMOTE_FILES=1` verhindert bei diesem Python-Modul normalerweise das anschließende Löschen. Die genauen Pfade stehen in der `-vvv`-Ausgabe.
