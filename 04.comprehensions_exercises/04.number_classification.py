inp_data = input().split(', ')
positive = [x for x in inp_data if int(x) >= 0]
negative = [x for x in inp_data if int(x) < 0]
odd = [x for x in inp_data if int(x) % 2 != 0]
even = [x for x in inp_data if int(x) % 2 == 0]
print('Positive: ' + ', '.join(positive))
print('Negative: ' + ', '.join(negative))
print('Even: ' + ', '.join(even))
print('Odd: ' + ', '.join(odd))