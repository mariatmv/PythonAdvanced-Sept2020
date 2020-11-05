from _collections import deque
materials = [int(x) for x in input().split()]
magic_values = deque(map(int, input().split()))
crafted = {'Doll': 0, 'Wooden trait': 0, 'Teddy bear': 0, 'Bicycle': 0}
while materials:
    if len(magic_values) < 1:
        break

    if magic_values[0] == 0:
        magic_values.popleft()
    elif materials[-1] == 0:
        materials.pop()
    else:
        current_mul = magic_values[0] * materials[-1]
        if current_mul == 150:
            crafted['Doll'] += 1
            magic_values.popleft()
            materials.pop()
        elif current_mul == 250:
            crafted['Wooden trait'] += 1
            magic_values.popleft()
            materials.pop()
        elif current_mul == 300:
            crafted['Teddy bear'] += 1
            magic_values.popleft()
            materials.pop()
        elif current_mul == 400:
            crafted['Bicycle'] += 1
            magic_values.popleft()
            materials.pop()
        elif current_mul < 0:
            sum = magic_values[0] + materials[-1]
            magic_values.popleft()
            materials.pop()
            materials.append(sum)
        else:
            magic_values.popleft()
            materials[-1] += 15

if crafted['Doll'] > 0 and crafted['Wooden trait'] > 0:
    print('The presents are crafted! Merry Christmas!')
elif crafted['Teddy bear'] > 0 and crafted['Bicycle'] > 0:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if len(materials):
    print(f'Materials left: {", ".join([str(x) for x in reversed(materials)])}')
if len(magic_values):
    print(f'Magic left: {", ".join([str(x) for x in magic_values])}')

for k, v in sorted(crafted.items()):
    if v > 0:
        print(f'{k} : {v}')