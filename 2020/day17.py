import itertools
import time
from utils import open_file, get_adjacent_with_diag

dir_path = __file__.split("/")
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = """.#.
..#
###"""
STRING = """"""


def parse_input():
    f = open_file(day, year)
    # f=TESTSTRING.split('\n')
    inputs = []
    for i, j in enumerate(f):
        for k, l in enumerate(j):
            if l == "#":
                inputs.append((k, -i))

    return set(inputs)


def get_ranges(d):
    return [[i + j for j in range(-1, 2)] for i in d]


def get_adj(d):
    ranges = get_ranges(d)

    adj = list(itertools.product(*ranges))
    return adj


def run1(data, cycles, dims):
    actives = {i + (0,) * (dims - 2) for i in data}
    for r in range(cycles):
        new_actives = set()
        for d in actives:
            adj = get_adj(d)
            count = sum(1 for i in adj if i in actives)
            if 3 <= count <= 4:
                new_actives.add(d)

            for ad in adj:
                if ad in actives:
                    continue
                if ad in new_actives:
                    continue
                count = sum(1 for i in get_adj(ad) if i in actives)
                if count == 3:
                    new_actives.add(ad)
        actives = new_actives
    return len(actives)


def run2(data):
    pass


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs, cycles=6, dims=3)
    g = run1(inputs, cycles=6, dims=4)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
