first_set_len, second_set_len = tuple(map(int, input().split()))
first_set = set()
second_set = set()
for i in range(first_set_len):
    first_set.add(input())
for i in range(second_set_len):
    second_set.add(input())
res_set = first_set & second_set
print('\n'.join(res_set))