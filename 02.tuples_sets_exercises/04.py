from _collections import OrderedDict
text = input()
occurances = {}
for i in text:
    if i not in occurances:
        occurances[i] = 1
    else:
        occurances[i] += 1

ordered = OrderedDict(sorted(occurances.items()))
for k, v in ordered.items():
    print(f'{k}: {v} time/s')