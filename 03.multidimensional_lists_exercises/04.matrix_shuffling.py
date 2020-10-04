def isItValid(command):
    if command[0] == 'swap':
        if len(command) == 5:
            if int(command[1]) <= rows and int(command[2]) <= cols:
                if int(command[3]) <= rows and int(command[4]) <= cols:
                    return True


def swap(command):
    first_cordinates = [int(command[1]), int(command[2])]
    second_cordinates = [int(command[3]), int(command[4])]
    current_second = matrix[second_cordinates[0]][second_cordinates[1]]
    current_first = matrix[first_cordinates[0]][first_cordinates[1]]
    matrix[first_cordinates[0]][first_cordinates[1]] = current_second
    matrix[second_cordinates[0]][second_cordinates[1]] = current_first

    for row in matrix:
        print(' '.join(row))


rows, cols = [int(x) for x in input().split()]
matrix = []
for i in range(rows):
    lane = input().split()
    matrix.append(lane)

command = input()
while command != 'END':
    command = command.split()
    if isItValid(command):
        swap(command)


    else:
        print('Invalid input!')

    command = input()