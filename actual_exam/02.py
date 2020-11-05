def check_up():
    cordinates = []
    if king_position[1] == 0:
        return None
    else:
        index = king_position[0] - 1
        while index > -1:
            if board[index][king_position[1]] == 'Q':
                cordinates.append(index)
                cordinates.append(king_position[1])
                return cordinates
            index -= 1
    return None


def check_down():
    cordinates = []
    if king_position[1] == 7:
        return False
    else:
        index = king_position[0] + 1
        while index < 8:
            if board[index][king_position[1]] == 'Q':
                cordinates.append(index)
                cordinates.append(king_position[1])
                return cordinates
            index += 1
    return None


def check_left():
    cordinates = []
    if king_position[1] == 0:
        return False
    else:
        index = king_position[1] - 1
        while index > -1:
            if board[king_position[0]][index] == 'Q':
                cordinates.append(king_position[0])
                cordinates.append(index)
                return cordinates
            index -= 1
    return None


def check_right():
    cordinates = []
    if king_position[1] == 7:
        return False
    else:
        index = king_position[1] + 1
        while index < 8:
            if board[king_position[0]][index] == 'Q':
                cordinates.append(king_position[0])
                cordinates.append(index)
                return cordinates
            index += 1
    return None

def check_Left_up_diagonal():
    #check left up
    cordinates = list()
    if king_position[0] == 0:
        return None
    index = king_position[0] - 1
    second_index = king_position[1] - 1
    while index > -1 and second_index > -1:
        if board[index][second_index] == 'Q':
            cordinates.append(index)
            cordinates.append(second_index)
            return cordinates
        index -= 1
        second_index -= 1
    return None

def check_right_up_diagonal():
    cordinates = []
    if king_position[0] == 0:
        return None
    index = king_position[0] - 1
    second_index = king_position[1] + 1
    while index > -1 and second_index < 8:
        if board[index][second_index] == 'Q':
            cordinates.append(index)
            cordinates.append(second_index)
            return cordinates
        index -= 1
        second_index += 1

    return None

def check_Left_down_diagonal():
    cordinates = []
    if king_position[0] == 7:
        return None
    index = king_position[0] + 1
    second_index = king_position[1]-1
    while index < 8 and second_index > -1:
        if board[index][second_index] == 'Q':
            cordinates.append(index)
            cordinates.append(second_index)
            return cordinates
        index += 1
        second_index -= 1

def check_right_down_diagonal():
    cordinates = []
    if king_position[0] == 7:
        return None
    index = king_position[0] + 1
    second_index = king_position[1] + 1
    while index < 8 and second_index < 8:
        if board[index][second_index] == 'Q':
            cordinates.append(index)
            cordinates.append(second_index)
            return cordinates
        index += 1
        second_index += 1


board = []
for i in range(8):
    line = input().split()
    board.append(line)

king_position = []
for row in range(len(board)):
    for col in range(len(board[row])):
        if board[row][col] == 'K':
            king_position.append(row)
            king_position.append(col)


is_king_safe = True

if check_up() is not None:
    print(check_up())
    is_king_safe = False
if check_down() is not None:
    print(check_down())
    is_king_safe = False
if check_right() is not None:
    print(check_right())
    is_king_safe = False
if check_left() is not None:
    print(check_left())
    is_king_safe = False
if check_Left_down_diagonal() is not None:
    print(check_Left_down_diagonal())
    is_king_safe = False
if check_right_down_diagonal() is not None:
    print(check_right_down_diagonal())
    is_king_safe = False
if check_Left_up_diagonal() is not None:
    print(check_Left_up_diagonal())
    is_king_safe = False
if check_right_up_diagonal() is not None:
    print(check_right_up_diagonal())
    is_king_safe = False

if is_king_safe:
    print('The king is safe!')