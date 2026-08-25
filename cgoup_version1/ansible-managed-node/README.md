# Ansible Managed Node

Dies ist bewusst eine minimale erste Managed Node.

Sie verwendet noch kein systemd und keine besondere cgroup-Konfiguration.
Zunächst testen wir ausschließlich Docker-Netzwerk, SSH, Python und Ansible.

## Voraussetzung

Die Control Node muss bereits laufen. Sie erzeugt das Docker-Netzwerk:

```text
ansible-training
```

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
docker compose -f docker-compose-node.yml ps
```

## SSH vom Host testen

Der SSH-Port wird zu Testzwecken als Port 2222 veröffentlicht:

```bash
ssh ansible@localhost -p 2222
```

Passwort:

```text
ansible
```

## SSH von der Control Node testen

Control Node öffnen:

```bash
docker compose -f docker-compose-control.yml exec control bash
```

Dort:

```bash
ssh ansible@node1
```

Passwort:

```text
ansible
```

## Ansible testen

Auf der Control Node:

```bash
ansible node1 \
  -i 'node1,' \
  -u ansible \
  -k \
  -m ping
```

Für `-k` benötigt die Control Node `sshpass`. Falls das aktuelle Control-Image
noch kein `sshpass` enthält, kann zunächst der normale SSH-Test verwendet oder
das Control-Image um `sshpass` ergänzt werden.

## become testen

```bash
ansible node1 \
  -i 'node1,' \
  -u ansible \
  -k \
  -b \
  -m command \
  -a 'id'
```

Der Benutzer `ansible` besitzt für die Trainingsumgebung passwortlose
sudo-Rechte.

## Wichtig

Diese erste Managed Node enthält absichtlich:

- kein systemd als PID 1
- kein `privileged: true`
- keinen cgroup-Mount
- keine cgroup-Namespace-Konfiguration

Damit können wir zunächst sicherstellen, dass die grundlegende Kommunikation
zwischen Control Node und Managed Node funktioniert. systemd bauen wir danach
als separaten Schritt ein.
