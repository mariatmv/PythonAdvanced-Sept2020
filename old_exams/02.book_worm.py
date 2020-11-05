def remove_last_letter(new_string):
    if len(new_string) > 0:
        new_string = new_string[:-1]
    return new_string


initial_string = input()
new_string = ''
n = int(input())
matrix = []
current_position = []
for rows in range(n):
    row = input()
    matrix.append(list(row))

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 'P':
            current_position.append(row)
            current_position.append(col)
            matrix[row][col] = '-'

m = int(input())
for i in range(m):
    command = input()
    if command == 'up':
        if current_position[0] > 0:
            current_position[0] = current_position[0] - 1
            if matrix[current_position[0]][current_position[1]] == '-':
                continue
            new_string += matrix[current_position[0]][current_position[1]]
            matrix[current_position[0]][current_position[1]] = '-'
        else:
            new_string = remove_last_letter(new_string)
    elif command == 'down':
        if current_position[0] < n:
            current_position[0] = current_position[0] + 1
            if matrix[current_position[0]][current_position[1]] == '-':
                continue
            new_string += matrix[current_position[0]][current_position[1]]
            matrix[current_position[0]][current_position[1]] = '-'
        else:
            new_string = remove_last_letter(new_string)
    elif command == 'left':
        if current_position[1] > 0:
            current_position[1] = current_position[1] - 1
            if matrix[current_position[0]][current_position[1]] == '-':
                continue
            new_string += matrix[current_position[0]][current_position[1]]
            matrix[current_position[0]][current_position[1]] = '-'
        else:
            new_string = remove_last_letter(new_string)
    elif command == 'right':
        if current_position[1] < n:
            current_position[1] = current_position[1] + 1
            if matrix[current_position[0]][current_position[1]] == '-':
                continue
            new_string += matrix[current_position[0]][current_position[1]]
            matrix[current_position[0]][current_position[1]] = '-'
        else:
            new_string = remove_last_letter(new_string)

print(initial_string + new_string)
matrix[current_position[0]][current_position[1]] = 'P'
for row in matrix:
    print(''.join(row))