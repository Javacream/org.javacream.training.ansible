# Ansible Control Node

Diese Umgebung enthält ausschließlich die Ansible-Control-Node.

## Start

```bash
docker compose -f docker-compose-control.yml up -d --build
```

## Shell öffnen

```bash
docker compose -f docker-compose-control.yml exec control bash
```

## Prüfen

```bash
ansible --version
ssh -V
```

## Verzeichnisse

- `./training` wird nach `/training` gemountet.
- `./ssh` wird nach `/home/ansible/.ssh` gemountet.

## Netzwerk

Die Control Node verwendet das benannte Docker-Netzwerk:

```text
ansible-training
```

Spätere Managed Nodes können in einer separaten Compose-Datei dasselbe Netzwerk verwenden.

## Stoppen

```bash
docker compose -f docker-compose-control.yml down
```
