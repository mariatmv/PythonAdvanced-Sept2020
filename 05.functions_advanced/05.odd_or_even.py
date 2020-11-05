def odd(*args):
    sum = 0
    count = 0
    for i in args[0]:
        if i % 2 != 0:
            sum += i
        count += 1
    print(sum * count)


def even(*args):
    sum = 0
    count = 0
    for i in args[0]:
        if i % 2 == 0:
            sum += i
        count += 1
    print(sum * count)


cmd = input()
l = [int(i) for i in input().split()]
if cmd == 'Odd':
    odd(l)
else:
    even(l)