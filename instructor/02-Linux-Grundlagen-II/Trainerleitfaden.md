# Trainerleitfaden – Block 2: Linux-Grundlagen II – Administration und einfache Automatisierung

## 1. Zielsetzung des Blocks

Block 2 erweitert die in Block 1 erworbenen Linux-Grundlagen um typische administrative Aufgaben und führt erstmals einfache Automatisierung mit Shell-Skripten ein.

Die Teilnehmenden sollen verstehen, wie Software installiert, Prozesse und Dienste verwaltet, Netzwerkverbindungen geprüft und entfernte Linux-Systeme über SSH erreicht werden. Shell-Skripte dienen dabei nicht als zweite Programmiersprache neben Python, sondern als einfaches Mittel, vorhandene Programme und Kommandos zu einem reproduzierbaren Ablauf zu verbinden.

Der Block bereitet damit unmittelbar die Einführung in Ansible vor: Viele Aufgaben, die hier noch manuell oder mit einfachen Shell-Skripten ausgeführt werden, werden später mit Ansible auf mehrere Systeme übertragen.

---

## 2. Lernziele

Nach Abschluss des Blocks können die Teilnehmenden:

- das Grundprinzip von Linux-Paketmanagement erklären,
- Pakete mit einem Paketmanager suchen, installieren und entfernen,
- laufende Prozesse anzeigen und Prozesse gezielt beenden,
- Dienste mit `systemctl` prüfen, starten, stoppen und neu starten,
- grundlegende Netzwerkparameter und Erreichbarkeit prüfen,
- den Zweck von Hostnamen, IP-Adressen und Ports erklären,
- sich per SSH mit einem entfernten Linux-System verbinden,
- den Unterschied zwischen Passwort- und Public-Key-Authentifizierung erklären,
- ein SSH-Schlüsselpaar erzeugen und einen öffentlichen Schlüssel für eine Anmeldung verwenden,
- einfache Shell-Skripte mit Befehlssequenzen, Variablen, Exit Codes und einfachen Bedingungen erstellen,
- Shell-Skripte als Orchestrierung mehrerer vorhandener Programme einsetzen.

---

## 3. Paketmanagement

### Inhalt

Zu behandeln sind:

- Zweck eines Paketmanagers
- Paketquellen bzw. Repositories
- Installation, Aktualisierung und Entfernen von Software
- Paketmetadaten
- Abhängigkeiten

Als praktisches Beispiel sollte der in der Schulungsumgebung verwendete Paketmanager eingesetzt werden.

Für Debian-/Ubuntu-basierte Systeme:

- `apt update`
- `apt install`
- `apt remove`
- `apt search`
- `apt show`

Als Überblick:

- `dnf`
- `yum`

### Didaktischer Hinweis

Es genügt nicht, einzelne Befehle zu zeigen. Die Teilnehmenden sollten verstehen, dass ein Paketmanager Software nicht einfach aus einer beliebigen Quelle herunterlädt, sondern mit konfigurierten Paketquellen und Paketmetadaten arbeitet.

`apt` sollte nicht gleichzeitig mit `dnf` oder `yum` praktisch geübt werden. Ein Paketmanager wird praktisch verwendet, die anderen werden lediglich konzeptionell eingeordnet.

### Demonstration

Der Trainer:

1. aktualisiert die Paketinformationen,
2. sucht ein ungefährliches kleines Paket,
3. zeigt dessen Informationen,
4. installiert es,
5. prüft die Installation,
6. entfernt es wieder.

### Übung

Die Teilnehmenden suchen ein vorgegebenes Paket, prüfen dessen Informationen und installieren es in der Schulungsumgebung. Anschließend überprüfen sie, ob das zugehörige Programm verfügbar ist.

Falls administrative Rechte erforderlich sind, wird `sudo` aus Block 1 wieder aufgegriffen.

### Typische Schwierigkeiten

- Verwechslung von `apt update` und einem eigentlichen Paket-Upgrade
- Annahme, dass ein Paketname immer dem Programmnamen entspricht
- fehlende administrative Berechtigungen
- Verwechslung von Paketinstallation und Start eines Dienstes

---

## 4. Prozesse verwalten

### Inhalt

Zu behandeln sind:

- Programm und Prozess
- Prozess-ID (PID)
- Eltern- und Kindprozesse
- laufende Prozesse anzeigen
- Prozesse gezielt beenden

