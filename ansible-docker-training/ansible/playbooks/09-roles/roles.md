# Roles und Wiederverwendung

Mit zunehmender Größe werden Playbooks unübersichtlich. Roles teilen zusammengehörende Inhalte in eine feste Verzeichnisstruktur auf.

Eine typische Role besitzt beispielsweise:

```text
roles/
└── webserver/
    ├── defaults/
    ├── handlers/
    ├── tasks/
    └── templates/
```

Die zentralen Tasks einer Role stehen in:

```text
roles/webserver/tasks/main.yml
```

Ein Play kann die Role anschließend verwenden:

```yaml
roles:
  - webserver
```

## Defaults

Standardwerte einer Role können in

```text
defaults/main.yml
```

definiert werden.

Diese Werte können später durch andere Variablen überschrieben werden.

## Handler und Templates

Auch Handler und Templates können Bestandteil einer Role sein. Dadurch bleibt die komplette Konfiguration einer fachlichen Aufgabe zusammen.

## Tasks einbinden

Kleinere Playbooks können auch ohne Role aufgeteilt werden.

Mit

```yaml
ansible.builtin.include_tasks: tasks/system_info.yml
```

werden zusätzliche Tasks während der Ausführung eingebunden.

Für größere, wiederverwendbare Einheiten sind Roles meist die übersichtlichere Struktur.
