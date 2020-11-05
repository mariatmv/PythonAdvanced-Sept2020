import math
operators = ['+', '-', '*', '/']
inp_data = input().split()
res = []
for n in inp_data:
    if n in operators:
        operator = n
        current = None
        for i in range(len(res) - 1):
            if operator == '+':
                current = int(res[0]) + int(res[1])
            if operator == '-':
                current = int(res[0]) - int(res[1])
            if operator == '*':
                current = int(res[0]) * int(res[1])
            if operator == '/':
                current = math.floor(int(res[0]) / int(res[1]))
            res.pop(0)
            res.insert(0, current)
            res.pop(1)

    else:
        res.append(n)

print(res[0])