countries = input().split(', ')
capitals = input().split(', ')
res = dict(zip(countries, capitals))
for k, v in res.items():
    print(f'{k} -> {v}')