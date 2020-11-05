import os


def create_file(filename):
    if os.path.isfile(filename):
        os.remove(filename)
    with open(filename, 'x'):
        pass


def append_line_to_file(filename, line_to_add):
    with open(filename, 'w') as file:
        file.write(f'{line_to_add}\n')


def replace_string_in_file(filename, old_string, new_string):
    if not os.path.exists(filename):
        print("An error occurred")
        return
    new_lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            new_lines.append(line.replace(old_string, new_string))
    with open(filename, 'w') as file:
        for line in new_lines:
            file.write(line)


def remove_file(filename):
    if not os.path.exists(filename):
        print("An error occurred")
        return

    os.remove(filename)


command = input()
while command != 'End':
    tokens = command.split('-')
    command_name = tokens[0]
    if command_name == 'Add':
        append_line_to_file(tokens[1], tokens[2])
    elif command_name == 'Create':
        create_file(tokens[1])
    elif command_name == 'Replace':
        replace_string_in_file(tokens[1], tokens[2], tokens[3])
    elif command_name == 'Delete':
        remove_file(tokens[1])
    command = input()
