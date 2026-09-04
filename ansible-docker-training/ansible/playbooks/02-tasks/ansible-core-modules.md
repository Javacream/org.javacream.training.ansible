# Module in ansible-core

`ansible-core` enthält eine Reihe von Modulen, die über die Collection `ansible.builtin` zur Verfügung stehen.

Module stellen die eigentlichen Funktionen bereit, die innerhalb von Tasks ausgeführt werden. Beispiele sind:

- `ansible.builtin.ping` – Verbindung zu einem Managed Node prüfen
- `ansible.builtin.command` – ein Kommando auf einem Managed Node ausführen
- `ansible.builtin.copy` – Dateien auf Managed Nodes kopieren
- `ansible.builtin.file` – Dateien und Verzeichnisse verwalten
- `ansible.builtin.package` – Pakete über den Paketmanager des Systems verwalten
- `ansible.builtin.service` – Dienste verwalten
- `ansible.builtin.user` – Benutzerkonten verwalten
- `ansible.builtin.setup` – Facts eines Managed Nodes ermitteln

Die verfügbaren Module und ihre Parameter sind in der offiziellen Ansible-Dokumentation beschrieben.

## Modulindex

Eine Übersicht über die in `ansible-core` enthaltenen Module bietet der offizielle Modulindex:

https://docs.ansible.com/projects/ansible-core/2.20/collections/index_module.html
