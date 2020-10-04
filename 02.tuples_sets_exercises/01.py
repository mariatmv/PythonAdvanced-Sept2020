n = int(input())
names = []
for i in range(n):
    name = input()
    if name not in names:
        names.append(name)

print('\n'.join(names))