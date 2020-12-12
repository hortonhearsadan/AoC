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
    for s in f:
        inputs.append(Move(s.strip()))
    return inputs


def run1(data):
    position = complex(0)
    current_dir = "E"
    for d in data:
        dir = d.direction
        v = d.value
        if dir in {"N", "E", "S", "W"}:
            position += v * dirs[dir]

        elif dir == "F":
            position += v * dirs[current_dir]

        elif dir in ("L", "R"):
            current_dir = reverse_dirs[dirs[current_dir] * ((dirs[dir]) ** (v / 90))]

    return abs(position.real) + abs(position.imag)


def run2(data):
    position = complex(0)
    waypoint = complex(10, 1)

    for d in data:
        dir = d.direction
        v = d.value
        if dir in {"N", "E", "S", "W"}:
            waypoint += v * dirs[dir]

        elif dir == "F":
            position += v * waypoint

        elif dir in {"L", "R"}:
            waypoint *= (dirs[dir]) ** (v / 90)

    return abs(position.real) + abs(position.imag)


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs)
    g = run2(inputs)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
