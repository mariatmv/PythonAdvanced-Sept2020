def is_valid(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True


size = int(input())
matrix = [[int(i) for i in input().split()] for x in range(size)]
cmd = input()
while cmd != 'END':
    args = cmd.split()
    todo = args[0]
    row = int(args[1])
    col = int(args[2])
    value = int(args[3])
    if is_valid(row, col):
        if todo == 'Add':
            matrix[row][col] += value
        elif todo == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')

    cmd = input()

for row in matrix:
    print(' '.join(list(map(str, row))))