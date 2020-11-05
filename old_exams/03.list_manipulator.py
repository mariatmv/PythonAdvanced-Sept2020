def list_manipulator(list, command, position, *numbers):
    if command == 'add':
        if position == 'beginning':
            new_list = []
            for number in numbers:
                new_list.append(number)
            for n in reversed(new_list):
                list.insert(0, n)
        elif position == 'end':
            for number in numbers:
                list.append(number)
    elif command == 'remove':
        if position == 'beginning':
            if numbers:
                list = list[numbers[0]:]
            else:
                list = list[1:]
        elif position == 'end':
            if numbers:
                diff = len(list) - numbers[0]
                list = list[:diff]
            else:
                list = list[:-1]
    return list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

