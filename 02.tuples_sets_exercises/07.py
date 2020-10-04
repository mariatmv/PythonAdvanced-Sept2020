n = int(input())
even_set = set()
odd_set = set()
for i in range(1, n + 1):
    name = input()
    current_name_sum = 0
    for n in name:
        current_name_sum += ord(n)
    devised_num = int(current_name_sum / i)
    if devised_num % 2 == 0:
        even_set.add(devised_num)
    else:
        odd_set.add(devised_num)
sum_odd = sum(odd_set)
sum_even = sum(even_set)
if sum_odd == sum_even:
    union = list(map(str, even_set | odd_set))
    print(', '.join(union))
elif sum_even > sum_odd:
    symmetric = list(map(str, even_set ^ odd_set))
    print(', '.join(symmetric))
elif sum_even < sum_odd:
    diff = list(map(str, odd_set - even_set))
    print(', '.join(diff))