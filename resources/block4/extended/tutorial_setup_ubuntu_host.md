# Tutorial: Ubuntu-Host per SSH für Ansible einrichten

## Ziel

Zusätzlich zu den Docker-basierten Managed Nodes soll auch der
Ubuntu-Host, auf dem die Trainingsumgebung läuft, von der Ansible
Control Node verwaltet werden können.

Die Verbindung erfolgt -- wie bei den übrigen Managed Nodes -- über SSH.
Für den Zugriff auf den Ubuntu-Host wird der Benutzer `sl01` verwendet.

Nach Abschluss der Einrichtung soll von der Control Node aus Folgendes
funktionieren:

``` bash
ssh sl01@host.docker.internal
ansible dockerhost -m ping
```

## 1. Voraussetzungen

Auf dem Ubuntu-Host benötigen wir:

-   den Benutzer `sl01`,
-   einen laufenden SSH-Server,
-   Python 3,
-   Netzwerkzugriff von der Docker-Control-Node auf den Host.

Die Ansible Control Node besitzt bereits ein SSH-Schlüsselpaar. Dieses
verwenden wir auch für den Zugriff auf den Ubuntu-Host.

## 2. SSH-Server auf dem Ubuntu-Host prüfen

Die folgenden Kommandos werden zunächst **direkt auf dem Ubuntu-Host**
ausgeführt.

``` bash
sudo systemctl status ssh
```

Ist OpenSSH noch nicht installiert:

``` bash
sudo apt update
sudo apt install openssh-server
sudo systemctl enable --now ssh
```

Anschließend:

``` bash
sudo systemctl status ssh
```

## 3. Benutzer `sl01` prüfen

``` bash
id sl01
groups sl01
```

Falls `sl01` für spätere Ansible-Übungen administrative Aufgaben
ausführen soll, kann der Benutzer der Gruppe `sudo` hinzugefügt werden:

``` bash
sudo usermod -aG sudo sl01
```

Eine neue Gruppenmitgliedschaft wird bei einer bestehenden Anmeldung
normalerweise erst nach einer erneuten Anmeldung wirksam.

## 4. Docker-Host aus der Control Node erreichbar machen

Die Control Node läuft selbst in einem Docker-Container. In
`docker-compose.yml` wird beim Service `control` ergänzt:

``` yaml
services:
  control:
    # ...
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

Dadurch steht innerhalb der Control Node der Name `host.docker.internal`
für den Docker-Host zur Verfügung.

Nach der Änderung wird die Control Node neu erzeugt:

``` bash
docker compose up -d --force-recreate control
```

## 5. Namensauflösung testen

Shell auf der Control Node öffnen:

``` bash
docker compose exec control bash
```

Dort:

``` bash
getent hosts host.docker.internal
```

Optional:

``` bash
ping -c 2 host.docker.internal
```

Ein fehlgeschlagener Ping bedeutet nicht zwingend, dass SSH ebenfalls
nicht funktioniert. Für Ansible ist die Erreichbarkeit des SSH-Dienstes
entscheidend.

## 6. Erste SSH-Verbindung testen

Von der **Control Node** aus:

``` bash
ssh sl01@host.docker.internal
```

Bei der ersten Verbindung kennt der SSH-Client den Host-Key noch nicht.
Nach Prüfung des Fingerprints wird die Aufnahme in `known_hosts` mit
`yes` bestätigt.

Anschließend erfolgt zunächst die Anmeldung mit dem Passwort des
Benutzers `sl01`.

Wenn die Anmeldung funktioniert, wissen wir, dass:

-   die Namensauflösung funktioniert,
-   der Ubuntu-Host aus dem Container erreichbar ist,
-   der SSH-Server läuft,
-   sich `sl01` per SSH anmelden kann.

Sitzung beenden:

``` bash
exit
```

## 7. Vorhandenen Trainings-Key verwenden

Auf der Control Node ist bereits ein SSH-Schlüsselpaar vorhanden:

``` bash
ls -l ~/.ssh
```

Dort sollten unter anderem vorhanden sein:

``` text
id_ed25519
id_ed25519.pub
```

Wir erzeugen **keinen neuen Schlüssel**, sondern verwenden diesen
vorhandenen Trainings-Key auch für den Ubuntu-Host.

## 8. Public Key auf den Ubuntu-Host übertragen

Von der Control Node:

``` bash
ssh-copy-id sl01@host.docker.internal
```

Dabei wird noch einmal nach dem Passwort von `sl01` gefragt.

`ssh-copy-id` übernimmt den öffentlichen Schlüssel aus
`~/.ssh/id_ed25519.pub` und trägt ihn auf dem Ubuntu-Host für `sl01` in
`~/.ssh/authorized_keys` ein.

Der private Schlüssel verlässt die Control Node dabei nicht.

## 9. Anmeldung ohne Passwort testen

``` bash
ssh sl01@host.docker.internal
```

Die Anmeldung sollte nun ohne Passwortabfrage funktionieren.

Weitere Tests:

``` bash
ssh sl01@host.docker.internal hostname
ssh sl01@host.docker.internal id
```

## 10. Ubuntu-Host in das Ansible-Inventory aufnehmen

Eine eigene Gruppe macht deutlich, dass dieser Host **nicht zu den
wegwerfbaren Docker-Managed-Nodes** gehört:

``` ini
[physical]
dockerhost ansible_host=host.docker.internal ansible_user=sl01
```

Ein vollständiges Inventory kann beispielsweise so aussehen:

``` ini
[webservers]
web1
web2

