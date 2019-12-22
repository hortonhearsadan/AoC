import time
from utils import open_file

day = 7
year = 2015

TESTSTRING = ''''''
STRING = ''''''


class Instruction:
    def __init__(self, op=None, inputs=None, output=None):
        self.op = op
        self.inputs = inputs
        self.output = output


def parse_instructions(string):
    instructions = []
    for s in string:
        s = s.split('->')
        for input, output in s:
            input = input.split(' ')
            if len(input) == 1:
                instructions.append(Instruction(None, input, output))

            elif len(input) == 2:
                instructions.append(Instruction(op=input[0], inputs=input[1], output=output))
            elif len(input) == 3:
                instructions.append(Instruction(op=input[1], inputs=[input[0], input[2]], output=output))
    return instructions

def run1():
    string = open_file(day, year)
    instructions = parse_instructions(string)


def run2():
    pass


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
