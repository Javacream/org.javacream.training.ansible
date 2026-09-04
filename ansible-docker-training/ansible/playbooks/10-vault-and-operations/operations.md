# Vault, Tags und operative Ausführung

## Tags

Tasks können mit Tags versehen werden:

```yaml
tags:
  - info
```

Dann lassen sich gezielt nur bestimmte Teile eines Playbooks ausführen:

```bash
ansible-playbook tags.yml --tags info
```

Oder bestimmte Tags können ausgeschlossen werden:

```bash
ansible-playbook tags.yml --skip-tags configure
```

## Ansible Vault

Passwörter und andere Secrets sollten nicht unverschlüsselt in Playbooks gespeichert werden.

Ansible Vault kann YAML-Dateien verschlüsseln.

Aus einer normalen Datei wie

```yaml
database_password: change_me
```

kann mit

```bash
ansible-vault encrypt secret_vars.yml
```

eine verschlüsselte Vault-Datei erzeugt werden.

Ein Playbook kann diese Datei wie eine normale Variablendatei einbinden:

```yaml
vars_files:
  - secret_vars.yml
```

Zur Ausführung kann Ansible nach dem Vault-Passwort fragen:

```bash
ansible-playbook vault_example.yml --ask-vault-pass
```

## Collections und Galaxy

Collections bündeln Module, Plugins, Roles und weitere Ansible-Inhalte.

Der bereits verwendete Modulname

```text
ansible.builtin.copy
```

besteht aus:

```text
Namespace.Collection.Modul
```

`ansible.builtin` gehört zur mit ansible-core ausgelieferten Builtin-Collection.

Zusätzliche Collections können beispielsweise mit

```bash
ansible-galaxy collection install <namespace>.<collection>
```

installiert werden.

Auch Roles können über Ansible Galaxy bereitgestellt und installiert werden.

## Check Mode und Diff Mode

Für operative Änderungen sind außerdem die bereits eingeführten Optionen hilfreich:

```bash
ansible-playbook playbook.yml --check
ansible-playbook playbook.yml --diff
```

Sie ermöglichen eine kontrolliertere Ausführung deklarativer Playbooks.
