import copy
import time
from enum import Enum

from utils import open_file

dir_path = __file__.split("/")
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
STRING = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


# Ops
ACC = "acc"
JMP = "jmp"
NOP = "nop"


class State(Enum):
    TERMINATES = "terminates"
    INFINITE_LOOP = "loop"


### FANCY START ####
class GameConsole:
    def __init__(self, instructions):
        self.instructions = instructions
        self.pointer = 0
        self.accumulator = 0
        self.state = None

    def run_until_state_known(self):
        used_instructions = set()
        while self.pointer not in used_instructions:
            instr = self.instructions[self.pointer]
            used_instructions.add(self.pointer)

            if instr.op == ACC:
                self.accumulator += instr.value
                self.pointer += 1
            elif instr.op == NOP:
                self.pointer += 1
            elif instr.op == JMP:
                self.pointer += instr.value

            if self.pointer == len(self.instructions):
                self.state = State.TERMINATES
                return self.accumulator, State.TERMINATES

        self.state = State.INFINITE_LOOP
        return self.accumulator, self.state

    def modify_until_state_terminates(self):
        jumps_and_nops = [i for i, j in enumerate(self.instructions) if j.op != ACC]

        for j in jumps_and_nops:
            self.reset()
            self.modify_and_run(j)

            if self.state == State.TERMINATES:
                return self.accumulator

    def modify_and_run(self, j):
        self.accumulator = 0
        self.instructions[j].switch_op()
        _, state = self.run_until_state_known()
        self.instructions[j].switch_op()
        return state

    def reset(self):
        self.pointer = 0
        self.accumulator = 0
        self.state = None


### FANCY END ####


class Instruction:
    def __init__(self, op, value):
        self.op = op
        self.value = value

    def switch_op(self):
        if self.op == JMP:
            self.op = NOP
        elif self.op == NOP:
            self.op = JMP


def parse_input():
    f = open_file(day, year)
    # f=STRING.split('\n')
    instrs = []
    for i in f:
        op, value = i.strip().split(" ")
        instrs.append(Instruction(op, int(value)))
    return instrs


###### UNFANCY START ######


def run1(instructions):
    pointer = 0
    used_instructions = set()
    accumulator = 0
    terminates = False
    while pointer not in used_instructions:
        instr = instructions[pointer]
        used_instructions.add(pointer)

        if instr.op == ACC:
            accumulator += instr.value
            pointer += 1
        elif instr.op == NOP:
            pointer += 1
        elif instr.op == JMP:
            pointer += instr.value

        if pointer == len(instructions):
            terminates = True
            return accumulator, terminates
    return accumulator, terminates


def run2(instructions):
    jumps_and_nops = [i for i, j in enumerate(instructions) if j.op != ACC]

    for j in jumps_and_nops:
        instructions[j].switch_op()
        accumulator, terminates = run1(instructions)
        instructions[j].switch_op()

        if terminates:
            return accumulator


###### UNFANCY END ######

if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    # f, terms = run1(inputs)
    gc = GameConsole(inputs)
    f, terms = gc.run_until_state_known()
    # g = run2(inputs)
    g = gc.modify_until_state_terminates()
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
