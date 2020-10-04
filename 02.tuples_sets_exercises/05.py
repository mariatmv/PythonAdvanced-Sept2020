phonebook = {}
while True:
    inp_str = input()
    if inp_str.isnumeric():
        break
    name, number = inp_str.split('-')
    phonebook[name] = number

n = int(inp_str)
for i in range(n):
    name = input()
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')
