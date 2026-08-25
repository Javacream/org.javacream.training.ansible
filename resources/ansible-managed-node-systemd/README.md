# Ansible Managed Node mit systemd

Diese Umgebung enthält genau **einen** realistischeren Ansible Managed Node.

## Eigenschaften

- Ubuntu 24.04
- `systemd` als PID 1
- OpenSSH Server
- Python 3
- Benutzer `ansible`
- Passwort: `ansible`
- passwortloses `sudo`
- Docker-Netzwerk `ansible-training`
- SSH zusätzlich vom Host über Port `2222` erreichbar

Diese Variante ist für einen Docker-Host mit

```text
Cgroup Version: 1
Driver: cgroupfs
```

gedacht.

## Voraussetzung

Die Control Node sollte bereits laufen und das externe Docker-Netzwerk

```text
ansible-training
```

angelegt haben.

Prüfen:

```bash
docker network inspect ansible-training
```

## Managed Node starten

```bash
docker compose -f docker-compose-node.yml up -d --build
```

## Status prüfen

```bash
docker compose -f docker-compose-node.yml ps -a
```

## Prüfen, ob systemd PID 1 ist

```bash
docker compose -f docker-compose-node.yml exec node1 \
  ps -p 1 -o pid,comm,args
```

Erwartet:

```text
PID COMMAND         COMMAND
  1 systemd         /sbin/init
```

## systemd prüfen

```bash
docker compose -f docker-compose-node.yml exec node1 \
  systemctl is-system-running
```

In einem Container kann der Zustand `degraded` sein. Entscheidend ist,
dass die für das Training relevanten Services über systemd verwaltet werden können.

SSH prüfen:

```bash
docker compose -f docker-compose-node.yml exec node1 \
  systemctl status ssh --no-pager
```

## SSH vom Host

```bash
ssh ansible@localhost -p 2222
```

Passwort:

```text
ansible
```

## SSH von der Control Node

```bash
ssh ansible@node1
```

Passwort:

```text
ansible
```

## Ansible-Test

Auf der Control Node:

```bash
ansible node1 \
  -i 'node1,' \
  -u ansible \
  -k \
  -m ping
```

Falls Host-Key-Checking für die Docker-Laborumgebung abgeschaltet werden soll:

```bash
ANSIBLE_HOST_KEY_CHECKING=False \
ansible node1 -i 'node1,' -u ansible -k -m ping
```

## become testen

```bash
ANSIBLE_HOST_KEY_CHECKING=False \
ansible node1 \
  -i 'node1,' \
  -u ansible \
  -k \
  -b \
  -m command \
  -a 'id'
```

Erwartet wird u.a.:

```text
uid=0(root)
```

## Service-Management testen

Zum Beispiel Cron installieren:

```bash
ANSIBLE_HOST_KEY_CHECKING=False \
ansible node1 \
  -i 'node1,' \
  -u ansible \
  -k \
  -b \
  -m ansible.builtin.apt \
  -a 'name=cron state=present update_cache=true'
```

Danach:

```bash
ANSIBLE_HOST_KEY_CHECKING=False \
ansible node1 \
  -i 'node1,' \
  -u ansible \
  -k \
  -b \
  -m ansible.builtin.systemd_service \
  -a 'name=cron state=started enabled=true'
```

## Warum privileged?

`systemd` als vollständiges Init-System benötigt in einem Docker-Container
Zugriffe, die ein normaler Container nicht besitzt. Diese Einstellung ist
für eine lokale Trainingsumgebung gedacht und kein Produktionsmuster.

## Warum /sys/fs/cgroup read-only?

Der Docker-Host verwendet cgroup v1. Der Container benötigt Einblick in die
cgroup-Hierarchie, soll sie aber nicht verändern können:

```yaml
volumes:
  - /sys/fs/cgroup:/sys/fs/cgroup:ro
```

Bewusst **nicht** verwendet wird:

```yaml
/sys/fs/cgroup:/sys/fs/cgroup:rw
```

## Stoppen

```bash
docker compose -f docker-compose-node.yml down
```

## Diagnose, falls der Container beendet wird

```bash
docker compose -f docker-compose-node.yml ps -a
docker compose -f docker-compose-node.yml logs node1
```
