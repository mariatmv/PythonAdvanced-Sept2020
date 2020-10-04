from _collections import deque
food_for_the_day = int(input())
eaters = deque(map(int, input().split()))
biggest = max(eaters)
print(biggest)
complete = True
while eaters:
    if eaters[0] <= food_for_the_day:
        removed = eaters.popleft()
        food_for_the_day -= removed
    else:
        complete = False
        print(f'Orders left: {len(eaters)}')

if complete:
    print('Orders complete')