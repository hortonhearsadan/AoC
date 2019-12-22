import time
from collections import defaultdict

import networkx as nx

from utils import open_file

day = 7
year = 2015

TESTSTRING = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i'''
STRING = ''''''


class Instruction:
    def __init__(self, _id, op=None, inputs=None, output=None):
        self.op = op
        self.inputs = inputs
        self.output = output
        self.letter_inputs = [p for p in inputs if not p.isdigit()]
        self.id = _id


def parse_instructions(string):
    instructions = []
    i = 0
    for s in string:
        i += 1
        s = list(filter(None, s.replace('\n', '').split('->')))
        input, output = s
        input = list(filter(None, input.split(' ')))
        if len(input) == 1:
            instructions.append(Instruction(i, None, input, output.strip()))

        elif len(input) == 2:
            instructions.append(Instruction(i, op=input[0], inputs=input[1], output=output.strip()))
        elif len(input) == 3:
            instructions.append(Instruction(i, op=input[1], inputs=[input[0], input[2]], output=output.strip()))
    return instructions


def get_graph(instructions, outputs, inputs):
    g = nx.DiGraph()
    for i in instructions:
        for j in i.letter_inputs:
            for k in outputs[j]:
                g.add_edge(k.id, i.id)

    return g


def run1():
    string = open_file(day, year)
    instructions = parse_instructions(string)
    outputs = defaultdict(list)
    inputs = defaultdict(list)
    instruction_dict = {}
    valuedict = {}
    for i in instructions:
        outputs[i.output].append(i)
        valuedict[i.output] = 0
        for j in i.letter_inputs:
            inputs[j].append(i)

        instruction_dict[i.id] = i

    graph = get_graph(instructions, outputs, inputs)
    order = list(nx.topological_sort(graph))

    for i in order:
        instr = instruction_dict[i]
        inputs = instr.inputs
        o = instr.output
        op = instr.op
        if op is None:
            valuedict[o] = int(inputs[0])
        elif op == 'LSHIFT':
            valuedict[o] = valuedict[inputs[0]] >> int(inputs[1])
        elif op == 'RSHIFT':
            valuedict[o] = valuedict[inputs[0]] << int(inputs[1])
        elif op == 'AND':
            valuedict[o] = valuedict[inputs[0]] & valuedict[inputs[1]]
        elif op == 'NOT':
            valuedict[o] = ~ valuedict[inputs[0]] % 65536
        elif op == 'OR':
            valuedict[o] = valuedict[inputs[0]] | valuedict[inputs[1]]

    return valuedict['a']


def run2():
    pass


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