Wichtige Befehle:

- `ps`
- `ps aux`
- `pgrep`
- `kill`

Optional zur Veranschaulichung:

- `top`

### Trainerhinweis

Signale sollten nur so weit behandelt werden, wie sie für das Verständnis von `kill` notwendig sind. Eine vollständige Behandlung der POSIX-Signale gehört nicht in diesen Block.

Der Unterschied zwischen regulärem Beenden und erzwungenem Beenden sollte angesprochen werden. `kill -9` sollte ausdrücklich nicht als Standardlösung vermittelt werden.

### Demonstration

Der Trainer startet einen einfachen länger laufenden Prozess, ermittelt dessen PID und beendet ihn anschließend gezielt.

### Übung

Die Teilnehmenden starten einen ungefährlichen Testprozess, finden ihn mit geeigneten Werkzeugen und beenden ihn anschließend.

### Typische Schwierigkeiten

- PID mit Portnummer oder Benutzer-ID verwechseln
- ungeprüft mehrere Prozesse beenden
- sofortige Verwendung von `kill -9`
- Prozessname und ausführbare Datei gleichsetzen

---

## 5. Dienste mit systemd verwalten

### Inhalt

Einführung in:

- Hintergrunddienste
- systemd
- Units
- Service Units

Wichtige Kommandos:

- `systemctl status`
- `systemctl start`
- `systemctl stop`
- `systemctl restart`
- `systemctl reload`
- `systemctl enable`
- `systemctl disable`
- `systemctl is-active`
- `systemctl is-enabled`

### Didaktischer Hinweis

Besonders wichtig ist die Trennung von:

- aktuell laufendem Zustand
- Verhalten beim Systemstart

`start` und `enable` dürfen nicht synonym behandelt werden.

### Demonstration

An einem ungefährlichen Dienst zeigt der Trainer:

- Status prüfen
- Dienst stoppen und starten
- Neustart
- Aktivierungsstatus prüfen

### Übung

Die Teilnehmenden untersuchen einen vorgegebenen Dienst und beantworten:

- Läuft der Dienst?
- Ist er für den Systemstart aktiviert?
- Wie wird er neu gestartet?
- Wie kann der aktuelle Status automatisiert geprüft werden?

### Ausblick auf Ansible

Der Trainer kann darauf hinweisen, dass das spätere Ansible-Modul `service` bzw. systemd-bezogene Module denselben administrativen Zustand deklarativ verwalten können.

Es wird noch kein Ansible-Code gezeigt.

---

## 6. Netzwerkgrundlagen

### Inhalt

Zu behandeln sind:

- Hostname
- IP-Adresse
- IPv4-Grundidee
- lokale und entfernte Systeme
- Ports als Endpunkte von Diensten
- Erreichbarkeit und Dienstverfügbarkeit als unterschiedliche Fragestellungen

Geeignete Werkzeuge:

- `hostname`
- `hostname -I`
- `ip addr`
- `ip route`
- `ping`
- optional `ss`

### Trainerhinweis

Der Netzwerkanteil soll keine allgemeine Netzwerkschulung werden. Es geht ausschließlich um das Wissen, das für SSH, Remote-Administration und später Ansible benötigt wird.

Insbesondere sollte herausgestellt werden:

`ping` prüft nicht, ob ein bestimmter Anwendungsdienst verfügbar ist.

### Demonstration

Der Trainer zeigt:

- Hostname
- lokale IP-Adresse
- Routinginformation
- Erreichbarkeit eines Zielsystems
- optional einen lokal geöffneten Port

### Übung

Die Teilnehmenden ermitteln:

- eigenen Hostnamen,
- eigene IP-Adresse,
- Standardroute,
- Erreichbarkeit eines vorgegebenen Zielsystems.

### Typische Schwierigkeiten

- Hostname und IP-Adresse gleichsetzen
- Erreichbarkeit per `ping` mit Verfügbarkeit eines Dienstes gleichsetzen
- lokale Adresse und Standardgateway verwechseln

---

## 7. SSH – Remote-Zugriff

### Inhalt

Zu behandeln sind:

- Zweck von SSH
- Client und Server
- SSH-Verbindung
- Benutzername
- Hostname bzw. IP-Adresse
- Standardport 22
- Host-Key-Prüfung
- Remote-Shell

Grundlegender Aufruf:

- `ssh user@host`

Optional:

