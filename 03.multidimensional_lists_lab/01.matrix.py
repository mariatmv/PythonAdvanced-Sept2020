rows, cols = list(map(int, input().split(', ')))
matrix = []
Sum = 0
for i in range(rows):
    matrix.append(list(map(int, input().split(', '))))
    Sum += sum(matrix[i])
print(Sum)
print(matrix)