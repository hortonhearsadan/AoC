import time

from utils import open_file

day = 3
year = 2020

TESTSTRING = """"""
STRING = """"""

TREE = "#"
SOIL = "."


def parse_input():
    string = open_file(day, year)
    strs = [s.rstrip() for s in string]
    return strs


def run1(x, y):
    l = len(inputs[0])
    count = 0
    x0 = x
    y0 = y

    while y0 < len(inputs):
        is_tree = inputs[y0][x0 % l] == TREE

        count += is_tree
        x0 += x
        y0 += y

    return count


def run2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = 1
    for slope in slopes:
        trees *= run1(*slope)
    return trees


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(3, 1)
    g = run2()
    print(f"Runtime: {round((time.time() - a)*1000, 3)}ms")
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
