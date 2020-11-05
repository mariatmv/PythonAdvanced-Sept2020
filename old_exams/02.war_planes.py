def validate_position(direction, steps):
    if direction == 'right':
        if plane_position[1] + steps >= n:
            return False
    elif direction == 'left':
        if plane_position[1] - steps < 0:
            return False
    elif direction == 'up':
        if plane_position[0] - steps < 0:
            return False
    elif direction == 'down':
        if plane_position[0] + steps >= n:
            return False

    return True


n = int(input())
field = [input().split() for i in range(n)]
plane_position = []
total_targets = 0
for row in range(len(field)):
    for col in range(len(field[row])):
        if field[row][col] == 'p':
            plane_position.append(row)
            plane_position.append(col)
        elif field[row][col] == 't':
            total_targets += 1
m = int(input())
shot_targets = 0
for i in range(m):
    if shot_targets == total_targets:
        break
    args = input().split()
    command = args[0]
    direction = args[1]
    steps = int(args[2])
    if command == 'move':
        if validate_position(direction, steps):
            if direction == 'left':
                if field[plane_position[0]][plane_position[1] - steps] == '.':
                    field[plane_position[0]][plane_position[1]] = '.'
                    plane_position[1] -= steps
            if direction == 'right':
                if field[plane_position[0]][plane_position[1] + steps] == '.':
                    field[plane_position[0]][plane_position[1]] = '.'
                    plane_position[1] += steps
            if direction == 'up':
                if field[plane_position[0] - steps][plane_position[1]] == '.':
                    field[plane_position[0]][plane_position[1]] = '.'
                    plane_position[0] -= steps
            if direction == 'down':
                if field[plane_position[0] + steps][plane_position[1]] == '.':
                    field[plane_position[0]][plane_position[1]] = '.'
                    plane_position[0] += steps
    elif command == 'shoot':
        if validate_position(direction, steps):
            if direction == 'left':
                if field[plane_position[0]][plane_position[1] - steps] == 't':
                    shot_targets += 1
                field[plane_position[0]][plane_position[1] - steps] = 'x'
            elif direction == 'right':
                if field[plane_position[0]][plane_position[1] + steps] == 't':
                    shot_targets += 1
                field[plane_position[0]][plane_position[1] + steps] = 'x'
            elif direction == 'up':
                if field[plane_position[0] - steps][plane_position[1]] == 't':
                    shot_targets += 1
                field[plane_position[0] - steps][plane_position[1]] = 'x'
            elif direction == 'down':
                if field[plane_position[0] + steps][plane_position[1]] == 't':
                    shot_targets += 1
                field[plane_position[0] + steps][plane_position[1]] = 'x'

if shot_targets == total_targets:
    print(f'Mission accomplished! All {total_targets} targets destroyed.')
else:
    print(f'Mission failed! {total_targets - shot_targets} targets left.')

field[plane_position[0]][plane_position[1]] = 'p'
for row in field:
    print(' '.join(row))
