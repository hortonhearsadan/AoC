import time
from collections import defaultdict
import itertools
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
            instructions.append(Instruction(i, op=input[0], inputs=[input[1]], output=output.strip()))
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
    v = {}
    for i in instructions:
        outputs[i.output].append(i)
        for j in i.letter_inputs:
            inputs[j].append(i)

        instruction_dict[i.id] = i

    graph = get_graph(instructions, outputs, inputs)
    order = list(nx.topological_sort(graph))
    # cycle = nx.find_cycle(graph)
    # nodes = list(itertools.chain(*cycle))
    # nodes = nodes[::2]
    # for n in nodes:
    #     print(instruction_dict[n].inputs, instruction_dict[n].output,'-----', string[n-1])

    for i in order:
        instr = instruction_dict[i]
        inputs = instr.inputs
        o = instr.output
        op = instr.op
        x = inputs[0]
        if len(inputs) > 1:
            y = inputs[1]
        if op is None:
            if x.isdigit():
                v[o] = int(inputs[0])
            else:
                v[o] = v[x]
        elif op == 'LSHIFT':
            v[o] = v[inputs[0]] << int(inputs[1])
        elif op == 'RSHIFT':
            v[o] = v[inputs[0]] >> int(inputs[1])
        elif op == 'AND':
            if y.isdigit():
                v_y = int(inputs[1])
            else:
                v_y = v[y]
            if x.isdigit():
                v_x = int(inputs[0])
            else:
                v_x = v[x]
            v[o] = v_x & v_y
        elif op == 'NOT':
            v[o] = ~ v[inputs[0]] % 65536
        elif op == 'OR':
            v[o] = v[inputs[0]] | v[inputs[1]]

    return v['a']


def run2(override):
    string = open_file(day, year)
    instructions = parse_instructions(string)
    outputs = defaultdict(list)
    inputs = defaultdict(list)
    instruction_dict = {}
    v = {}
    for i in instructions:
        outputs[i.output].append(i)
        for j in i.letter_inputs:
            inputs[j].append(i)

        instruction_dict[i.id] = i

    graph = get_graph(instructions, outputs, inputs)
    order = list(nx.topological_sort(graph))
    # cycle = nx.find_cycle(graph)
    # nodes = list(itertools.chain(*cycle))
    # nodes = nodes[::2]
    # for n in nodes:
    #     print(instruction_dict[n].inputs, instruction_dict[n].output,'-----', string[n-1])

    for i in order:
        instr = instruction_dict[i]
        inputs = instr.inputs
        o = instr.output
        op = instr.op
        x = inputs[0]
        if len(inputs) > 1:
            y = inputs[1]
        if op is None:
            if o == 'b':
                v[o] = override
            else:
                if x.isdigit():
                    v[o] = int(inputs[0])
                else:
                    v[o] = v[x]
        elif op == 'LSHIFT':
            v[o] = v[inputs[0]] << int(inputs[1])
        elif op == 'RSHIFT':
            v[o] = v[inputs[0]] >> int(inputs[1])
        elif op == 'AND':
            if y.isdigit():
                v_y = int(inputs[1])
            else:
                v_y = v[y]
            if x.isdigit():
                v_x = int(inputs[0])
            else:
                v_x = v[x]
            v[o] = v_x & v_y
        elif op == 'NOT':
            v[o] = ~ v[inputs[0]] % 65536
        elif op == 'OR':
            v[o] = v[inputs[0]] | v[inputs[1]]

    return v['a']


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2(f)
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
