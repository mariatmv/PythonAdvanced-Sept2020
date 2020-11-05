from _collections import deque


def is_successful(crafted_bombs):
    if crafted_bombs['Datura Bombs'] > 2 and crafted_bombs['Cherry Bombs'] > 2 and crafted_bombs['Smoke Decoy Bombs'] > 2:
        return True
    else:
        return False


bomb_effects = deque(map(int, input().split(', ')))
bomb_casings = [int(x) for x in input().split(', ')]
crafted_bombs = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
while len(bomb_effects) > 0:
    if len(bomb_casings) < 1 or is_successful(crafted_bombs):
        break

    sum = bomb_effects[0] + bomb_casings[-1]
    if sum == 40:
        crafted_bombs['Datura Bombs'] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif sum == 60:
        bomb_effects.popleft()
        bomb_casings.pop()
        crafted_bombs['Cherry Bombs'] += 1
    elif sum == 120:
        bomb_effects.popleft()
        bomb_casings.pop()
        crafted_bombs['Smoke Decoy Bombs'] += 1
    else:
        bomb_casings[-1] -= 5

if is_successful(crafted_bombs):
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print('You don\'t have enough materials to fill the bomb pouch.')

if len(bomb_effects) > 0:
    print(f'Bomb effects: {", ".join([str(x) for x in bomb_effects])}')
else:
    print('Bomb effects: empty')

if len(bomb_casings) > 0:
    print(f'Bomb casings: {", ".join([str(x) for x in bomb_casings])}')
else:
    print('Bomb casings: empty')

for k, v in sorted(crafted_bombs.items()):
    print(f'{k}: {v}')