# Deklarative Module und `state`

Ansible wird häufig deklarativ verwendet:

> Im Playbook wird beschrieben, welcher Zustand auf dem Managed Node erreicht werden soll.

Ein typisches Beispiel ist das Modul `ansible.builtin.file`:

```yaml
ansible.builtin.file:
  path: /tmp/demo
  state: directory
```

Hier wird nicht beschrieben, **wie** das Verzeichnis erzeugt werden soll. Es wird lediglich festgelegt, dass es existieren soll.

## `state` ist kein allgemeiner Ansible-Parameter

Der Parameter `state` gehört nicht automatisch zu jedem Modul.

Er wird von verschiedenen Modulen angeboten, wenn sich damit ein gewünschter Zustand sinnvoll beschreiben lässt.

Beispiele sind:

```text
ansible.builtin.file
ansible.builtin.package
ansible.builtin.apt
ansible.builtin.dnf
ansible.builtin.service
ansible.builtin.user
```

Je nach Modul kann `state` unterschiedliche Werte besitzen.

Beispielsweise:

```yaml
ansible.builtin.package:
  name: nginx
  state: present
```

oder:

```yaml
ansible.builtin.service:
  name: nginx
  state: started
```

## Deklarativ bedeutet nicht automatisch `state`

Ein Modul kann auch deklarativ und idempotent arbeiten, ohne einen Parameter namens `state` zu besitzen.

Beispielsweise:

```yaml
ansible.builtin.copy:
  src: config.txt
  dest: /tmp/config.txt
```

Ansible prüft, ob die Zieldatei bereits dem gewünschten Inhalt entspricht. Nur wenn eine Änderung notwendig ist, wird die Datei kopiert.

Das Gleiche gilt beispielsweise für:

```text
ansible.builtin.template
```

## Imperative Module

Andere Module führen in erster Linie eine Aktion aus.

Typische Beispiele sind:

```text
ansible.builtin.command
ansible.builtin.shell
ansible.builtin.raw
```

Bei

```yaml
ansible.builtin.command:
  cmd: mkdir /tmp/demo
```

wird Ansible angewiesen, das Kommando `mkdir` auszuführen.

Das Modul weiß dabei nicht, dass das eigentliche Ziel lautet:

```text
Das Verzeichnis /tmp/demo soll existieren.
```

Diese Information wird erst mit einem deklarativen Modul wie `ansible.builtin.file` ausgedrückt.

## Idempotenz

Ein deklaratives Modul kann prüfen, ob der gewünschte Zustand bereits erreicht ist.

Ist beispielsweise ein Paket bereits in der gewünschten Version installiert, muss Ansible nichts ändern.

Dadurch können Playbooks wiederholt ausgeführt werden, ohne bei jedem Lauf unnötig Änderungen vorzunehmen.

Das wird als **Idempotenz** bezeichnet.

Wichtig ist daher:

> Deklarativ bedeutet nicht „verwendet `state`“.

`state` ist lediglich ein häufig verwendeter Modulparameter. Entscheidend ist, dass das Playbook den gewünschten Zustand beschreibt und das Modul prüfen kann, ob dieser Zustand bereits erreicht ist.
