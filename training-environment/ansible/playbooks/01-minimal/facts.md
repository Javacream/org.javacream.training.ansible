# Ansible Facts

## Was sind Facts?

Beim Start eines Plays sammelt Ansible standardmäßig Informationen über die angesprochenen **Managed Nodes**. Diese Informationen werden als **Facts** bezeichnet.

Facts beschreiben Eigenschaften des jeweiligen Managed Nodes, beispielsweise:

- Hostname
- Betriebssystem und Version
- Prozessorarchitektur
- Arbeitsspeicher
- Netzwerkschnittstellen
- IP-Adressen

Ansible kann diese Informationen später innerhalb eines Playbooks verwenden.

### Warum sind Facts wichtig?

Ein Playbook soll häufig auf unterschiedlichen Systemen funktionieren. Dabei kann es notwendig sein, auf verschiedenen Managed Nodes unterschiedliche Aktionen auszuführen.

Durch die Facts „weiß“ das Playbook, **auf welchem System es gerade arbeitet und was dort ausgeführt werden soll bzw. kann**.

Ein typisches Beispiel ist die Installation von Software. Verschiedene Linux-Distributionen verwenden unterschiedliche Paketmanager. Beispielsweise kommen auf Debian- und Ubuntu-Systemen typischerweise `apt` und auf Red-Hat-basierten Systemen `dnf` zum Einsatz.

Ein Playbook kann mithilfe der Facts zunächst feststellen, welche Linux-Distribution auf einem Managed Node installiert ist. Abhängig davon kann es anschließend die für dieses System geeigneten Aktionen ausführen.

Vereinfacht dargestellt:

```text
Managed Node
     │
     ├── Ubuntu  ──→ apt
     │
     └── Fedora  ──→ dnf
```

Die Facts liefern dem Playbook also Informationen über den Managed Node. Diese Informationen können später verwendet werden, um **Entscheidungen über die auszuführenden Aktionen zu treffen**.

Facts sind damit eine wichtige Grundlage dafür, Playbooks portabel und an unterschiedliche Managed Nodes anpassbar zu gestalten.

## Gathering Facts

Betrachten wir unser minimales Playbook:

```yaml
---
- name: Minimales Play
  hosts: all
```

Das Playbook enthält keine von uns definierten Tasks.

Trotzdem erscheint bei der Ausführung

```bash
ansible-playbook minimal.yml
```

in der Ausgabe ein Task mit dem Namen:

```text
TASK [Gathering Facts]
```

Ansible sammelt die Facts automatisch **zu Beginn eines Plays**, bevor die von uns definierten Tasks ausgeführt werden.

Deshalb führt bereits unser minimales Playbook eine Aktion auf den Managed Nodes aus.

## Das Modul `setup`

Für das Sammeln der Facts verwendet Ansible das Modul

```text
ansible.builtin.setup
```

Wir können dieses Modul auch mit einem Ad-hoc-Kommando explizit aufrufen:

```bash
ansible all -m setup
```

Dadurch erhalten wir die von Ansible ermittelten Facts für die Hosts unseres Inventories.

Da die Menge der Informationen recht groß ist, kann man die Ausgabe beispielsweise mit einem Filter einschränken:

```bash
ansible all -m setup -a "filter=ansible_distribution"
```

Damit lässt sich beispielsweise die erkannte Linux-Distribution anzeigen.

## Fact Gathering deaktivieren

Nicht jedes Playbook benötigt Informationen über die Managed Nodes. Das automatische Sammeln kann deshalb für ein Play deaktiviert werden:

```yaml
---
- name: Minimales Play
  hosts: all
  gather_facts: false
```

Bei der Ausführung erscheint nun kein `Gathering Facts` mehr.

## Wichtig

`Gathering Facts` ist kein Task, den wir in unserem Playbook definiert haben. Ansible führt diesen Schritt standardmäßig selbst aus.

Damit können auch Playbooks ohne einen eigenen `tasks`-Abschnitt bereits Aktionen auf den Managed Nodes ausführen.

Die gesammelten Facts ermöglichen es später, die Ausführung eines Playbooks **von den Eigenschaften des jeweiligen Managed Nodes abhängig zu machen**.
