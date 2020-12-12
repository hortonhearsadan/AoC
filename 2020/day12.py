import time
from utils import open_file
import networkx as nx
import numpy as np

dir_path = __file__.split("/")
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])


TESTSTRING = """F10
N3
F7
R90
F11"""
STRING = """"""


class Move:
    def __init__(self, s):
        self.direction = s[0]
        self.value = int(s[1:])


dirs = {"N": 1j, "S": -1j, "E": 1, "W": -1, "L": 1j, "R": -1j}
reverse_dirs = {1j: "N", -1j: "S", 1: "E", -1: "W"}


def parse_input():
    f = open_file(day, year)
    # f=TESTSTRING.split('\n')
    inputs = []
    # for s in f:
    #     inputs.append(Move(s.strip()))
    # return inputs
    return f


def run1(data):
    position1 = complex(0)
    position2 = complex(0)
    waypoint = complex(10,1)
    current_dir = "E"
    for d in data:
        dir = d[0]
        v = int(d[1:])
        if dir in {"N", "E", "S", "W"}:
            action = v * dirs[dir]
            position1 += action
            waypoint += action

        elif dir == "F":
            position1 += v * dirs[current_dir]
            position2 += v * waypoint

        elif dir in {"L", "R"}:
            turn = (dirs[dir]) ** (v / 90)
            current_dir = reverse_dirs[dirs[current_dir] * turn]
            waypoint *= turn

    part1 =abs(position1.real) + abs(position1.imag)
    part2 = abs(position2.real) + abs(position2.imag)
    return part1,part2


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f,g = run1(inputs)
    # g = run2(inputs)
    # f,g=0,0
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
