# Die Ansible-Trainingsumgebung

## 1. Überblick

Für die praktischen Übungen steht eine abgeschlossene Trainingsumgebung zur Verfügung. Sie besteht aus mehreren Linux-Systemen, die als Docker-Container ausgeführt werden.

Die Umgebung enthält eine **Ansible Control Node** und vier **Managed Nodes**:

```text
                         control
                     Ansible Control Node
                            |
              +-------------+-------------+
              |             |             |
            web1          web2           db1
              |
            misc1
```

Die Container befinden sich in einem gemeinsamen Docker-Netzwerk und können sich über ihre Namen erreichen.

Docker stellt dabei lediglich die benötigten Linux-Systeme bereit. Die eigentliche Konfiguration dieser Systeme erfolgt im Laufe des Trainings mit Ansible.

Ein wichtiger Grundgedanke der Trainingsumgebung lautet daher:

**Die Managed Nodes starten technisch weitgehend gleich. Ihre unterschiedlichen Aufgaben und Konfigurationen entstehen durch Ansible.**

---

## 2. Die Systeme

Die Trainingsumgebung besteht aus fünf Systemen.

| System | Aufgabe |
|---|---|
| `control` | Ansible Control Node |
| `web1` | Managed Node, vorgesehen als Webserver |
| `web2` | Managed Node, vorgesehen als Webserver |
| `db1` | Managed Node, vorgesehen als Datenbankserver |
| `misc1` | Managed Node für weitere Übungen |

Die Namen `web1`, `web2` oder `db1` bedeuten zunächst nicht, dass auf diesen Systemen bereits ein Webserver oder eine Datenbank installiert ist.

Beispielsweise werden `web1` und `web2` erst dann tatsächlich zu Webservern, wenn sie durch ein entsprechendes Ansible-Playbook konfiguriert werden.

Damit lässt sich im Training nachvollziehen, wie aus zunächst gleichartigen Linux-Systemen durch automatisierte Konfiguration Systeme mit unterschiedlichen Aufgaben entstehen.

---

## 3. Control Node und Managed Nodes

Ansible unterscheidet zwischen der **Control Node** und den **Managed Nodes**.

### Control Node

Die Control Node ist das System, auf dem Ansible installiert ist und von dem aus die Automatisierung durchgeführt wird.

In unserer Trainingsumgebung ist dies:

```text
control
```

Auf der Control Node befinden sich unter anderem:

- Ansible
- die Ansible-Konfiguration
- das Inventory
- Playbooks
- der SSH-Schlüssel für den Zugriff auf die Managed Nodes

Die meisten Ansible-Kommandos des Trainings werden deshalb auf der Control Node ausgeführt.

### Managed Nodes

Die Systeme

```text
web1
web2
db1
misc1
```

sind die Managed Nodes.

Auf ihnen muss Ansible selbst nicht installiert sein. Ansible verbindet sich per SSH mit diesen Systemen und führt dort die erforderlichen Aktionen aus.

Für die Ausführung vieler Ansible-Module steht auf den Managed Nodes Python 3 zur Verfügung.

---

## 4. Die Trainingsumgebung starten

Die komplette Umgebung wird mit Docker Compose gestartet.

Unter Linux oder WSL erfolgt die erstmalige Einrichtung mit:

```bash
./setup.sh
```

Das Setup erzeugt unter anderem den für die Trainingsumgebung benötigten SSH-Schlüssel und baut anschließend die Docker-Images.

Unter Windows PowerShell steht entsprechend zur Verfügung:

```powershell
.\setup.ps1
```

Der Zustand der Container kann auf dem Docker-Host überprüft werden:

```bash
docker compose ps
```

Nach dem Start sollten die Control Node und alle vier Managed Nodes laufen.

---

## 5. Auf der Control Node arbeiten

Für die Ansible-Übungen wird zunächst eine Shell auf der Control Node geöffnet:

```bash
docker compose exec control bash
```

Die folgenden Ansible-Kommandos werden – sofern in der jeweiligen Übung nichts anderes angegeben ist – innerhalb dieser Shell ausgeführt.

Das zentrale Arbeitsverzeichnis ist:

```text
/training
```

Das Verzeichnis `ansible` der Trainingsumgebung auf dem Docker-Host ist dort eingebunden. Änderungen an Inventory, Playbooks oder anderen Ansible-Dateien stehen deshalb unmittelbar innerhalb der Control Node zur Verfügung.

Das aktuelle Verzeichnis kann beispielsweise mit

```bash
pwd
```

überprüft werden.

---

## 6. Das Inventory

Ansible benötigt eine Beschreibung der Systeme, die verwaltet werden sollen. Diese Aufgabe übernimmt das **Inventory**.

