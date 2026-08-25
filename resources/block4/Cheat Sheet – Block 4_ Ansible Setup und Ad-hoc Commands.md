# Cheat Sheet – Block 4: Ansible Setup und Ad-hoc Commands

## 1. Ansible-Installation prüfen

```bash
ansible --version
```

Zeigt unter anderem:

- Ansible-Version
- verwendete Python-Version
- verwendete Konfigurationsdatei
- Modul- und Collection-Pfade

```bash
which ansible
```

Zeigt den Pfad der verwendeten Ansible-Installation.

---

## 2. Projektverzeichnis

```bash
mkdir -p ~/ansible-training/block4
cd ~/ansible-training/block4
```

---

## 3. Inventory prüfen

Inventory als Baumstruktur:

```bash
ansible-inventory -i inventory.ini --graph
```

Inventory vollständig anzeigen:

```bash
ansible-inventory -i inventory.ini --list
```

Beispiel:

```ini
[web]
web01
web02

[db]
db01
```

---

## 4. SSH-Verbindung prüfen

Direkte Verbindung zu einem Managed Node:

```bash
ssh training@web01
```

Allgemein:

```bash
ssh <user>@<host>
```

Remote-Sitzung beenden:

```bash
exit
```

SSH-Key explizit angeben:

```bash
ssh -i ~/.ssh/linux_training training@web01
```

---

## 5. Grundstruktur eines Ad-hoc Commands

```bash
ansible <host-pattern> \
  -i <inventory> \
  -m <module> \
  -a "<argumente>"
```

Beispiel:

```bash
ansible web \
  -i inventory.ini \
  -m command \
  -a "hostname"
```

Ohne Modulargumente:

```bash
ansible all \
  -i inventory.ini \
  -m ping
```

---

## 6. Host Patterns

Alle Hosts:

```bash
ansible all -i inventory.ini -m ping
```

Eine Gruppe:

```bash
ansible web -i inventory.ini -m ping
```

Ein bestimmter Host:

```bash
ansible web01 -i inventory.ini -m ping
```

Mehrere Gruppen:

```bash
ansible 'web:db' -i inventory.ini -m ping
```

Hosts ausschließen:

```bash
ansible 'all:!db' -i inventory.ini -m ping
```

---

# 7. Verbindung mit `ping` testen

```bash
ansible all -i inventory.ini -m ping
```

Nur Webserver:

```bash
ansible web -i inventory.ini -m ping
```

Wichtig:

`ansible.builtin.ping` ist **kein ICMP-Ping**.

Das Modul prüft unter anderem:

- SSH-Verbindung
- Authentifizierung
- grundsätzliche Ausführung eines Ansible-Moduls

Erfolgreiche Ausgabe:

```text
web01 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

---

# 8. Remote-Befehle mit `command`

Hostname abfragen:

```bash
ansible all \
  -i inventory.ini \
  -m command \
  -a "hostname"
```

Uptime anzeigen:

```bash
ansible all \
  -i inventory.ini \
  -m command \
  -a "uptime"
```

Betriebssysteminformationen anzeigen:

```bash
ansible all \
  -i inventory.ini \
  -m command \
  -a "cat /etc/os-release"
```

---

# 9. Dateien mit `copy` übertragen

Lokale Datei erzeugen:

```bash
echo "Block 4" > demo.txt
```

Datei auf Managed Nodes kopieren:

```bash
ansible web \
  -i inventory.ini \
  -m copy \
  -a "src=demo.txt dest=/tmp/demo.txt"
```

Datei kontrollieren:

```bash
ansible web \
  -i inventory.ini \
  -m command \
  -a "cat /tmp/demo.txt"
```

---

# 10. Pakete mit `package` verwalten

Paket installieren:

```bash
ansible web \
  -i inventory.ini \
  -m package \
  -a "name=tree state=present"
```

Paket entfernen:

```bash
ansible web \
  -i inventory.ini \
  -m package \
  -a "name=tree state=absent"
```

Typische Zustände:

```text
state=present
state=absent
state=latest
```

Für Paketoperationen werden normalerweise administrative Rechte benötigt.

---

# 11. Privilege Escalation mit `become`

Ansible verbindet sich typischerweise zunächst als normaler Benutzer mit dem Managed Node.

Beispiel:

```text
Control Node
     │
     │ SSH
     ▼
training@web01
     │
     │ become / sudo
     ▼
    root
```

`become` ermöglicht anschließend die Ausführung eines Tasks mit erhöhten Rechten.

## `--become`

```bash
ansible web \
  -i inventory.ini \
  --become \
  -m package \
  -a "name=tree state=present"
```

Kurzform:

```bash
ansible web \
  -i inventory.ini \
  -b \
  -m package \
  -a "name=tree state=present"
```

Dabei gilt:

```text
-b = --become
```

---

## SSH-Benutzer und `become`

Remote-Benutzer explizit festlegen:

```bash
ansible web \
  -i inventory.ini \
  -u training \
  -b \
  -m package \
  -a "name=tree state=present"
```

Bedeutung:

```text
-u training
     │
     └── SSH-Anmeldung als training

-b
     │
     └── Rechteerhöhung auf dem Managed Node
```

Damit sind **Remote-Anmeldung und Rechteerhöhung zwei unterschiedliche Vorgänge**.

---

## Become-Passwort abfragen

Benötigt `sudo` ein Passwort:

```bash
ansible web \
  -i inventory.ini \
  -b \
  -K \
  -m package \
  -a "name=tree state=present"
