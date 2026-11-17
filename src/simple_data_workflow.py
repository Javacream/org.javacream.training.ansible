# liste von ip-Addressen
ip_addresses = ['10.1.1.1', '10.1.2.2', '10.1.2.3']

# Dictionary von Namen und IP-Addressen
services = {'web1': ('10.1.1.1', 8080), 'db1': ('10.1.2.2', 6666), 'web2': ('10.1.2.3', 8080)}

# Zugriff auf Listenelement mit Index
print(ip_addresses[1])

# Zugriff auf Dictionary-Eintrag mit Key

print(services['web1'][1])