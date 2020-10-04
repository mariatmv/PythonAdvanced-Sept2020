str_inp = input()
l = []
for ch in range(len(str_inp)):
    start_index = 0
    end_index = 0
    if str_inp[ch] == '(':
        start_index = ch
    if str_inp[ch] == ')':
        end_index = ch
    substring = str_inp[start_index:end_index + 1]
    l.append(substring)
print('\n'.join(l))