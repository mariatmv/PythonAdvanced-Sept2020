count_of_presents = int(input())
size_of_matrix = int(input())
matrix = []
happy_nice_kids = 0
for rows in range(size_of_matrix):
    row = input().split()
    matrix.append(row)

current_position = []
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 'S':
            current_position.append(row)
            current_position.append(col)
            matrix[row][col] = '-'
        if matrix[row][col] == 'V':
            happy_nice_kids += 1

while True:
    if count_of_presents < 1:
        break
    command = input()
    if command == 'Christmas morning':
        break

    if command == 'up':
        current_position[0] -= 1
    elif command == 'down':
        current_position[0] += 1
    elif command == 'right':
        current_position[1] += 1
    elif command == 'left':
        current_position[1] -= 1

    if matrix[current_position[0]][current_position[1]] == 'X':
        matrix[current_position[0]][current_position[1]] = '-'
    if matrix[current_position[0]][current_position[1]] == 'V':
        count_of_presents -= 1
        matrix[current_position[0]][current_position[1]] = '-'
    if matrix[current_position[0]][current_position[1]] == 'C':
        matrix[current_position[0]][current_position[1]] = '-'
        if matrix[current_position[0] - 1][current_position[1]] != '-':
            matrix[current_position[0] - 1][current_position[1]] = '-'
            count_of_presents -= 1
        if matrix[current_position[0] + 1][current_position[1]] != '-':
            matrix[current_position[0] + 1][current_position[1]] = '-'
            count_of_presents -= 1
        if matrix[current_position[0]][current_position[1] - 1] != '-':
            matrix[current_position[0]][current_position[1] - 1] = '-'
            count_of_presents -= 1
        if matrix[current_position[0]][current_position[1] + 1] != '-':
            matrix[current_position[0]][current_position[1] + 1] = '-'
            count_of_presents -= 1

if count_of_presents < 1:
    print("Santa ran out of presents!")

matrix[current_position[0]][current_position[1]] = 'S'
for row in matrix:
    print(' '.join(row), end=' \n')

not_enough = 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 'V':
            not_enough += 1

if not_enough > 0:
    print(f'No presents for {not_enough} nice kid/s.')
else:
    print(f'Good job, Santa! {happy_nice_kids} happy nice kid/s.')