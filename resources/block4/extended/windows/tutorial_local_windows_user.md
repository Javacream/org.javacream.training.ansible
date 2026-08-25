# Tutorial: Lokalen Windows-Benutzer mit Administratorrechten anlegen

## Ziel

Auf dem Windows-System wird der lokale Benutzer `sl01` angelegt und anschließend der lokalen Administratorengruppe hinzugefügt. Er ist für die Ansible-Trainingsumgebung vorgesehen und kann später per SSH vom Ansible Control Node verwendet werden.

> Die administrativen Befehle werden in einer **PowerShell als Administrator** ausgeführt.

## 1. Prüfen, ob der Benutzer bereits existiert

```powershell
Get-LocalUser -Name "sl01"
```

Alle lokalen Benutzer:

```powershell
Get-LocalUser
```

## 2. Kennwortrichtlinie prüfen

```powershell
net accounts
```

Für zusätzliche Werte einschließlich der Komplexitätsanforderung:

```powershell
secedit /export /cfg "$env:TEMP\secpol.cfg"

Select-String `
    -Path "$env:TEMP\secpol.cfg" `
    -Pattern "PasswordComplexity|MinimumPasswordLength|PasswordHistorySize|MaximumPasswordAge|MinimumPasswordAge"
```

Dabei bedeutet insbesondere:

- `PasswordComplexity = 1`: Komplexitätsanforderungen aktiviert
- `PasswordComplexity = 0`: Komplexitätsanforderungen deaktiviert
- `MinimumPasswordLength`: Mindestlänge des Kennworts
- `PasswordHistorySize`: Anzahl berücksichtigter früherer Kennwörter

Grafisch:

```powershell
secpol.msc
```

Auf einem deutschen Windows: **Kontorichtlinien → Kennwortrichtlinien**.

## 3. Kennwort sicher einlesen

Das Kennwort sollte nicht als Klartext im Befehl stehen:

```powershell
$Password = Read-Host "Passwort für sl01" -AsSecureString
```

## 4. Benutzer anlegen

```powershell
New-LocalUser `
    -Name "sl01" `
    -Password $Password `
    -FullName "Ansible Training User" `
    -Description "Benutzer für das Ansible-Training"
```

Kontrolle:

```powershell
Get-LocalUser -Name "sl01"
```

## 5. Administratorengruppe sprachunabhängig bestimmen

Der Gruppenname ist sprachabhängig (`Administratoren` bzw. `Administrators`). Die SID der eingebauten Administratorengruppe ist dagegen eindeutig:

```text
S-1-5-32-544
```

Deshalb:

```powershell
$AdminGroup = Get-LocalGroup -SID "S-1-5-32-544"
$AdminGroup
```

## 6. `sl01` Administratorrechte geben

```powershell
Add-LocalGroupMember `
    -Group $AdminGroup.Name `
    -Member "sl01"
```

Kontrolle:

```powershell
Get-LocalGroupMember -Group $AdminGroup.Name
```

## 7. Anmeldung über SSH testen

Vom Ansible Control Node:

```bash
ssh sl01@<windows-ip>
```

Nach erfolgreicher Anmeldung:

```powershell
whoami
```

Beispiel:

```text
meinrechner\sl01
```

Gruppenmitgliedschaften:

```powershell
whoami /groups
```

## 8. Kennwort später zurücksetzen

Sicher über PowerShell:

```powershell
$Password = Read-Host "Neues Passwort" -AsSecureString
Set-LocalUser -Name "sl01" -Password $Password
```

Oder interaktiv:

```powershell
net user sl01 *
```

Nicht empfehlenswert ist ein Kennwort im Klartext auf der Befehlszeile.

## 9. Besonderheit für die spätere SSH-Key-Authentifizierung

Für normale Benutzer liegt `authorized_keys` typischerweise hier:

```text
C:\Users\sl01\.ssh\authorized_keys
```

Da `sl01` Mitglied der lokalen Administratorengruppe ist, verwendet eine typische Windows-OpenSSH-Standardkonfiguration für Administratoren stattdessen:

```text
C:\ProgramData\ssh\administrators_authorized_keys
```

Das wird beim nächsten Schritt – der Public-Key-Authentifizierung – relevant.

## 10. Kompletter Ablauf kompakt

```powershell
$Password = Read-Host "Passwort für sl01" -AsSecureString

New-LocalUser `
    -Name "sl01" `
    -Password $Password `
    -FullName "Ansible Training User" `
    -Description "Benutzer für das Ansible-Training"

$AdminGroup = Get-LocalGroup -SID "S-1-5-32-544"

Add-LocalGroupMember `
    -Group $AdminGroup.Name `
    -Member "sl01"

Get-LocalUser -Name "sl01"
Get-LocalGroupMember -Group $AdminGroup.Name
```

## Ergebnis

Der Windows-Rechner besitzt jetzt einen lokalen Benutzer `sl01`, der:

- ein lokales Windows-Konto besitzt,
- ein Kennwort gemäß der lokalen Password Policy verwendet,
- Mitglied der lokalen Administratorengruppe ist,
- per SSH verwendet werden kann,
- später als Ansible-Benutzer des Windows Managed Node dienen kann.

Als nächster Schritt kann die **SSH-Public-Key-Authentifizierung für `sl01`** eingerichtet werden.
