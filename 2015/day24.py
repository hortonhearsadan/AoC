import math
import operator
import time
from functools import reduce
from itertools import combinations

from utils import open_file, get_group_size

day = 24
year = 2015

TESTSTRING = ''''''
STRING = ''''''


def get_combs_that_equal_group_weight(packages, group_weight, min_size, max_size):
    p = []
    if len(packages) > 0:
        for r in range(min_size, max_size + 1):
            combs = combinations(packages, r)

            for item in combs:
                if sum(item) == group_weight:
                    p.append(set(item))

    return p


def run1():
    string = open_file(day, year)
    packages = set(int(s) for s in string)
    total_weight = sum(packages)
    group_weight = total_weight / 3
    min_group_size = get_group_size(sorted(packages)[::-1], group_weight)
    max_group_size = get_group_size(sorted(packages), group_weight)
    for i in range(min_group_size, max_group_size + 1):
        combs = [set(c) for c in combinations(packages, i) if sum(c) == group_weight]
        for c in combs:
            new_packages = packages - c
            for j in range(min_group_size, max_group_size + 1):
                new_combs = [set(c) for c in combinations(packages, i) if sum(c) == group_weight]
                for d in new_combs:
                    if sum(d) == group_weight:
                        return reduce(operator.mul, c)

    pass


def run2():
    string = open_file(day, year)
    packages = set(int(s) for s in string)
    total_weight = sum(packages)
    group_weight = total_weight / 4
    min_group_size = get_group_size(sorted(packages)[::-1], group_weight)
    max_group_size = get_group_size(sorted(packages), group_weight)
    for i in range(min_group_size, max_group_size + 1):
        combs = [set(c) for c in combinations(packages, i) if sum(c) == group_weight]
        for c in combs:
            new_packages = packages - c
            for j in range(min_group_size, max_group_size + 1):
                new_combs = [set(c) for c in combinations(packages, i) if sum(c) == group_weight]
                for d in new_combs:
                    newer_packages = new_packages - d
                    for j in range(min_group_size, max_group_size + 1):
                        newer_combs = [set(c) for c in combinations(packages, i) if sum(c) == group_weight]
                        for e in newer_combs:
                            if sum(e) == group_weight:
                                return reduce(operator.mul, c)


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
