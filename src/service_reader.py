with open ('data/services.txt', 'rt', encoding='utf-8') as service_file:
    content = service_file.read()
service_descriptions = content.split('\n')
service_dictionary = {}
for description in service_descriptions:
    if description.strip() != '':
        service_info = description.split(',')
        service_name = service_info[0]
        service_ip_address = service_info[1]
        service_port = int(service_info[2])
    service_dictionary[service_name] = (service_ip_address, service_port)
print(service_dictionary)    
