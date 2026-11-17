# Das Programm soll die Zeichenkette "Hello from Püthon" in die Datei out.txt schreiben
content = "Hello from Püthon"
out_file = open('data/output.txt', 'wt', encoding='utf-8')
out_file.write(content)
out_file.close()