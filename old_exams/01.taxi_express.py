from _collections import deque
customers = deque([int(x) for x in input().split(', ')])
taxis = [int(x) for x in input().split(', ')]
total_time = 0
successful = True

while customers:
    if len(taxis) < 1:
        successful = False
        break

    if taxis[-1] < customers[0]:
        taxis.pop()
    else:
        total_time += customers[0]
        customers.popleft()
        taxis.pop()

if not successful:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join([str(x) for x in customers])}')
else:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')