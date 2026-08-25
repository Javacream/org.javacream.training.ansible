# Tutorial: Windows-Host per SSH für Ansible einrichten

## Ziel

Zusätzlich zu den Linux-basierten Managed Nodes soll eine reale
Windows-Maschine von der Ansible Control Node verwaltet werden.

In dieser Trainingsumgebung verwenden wir dafür **OpenSSH**. Damit
erfolgt der Transport sowohl zu Linux- als auch zu Windows-Systemen über
SSH.

``` text
Ansible Control Node
        |
        | SSH
        +------> Linux Managed Nodes
        +------> Ubuntu-Host
        +------> Windows-Host
```

Der Transportweg ist einheitlich, die Verarbeitung auf dem Zielsystem
unterscheidet sich:

``` text
Linux:    SSH -> Linux-Shell / Python
Windows:  SSH -> PowerShell
```

Für Windows verwenden wir deshalb weiterhin Windows-spezifische
Ansible-Module.

> **Hinweis:** Der klassische Ansible-Transport für Windows ist WinRM.
> Diese Variante wird am Ende des Tutorials erläutert und mit der hier
> verwendeten SSH-Lösung verglichen.

------------------------------------------------------------------------

## 1. Voraussetzungen

Auf der Windows-Maschine benötigen wir:

-   PowerShell,
-   OpenSSH Server,
-   einen Windows-Benutzer für den Ansible-Zugriff,
-   Netzwerkzugriff von der Control Node auf Port 22.

Die Control Node besitzt bereits das SSH-Schlüsselpaar der
Trainingsumgebung. Dieses verwenden wir auch für Windows.

Die PowerShell-Kommandos werden auf Windows in einer **PowerShell mit
Administratorrechten** ausgeführt, sofern nicht anders angegeben.

## 2. PowerShell prüfen

``` powershell
$PSVersionTable
```

Für Windows verwendet Ansible PowerShell. Für die üblichen
Windows-Module ist auf dem Managed Node kein Python erforderlich.

## 3. OpenSSH Server prüfen

``` powershell
Get-WindowsCapability -Online |
    Where-Object Name -Like 'OpenSSH.Server*'
```

Ist OpenSSH Server installiert, sollte `State : Installed` angezeigt
werden.

## 4. OpenSSH Server installieren

Falls erforderlich:

``` powershell
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

Danach erneut prüfen:

``` powershell
Get-WindowsCapability -Online |
    Where-Object Name -Like 'OpenSSH.Server*'
```

## 5. SSH-Dienst starten

``` powershell
Get-Service sshd
Start-Service sshd
Set-Service -Name sshd -StartupType Automatic
Get-Service sshd
```

Der Status sollte anschließend `Running` sein.

## 6. Firewall-Regel prüfen

OpenSSH verwendet standardmäßig TCP-Port 22.

``` powershell
Get-NetFirewallRule -Name OpenSSH-Server-In-TCP
```

Falls die Regel deaktiviert ist:

``` powershell
Enable-NetFirewallRule -Name OpenSSH-Server-In-TCP
```

Falls sie fehlt:

``` powershell
New-NetFirewallRule `
    -Name "OpenSSH-Server-In-TCP" `
    -DisplayName "OpenSSH Server (sshd)" `
    -Enabled True `
    -Direction Inbound `
    -Protocol TCP `
    -Action Allow `
    -LocalPort 22
```

Die Windows-Firewall wird nicht pauschal deaktiviert.

## 7. Windows-Benutzer festlegen

Wir verwenden für den SSH-Zugriff:

``` text
sl01
```

Prüfen:

``` powershell
Get-LocalUser -Name "sl01"
```

Administratorengruppe prüfen:

``` powershell
Get-LocalGroupMember -Group "Administrators"
```

Bei lokalisierten Windows-Versionen kann der Gruppenname abweichen:

``` powershell
Get-LocalGroup
```

## 8. IP-Adresse feststellen

``` powershell
Get-NetIPAddress -AddressFamily IPv4
```

Alternativ:

``` powershell
ipconfig
```

Im Beispiel verwenden wir `192.168.1.50`. Die tatsächliche Adresse muss
entsprechend eingesetzt werden.

## 9. Verbindung von der Control Node testen

Auf dem Docker-Host:

``` bash
docker compose exec control bash
```

Innerhalb der Control Node:

``` bash
ping -c 2 192.168.1.50
ssh sl01@192.168.1.50
```

Bei der ersten SSH-Verbindung wird der Host-Key nach Prüfung akzeptiert.
Danach erfolgt zunächst die Anmeldung mit dem Passwort von `sl01`.

## 10. Erste SSH-Sitzung

Auf Windows:

``` powershell
hostname
whoami
exit
```

