def operand_set(pc, memory, parameter_number, write_value):
    val = memory[pc + parameter_number]
    opcode = memory[pc]
    mode = (opcode // 10 ** (1 + parameter_number)) % 10

    if mode == 0:  # position
        if write_value is None:
            return memory[val]
        else:
            memory[val] = write_value
    elif mode == 1:  # immediate
        if write_value is None:
            return val
        else:
            raise ValueError()


def operand_get(pc, memory, parameter_number):
    return operand_set(pc, memory, parameter_number, None)


def op_template(func):
    def operation(pc, memory):
        operand1 = operand_get(pc, memory, 1)
        operand2 = operand_get(pc, memory, 2)
        operand_set(pc, memory, 3, func(operand1, operand2))
        return pc + 4
    return operation


def op_conditional_jump(cond):
    def operation(pc, memory):
        if cond(operand_get(pc, memory, 1)):
            return operand_get(pc, memory, 2)
        else:
            return pc + 3
    return operation


def opcode3_input(pc, memory):
    while True:
        try:
            val = int(input('Input: '))
            break
        except ValueError:
            print("Please provide an integer")
    operand_set(pc, memory, 1, val)
    return pc + 2


def opcode4_output(pc, memory):
    print(operand_get(pc, memory, 1))
    return pc + 2


OPCODES = {
    1: op_template(lambda x, y: x + y),                     # +
    2: op_template(lambda x, y: x * y),                     # *
    3: opcode3_input,                                       # input
    4: opcode4_output,                                      # output
    5: op_conditional_jump(lambda x: x),                    # jump if true
    6: op_conditional_jump(lambda x: not x),                # jump if false
    7: op_template(lambda x, y: 1 if x < y else 0),         # less than
    8: op_template(lambda x, y: 1 if x == y else 0)         # equal to
}


def run_program(memory):
    pc = 0
    while pc < len(memory) and memory[pc] % 100 != 99:
        pc = OPCODES[memory[pc] % 100](pc, memory)


if __name__ == "__main__":
    with open(__file__.replace(".py", ".in"), "r") as in_file:
        data = [int(x.strip()) for x in in_file.read().split(",")]
    run_program(data)
