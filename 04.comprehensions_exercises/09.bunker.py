categories = input().split(', ')
n = int(input())
count_of_items = 0
sum_quality = []
d = {}
for i in range(n):
    category, name, quant = input().split(' - ')
    if category not in d:
        d[category] = [name]
    else:
        d[category].append(name)
    quantity, quality = quant.split(';')
    num_quantity = quantity.split(':')
    num_quality = quality.split(':')
    count_of_items += int(num_quantity[1])
    sum_quality.append(int(num_quality[1]))
print(f'Count of items: {count_of_items}')
print(f'Average quality: {(sum(sum_quality) / len(categories)):.2f}')
for k, v in d.items():
    print(f'{k} -> {", ".join(v)}')