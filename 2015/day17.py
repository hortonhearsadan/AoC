import time
from itertools import combinations

from utils import open_file, get_group_size

day = 17
year = 2015

TESTSTRING = ''''''
STRING = ''''''


def run1():
    target = 150
    string = open_file(day, year)
    containers = [int(c) for c in string]
    min_group_size = get_group_size(sorted(containers)[::-1], target)
    max_group_size = get_group_size(sorted(containers), target)
    combs = []
    for i in range(min_group_size, max_group_size + 1):
        combs += [c for c in combinations(containers, i) if sum(c) == target]
    return len(combs)


def run2():
    target = 150
    string = open_file(day, year)
    containers = [int(c) for c in string]
    min_group_size = get_group_size(sorted(containers)[::-1], target)
    combs = [c for c in combinations(containers, min_group_size) if sum(c) == target]
    return len(combs)


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
