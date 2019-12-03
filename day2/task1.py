with open(__file__.replace(".py", ".in"), "r") as in_file:
    data = [int(x.strip()) for x in in_file.read().split(",")]

data[1] = 12
data[2] = 2

idx = 0
opcodes = {1: lambda x, y: x + y, 2: lambda x, y: x * y}
while idx < len(data) and data[idx] in opcodes:
    data[data[idx + 3]] = opcodes[data[idx]](data[data[idx + 1]], data[data[idx + 2]])
    idx += 4

print(data)