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
        for row_idx, row in enumerate(plan[1:-1], 1):
            for col_idx, seat in enumerate(row[1:-1], 1):
                adj = plan[row_idx - 1 : row_idx + 2, col_idx - 1 : col_idx + 2]
                occupied = np.count_nonzero(adj == "#")

                if seat == "L":
                    if occupied == 0:
                        next_plan[row_idx, col_idx] = "#"

                elif seat == "#":
                    if occupied >= 5:
                        next_plan[row_idx, col_idx] = "L"

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
