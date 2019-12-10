with open("input.in", "r") as in_file:
    DATA = [int(x.strip()) for x in in_file.read().split(",")]


def run(noun, verb):
    data = DATA[:]
    data[1] = noun
    data[2] = verb

    idx = 0
    opcodes = {1: lambda x, y: x + y, 2: lambda x, y: x * y}
    while idx < len(data) and data[idx] in opcodes:
        data[data[idx + 3]] = opcodes[data[idx]](data[data[idx + 1]], data[data[idx + 2]])
        idx += 4

    return data[0]


noun, verb = next((x, y) for x in range(100) for y in range(100) if run(x, y) == 19690720)
print(noun, verb)
print(100 * noun + verb)
