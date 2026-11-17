# Python auf dem Ansible Controller

Das Beispiel `ansible-caller.py` führt Ansible aus einem Python-Programm auf dem Controller aus.

Auf der Control Node im Verzeichnis `/training`:

```bash
python3 src/control/ansible-caller.py
```

Die Ansible-Konfiguration befindet sich in `/training/ansible.cfg`; das Inventory ist dort als `inventory.ini` eingetragen.
