def func_executor(*args):
    l = []
    for i in range(len(args)):
        func, params = args[i].split(', ')
        l.append(func(params))


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
