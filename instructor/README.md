# Hinweise für Trainerinnen und Trainer

Dieses Verzeichnis enthält die Trainerleitfäden und Musterlösungen zu den zwölf Seminarblöcken. Die Übungen für Teilnehmende liegen unter `resources/`.

## Git

### Musterlösung während des Seminars bereitstellen

Mit dem Git-Alias `solution` lässt sich die Musterlösung eines Blocks aus dem Branch `training` in das zugehörige Verzeichnis `resources/` des aktuell ausgecheckten Branches kopieren. Die Blocknummer wird zweistellig angegeben, beispielsweise `03`.

Den Alias **einmalig im lokalen Repository** einrichten (Bash bzw. POSIX-kompatible Shell):

```bash
git config alias.solution '!f() {
  dir=$(find resources -maxdepth 1 -type d -name "$1-*" -print -quit)
  if [ -z "$dir" ]; then
    echo "Block $1 nicht gefunden" >&2
    return 1
  fi
  git show "origin/training:instructor/${dir#resources/}/Musterloesung.ipynb" > "$dir/Musterloesung.ipynb"
}; f'
```

Vor dem ersten Einsatz den Remote-Tracking-Branch aktualisieren:

```bash
git fetch origin
```

Anschließend die gewünschte Musterlösung mit **einem Befehl** bereitstellen:

```bash
git solution 03
```

Beispielsweise wird dabei die Datei `instructor/03-Einfuehrung-in-Ansible/Musterloesung.ipynb` aus `origin/training` nach `resources/03-Einfuehrung-in-Ansible/Musterloesung.ipynb` im aktuellen Arbeitsverzeichnis kopiert. Weitere Aufrufe sind `git solution 01`, `git solution 07` und `git solution 12`.

**Wichtig:**

- Vorher den gewünschten Kunden-Branch auschecken; der Alias wechselt den Branch nicht selbst.
- Die Quelldatei wird aus `origin/training` gelesen; dieser Branch wird nicht verändert.
- Es wird nur die lokale Zieldatei angelegt beziehungsweise überschrieben. Ein Commit oder Push erfolgt nicht automatisch.
- Zum Veröffentlichen die Datei bei Bedarf mit `git add`, `git commit` und `git push` übernehmen.
- Der Alias ist lokal auf dieses Repository begrenzt und setzt `find` sowie eine POSIX-kompatible Shell voraus.
