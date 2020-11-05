def filtered(*args):
    for i in args:
        if i % 2 == 0:
            return i


nums = [int(i) for i in input().split()]
print(list(filter(filtered, nums)))