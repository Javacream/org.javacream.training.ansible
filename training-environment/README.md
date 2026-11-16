# Ansible-Trainingsumgebung mit Docker und systemd

Diese Umgebung simuliert mehrere Linux-Server als Docker-Container. Die Managed Nodes
laufen mit `systemd` als PID 1 und sind per SSH erreichbar. Dadurch lassen sich typische
Ansible-Themen wie `become`, Paketverwaltung und Service-Management realitätsnah üben.

## Architektur

```text
                         Docker-Netzwerk: ansible-training

                         +--------------------+
                         |  ansible-control   |
                         |  Ansible + SSH     |
                         +---------+----------+
                                   |
                    SSH            |            SSH
             +---------------------+---------------------+
             |                     |                     |
        +----v----+           +----v----+           +----v----+
        |  web1   |           |  web2   |           |   db1   |
        | systemd |           | systemd |           | systemd |
        +---------+           +---------+           +---------+
                                   |
                              +----v-----+
                              |  misc1   |
                              | systemd  |
                              +----------+
```

Alle Managed Nodes entstehen aus demselben Ubuntu-24.04-Image. Die fachliche Rolle
wird ausschließlich über das Ansible-Inventar definiert.

## Voraussetzungen

- Docker Engine oder Docker Desktop
- Docker Compose v2 (`docker compose`)
- OpenSSH-Client auf dem Host, damit `ssh-keygen` verfügbar ist
- Linux-Container-Modus bei Docker Desktop

Die Managed Nodes benötigen erweiterte Container-Rechte, weil in ihnen `systemd`
als Init-System läuft. Das Setup verwendet deshalb `privileged: true`, bindet
`/sys/fs/cgroup` ein und nutzt den Cgroup-Namespace des Hosts. Das ist für eine
lokale Trainingsumgebung gedacht, nicht als Produktionsmuster.

Die konkrete Cgroup-Konfiguration ist von der Docker-Laufzeitumgebung abhängig.
Die Trainingsumgebung setzt eine Laufzeitumgebung voraus, in der die in
`docker-compose.yml` verwendeten Einstellungen für `privileged`, Cgroups und
`/sys/fs/cgroup` unterstützt werden.

## Start unter Linux, macOS oder WSL

```bash
chmod +x setup.sh reset.sh
./setup.sh
```

## Start unter Windows PowerShell

```powershell
.\setup.ps1
```

## Control Node öffnen

```bash
docker compose exec control bash
```

Das Verzeichnis `./ansible` des Hosts ist dort als `/training` eingebunden.

## Erster Verbindungstest

Auf der Control Node:

```bash
ansible all -m ping
```

Erwartung: `web1`, `web2`, `db1` und `misc1` liefern `SUCCESS`.

## systemd testen

```bash
ansible-playbook playbooks/01-systemd.yml
```

Oder direkt:

```bash
ansible all -b -m ansible.builtin.command -a "systemctl is-system-running"
```

Bei Containern kann `systemctl is-system-running` je nach deaktivierten,
container-untypischen Units auch `degraded` melden. Entscheidend für die Übungen
ist, dass relevante Dienste wie `ssh` oder später `apache2` durch systemd
verwaltet werden können.

## Beispiel: Webserver konfigurieren

```bash
ansible-playbook playbooks/02-webservers.yml
```

Nur `web1` und `web2` werden dabei zu Webservern. Docker selbst liefert keine
vorinstallierten Webserver-Images.

Danach prüfen:

```bash
ansible webservers -b -m ansible.builtin.command -a "systemctl status apache2 --no-pager"
```

## SSH-Verbindung

Der Setup-Schritt erzeugt einmalig:

```text
ssh/id_ed25519
ssh/id_ed25519.pub
```

Beim Build werden die Schlüssel anschließend gezielt verteilt:

- Der Public Key wird in den Managed Nodes als
  `/home/ansible/.ssh/authorized_keys` hinterlegt.
- Der private Key wird in das Image der Control Node als
  `/home/ansible/.ssh/id_ed25519` kopiert.

Die SSH-Schlüssel werden damit nicht zur Laufzeit in die Control Node gemountet.
Die erforderlichen Dateirechte und Eigentümer werden bereits beim Image-Build
gesetzt.

Damit funktioniert beispielsweise von der Control Node aus:

```bash
ssh ansible@web1
```

und Ansible kann ohne Passwortabfrage auf die Managed Nodes zugreifen:

```bash
ansible all -m ping
```

Das Benutzerkonto `ansible` besitzt passwortlose sudo-Rechte. So können
`become: true` und `-b` ohne zusätzliche Passwortabfrage eingesetzt werden.

> **Hinweis:** Der private SSH-Key ist Bestandteil des Control-Node-Images.
> Dieses Vorgehen ist ausschließlich für die isolierte Trainingsumgebung
> vorgesehen. Der verwendete Schlüssel darf nicht für andere Systeme oder
> produktive Zugänge verwendet werden.

## Inventory

Das Inventory bildet die fachlichen Gruppen der Trainingsumgebung vollständig ab:

```ini
[webservers]
web1
web2

[databases]
db1

[misc]
misc1

[linux:children]
webservers
databases
misc

[all:vars]
ansible_user=ansible
ansible_python_interpreter=/usr/bin/python3
```

`webservers`, `databases` und `misc` enthalten die einzelnen Managed Nodes.
Die übergeordnete Gruppe `linux` fasst diese Gruppen zusammen. Über `[all:vars]`
werden außerdem der SSH-Benutzer und der auf den Managed Nodes zu verwendende
Python-Interpreter zentral festgelegt.

Damit können typische Gruppenoperationen geübt werden:

```bash
ansible webservers -m ping
ansible databases -m ping
ansible linux -m setup
```

## Umgebung zurücksetzen

```bash
./reset.sh
```

Alternativ:

```bash
docker compose down -v --remove-orphans
docker compose up -d --build
```

Die SSH-Schlüssel im Verzeichnis `ssh` bleiben dabei erhalten. Beim erneuten Build
werden dieselben Schlüssel wieder in die Images übernommen.

Für einen vollständigen Neuaufbau inklusive neuem SSH-Key:

```bash
docker compose down -v --remove-orphans
rm -rf ssh
./setup.sh
```

## Nützliche Docker-Kommandos

```bash
docker compose ps
docker compose logs web1
docker compose exec web1 bash
docker compose exec web1 systemctl status ssh
docker compose exec control bash
docker compose down
```

## Didaktische Idee

Docker stellt nur die "Maschinen" bereit. Die eigentliche Konfiguration erfolgt
durch Ansible.

- `web1`, `web2`, `db1` und `misc1` starten technisch gleich.
- Inventories und Gruppen geben ihnen unterschiedliche Rollen.
- Software wie Apache oder MariaDB wird erst durch Playbooks installiert.
- systemd erlaubt echte Übungen mit `systemd_service`.
- SSH sorgt dafür, dass Ansible denselben Transportweg wie bei klassischen
  Linux-Servern verwendet.

## Sicherheitshinweis

`privileged: true` gibt den Managed-Node-Containern weitreichende Rechte auf dem
Docker-Host. Dieses Setup ist ausdrücklich für lokale Schulungs- und
Laborumgebungen vorgesehen. Für Produktionsumgebungen sollte dieses Muster nicht
übernommen werden.

Auch der private SSH-Key wird für die reproduzierbare Trainingsumgebung in das
Control-Node-Image kopiert. Es muss sich deshalb um einen ausschließlich für
diese Trainingsumgebung erzeugten Schlüssel handeln.