# liste von ip-Addressen
ip_addresses = ['10.1.1.1', '10.1.2.2', '10.1.2.3']

# Dictionary von Namen und IP-Addressen
services = {'web1': ('10.1.1.1', 8080), 'db1': ('10.1.2.2', 6666), 'web2': ('10.1.2.3', 8080)}

# Zugriff auf Listenelement mit Index
element1 = ip_addresses[1]
print(element1)

# Zugriff auf Dictionary-Eintrag mit Key
key = 'web1'
service_ip = services[key]
port_for_web1 = service_ip[1]

print(f'Port for service key... is ...')