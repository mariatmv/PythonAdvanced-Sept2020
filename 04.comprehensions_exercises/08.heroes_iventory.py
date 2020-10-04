d = {i: [[],0] for i in input().split(', ')}
cmd = input()
while cmd != 'End':
    name, item, cost = cmd.split('-')
    if item not in d[name][0]:
        d[name][0].append(item)
        d[name][1] += int(cost)
    cmd = input()

for k, v in d.items():
    print(f'{k} -> Items: {len(v[0])}, Cost: {v[1]}')