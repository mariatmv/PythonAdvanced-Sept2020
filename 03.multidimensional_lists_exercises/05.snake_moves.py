# SoftUn
# UtfoSi
# niSoft
# foSinU
# tUniSo
from _collections import deque
rows, cols = [int(x) for x in input().split()]
text = deque(input())
matrix = []
for i in range(rows):
    matrix.append(deque())

for i in range(rows):
    for j in range(cols):
        if i % 2 == 0:
            current_char = text.popleft()
            matrix[i].append(current_char)
            text.append(current_char)

        else:
            current_char = text.popleft()
            matrix[i].appendleft(current_char)
            text.append(current_char)

for row in matrix:
    print(''.join(row))