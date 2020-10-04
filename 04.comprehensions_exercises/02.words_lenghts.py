inp_data = input().split(', ')
d = {inp_data[i]:len(inp_data[i]) for i in range(len(inp_data))}
print(", ".join([" -> ".join([key, str(val)]) for key, val in d.items()]))