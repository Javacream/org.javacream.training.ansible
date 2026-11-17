# Ansible Collection `javacream.training`

Diese Collection enthält das Beispielmodul `node_executor`. Es ermittelt Hostname und Prozess-ID auf dem Managed Node, wartet 30 Sekunden und liefert die Ergebnisse über `exit_json()` zurück.

## Collection bauen

Auf der Control Node im Verzeichnis `/training`:

```bash
cd src/node/collection/javacream/training
ansible-galaxy collection build
```

Das Ergebnis ist `javacream-training-1.0.0.tar.gz`.

## Lokal installieren und testen

```bash
ansible-galaxy collection install javacream-training-1.0.0.tar.gz
cd /training
ansible web1 -m javacream.training.node_executor
ansible-doc javacream.training.node_executor
ansible-playbook src/node/collection/demo.yml
```

Alternativ kann die Collection direkt aus dem Quellverzeichnis genutzt werden, wenn sie unter einem konfigurierten Collection-Suchpfad mit der Struktur `ansible_collections/javacream/training` liegt.

## Auf Ansible Galaxy veröffentlichen (optional)

Die öffentliche Registry ist [Ansible Galaxy](https://galaxy.ansible.com/). Dort wird die gebaute Collection als Archiv veröffentlicht.

Voraussetzungen:
- Galaxy-Konto, berechtigter Namespace `javacream` und API-Token
- Passende, rechtlich geklärte Lizenz und geprüfte Metadaten in `galaxy.yml`
- Eine noch nicht veröffentlichte Versionsnummer

**Wichtig:** Der Namespace `javacream` ist ein Beispiel und muss auf Galaxy tatsächlich verfügbar sein beziehungsweise deinem Konto gehören. Die Angabe `MIT` in `galaxy.yml` ist ein Vorschlag; vor einer Veröffentlichung die gewünschte Lizenz bestätigen und die Lizenzdatei ergänzen.

API-Token lokal konfigurieren (nicht ins Git-Repository committen). In der verwendeten `ansible.cfg` können beispielsweise folgende Abschnitte ergänzt werden:

```ini
[galaxy]
server_list = release_galaxy

[galaxy_server.release_galaxy]
url = https://galaxy.ansible.com/
token = <GALAXY_API_TOKEN>
```

Anschließend im Collection-Verzeichnis:

```bash
ansible-galaxy collection build
ansible-galaxy collection publish javacream-training-1.0.0.tar.gz
```

Nach erfolgreichem Import kann die Collection von Galaxy installiert werden:

```bash
ansible-galaxy collection install javacream.training:1.0.0
```

Für weitere Veröffentlichungen die Versionsnummer in `galaxy.yml` erhöhen und das Archiv erneut bauen. Ein API-Token gehört weder in eine versionierte `ansible.cfg` noch in die Shell-History.

## Private Collection Registry

Für unternehmensinterne Collections eignen sich ein privater Automation Hub oder ein kompatibler Galaxy-/Pulp-Server. Dessen konkrete API-URL und Authentifizierung stellt der Betreiber bereit. Beispiel einer **lokalen**, nicht versionierten Konfiguration:

```ini
[galaxy]
server_list = private_hub

[galaxy_server.private_hub]
url = https://<SERVER>/api/galaxy/content/published/
token = <PRIVATE_HUB_TOKEN>
```

Je nach Produkt und Version kann die Veröffentlichungs-URL von der Installations-URL abweichen; deshalb die vom Betreiber dokumentierte URL für Uploads verwenden. Nach der Konfiguration:

```bash
ansible-galaxy collection publish javacream-training-1.0.0.tar.gz
ansible-galaxy collection install javacream.training:1.0.0
```

Die Veröffentlichung auf einer öffentlichen oder privaten Registry wird in dieser Schulungsumgebung **nicht automatisch ausgeführt**.

## Unterschied zum lokalen Modul

Ein einzelnes Modul kann mit `-M src/node/module` geladen werden. Eine Collection bündelt Module und weitere Ansible-Inhalte unter einem eindeutigen Namen (`javacream.training.node_executor`), ist versionierbar und als Archiv verteilbar.
