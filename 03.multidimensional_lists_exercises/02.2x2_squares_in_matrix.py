# A B B D
# E B B B
# I J B B
count = 0
rows, cols = list(map(int, input().split()))
matrix = [list(input().split()) for _ in range(rows)]
for i in range(rows):
    if matrix[i][i] == matrix[i][i + 1]:
        current = matrix[i][i]
        if matrix[i][i] == current and matrix[i][i + 1] == current:
            count += 1

print(count)