import collections


def numbers_searching(*args):
    dublicates = [item for item, count in collections.Counter(args).items() if count > 1]
    missing = None

    biggest = max(args)
    smallest = min(args)

    for i in range(smallest, biggest):
        if i not in args:
            missing = i

    return [missing, sorted(dublicates)]


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))