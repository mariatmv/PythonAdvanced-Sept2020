size = int(input())
matrix = []
total = 0
for i in range(size):
    matrix.append(list(map(int, input().split(' '))))
for i in range(size):
    total += matrix[i][i]
print(total)
