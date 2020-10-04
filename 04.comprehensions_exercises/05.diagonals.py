size = int(input())
matrix = [input().split(', ') for i in range(size)]
first_diagonal = [matrix[i][i] for i in range(size)]
new_matrix = list(reversed(matrix))
second_diagonal = [new_matrix[i][i] for i in range(size)]
sum_first = sum([int(i) for i in first_diagonal])
sum_second = sum([int(i) for i in second_diagonal])
print(f'First diagonal: {", ".join(first_diagonal)}. Sum: {sum_first}')
print(f'Second diagonal: {", ".join(list(reversed(second_diagonal)))}. Sum: {sum_second}')