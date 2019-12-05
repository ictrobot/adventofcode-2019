import functools


class InvalidState(Exception):
    pass


def resolve_parameter(pc, memory, parameter_number, write):
    val = memory[pc + parameter_number]
    opcode = memory[pc]
    mode = (opcode // 10 ** (1 + parameter_number)) % 10

    if mode == 0:  # position
        return functools.partial(memory.__setitem__ if write else memory.__getitem__, val)
    elif mode == 1:  # immediate
        if write:
            raise InvalidState()
        return lambda: val


def opcode1_plus(pc, memory):
    operand1 = resolve_parameter(pc, memory, 1, False)()
    operand2 = resolve_parameter(pc, memory, 2, False)()
    resolve_parameter(pc, memory, 3, True)(operand1 + operand2)
    return 3


def opcode2_mult(pc, memory):
    operand1 = resolve_parameter(pc, memory, 1, False)()
    operand2 = resolve_parameter(pc, memory, 2, False)()
    resolve_parameter(pc, memory, 3, True)(operand1 * operand2)
    return 3


def opcode3_input(pc, memory):
    while True:
        try:
            val = int(input('Input: '))
            break
        except ValueError:
            print("Please provide an integer")
    resolve_parameter(pc, memory, 1, True)(val)
    return 1


def opcode4_output(pc, memory):
    print(resolve_parameter(pc, memory, 1, False)())
    return 1


def run(memory):
    pc = 0
    opcodes = {1: opcode1_plus, 2: opcode2_mult, 3: opcode3_input, 4: opcode4_output}
    while pc < len(memory):
        opcode = memory[pc] % 100
        if opcode == 99:
            break
        operation = opcodes[opcode]
        pc += 1 + operation(pc, memory)


if __name__ == "__main__":
    with open(__file__.replace(".py", ".in"), "r") as in_file:
        data = [int(x.strip()) for x in in_file.read().split(",")]
    run(data)