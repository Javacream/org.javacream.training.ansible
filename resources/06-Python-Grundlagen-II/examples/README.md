# Beispiele für Block 6

## Lernziel und Einsatz

Python-Skripte mit Ansible ausführen. Zuerst Skripte aus Block 5 verstehen; danach die Playbooks in der Docker-Trainingsumgebung starten. Die Skriptdateien aus Block 5 müssen für die Playbooks bei Bedarf an den erwarteten relativen Pfad kopiert werden.

## Herkunft

Die Dateien in diesem Verzeichnis wurden unverändert aus dem Branch `bundesbank_2.9.2026` übernommen, ursprünglich unter `training-environment/ansible/playbooks/`. Die ursprüngliche Unterverzeichnisstruktur wurde erhalten.

## Voraussetzungen und Ausführung

- Docker-basierte Ansible-Trainingsumgebung aus `training-environment/` starten (`./setup.sh` bzw. `./setup.ps1`).
- Ansible-Playbooks in der Control Node mit `ansible-playbook <datei.yml>` ausführen; je nach Beispiel aus dem passenden Unterverzeichnis und mit passendem Inventory.
- Python-Dateien mit `python3 <datei.py>` ausführen, sofern sie eigenständig sind.
- Beispiele vor dem produktiven Seminareinsatz auf relative Pfade, erwartete Hosts, benötigte Dienste und Abhängigkeiten prüfen. Nicht alle Beispiele sind isoliert lauffähig.

## Status

Übernahme der Quelldateien erfolgt. Eine vollständige technische Ausführung und didaktische Überarbeitung stehen noch aus. Bestehende Handouts, Übungen, Musterlösungen und Trainerleitfäden wurden nicht verändert.
