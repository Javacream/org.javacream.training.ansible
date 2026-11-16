# Inventory, Gruppen und Variablen

Das Inventory beschreibt, auf welchen Managed Nodes Ansible arbeiten soll.

Ein einfaches Inventory kann Hosts zu Gruppen zusammenfassen:

```ini
[webservers]
web1
web2

[databases]
db1
```

Mit Gruppen können Plays gezielt auf mehrere Hosts angewendet werden:

```yaml
hosts: webservers
```

## Gruppen von Gruppen

Mit `:children` können Gruppen wiederum zu einer übergeordneten Gruppe zusammengefasst werden:

```ini
[linux:children]
webservers
databases
```

Damit kann ein Play beispielsweise auf alle Hosts der Gruppe `linux` angewendet werden.

## `group_vars`

Variablen, die für eine ganze Gruppe gelten, können in einem Verzeichnis `group_vars` abgelegt werden.

Beispiel:

```text
group_vars/
└── webservers.yml
```

```yaml
application_port: 8080
```

Diese Variable steht den Hosts der Gruppe `webservers` zur Verfügung.

## `host_vars`

Variablen für einen einzelnen Host können analog in `host_vars` abgelegt werden:

```text
host_vars/
└── web1.yml
```

```yaml
application_name: web-frontend-1
```

Damit lassen sich allgemeine Gruppenwerte mit hostspezifischen Einstellungen kombinieren.
