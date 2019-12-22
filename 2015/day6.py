import time
from utils import open_file
import re

day = 6
year = 2015
import numpy as np

TESTSTRING = ''''''
STRING = ''''''


class Instruction:
    def __init__(self, action, start, end):
        self.action = action
        self.start = tuple(int(s) for s in start.split(','))
        self.end = tuple(int(s) for s in end.split(','))


def switch(state, action):
    if action == 'off':
        return 0
    elif action == ' on':
        return 1
    elif action == 'toggle':
        return (state + 1) % 2


def trim(strings):
    instructions = []
    for s in strings:
        s = list(filter(None, s.replace('turn', '').replace('through', '').replace('\n', '').split(' ')))
        instructions.append(Instruction(*s))
    return instructions


def run1():
    strings = open_file(day, year)
    lights = np.zeros((1000, 1000))

    instructions = trim(strings)

    for i in instructions:
        if i.action == 'off':
            lights[i.start[1]:i.end[1] + 1, i.start[0]: i.end[0] + 1] = 0
        elif i.action == 'on':
            lights[i.start[1]:i.end[1] + 1, i.start[0]: i.end[0] + 1] = 1
        elif i.action == 'toggle':
            lights[i.start[1]:i.end[1] + 1, i.start[0]: i.end[0] + 1] = (lights[i.start[1]:i.end[1] + 1,
                                                                         i.start[0]: i.end[0] + 1] + 1) % 2
    return len(np.where(lights == 1)[1])


def run2():
    strings = open_file(day, year)
    lights = np.zeros((1000, 1000))

    instructions = trim(strings)

    for i in instructions:
        if i.action == 'off':
            lights[i.start[1]:i.end[1] + 1, i.start[0]: i.end[0] + 1] -= 1
            lights[lights < 0] = 0
        elif i.action == 'on':
            lights[i.start[1]:i.end[1] + 1, i.start[0]: i.end[0] + 1] += 1
        elif i.action == 'toggle':
            lights[i.start[1]:i.end[1] + 1, i.start[0]: i.end[0] + 1] += 2
    return int(np.sum(lights))


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