Das Inventory der Trainingsumgebung enthält:

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

Die Managed Nodes werden dabei verschiedenen Gruppen zugeordnet.

Die Gruppe `webservers` enthält `web1` und `web2`.

Die Gruppe `databases` enthält `db1`.

`misc1` befindet sich in der Gruppe `misc`.

Zusätzlich werden diese drei Gruppen über `[linux:children]` zur gemeinsamen Gruppe `linux` zusammengefasst.

Ansible kann dadurch gezielt einzelne Hosts oder ganze Gruppen ansprechen.

Die Struktur des Inventories lässt sich anzeigen mit:

```bash
ansible-inventory --graph
```

---

## 7. Verbindung zu den Managed Nodes

Die Kommunikation zwischen der Control Node und den Managed Nodes erfolgt über SSH.

Zum Beispiel kann von der Control Node eine direkte SSH-Verbindung zu `web1` hergestellt werden:

```bash
ssh ansible@web1
```

Für die Trainingsumgebung wurde bereits ein SSH-Schlüsselpaar erzeugt. Der private Schlüssel befindet sich auf der Control Node, der zugehörige öffentliche Schlüssel wurde auf den Managed Nodes für den Benutzer `ansible` hinterlegt.

Deshalb ist für die normale Arbeit mit Ansible keine Eingabe eines SSH-Passworts erforderlich.

Die SSH-Verbindung ist ein wichtiger Bestandteil der Umgebung: Ansible verwendet damit grundsätzlich denselben Zugriffsweg, der auch bei der Administration klassischer Linux-Server verwendet werden kann.

---

## 8. Der Benutzer `ansible`

Auf allen Managed Nodes existiert der Benutzer `ansible`.

Ansible verwendet diesen Benutzer für die SSH-Verbindung. Dies wird zentral im Inventory festgelegt:

```ini
[all:vars]
ansible_user=ansible
```

Der Benutzer besitzt außerdem die erforderlichen `sudo`-Rechte.

Damit können Aufgaben, für die Root-Berechtigungen erforderlich sind, mit Ansible über **Privilege Escalation** ausgeführt werden.

Bei einem Ad-hoc-Kommando geschieht dies beispielsweise mit:

```bash
ansible all -b -m command -a "id"
```

Die Option `-b` aktiviert `become`.

In einem Playbook kann dasselbe beispielsweise mit

```yaml
become: true
```

festgelegt werden.

Dadurch können später unter anderem Pakete installiert, Konfigurationsdateien verändert oder Systemdienste verwaltet werden.

---

## 9. Erster Ansible-Test

Nach dem Start der Umgebung kann die Verbindung zu allen Managed Nodes mit dem Ansible-Modul `ping` getestet werden:

```bash
ansible all -m ping
```

Für jeden erreichbaren Managed Node sollte Ansible unter anderem `SUCCESS` und `"ping": "pong"` melden.

Dieser Test überprüft mehr als nur die Netzwerkverbindung. Für einen erfolgreichen Ansible-Ping müssen unter anderem

- der Host erreichbar sein,
- SSH funktionieren,
- die Authentifizierung funktionieren und
- Ansible auf dem Managed Node Python verwenden können.

`ansible.builtin.ping` ist deshalb ein guter erster Funktionstest für die Trainingsumgebung.

---

## 10. Hosts und Gruppen ansprechen

Ansible-Kommandos müssen nicht immer auf allen Managed Nodes ausgeführt werden.

Alle Systeme können mit

```bash
ansible all -m ping
```

angesprochen werden.

Nur die Webserver werden angesprochen mit:

```bash
ansible webservers -m ping
```

Nur die Datenbankserver mit:

```bash
ansible databases -m ping
```

Und über die übergeordnete Gruppe `linux` können alle drei Untergruppen gemeinsam angesprochen werden:

```bash
ansible linux -m ping
```

Auch ein einzelner Host kann ausgewählt werden:

```bash
ansible web1 -m ping
```

Die Gruppierung im Inventory wird im weiteren Verlauf des Trainings eine wichtige Rolle spielen.

---

## 11. systemd auf den Managed Nodes

Die Managed Nodes unterscheiden sich in einem wichtigen Punkt von vielen einfachen Docker-Containern: Sie verwenden **systemd als Init-System**.

Dadurch können im Training Linux-Dienste weitgehend so verwaltet werden, wie dies auch auf einem klassischen Linux-Server möglich ist.

Beispielsweise kann der Zustand des SSH-Dienstes geprüft werden:

```bash
ansible all -b -m command -a "systemctl is-active ssh"
```

