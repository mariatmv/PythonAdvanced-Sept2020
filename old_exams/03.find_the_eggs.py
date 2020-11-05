test = ([-1, 7, 3, 15, 2, 12], 2)


def find_strongest_eggs(*args):
    eggs = args[0]
    sublists_count = args[-1]
    sublists = [[] for i in range(sublists_count)]
    index = 0
    for egg in eggs:
        if index == sublists_count:
            index = 0
        sublists[index].append(egg)
        index += 1

    strongest_eggs = []
    for l in sublists:
        mid_egg = l[len(l) // 2]
        left_egg = l[(len(l) // 2) - 1]
        right_egg = l[(len(l) // 2) + 1]
        if left_egg < mid_egg > right_egg > left_egg:
            strongest_eggs.append(mid_egg)

    return strongest_eggs


print(find_strongest_eggs(*test))
