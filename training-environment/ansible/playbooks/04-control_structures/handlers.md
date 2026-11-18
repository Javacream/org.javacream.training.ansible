# Handler

Handler sind spezielle Tasks, die nur dann ausgeführt werden, wenn sie von einem anderen Task benachrichtigt wurden und dieser Task tatsächlich eine Änderung verursacht hat.

Ein typischer Anwendungsfall ist:

```text
Konfigurationsdatei ändern
          │
          ▼
      changed?
       /    \
     nein    ja
      │       │
      │       ▼
      │    Handler
      │       │
      │       ▼
      │   Dienst neu starten
      │
      ▼
   nichts
```

## Einen Handler benachrichtigen

Ein normaler Task kann mit `notify` einen Handler benachrichtigen:

```yaml
- name: Konfigurationsdatei kopieren
  ansible.builtin.copy:
    content: "example configuration\n"
    dest: /tmp/example.conf
  notify: Konfiguration neu laden
```

`notify` bedeutet dabei nicht, dass der Handler sofort ausgeführt wird.

Der Handler wird für eine spätere Ausführung vorgemerkt, wenn der Task den Status `changed` erhält.

## Handler definieren

Handler werden im Play unter `handlers:` definiert:

```yaml
handlers:
  - name: Konfiguration neu laden
    ansible.builtin.debug:
      msg: "Die Konfiguration wurde geändert und der Handler wird ausgeführt"
```

Der Name des Handlers wird von `notify` referenziert:

```yaml
notify: Konfiguration neu laden
```

und

```yaml
- name: Konfiguration neu laden
```

gehören also zusammen.

## Handler werden nur bei Änderungen ausgeführt

Das ist der entscheidende Unterschied zu einem normalen nachfolgenden Task.

Beim ersten Lauf existiert `/tmp/example.conf` noch nicht. Das `copy`-Modul erzeugt die Datei und meldet:

```text
changed
```

Dadurch wird der Handler benachrichtigt.

Beim nächsten Lauf entspricht die Datei bereits dem gewünschten Zustand. Das `copy`-Modul muss nichts verändern und meldet:

```text
ok
```

Der Handler wird dann nicht ausgeführt.

## Typischer Einsatz

Handler werden häufig verwendet, wenn eine Änderung eine weitere Aktion notwendig macht.

Ein typisches Beispiel ist eine Konfigurationsdatei eines Dienstes:

```text
Konfiguration unverändert
        │
        └── Dienst muss nicht neu gestartet werden

Konfiguration geändert
        │
        └── Handler startet den Dienst neu
```

Dadurch werden unnötige Aktionen vermieden.

## Zusammenhang mit deklarativem Arbeiten

Handler passen gut zum deklarativen Ansatz von Ansible.

Ein Task beschreibt zunächst den gewünschten Zustand. Nur wenn Ansible diesen Zustand tatsächlich ändern muss, wird über `notify` eine Folgeaktion ausgelöst.

Die wichtigsten Begriffe sind daher:

```text
notify       Handler benachrichtigen
handlers    Handler definieren
changed     Voraussetzung für die Benachrichtigung
```

## Vertiefung: Weitere eventartige Mechanismen

Handler sind der zentrale eventartige Mechanismus innerhalb normaler Ansible-Playbooks. Es gibt jedoch einige verwandte Konzepte.

### Mehrere Handler mit `listen`

Mit `listen` können mehrere Handler auf denselben logischen Namen reagieren.

Ein Task kann beispielsweise ein Ereignis melden:

```yaml
notify: configuration changed
```

Mehrere Handler können darauf reagieren:

```yaml
handlers:
  - name: Meldung ausgeben
    ansible.builtin.debug:
      msg: "Configuration changed"
    listen: configuration changed

  - name: Weitere Aktion ausführen
    ansible.builtin.debug:
      msg: "Another reaction"
    listen: configuration changed
```

Dadurch kann ein `notify` mehrere Reaktionen auslösen.

Vereinfacht:

```text
Task meldet Änderung
        │
        ▼
notify: configuration changed
        │
        ├──► Handler 1
        │
        └──► Handler 2
```

### `block`, `rescue` und `always`

Mit `block`, `rescue` und `always` kann auf Fehler bei der Ausführung von Tasks reagiert werden.

Das ähnelt einer ereignisgesteuerten Reaktion, gehört aber eher zum Exception Handling als zum Handler-Konzept.

### Callback-Plugins

Ansible besitzt außerdem Callback-Plugins. Diese können auf Ereignisse während einer Ansible-Ausführung reagieren, beispielsweise auf den Start, Erfolg oder Fehler eines Tasks.

Sie werden unter anderem für Logging und angepasste Ausgaben verwendet.

Callback-Plugins sind ein fortgeschrittenes Thema und werden hier nicht weiter behandelt.

### Event-Driven Ansible

Mit Event-Driven Ansible existiert darüber hinaus ein eigener Ansatz, bei dem externe Ereignisse Regeln und Aktionen auslösen können.

Auch dieses Thema geht über normale Playbooks hinaus und wird hier nur der Vollständigkeit halber erwähnt.

