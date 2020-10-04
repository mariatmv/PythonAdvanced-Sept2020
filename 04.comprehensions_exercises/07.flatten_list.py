from itertools import chain
inp_data = [i for i in input().split('|')]
matrix = list(reversed(inp_data))
second_matrix = list(chain([i.strip() for i in matrix]))
print(' '.join(second_matrix))