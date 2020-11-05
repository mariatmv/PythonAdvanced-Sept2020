size_of_matrix = int(input())
matrix = [[''] * size_of_matrix for i in range(size_of_matrix)]
bombs = int(input())
for i in range(bombs):
    current_bomb = list(map(int, input().strip('()').split(', ')))
    if 0 <= current_bomb[0] <= size_of_matrix and 0 <= current_bomb[1] <= size_of_matrix:
        matrix[current_bomb[0]][current_bomb[1]] = '*'

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] != '*':
            current_sum = 0
            current_cordinates = [row, col]
            if row > 0:
                if matrix[row - 1][col] == '*':
                    current_sum += 1
                if col > 0:
                    if matrix[row-1][col-1] == '*':
                        current_sum += 1
                if col < size_of_matrix - 1:
                    if matrix[row-1][col+1] == '*':
                        current_sum += 1
            if row < size_of_matrix - 1:
                if matrix[row+1][col] == '*':
                    current_sum += 1
                if col > 0:
                    if matrix[row+1][col-1] == '*':
                        current_sum += 1
                if col < size_of_matrix - 1:
                    if matrix[row + 1][col+1] == '*':
                        current_sum += 1
            if col > 0:
                if matrix[row][col-1] == '*':
                    current_sum += 1
            if col < size_of_matrix - 1:
                if matrix[row][col+1] == '*':
                    current_sum += 1

            matrix[current_cordinates[0]][current_cordinates[1]] = current_sum

for row in matrix:
    print(' '.join([str(x) for x in row]))