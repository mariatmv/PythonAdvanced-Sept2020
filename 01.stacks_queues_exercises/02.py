n = int(input())
stack = []
for i in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        stack.insert(0, int(cmd[1]))
    elif cmd[0] == 2:
        stack = stack[:-1]
        print(' '.join(stack))
    elif cmd[0] == 3:
        print(max(stack))
    elif cmd[0] == 4:
        print(min(stack))

for s in range(len(stack)):
    if s < len(stack) -1:
        print(stack[s], end=', ')
    else:
        print(stack[s])