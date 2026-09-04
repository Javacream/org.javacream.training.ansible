hostnames_list = ["web1", "web2", "db1", "web1"]

# Ausgabe der gesamten Liste
print(hostnames_list)

# Indexzugriff
print(hostnames_list[1])

#Iteration
for hostname in hostnames_list:
    print(hostname)
print("Hugo")

hostnames_set = {"web1", "web2", "db1", "web1"}
print(hostnames_set)
#print(hostnames_set[1])
for hostname in hostnames_set:
    print(hostname)


from_1_to_3 = range(1,4)
for number in from_1_to_3:
    print(number)

print("__________________________")
List_length = len(hostnames_list) # Beispiel für einen prozeduralen Programmirstil
print(List_length)

hostnames_list.append("db2") # Beispiel für einen Objektorientierten Programmierstil
print(hostnames_list)


text = "Hello World"
print(len(text))

print(text.count("llo"))