- expliziter Port mit `-p`

### Demonstration

Der Trainer verbindet sich mit einem vorbereiteten Managed Host.

Dabei sollte sichtbar werden:

- Benutzername des lokalen Systems
- Benutzername des Remote-Systems
- Hostname vor und nach der Anmeldung
- Beenden der Remote-Sitzung

### Übung

Die Teilnehmenden verbinden sich mit einem bereitgestellten Zielsystem, prüfen dort Benutzer und Hostnamen und verlassen anschließend die SSH-Sitzung korrekt.

### Typische Schwierigkeiten

- lokaler und entfernter Benutzer werden verwechselt
- Hostname des Zielsystems wird mit dem Benutzernamen verwechselt
- unbekannter Host Key wird unreflektiert bestätigt
- Remote-Sitzung und lokale Shell werden verwechselt

---

## 8. SSH-Keys und Public-Key-Authentifizierung

### Inhalt

Zu behandeln sind:

- Schlüsselpaar
- privater Schlüssel
- öffentlicher Schlüssel
- Bedeutung des privaten Schlüssels
- Public-Key-Authentifizierung
- `~/.ssh`
- `authorized_keys`

Geeignete Werkzeuge:

- `ssh-keygen`
- `ssh-copy-id` oder alternative kontrollierte Bereitstellung des Public Keys

### Sicherheitsgrundsatz

Der private Schlüssel wird niemals auf den Zielserver kopiert oder weitergegeben.

### Demonstration

Der Trainer:

1. erzeugt ein SSH-Schlüsselpaar,
2. betrachtet die erzeugten Dateien,
3. erklärt privaten und öffentlichen Schlüssel,
4. installiert den öffentlichen Schlüssel auf einem Zielsystem,
5. meldet sich anschließend per Schlüssel an.

### Übung

Die Teilnehmenden erzeugen ein eigenes Schlüsselpaar für die Schulungsumgebung und richten die Anmeldung an einem vorbereiteten Zielsystem ein.

### Ausblick auf Ansible

Dieser Abschnitt ist eine direkte Voraussetzung für Block 3 und 4. Ansible nutzt typischerweise SSH für die Kommunikation mit Managed Nodes und kann dadurch dieselbe Authentifizierungsinfrastruktur verwenden.

---

## 9. Grundlagen einfacher Shell-Skripte

### Zielsetzung

Shell-Scripting wird bewusst nur in dem Umfang behandelt, der für einfache Prozess- und Pipeline-artige Abläufe notwendig ist.

Nicht Ziel dieses Blocks sind:

- komplexe Bash-Programmierung,
- Funktionen,
- Arrays,
- umfangreiche Schleifen,
- fortgeschrittene Parameterexpansion.

Diese Art eigener Programmlogik wird später mit Python behandelt.

### Inhalt

Zu behandeln sind:

- Textdatei als Skript
- Shebang
- Ausführungsrecht
- Skript direkt oder über die Shell ausführen
- Befehlssequenzen
- Kommentare
- einfache Variablen
- Quotierung von Variablen
- Exit Codes
- `$?`
- logische Verkettung mit `&&`
- einfache `if`-Bedingungen

### Demonstration

Der Trainer entwickelt schrittweise ein kleines Skript:

1. mehrere Befehle nacheinander,
2. Wert in einer Variablen,
3. Rückgabewert eines Kommandos prüfen,
4. einen Folgeschritt nur bei Erfolg ausführen.

### Didaktischer Hinweis

Im Mittelpunkt steht die Frage:

**Wie kann eine Folge bereits existierender Programme reproduzierbar ausgeführt werden?**

Die Shell übernimmt hier primär Orchestrierung. Eigene komplexere Logik wird später bewusst Python zugeordnet.

---

## 10. Exit Codes und Fehlerbehandlung in einfachen Abläufen

### Inhalt

Zu behandeln sind:

- Exit Code `0` als Erfolg
- von `0` verschiedene Werte als Fehler bzw. besondere Zustände
- `$?`
- `&&`
- `if command; then ... fi`

Optional:

- `||`

### Demonstration

Der Trainer führt ein erfolgreiches und ein fehlschlagendes Kommando aus und zeigt jeweils den Exit Code.

Danach wird ein Folgekommando nur dann ausgeführt, wenn der vorherige Schritt erfolgreich war.

### Übung

Die Teilnehmenden erstellen ein kleines Shell-Skript, das:

