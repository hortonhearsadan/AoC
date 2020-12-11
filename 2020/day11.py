import time
from utils import open_file
import numpy as np

dir_path = __file__.split("/")
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = """"""
STRING = """"""


def parse_input():
    f = open_file(day, year)
    matrix = np.array([list(s.strip()) for s in f])
    return matrix


def run1(plan):
    plan = np.pad(plan, [(1, 1), (1, 1)], "constant", constant_values=".")
    next_plan = plan.copy()
    while True:
        for i, j in enumerate(plan[1:-1], 1):
            for k, l in enumerate(j[1:-1], 1):
                adj = plan[i - 1 : i + 2, k - 1 : k + 2]
                occupied = np.count_nonzero(adj == "#")

                if l == "L":
                    if occupied == 0:
                        next_plan[i, k] = "#"

                elif l == "#":
                    if occupied >= 5:
                        next_plan[i, k] = "L"

        if not np.array_equal(plan, next_plan):
            plan = next_plan.copy()
        else:
            return np.count_nonzero(plan == "#")


def run2():
    pass


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs)
    g = run2()
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
