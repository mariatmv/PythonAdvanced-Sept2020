rows, cols = [int(i) for i in input().split(' ')]
matrix = []

for i in range(97, 97 + rows):
    for j in range(cols):
        matrix.append(chr(i) + chr(i + j) + chr(i))


new_matrix = []
for k in range(rows):
    current_matrix = []
    for i in range(cols):
        current = matrix.pop(0)
        current_matrix.append(current)
    new_matrix.append(current_matrix)

for row in new_matrix:
    print(' '.join(row))