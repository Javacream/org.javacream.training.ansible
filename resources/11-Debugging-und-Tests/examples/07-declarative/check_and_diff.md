# Check Mode und Diff Mode

Deklarative Playbooks beschreiben einen gewünschten Zustand. Ansible kann deshalb bei vielen Modulen bereits vor der eigentlichen Änderung prüfen, was verändert werden müsste.

## Check Mode

Mit

```bash
ansible-playbook declarative_modules.yml --check
```

wird ein Playbook probeweise ausgeführt.

Ansible versucht dabei zu ermitteln, welche Änderungen notwendig wären, ohne diese tatsächlich durchzuführen.

Der Check Mode ist besonders nützlich, wenn ein Playbook vor der produktiven Ausführung überprüft werden soll.

Nicht jedes Modul unterstützt den Check Mode vollständig. Module wie `command` oder `shell` können beispielsweise oft nicht zuverlässig vorhersagen, welche Auswirkungen ein Kommando hätte.

## Diff Mode

Mit

```bash
ansible-playbook declarative_modules.yml --diff
```

kann Ansible bei geeigneten Modulen Unterschiede zwischen aktuellem und gewünschtem Zustand anzeigen.

Besonders anschaulich ist das bei Dateien und Templates.

Beide Optionen können kombiniert werden:

```bash
ansible-playbook declarative_modules.yml --check --diff
```

Damit kann vor einer Änderung geprüft werden, **ob** Ansible etwas ändern würde und **was** sich dabei ändern würde.
