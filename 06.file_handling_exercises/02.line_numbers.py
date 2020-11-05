marks = ['-', ',', '.', '!', '?']
output = open('output.txt', 'w')
with open('test.txt') as file:
    for line in file:
        l = 1
        count_marks = 0
        count_letters = 0
        current_line = line.replace(' ', '')
        for char in current_line:
            if char in marks:
                count_marks += 1
            else:
                count_letters += 1
        output.write(f'Line {l}: {line} ({count_letters})({count_marks})')
        l += 1
