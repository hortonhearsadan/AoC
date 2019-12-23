from enum import IntEnum
from typing import List

class Mode(IntEnum):
    POSITION = 0
    VALUE = 1
    RELATIVE = 2


class Op(IntEnum):
    ADD = 1
    MUL = 2
    READ = 3
    WRITE = 4
    BNE = 5
    BEQ = 6
    LT = 7
    EQ = 8
    REL_BAS = 9
    HALT = 99


class Instruction:
    __slots__ = ["program", "mode1", "mode2", "mode3"]

    def __init__(self, program, mode1, mode2, mode3):
        self.program = program
        self.mode1 = mode1
        self.mode2 = mode2
        self.mode3 = mode3


class Computer:
    def __init__(self, codes):
        self.inputs = []
        self.codes = codes + [0] * 20000
        self.outputs = []
        self.halted = False
        self.ptr = 0
        self.paused = False
        self.relative_base = 0
        self.save_state= codes + [0] * 20000

    def value(self, program, arg, mode):
        if mode == Mode.VALUE:
            return arg
        elif mode == Mode.RELATIVE:
            return program[arg + self.relative_base]
        else:
            return program[arg]

    def _map_address(self, addr, mode):
        if mode == Mode.RELATIVE:
            return addr + self.relative_base
        elif mode == Mode.POSITION:
            return addr
        else:
            return None

    def add_inputs(self, inputs: List):
        self.inputs.extend(inputs)

    def add_input(self, input: int):
        self.inputs.append(input)

    def program(self, reset=False):
        output = None
        # program = self.codes + [0] * 2000
        program = self.codes
        while program[self.ptr] != Op.HALT:
            code = program[self.ptr]
            self.ptr += 1

            mode3, code = divmod(code, 10000)
            mode2, code = divmod(code, 1000)
            mode1, code = divmod(code, 100)

            instruction = Instruction(program, mode1, mode2, mode3)
            if code == Op.ADD:
                self._add(instruction)

            elif code == Op.MUL:
                self._mul(instruction)

            elif code == Op.READ:
                error = self._read(instruction)
                if error:
                    break

            elif code == Op.WRITE:
                output = self._write(instruction)

            elif code == Op.BNE:
                self._bne(instruction)

            elif code == Op.BEQ:
                self._beq(instruction)

            elif code == Op.LT:
                self._lt(instruction)

            elif code == Op.EQ:
                self._eq(instruction)

            elif code == Op.REL_BAS:
                self._rel_bas(instruction)

            # unknown opcode
            else:
                return None
        if program[self.ptr] == Op.HALT:
            self.halted = True
        if reset:
            self.codes = self.save_state
            self.ptr =0
            self.relative_base = 0
            self.halted = False
        return output

    def _add(self, instr):
        arg1, arg2, pos = instr.program[self.ptr: self.ptr + 3]
        pos = self._map_address(pos, instr.mode3)
        instr.program[pos] = self.value(instr.program, arg1, instr.mode1) + self.value(instr.program, arg2, instr.mode2)
        self.ptr += 3

    def _mul(self, instr):
        arg1, arg2, pos = instr.program[self.ptr: self.ptr + 3]
        pos = self._map_address(pos, instr.mode3)
        instr.program[pos] = self.value(instr.program, arg1, instr.mode1) * self.value(instr.program, arg2, instr.mode2)

        self.ptr += 3

    def _read(self, instr):
        pos = instr.program[self.ptr]
        pos = self._map_address(pos, instr.mode1)
        try:
            instr.program[pos] = self.inputs.pop(0)
            self.ptr += 1
        except:
            self.ptr -= 1
            return True

    def _write(self, instr):
        pos = instr.program[self.ptr]
        output = self.value(instr.program, pos, instr.mode1)
        self.outputs.append(output)
        self.ptr += 1
        return output

    def _bne(self, instr):
        arg1, arg2 = instr.program[self.ptr: self.ptr + 2]
        self.ptr += 2

        if self.value(instr.program, arg1, instr.mode1) != 0:
            self.ptr = self.value(instr.program, arg2, instr.mode2)

    def _beq(self, instr):
        arg1, arg2 = instr.program[self.ptr: self.ptr + 2]
        self.ptr += 2

        if self.value(instr.program, arg1, instr.mode1) == 0:
            self.ptr = self.value(instr.program, arg2, instr.mode2)

    def _lt(self, instr):
        arg1, arg2, pos = instr.program[self.ptr: self.ptr + 3]
        pos = self._map_address(pos, instr.mode3)
        instr.program[pos] = 1 if self.value(instr.program, arg1, instr.mode1) < self.value(instr.program, arg2,
                                                                                            instr.mode2) else 0
        self.ptr += 3

    def _eq(self, instr):
        arg1, arg2, pos = instr.program[self.ptr: self.ptr + 3]
        pos = self._map_address(pos, instr.mode3)
        instr.program[pos] = 1 if self.value(instr.program, arg1, instr.mode1) == self.value(instr.program, arg2,
                                                                                             instr.mode2) else 0

        self.ptr += 3

    def _rel_bas(self, instr):
        arg1 = instr.program[self.ptr]
        offset = self.value(instr.program, arg1, instr.mode1)
        self.relative_base += offset
        self.ptr += 1

    def clear_outputs(self):
        self.outputs = []