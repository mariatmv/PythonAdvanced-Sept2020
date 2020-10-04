n = int(input())
chemicals = set()
for i in range(n):
    t = tuple(input().split())
    for j in t:
        chemicals.add(j)

print('\n'.join(chemicals))