Damit ist geprüft, dass Netzwerk, Port 22, OpenSSH Server und
Benutzeranmeldung funktionieren.

## 11. PowerShell als Standard-Shell für OpenSSH

Für Ansible soll PowerShell als SSH-Shell verwendet werden.

``` powershell
New-ItemProperty `
    -Path "HKLM:\SOFTWARE\OpenSSH" `
    -Name DefaultShell `
    -Value "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" `
    -PropertyType String `
    -Force

Restart-Service sshd
```

Danach erneut von der Control Node testen:

``` bash
ssh sl01@192.168.1.50
```

## 12. Vorhandenen Trainings-Key verwenden

Auf der Control Node:

``` bash
ls -l ~/.ssh
cat ~/.ssh/id_ed25519.pub
```

Wir verwenden das vorhandene Paar `id_ed25519` / `id_ed25519.pub`. Der
private Schlüssel bleibt auf der Control Node.

## 13. Public Key unter Windows hinterlegen

### Normaler Benutzer

Für einen normalen Benutzer liegt die Datei unter:

``` text
C:\Users\sl01\.ssh\authorized_keys
```

Als `sl01`:

``` powershell
New-Item -ItemType Directory -Force "$HOME\.ssh"
notepad "$HOME\.ssh\authorized_keys"
```

Dort wird der Inhalt von `~/.ssh/id_ed25519.pub` der Control Node
eingefügt.

### Administrator

Für Mitglieder der lokalen Administratorengruppe verwendet die
OpenSSH-Standardkonfiguration typischerweise:

``` text
C:\ProgramData\ssh\administrators_authorized_keys
```

Public Key eintragen:

``` powershell
notepad C:\ProgramData\ssh\administrators_authorized_keys
```

Berechtigungen entsprechend absichern, z. B.:

``` powershell
icacls.exe "C:\ProgramData\ssh\administrators_authorized_keys" /inheritance:r
icacls.exe "C:\ProgramData\ssh\administrators_authorized_keys" /grant "Administrators:F"
icacls.exe "C:\ProgramData\ssh\administrators_authorized_keys" /grant "SYSTEM:F"
```

Bei lokalisierten Windows-Versionen können Gruppennamen abweichen.

## 14. Public-Key-Anmeldung testen

``` bash
ssh sl01@192.168.1.50
ssh sl01@192.168.1.50 hostname
ssh sl01@192.168.1.50 whoami
```

Die Anmeldung sollte jetzt ohne Passwortabfrage funktionieren.

## 15. Windows-Collection prüfen

``` bash
ansible-galaxy collection list
```

Falls `ansible.windows` fehlt:

``` bash
ansible-galaxy collection install ansible.windows
```

Für die endgültige Trainingsumgebung sollte diese Abhängigkeit
reproduzierbar bereitgestellt werden.

## 16. Windows-Host ins Inventory aufnehmen

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

[physical_linux]
dockerhost ansible_host=host.docker.internal ansible_user=sl01

[physical_windows]
windows1 ansible_host=192.168.1.50 ansible_user=sl01

[physical_windows:vars]
ansible_connection=ssh
ansible_shell_type=powershell

[all:vars]
ansible_user=ansible
```

Die Docker-Nodes verwenden weiterhin `ansible`, die beiden realen Hosts
`sl01`.

## 17. Inventory prüfen

``` bash
ansible-inventory --graph
```

Sinngemäß:

``` text
@all:
  |--@physical_linux:
  |  |--dockerhost
  |--@physical_windows:
  |  |--windows1
  |--@training:
     |--@databases:
     |  |--db1
     |--@misc:
     |  |--misc1
     |--@webservers:
        |--web1
        |--web2
```

## 18. Windows mit Ansible testen

Linux:

``` bash
ansible web1 -m ansible.builtin.ping
```

Windows:

``` bash
ansible windows1 -m ansible.windows.win_ping
```

Erwartet:

