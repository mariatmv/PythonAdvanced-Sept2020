size = int(input())
matrix = []
first_diagonal = 0
second_diagonal = 0
for i in range(size):
    matrix.append(list(map(int, input().split(' '))))
for i in range(size):
    first_diagonal += matrix[i][i]

second_matrix = list(reversed(matrix))
for i in range(size):
    second_diagonal += second_matrix[i][i]

print(abs(first_diagonal - second_diagonal))
