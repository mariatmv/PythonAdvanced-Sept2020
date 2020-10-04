rows, cols = list(map(int, input().split(', ')))
matrix = []
for i in range(rows):
    matrix.append(list(map(int, input().split(' '))))
for c in range(cols):
    current_sum = 0
    for r in range(rows):
        current = matrix[r][c]
        current_sum += current
    print(current_sum)