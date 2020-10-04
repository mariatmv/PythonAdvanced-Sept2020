clothes = list(map(int, input().split()))
capacity_of_rack = int(input())
count_of_racks = 0
sum = 0
for i in range(len(clothes)):
    current = clothes.pop()
    if sum + current < capacity_of_rack:
        sum += current
    elif sum + current > capacity_of_rack:
        sum = 0
        count_of_racks += 2
    elif sum + current == capacity_of_rack:
        if len(clothes) > 0:
            count_of_racks += 1
            sum = 0

print(count_of_racks)