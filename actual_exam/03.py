def best_list_pureness(*args):
    pureness = {}
    l = list(args[0])
    rotations = args[-1]
    for rotation in range(rotations + 1):
        if rotation != 0:
            last = l.pop()
            l.insert(0, last)
        current_purenes = 0
        for index in range(len(l)):
            current_purenes += l[index] * index
        pureness[rotation] = current_purenes

    max_purreness = [-1, -1]
    for k, v in pureness.items():
        if v > max_purreness[1]:
            max_purreness[0] = k
            max_purreness[1] = v

    return f'Best pureness {max_purreness[1]} after {max_purreness[0]} rotations'


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)



