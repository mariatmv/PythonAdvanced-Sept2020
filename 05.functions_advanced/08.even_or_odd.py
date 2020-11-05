def even_odd(*args):
    cmd = args[-1]
    l = []
    if cmd == 'even':
        for i in range(len(args) - 1):
            if args[i] % 2 == 0:
                l.append(args[i])
    elif cmd == 'odd':
        for i in range(len(args) - 1):
            if args[i] % 2 != 0:
                l.append(args[i])
    return l
