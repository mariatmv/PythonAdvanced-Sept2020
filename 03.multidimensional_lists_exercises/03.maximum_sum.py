import sys
from itertools import chain
rows, cols = [int(x) for x in input().split(' ')]
matrix = []
for _ in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)
maximum_sum = -sys.maxsize
maximum_matrix = []
for i in range(rows-2):
    rectangle = []
    current_sum = 0
    row = matrix[i]
    for j in range(cols - 2):
        rectangle = [
            [matrix[i][j], matrix[i][j+1], matrix[i][j+2]],
            [matrix[i+1][j], matrix[i+1][j + 1], matrix[i+1][j + 2]],
            [matrix[i+2][j], matrix[i+2][j + 1], matrix[i+2][j + 2]],
        ]
        current_sum = sum(list(chain(*rectangle)))
        if current_sum > maximum_sum:
            maximum_sum = current_sum
            maximum_matrix = rectangle
print(f"Sum = {maximum_sum}")
[print(" ".join(map(str, row))) for row in maximum_matrix]