- einen ersten Arbeitsschritt ausführt,
- dessen Erfolg prüft,
- nur bei Erfolg einen weiteren Arbeitsschritt startet,
- bei einem Fehler eine verständliche Meldung ausgibt.

### Typische Schwierigkeiten

- Ausgabe eines Programms mit dessen Exit Code verwechseln
- `$?` zu spät auslesen und damit den Exit Code eines anderen Befehls erhalten
- erfolgreiche Ausführung mit fachlich korrektem Ergebnis gleichsetzen

---

## 11. Shell als Orchestrierung mehrerer Programme

### Inhalt

Mehrere Werkzeuge werden zu einem Ablauf kombiniert.

Geeignete Kategorien sind beispielsweise:

- Dateioperation
- Aufruf eines Versionsverwaltungswerkzeugs
- Ausführung eines Python-Programms
- anschließende Prüfung eines Zielsystems

Entscheidend ist nicht ein bestimmtes Beispiel, sondern das Muster:

1. Werkzeug A ausführen
2. Erfolg prüfen
3. Werkzeug B ausführen
4. Ergebnis prüfen
5. optional Werkzeug C ausführen

### Didaktischer Hinweis

Hier sollte ausdrücklich die spätere Abgrenzung vorbereitet werden:

- Shell: vorhandene Werkzeuge zu Abläufen verbinden
- Python: eigene Programmlogik implementieren
- Ansible: gewünschte Zustände auf Systemen automatisiert herstellen

Dabei muss ebenso klar sein, dass Ansible nicht voraussetzt, dass Anwender eigene Python-Skripte schreiben.

---

## 12. Abschlussübung

Die Abschlussübung verbindet die administrativen und automatisierungsbezogenen Inhalte des Blocks.

Sie sollte folgende Elemente enthalten:

- Paket bzw. vorhandenes Programm überprüfen,
- Prozess oder Dienst untersuchen,
- Netzwerkparameter ermitteln,
- Erreichbarkeit eines Zielsystems prüfen,
- SSH-Verbindung zu einem entfernten System herstellen,
- mindestens einen Remote-Befehl ausführen,
- einen einfachen Ablauf als Shell-Skript zusammenfassen,
- Erfolg eines Schrittes über dessen Exit Code prüfen,
- Folgeschritt nur bei erfolgreicher Ausführung starten.

Die Aufgabe sollte Anforderungen formulieren und möglichst wenig konkrete Befehle vorgeben.

---

## 13. Typische Fragen und Fehler

Der Trainer sollte insbesondere mit folgenden Punkten rechnen:

- Paketmanager und Paketquelle werden verwechselt
- `apt update` wird als Software-Upgrade verstanden
- Prozess und Dienst werden gleichgesetzt
- PID und Portnummer werden verwechselt
- `systemctl start` und `systemctl enable` werden verwechselt
- `ping` wird als Test eines konkreten Dienstes verstanden
- lokale und entfernte Shell werden verwechselt
- privater und öffentlicher SSH-Schlüssel werden verwechselt
- privater Schlüssel wird fälschlicherweise auf den Server kopiert
- Skript ist wegen fehlendem Execute-Bit nicht direkt ausführbar
- Shebang wird mit einem Kommentar ohne Bedeutung verwechselt
- Ausgabe eines Kommandos und Exit Code werden verwechselt
- `$?` wird nicht unmittelbar nach dem relevanten Kommando ausgewertet

---

## 14. Überleitung zu Block 3

Block 2 endet mit einer wichtigen Beobachtung:

Die Teilnehmenden können nun Linux-Systeme lokal und per SSH administrieren und einzelne Abläufe mit Shell-Skripten reproduzierbar machen.

Bei mehreren Zielsystemen entstehen jedoch schnell neue Probleme:

- derselbe Befehl muss auf vielen Hosts ausgeführt werden,
- Systeme können unterschiedliche Zustände haben,
- Änderungen sollen reproduzierbar sein,
- Fehler auf einzelnen Hosts müssen sichtbar bleiben,
- Konfigurationen sollen zentral verwaltet werden.

Damit ergibt sich die Leitfrage für Block 3:

**Wie können wir solche administrativen Aufgaben zentral, wiederholbar und auf mehrere Linux-Systeme verteilt automatisieren?**

An dieser Stelle wird Ansible als nächster Automatisierungsschritt eingeführt.
