size = int(input())
matrix = [list(input()) for _ in range(size)]
found_row = None
found_col = None
found = False
searched_symbol = input()
for row in range(size):
    for col in range(size):
        if matrix[row][col] == searched_symbol:
            found_row = row
            found_col = col
            found = True
    if found:
        break

if found:
    print(f'({found_row}, {found_col})')
else:
    print(f'{searched_symbol} does not occur in the matrix')