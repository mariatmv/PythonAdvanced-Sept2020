def get_repeating_DNA(test):
    l = []
    for i in range(len(test)):
        current = test[i:i+10]
        count = 1
        if current in test[i+1:] and current not in l:
            l.append(current)

    return l



test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)
test2 = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"

result2 = get_repeating_DNA(test2)
print(result2)

test3 = "AAAAAAAAAAA"
result3 = get_repeating_DNA(test3)
print(result3)
