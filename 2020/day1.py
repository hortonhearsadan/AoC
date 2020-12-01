import time
from itertools import combinations

from utils import open_file

day = 1
year = 2020

TESTSTRING = """1721
979
366
299
675
1456"""
STRING = """"""


def parse_nums():
    with open(f"../input{year}{day}") as f:
        string = f.readlines()
    return [int(s) for s in string]


def run1():
    numbers = parse_nums()

    return sum(i * j for i, j in combinations(numbers, 2) if i + j == 2020)


def run2():
    numbers = parse_nums()

    return sum(i * j * k for i, j, k in combinations(numbers, 3) if i + j + k == 2020)


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
