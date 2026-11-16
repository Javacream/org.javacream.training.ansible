# SSH-Demo unter Ubuntu

In dieser Demo wird auf einem Ubuntu-System der Benutzer `user0` angelegt und der OpenSSH-Server als **systemd-Dienst** eingerichtet. Anschließend wird eine SSH-Verbindung getestet.

## 1. Benutzer anlegen

```bash
sudo adduser user0
```

Dabei wird ein Passwort vergeben. Ubuntu legt üblicherweise das Home-Verzeichnis `/home/user0`, die gleichnamige primäre Gruppe und eine Login-Shell an.

Benutzer überprüfen:

```bash
id user0
getent passwd user0
```

## 2. OpenSSH-Server installieren

```bash
sudo apt update
sudo apt install openssh-server
```

Der Server wird unter Ubuntu über die systemd-Unit `ssh.service` verwaltet.

## 3. SSH-Dienst starten und aktivieren

```bash
sudo systemctl enable --now ssh
```

- `enable` aktiviert den automatischen Start beim Systemstart.
- `--now` startet den Dienst sofort.

Status kontrollieren:

```bash
systemctl status ssh
```

Erwarteter Status: `active (running)`.

Prüfen, ob der SSH-Server auf Port 22 lauscht:

```bash
sudo ss -tlnp | grep ':22'
```

## 4. Lokale SSH-Verbindung testen

```bash
ssh user0@localhost
```

Beim ersten Verbindungsaufbau gegebenenfalls den Host-Key bestätigen und anschließend das Passwort von `user0` eingeben (sofern Passwortauthentifizierung aktiviert ist).

Nach der Anmeldung:

```bash
whoami
hostname
exit
```

## 5. Verbindung von einem anderen Rechner

IP-Adressen des Ubuntu-Systems anzeigen:

```bash
hostname -I
```

Beispiel für eine Verbindung zu einem Ubuntu-System mit der Adresse `192.168.1.100`:

```bash
ssh user0@192.168.1.100
```

Falls die Firewall UFW aktiviert ist, SSH freigeben:

```bash
sudo ufw allow OpenSSH
```

Die Beispiel-IP-Adresse muss durch die tatsächliche Adresse des Systems ersetzt werden.

## 6. SSH-Dienst mit systemd verwalten

| Befehl | Wirkung |
| --- | --- |
| `sudo systemctl start ssh` | Dienst starten |
| `sudo systemctl stop ssh` | Dienst stoppen |
| `sudo systemctl restart ssh` | Dienst neu starten |
| `sudo systemctl enable ssh` | Autostart aktivieren |
| `sudo systemctl disable ssh` | Autostart deaktivieren |
| `systemctl status ssh` | Dienststatus anzeigen |
| `journalctl -u ssh -n 30` | Letzte 30 Logeinträge anzeigen |

## 7. Optional: Zugriff mit Ansible

Der Ubuntu-Rechner kann als zusätzlicher Managed Node in ein Ansible-Inventory aufgenommen werden:

```ini
[physical]
ubuntu-host ansible_host=192.168.1.100 ansible_user=user0
```

Wenn die Ansible-Control-Node den Ubuntu-Rechner über das Netzwerk erreichen kann, lässt sich die Verbindung prüfen:

```bash
ansible physical -m ping -k
```

Die Option `-k` fragt nach dem SSH-Passwort. Für einen dauerhaften Einsatz empfiehlt sich die SSH-Key-Authentifizierung.

**Hinweis:** Die Verwaltung über `systemctl` setzt ein laufendes systemd voraus. Bei Ubuntu unter WSL muss systemd gegebenenfalls erst aktiviert werden.
