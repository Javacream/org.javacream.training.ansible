# Das Programm soll die Zeichenkette "Hello from Püthon" in die Datei out.txt schreiben
content = "Hello from Püthon"
with open('data/output.txt', 'wt', encoding='utf-8') as out_file:
    out_file.write(content)
