# Python-Skript auf einem Managed Node ausführen

Das Modul `ansible.builtin.script` überträgt `node-executor.py` vom Controller auf den Managed Node `web1` und führt es dort mit Python aus+.

Auf der Control Node im Verzeichnis `/training`:

```bash
ansible web1 -m ansible.builtin.script -a "src/node/node-executor.py executable=/usr/bin/python3"
```

## Übertragung beobachten

```bash
ANSIBLE_KEEP_REMOTE_FILES=1 ansible web1 \
  -m ansible.builtin.script \
  -a "src/node/node-executor.py executable=/usr/bin/python3" -vvv
```

`-vvv` zeigt den SSH-Transfer und den temporären Dateipfad. Während der Ausführung kann man auf `web1` nach dem Prozess und der übertragenen Datei suchen:

```bash
ps -ef | grep '[p]ython'
find ~/.ansible/tmp -type f
```

**Hinweis:** `ANSIBLE_KEEP_REMOTE_FILES=1` garantiert beim `script`-Modul nicht, dass die temporäre Datei nach der Ausführung erhalten bleibt.
