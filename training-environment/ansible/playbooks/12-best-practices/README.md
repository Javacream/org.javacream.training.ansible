# Abschluss des Lernpfads

Dieses Unterkapitel fasst Best Practices für die bisher behandelten Ansible-Konzepte zusammen.

Enthalten sind:

- `best-practices.md` – Empfehlungen für Aufbau und Betrieb von Ansible-Projekten
- `troubleshooting.yml` – kleines Beispiel für `assert`, Facts und Debugging

Nützliche Prüfkommandos:

```bash
ansible-playbook troubleshooting.yml --syntax-check
ansible-playbook troubleshooting.yml --check
ansible-playbook troubleshooting.yml -v
ansible-lint troubleshooting.yml
```