```

Ansible fragt dann:

```text
BECOME password:
```

Dabei gilt:

```text
-K = --ask-become-pass
```

---

## Become-Benutzer festlegen

Standardmäßig erfolgt die Rechteerhöhung typischerweise zu `root`.

Ein anderer Benutzer kann angegeben werden:

```bash
ansible web \
  -i inventory.ini \
  -b \
  --become-user appuser \
  -m command \
  -a "whoami"
```

---

## Become-Methode

Standard unter Linux ist normalerweise `sudo`.

Explizite Angabe:

```bash
ansible web \
  -i inventory.ini \
  -b \
  --become-method sudo \
  -m command \
  -a "whoami"
```

---

## Wichtige Become-Optionen

| Option | Kurzform | Bedeutung |
|---|---|---|
| `--become` | `-b` | Privilege Escalation aktivieren |
| `--ask-become-pass` | `-K` | Become-Passwort abfragen |
| `--become-user USER` | – | Zielbenutzer der Rechteerhöhung |
| `--become-method METHOD` | – | Verfahren, z. B. `sudo` |

Merksatz:

> **SSH bestimmt, als wer ich mich verbinde. `become` bestimmt, mit welchen Rechten der Task ausgeführt wird.**

---

# 12. SSH-Benutzer angeben

```bash
ansible all \
  -i inventory.ini \
  -u training \
  -m ping
```

```text
-u = --user
```

---

# 13. SSH-Key angeben

```bash
ansible all \
  -i inventory.ini \
  --private-key ~/.ssh/linux_training \
  -m ping
```

---

# 14. Modulhilfe mit `ansible-doc`

Dokumentation für `ping`:

```bash
ansible-doc ping
```

Für `command`:

```bash
ansible-doc command
```

Für `copy`:

```bash
ansible-doc copy
```

Für `package`:

```bash
ansible-doc package
```

Kurzfassung:

```bash
ansible-doc -s package
```

---

# 15. Ausführlichere Ausgabe

Einfache zusätzliche Informationen:

```bash
ansible all -i inventory.ini -m ping -v
```

Mehr Details:

```bash
ansible all -i inventory.ini -m ping -vv
```

Detaillierte SSH- und Verbindungsinformationen:

```bash
ansible all -i inventory.ini -m ping -vvv
```

---

# 16. Wichtige Optionen des `ansible`-Kommandos

| Option | Bedeutung |
|---|---|
| `-i FILE` | Inventory auswählen |
| `-m MODULE` | Modul auswählen |
| `-a "ARGS"` | Modulargumente |
| `-u USER` | SSH-Benutzer |
| `--private-key FILE` | privaten SSH-Key auswählen |
| `-b` | `become` aktivieren |
| `-K` | Become-Passwort abfragen |
| `--become-user USER` | Benutzer für Rechteerhöhung |
| `-v` | ausführlichere Ausgabe |
| `-vv` | noch ausführlichere Ausgabe |
| `-vvv` | detaillierte Debug-Ausgabe |

---

# 17. Statusmeldungen verstehen

## `SUCCESS`

Der Host wurde erreicht und der Task erfolgreich ausgeführt.

## `CHANGED`

Der Task war erfolgreich und hat den Zustand des Managed Nodes verändert.

Beispiel:

```text
web01 | CHANGED => ...
```

## `FAILED`

Der Managed Node wurde erreicht, aber der Task ist fehlgeschlagen.

Typische Ursachen:

- fehlende Rechte
- falscher Paketname
- falsche Modulargumente
- Kommando schlägt fehl

## `UNREACHABLE`

Ansible konnte den Managed Node nicht erreichen.

Typische Ursachen:

- falscher Hostname
- falsche IP-Adresse
- SSH nicht erreichbar
- falscher SSH-Benutzer
- falscher SSH-Key
- Authentifizierungsproblem

---

# 18. Typischer Arbeitsablauf in Block 4

### 1. Projekt öffnen

```bash
cd ~/ansible-training/block4
```

### 2. Inventory kontrollieren

```bash
ansible-inventory -i inventory.ini --graph
```

### 3. Verbindung testen

```bash
ansible all -i inventory.ini -m ping
```

### 4. Hostnamen ermitteln

```bash
ansible all \
  -i inventory.ini \
  -m command \
  -a "hostname"
```

### 5. Uptime prüfen

```bash
ansible all \
  -i inventory.ini \
  -m command \
  -a "uptime"
```

### 6. Datei verteilen

```bash
echo "Block 4" > demo.txt
```

```bash
ansible web \
  -i inventory.ini \
  -m copy \
  -a "src=demo.txt dest=/tmp/demo.txt"
```

### 7. Administrative Änderung durchführen

```bash
ansible web \
  -i inventory.ini \
  -b \
  -m package \
  -a "name=tree state=present"
```

### 8. Bei Problemen Details anzeigen

```bash
ansible web \
  -i inventory.ini \
  -m ping \
  -vvv
```

---

# 19. Grundmodell für Ad-hoc Commands

```text
ansible
   │
   ├── Welche Hosts?
   │      Host Pattern
   │
   ├── Welches Inventory?
   │      -i
   │
   ├── Welche Aktion?
   │      -m Modul
   │
   ├── Mit welchen Parametern?
   │      -a Argumente
   │
   ├── Als welcher SSH-Benutzer?
   │      -u
   │
   └── Administrative Rechte?
          -b / --become
```

Beispiel:

```bash
ansible web \
  -i inventory.ini \
  -u training \
  -b \
  -m package \
  -a "name=tree state=present"
```

lässt sich lesen als:

> **Auf allen Hosts der Gruppe `web`, aus `inventory.ini`, per SSH als `training` anmelden, Rechte erhöhen und mit dem `package`-Modul sicherstellen, dass das Paket `tree` installiert ist.**