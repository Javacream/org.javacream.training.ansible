message = 'Hello'
integer_number = 42
float_number = 47.11
output = f'Message: {message}, Integer: {integer_number}, Float: {float_number}'
print(output)

names_list = ['web1', 'db1', 'web1']
names_set = {'web1', 'db1', 'web1'}

for name in names_set:
    print(name)

if message == 'Hello':
    print('friendly')
else:
    print('formal')