[databases]
db1

[misc]
misc1

[training:children]
webservers
databases
misc

[physical]
dockerhost ansible_host=host.docker.internal ansible_user=sl01

[all:vars]
ansible_user=ansible
ansible_python_interpreter=/usr/bin/python3
```

Die hostspezifische Einstellung `ansible_user=sl01` überschreibt für
`dockerhost` die globale Einstellung `ansible_user=ansible`.

Die Docker-Managed-Nodes verwenden also weiterhin `ansible`, während für
den Ubuntu-Host `sl01` verwendet wird.

## 11. Inventory prüfen

``` bash
ansible-inventory --graph
```

Die Struktur sollte sinngemäß enthalten:

``` text
@all:
  |--@physical:
  |  |--dockerhost
  |--@training:
     |--@databases:
     |  |--db1
     |--@misc:
     |  |--misc1
     |--@webservers:
        |--web1
        |--web2
```

Damit ist zwischen Docker-basierten Trainingssystemen und dem realen
Ubuntu-Host getrennt.

## 12. Ansible-Ping auf den Ubuntu-Host

``` bash
ansible dockerhost -m ping
```

Erwartet wird:

``` text
dockerhost | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

Danach:

``` bash
ansible physical -m ping
ansible all -m ping
```

`all` umfasst jetzt sowohl die Docker-basierten Managed Nodes als auch
den Ubuntu-Host.

## 13. Facts des Ubuntu-Hosts abfragen

``` bash
ansible dockerhost -m setup -a "filter=ansible_distribution*"
```

Weitere Beispiele:

``` bash
ansible dockerhost -m setup -a "filter=ansible_hostname"
ansible dockerhost -m command -a "uname -a"
```

## 14. `become` auf dem Ubuntu-Host testen

``` bash
ansible dockerhost -b -m command -a "id"
```

Je nach `sudo`-Konfiguration von `sl01` kann ein Become-Passwort
benötigt werden:

``` bash
ansible dockerhost -b -K -m command -a "id"
```

`-K` entspricht `--ask-become-pass`.

Bei erfolgreicher Privilege Escalation enthält die Ausgabe:

``` text
uid=0(root)
```

## 15. Vorsicht beim Arbeiten mit `all`

Mit der Aufnahme des Ubuntu-Hosts verändert sich die Bedeutung von
`all`.

Vorher bezeichnete `all` ausschließlich die wegwerfbaren
Docker-Managed-Nodes. Jetzt enthält `all` zusätzlich den **realen
Ubuntu-Host**.

Ein harmloser Befehl wie

``` bash
ansible all -m ping
```

ist unproblematisch.

Ein Befehl wie

``` bash
ansible all -b -m apt -a "name=tree state=present"
```

würde dagegen auch Software auf dem realen Ubuntu-Host installieren.

Für Übungen, die ausschließlich die zurücksetzbaren Docker-Systeme
verändern sollen, verwenden wir deshalb die Gruppe `training`:

``` bash
ansible training -m ping
ansible training -b -m apt -a "name=tree state=present"
```

Die Gruppe `physical` wird verwendet, wenn ausdrücklich der reale
Ubuntu-Host angesprochen werden soll.

## 16. Ergebnis

Nach Abschluss der Einrichtung besteht die Trainingsumgebung aus zwei
Arten von Managed Nodes:

``` text
Control Node
    |
    +-- training
    |     +-- web1
    |     +-- web2
    |     +-- db1
    |     +-- misc1
    |
    +-- physical
          +-- dockerhost
```

Die Docker-basierten Systeme sind zurücksetzbare Trainingssysteme.
`dockerhost` ist dagegen der reale Ubuntu-Host und sollte deshalb
bewusst und gezielt angesprochen werden.

Die SSH-Verbindung erfolgt in beiden Fällen nach demselben Grundprinzip:

``` text
Ansible Control Node
        |
        | SSH + Public-Key-Authentifizierung
        |
        +------> Docker Managed Nodes
        |
        +------> Ubuntu-Host
```

Damit kann Ansible sowohl die simulierte Serverlandschaft als auch ein
reales Linux-System verwalten.
