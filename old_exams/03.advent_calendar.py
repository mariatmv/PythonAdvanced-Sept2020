def is_it_sorted(list):
    for i in range(len(list) - 1):
        if list[i] < list[i + 1]:
            pass
        else:
            return False
    return True


def fix_calendar(*args):
    list = args[0]
    while not is_it_sorted(list):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list


numbers = [3, 2, 1, 4, 8, 0]
fixed = fix_calendar(numbers)
print(fixed)