``` text
windows1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

`win_ping` prüft, ob Ansible mit Windows kommunizieren und dort
PowerShell-Code ausführen kann.

## 19. Erstes Windows-Kommando

``` bash
ansible windows1 -m ansible.windows.win_command -a "whoami"
ansible windows1 -m ansible.windows.win_command -a "hostname"
```

## 20. PowerShell mit Ansible ausführen

``` bash
ansible windows1     -m ansible.windows.win_shell     -a "Get-Service | Select-Object -First 5"
```

Linux verwendet beispielsweise `ansible.builtin.command` und
`ansible.builtin.shell`, Windows dagegen `ansible.windows.win_command`
und `ansible.windows.win_shell`.

## 21. Windows Facts

``` bash
ansible windows1 -m ansible.builtin.setup
```

Gefiltert:

``` bash
ansible windows1     -m ansible.builtin.setup     -a "filter=ansible_os_family"
```

## 22. Linux- und Windows-Module

  -------------------------------------------------------------------------------------------
  Aufgabe                 Linux                               Windows
  ----------------------- ----------------------------------- -------------------------------
  Verbindung testen       `ansible.builtin.ping`              `ansible.windows.win_ping`

  Kommando                `ansible.builtin.command`           `ansible.windows.win_command`

  Shell                   `ansible.builtin.shell`             `ansible.windows.win_shell`

  Datei kopieren          `ansible.builtin.copy`              `ansible.windows.win_copy`

  Dienst verwalten        `ansible.builtin.systemd_service`   `ansible.windows.win_service`
  -------------------------------------------------------------------------------------------

``` text
                    SSH
                     |
              +------+------+
              |             |
            Linux         Windows
              |             |
           Python        PowerShell
              |             |
       Linux-Module    Windows-Module
```

## 23. Warum verwenden wir im Seminar SSH?

SSH hält den Transportmechanismus für die Trainingsumgebung einheitlich.
Die Teilnehmenden kennen bereits SSH, SSH-Keys,
Public-Key-Authentifizierung, Zielbenutzer und Inventory-Variablen.

Gleichzeitig zeigt Windows, dass ein identischer Transportweg nicht
bedeutet, dass Ansible auf allen Zielplattformen dieselben Module
verwendet.

------------------------------------------------------------------------

# Klassische Windows-Anbindung: WinRM

## 24. WinRM als klassischer Ansible-Weg

Windows wurde traditionell von Ansible über **WinRM -- Windows Remote
Management** verwaltet. Deshalb findet man in vielen Ansible-Anleitungen
und bestehenden Unternehmensumgebungen:

``` ini
[windows]
windows1 ansible_host=192.168.1.50

[windows:vars]
ansible_connection=winrm
ansible_user=sl01
```

WinRM basiert auf WS-Management.

Typische Ports:

``` text
5985  WinRM über HTTP
5986  WinRM über HTTPS
```

## 25. Authentifizierung bei WinRM

Je nach Umgebung kommen unter anderem NTLM, Kerberos, CredSSP oder
zertifikatsbasierte Verfahren infrage.

Beispiel für NTLM:

``` ini
[windows:vars]
ansible_connection=winrm
ansible_winrm_transport=ntlm
ansible_port=5985
```

In Active-Directory-Umgebungen ist insbesondere Kerberos relevant.

## 26. SSH und WinRM im Vergleich

  Eigenschaft                      SSH             WinRM
  -------------------------------- --------------- --------------------------
  Typischer Port                   22              5985 / 5986
  Linux                            Standard        unüblich
  Windows                          mit OpenSSH     klassischer Ansible-Weg
  Public-Key-Authentifizierung     typisch         nicht das übliche Modell
  NTLM/Kerberos                    nicht typisch   möglich
  PowerShell                       ja              ja
  Windows-Module                   ja              ja
  Einheitliches Trainingskonzept   sehr gut        zusätzlicher Transport

Die Wahl zwischen SSH und WinRM betrifft hauptsächlich Transport und
Authentifizierung. Windows-spezifische Ansible-Module werden in beiden
Fällen benötigt.

## 27. Wann ist WinRM weiterhin interessant?

WinRM ist insbesondere relevant, wenn

-   eine bestehende Windows-Infrastruktur bereits darauf basiert,
-   Active Directory und Kerberos eingesetzt werden,
-   Unternehmensrichtlinien WinRM vorgeben,
-   bestehende Ansible-Projekte WinRM verwenden,
-   OpenSSH Server auf den Windows-Systemen nicht vorgesehen ist.

Deshalb sollten Ansible-Anwender WinRM kennen, auch wenn wir es in
dieser Trainingsumgebung nicht als primären Transport verwenden.

## 28. Ergebnis

``` text
Ansible Control Node
        |
        | SSH
        |
        +-- training
        |     +-- web1       Linux
        |     +-- web2       Linux
        |     +-- db1        Linux
        |     +-- misc1      Linux
        |
        +-- physical_linux
        |     +-- dockerhost Ubuntu
        |
        +-- physical_windows
              +-- windows1   Windows
```

Der Transportweg bleibt in unserer Umgebung einheitlich:

``` text
SSH
```

Die Ausführung unterscheidet sich:

``` text
Linux                       Windows
  |                            |
Python                     PowerShell
  |                            |
Linux-Module              Windows-Module
```

WinRM bleibt als klassischer und in vielen Windows-Enterprise-Umgebungen
relevanter Ansible-Transport eine wichtige Alternative.
