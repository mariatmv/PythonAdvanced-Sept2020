def is_invalid(command):
    if command == 'left':
        if current_position[1] + 1 < 0:
            return True
    elif command == 'right':
        if current_position[1] + 1 > n - 1:
            return True
    elif command == 'up':
        if current_position[0] - 1 < 0:
            return True
    elif command == 'down':
        if current_position[0] + 1 > n - 1:
            return True
    else:
        return False


n = int(input())
matrix = []
eaten_food = 0
last_is_invalid = False
for i in range(n):
    row = input()
    matrix.append(list(row))

current_position = []
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 'S':
            current_position.append(row)
            current_position.append(col)

while eaten_food < 10:
    command = input()
    if is_invalid(command):
        print('Game over!')
        last_is_invalid = True
        break

    matrix[current_position[0]][current_position[1]] = '.'
    if command == 'left':
        current_position[1] -= 1
    elif command == 'right':
        current_position[1] += 1
    elif command == 'up':
        current_position[0] -= 1
    elif command == 'down':
        current_position[0] += 1

    if matrix[current_position[0]][current_position[1]] == '*':
        eaten_food += 1
    elif matrix[current_position[0]][current_position[1]] == 'B':
        matrix[current_position[0]][current_position[1]] = '.'
        current_position = []
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 'B':
                    current_position.append(row)
                    current_position.append(col)
                    matrix[current_position[0]][current_position[1]] = '.'
    matrix[current_position[0]][current_position[1]] = '.'


if eaten_food >= 10:
    print('You won! You fed the snake.')

print(f'Food eaten: {eaten_food}')
if not last_is_invalid:
    matrix[current_position[0]][current_position[1]] = 'S'
for row in matrix:
    print(''.join(row))