Später können Dienste mit dem Ansible-Modul `systemd_service` gestartet, gestoppt und für den automatischen Start aktiviert werden.

Dies ist beispielsweise für Übungen mit Apache oder anderen Systemdiensten relevant.

Die Verwendung von systemd ist einer der Gründe dafür, dass die Managed Nodes mit besonderen Docker-Berechtigungen gestartet werden. Die Docker-Konfiguration dieser Container ist daher Bestandteil der vorbereiteten Trainingsinfrastruktur und muss für die Übungen normalerweise nicht verändert werden.

---

## 12. Docker und Ansible haben unterschiedliche Aufgaben

Für die Arbeit mit der Trainingsumgebung ist die Trennung zwischen Docker und Ansible wichtig.

**Docker** stellt die benötigten Systeme bereit:

```text
control
web1
web2
db1
misc1
```

**Ansible** konfiguriert die Managed Nodes.

Ein Webserver sollte deshalb beispielsweise nicht dadurch eingerichtet werden, dass das Docker-Image von `web1` manuell verändert wird.

Stattdessen wird die gewünschte Konfiguration mit Ansible beschrieben und anschließend auf die entsprechende Inventory-Gruppe angewendet.

Das ermöglicht beispielsweise:

```text
web1 ─┐
      ├── Gruppe webservers ── Ansible Playbook ── Apache
web2 ─┘

db1 ─── Gruppe databases ───── Ansible Playbook ── Datenbank
```

Diese Trennung bildet die Grundlage für viele der folgenden Übungen.

---

## 13. Änderungen während der Übungen

Die Managed Nodes sind bewusst als Trainingssysteme vorgesehen. Im Verlauf der Übungen werden dort unter anderem

- Pakete installiert,
- Dateien erzeugt und verändert,
- Benutzer und Gruppen verwaltet,
- Dienste konfiguriert,
- Dienste gestartet und gestoppt und
- unterschiedliche Serverrollen aufgebaut.

Es ist daher normal, dass sich der Zustand der Managed Nodes während des Trainings verändert.

Die Ansible-Dateien im Verzeichnis `/training` bleiben dagegen außerhalb der Managed Nodes erhalten und können fortlaufend weiterentwickelt werden.

---

## 14. Trainingsumgebung zurücksetzen

Wenn die Managed Nodes wieder in ihren ursprünglichen Zustand versetzt werden sollen, kann die Umgebung auf dem Docker-Host zurückgesetzt werden:

```bash
./reset.sh
```

Dabei werden die Container neu erzeugt.

Die für die Trainingsumgebung erzeugten SSH-Schlüssel bleiben erhalten und werden beim erneuten Build wieder verwendet.

Dadurch können die Serverzustände zurückgesetzt werden, ohne gleichzeitig die SSH-Konfiguration der Trainingsumgebung neu aufbauen zu müssen.

Ein Reset ist beispielsweise sinnvoll,

- vor einem neuen Trainingsblock,
- nach umfangreichen Experimenten oder
- wenn eine Übung bewusst noch einmal von vorne durchgeführt werden soll.

---

## 15. Nützliche Kommandos

Einige Kommandos werden während des Trainings immer wieder benötigt.

Status der Docker-Container:

```bash
docker compose ps
```

Shell auf der Control Node öffnen:

```bash
docker compose exec control bash
```

Shell direkt auf einem Managed Node öffnen:

```bash
docker compose exec web1 bash
```

Ansible-Verbindung testen:

```bash
ansible all -m ping
```

Inventory anzeigen:

```bash
ansible-inventory --graph
```

Ein Kommando auf allen Managed Nodes ausführen:

```bash
ansible all -m command -a "hostname"
```

Ein Kommando mit Root-Berechtigungen ausführen:

```bash
ansible all -b -m command -a "id"
```

Ein Playbook starten:

```bash
ansible-playbook playbooks/00-ping.yml
```

---

## 16. Zusammenfassung

Die Trainingsumgebung stellt eine kleine Infrastruktur aus mehreren Linux-Systemen zur Verfügung.

Docker übernimmt die Bereitstellung dieser Systeme. Ansible übernimmt ihre Konfiguration.

Die Control Node `control` ist der zentrale Arbeitsplatz für die Ansible-Übungen.

Die Managed Nodes `web1`, `web2`, `db1` und `misc1` werden über SSH verwaltet und über das Inventory zu Gruppen zusammengefasst.

Damit steht für die folgenden Trainingsblöcke eine reproduzierbare Umgebung zur Verfügung, in der zentrale Ansible-Konzepte praktisch erarbeitet werden können – von einfachen Ad-hoc-Kommandos über Playbooks bis hin zur Konfiguration unterschiedlicher Serverrollen.
