import itertools


class InputNeeded(Exception):
    pass


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

    def __init__(self, memory, inputs):
        self.pc = 0
        self.memory = memory[:]
        self.inputs = inputs
        self.outputs = []
        self.operand = self.Operands(self)

    def run(self):
        while self.pc < len(self.memory) and self.memory[self.pc] % 100 != 99:
            self.pc = OPCODES[self.memory[self.pc] % 100](self)

    def run_outputs(self):
        while self.pc < len(self.memory) and self.memory[self.pc] % 100 != 99:
            self.pc = OPCODES[self.memory[self.pc] % 100](self)
            while self.outputs:
                yield self.outputs.pop(0)


def get_opcodes():
    def op_template(func):
        def operation(ic):
            ic.operand[3] = func(ic.operand[1], ic.operand[2])
            return ic.pc + 4
        return operation

    def op_conditional_jump(cond):
        return lambda ic: ic.operand[2] if cond(ic.operand[1]) else ic.pc + 3

    def opcode3_input(ic):
        if ic.inputs:
            ic.operand[1] = int(ic.inputs.pop(0))
            return ic.pc + 2
        else:
            raise InputNeeded()

    def opcode4_output(ic):
        ic.outputs.append(ic.operand[1])
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
    with open("input.in", "r") as in_file:
        program = [int(x.strip()) for x in in_file.read().split(",")]

    def test(permutation):
        ics = [IntcodeComputer(program, [p]) for p in permutation]
        signal = 0

        while True:
            for ic in ics:
                ic.inputs.append(signal)
                try:
                    signal = next(ic.run_outputs())
                except (InputNeeded, StopIteration):
                    return signal

    scores = {p: test(p) for p in itertools.permutations(range(5, 10))}
    print(sorted(scores.items(), key=lambda x: x[1], reverse=True)[0])