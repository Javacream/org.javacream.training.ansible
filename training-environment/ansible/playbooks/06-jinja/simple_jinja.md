# Einfache Jinja-Ausdrücke

In den bisherigen Playbooks haben wir bereits mehrfach die Schreibweise

```text
{{ ... }}
```

verwendet.

Diese Syntax gehört zu **Jinja**. Ansible verwendet Jinja, um Werte in Playbooks einzusetzen und Ausdrücke auszuwerten.

Das Playbook `simple_jinja.yml` zeigt vier einfache Beispiele.

## Variablen einsetzen

```yaml
msg: "{{ name }}"
```

Ansible ersetzt `{{ name }}` durch den Wert der Variablen.

Bei

```yaml
name: Hugo
```

wird also ausgegeben:

```text
Hugo
```

## Ausdrücke auswerten

Innerhalb von `{{ ... }}` können auch Ausdrücke stehen:

```yaml
msg: "{{ number1 + number2 }}"
```

Bei

```yaml
number1: 10
number2: 5
```

ergibt das:

```text
15
```

## Zeichenketten zusammensetzen

Jinja-Ausdrücke können auch innerhalb eines Textes verwendet werden:

```yaml
msg: "Hallo {{ name }}"
```

Die Ausgabe lautet:

```text
Hallo Hugo
```

Das Prinzip ähnelt einem Python-f-String:

```python
name = "Hugo"

print(f"Hallo {name}")
```

In Ansible mit Jinja:

```yaml
msg: "Hallo {{ name }}"
```

## Filter verwenden

Jinja kann Werte mit sogenannten **Filtern** verändern.

Filter werden mit `|` angegeben:

```yaml
msg: "{{ name | upper }}"
```

Der Filter `upper` wandelt eine Zeichenkette in Großbuchstaben um.

Aus

```text
Hugo
```

wird:

```text
HUGO
```

Der grundsätzliche Aufbau ist:

```text
{{ Wert | Filter }}
```

Für den Einstieg reicht damit folgende Vorstellung:

```text
{{ variable }}                  Wert einsetzen
{{ number1 + number2 }}         Ausdruck auswerten
Hallo {{ name }}                Wert in Text einsetzen
{{ name | upper }}              Filter anwenden
```
