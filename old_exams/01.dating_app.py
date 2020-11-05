from _collections import deque
males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches = 0

while females:
    if len(males) < 1:
        break
    if females[0] <= 0 or males[-1] <= 0:
        if females[0] <= 0:
            females.popleft()
        if males[-1] <= 0:
            males.pop()
    else:
        if females[0] % 25 == 0 or males[-1] % 25 == 0:
            if females[0] % 25 == 0:
                females.popleft()
                if len(females) > 0:
                    females.popleft()
            if males[-1] % 25 == 0:
                males.pop()
                males.pop()
        else:
            if females[0] == males[-1]:
                matches += 1
                females.popleft()
                males.pop()
            else:
                females.popleft()
                males[-1] -= 2

print(f'Matches: {matches}')
if len(males) > 0:
    print(f'Males left: {", ".join([str(x) for x in males])}')
else:
    print(f'Males left: none')
if len(females) > 0:
    print(f'Females left: {", ".join([str(x) for x in females])}')
else:
    print(f'Females left: none')