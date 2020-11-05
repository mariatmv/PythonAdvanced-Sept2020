def get_up_values():
    sum_values = 0
    taken = []
    if bunny_position[0] == 0:
        return 0, 0, 0
    else:
        index = bunny_position[0] - 1
        for i in range(bunny_position[0]):
            if matrix[index][bunny_position[1]] != 'X':
                sum_values += int(matrix[index][bunny_position[1]])
                current_pos = [index, bunny_position[1]]
                taken.append(current_pos)
            index -= 1

    return sum_values, taken


def get_down_values():
    sum_values = 0
    taken = []
    if bunny_position[0] == n - 1:
        return 0, 0, 0
    else:
        index = bunny_position[0] + 1
        for i in range(n - bunny_position[0] - 1):
            if matrix[index][bunny_position[1]] != 'X':
                sum_values += int(matrix[index][bunny_position[1]])
                current_pos = [index, bunny_position[1]]
                taken.append(current_pos)
            index += 1

    return sum_values, taken


def get_left_values():
    sum_values = 0
    taken = []
    if bunny_position[1] == 0:
        return 0, 0, 0
    else:
        index = bunny_position[1] - 1
        for i in range(bunny_position[1]):
            if matrix[bunny_position[0]][index] != 'X':
                sum_values += int(matrix[bunny_position[0]][index])
                current_pos = [bunny_position[0], index]
                taken.append(current_pos)
            index -= 1

    return sum_values, taken


def get_right_values():
    sum_values = 0
    taken = []
    if bunny_position[1] == n - 1:
        return 0, 0, 0
    else:
        index = bunny_position[1] + 1
        for i in range(n - 1 - bunny_position[1]):
            if matrix[bunny_position[0]][index] != 'X':
                sum_values += int(matrix[bunny_position[0]][index])
                current_pos = [bunny_position[0], index]
                taken.append(current_pos)
            index += 1

    return sum_values, taken


n = int(input())
matrix = [input().split() for i in range(n)]
bunny_position = []
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 'B':
            bunny_position.append(row)
            bunny_position.append(col)

values = {'up': get_up_values(), 'down': get_down_values(), 'left': get_left_values(), 'right': get_right_values()}
collected_matrix = []
biggest = ['', -1, []]
for k, v in values.items():
    if v[0] > biggest[1]:
        biggest[0] = k
        biggest[1] = v[0]
        biggest[2] = v[1]

print(biggest[0])
for l in biggest[2]:
    print(l)
print(biggest[1])