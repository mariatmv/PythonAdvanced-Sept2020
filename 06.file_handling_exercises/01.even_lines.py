symbols = ['-', ',', '.', '!', '?']
with open('test.txt') as file:
    i = 0
    for line in file:
        if i % 2 != 0:
            i += 1
            continue
        for symbol in symbols:
            line = line.replace(symbol, '@')

        line_list = line.split(' ')
        line_reversed = list(reversed(line_list))
        line_output = ' '.join(line_reversed)

        print(line_output)
        i += 1