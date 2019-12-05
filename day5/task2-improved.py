class IntcodeComputer:
    class Operands:
        def __init__(self, ic):
            self.ic = ic

        def __setitem__(self, parameter_number, write_value):
            val = self.ic.memory[self.ic.pc + parameter_number]
            opcode = self.ic.memory[self.ic.pc]
            mode = (opcode // 10 ** (1 + parameter_number)) % 10

            if mode == 0:  # position
                self.ic.memory[val] = write_value
            elif mode == 1:  # immediate
                raise ValueError()

        def __getitem__(self, parameter_number):
            val = self.ic.memory[self.ic.pc + parameter_number]
            opcode = self.ic.memory[self.ic.pc]
            mode = (opcode // 10 ** (1 + parameter_number)) % 10

            if mode == 0:  # position
                return self.ic.memory[val]
            elif mode == 1:  # immediate
                return val

    def __init__(self, memory):
        self.pc = 0
        self.memory = memory[:]
        self.operand = self.Operands(self)

    def run(self):
        while self.pc < len(self.memory) and self.memory[self.pc] % 100 != 99:
            self.pc = OPCODES[self.memory[self.pc] % 100](self)


def get_opcodes():
    def op_template(func):
        def operation(ic):
            ic.operand[3] = func(ic.operand[1], ic.operand[2])
            return ic.pc + 4
        return operation

    def op_conditional_jump(cond):
        return lambda ic: ic.operand[2] if cond(ic.operand[1]) else ic.pc + 3

    def opcode3_input(ic):
        while True:
            try:
                ic.operand[1] = int(input('Input: '))
                return ic.pc + 2
            except ValueError:
                print("Please provide an integer")

    def opcode4_output(ic):
        print(ic.operand[1])
        return ic.pc + 2

    return {
        1: op_template(lambda x, y: x + y),                     # +
        2: op_template(lambda x, y: x * y),                     # *
        3: opcode3_input,                                       # input
        4: opcode4_output,                                      # output
        5: op_conditional_jump(lambda x: x),                    # jump if true
        6: op_conditional_jump(lambda x: not x),                # jump if false
        7: op_template(lambda x, y: 1 if x < y else 0),         # less than
        8: op_template(lambda x, y: 1 if x == y else 0)         # equal to
    }


OPCODES = get_opcodes()

if __name__ == "__main__":
    with open(__file__.replace(".py", ".in"), "r") as in_file:
        data = [int(x.strip()) for x in in_file.read().split(",")]
    IntcodeComputer(data).run()