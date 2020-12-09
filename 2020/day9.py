import time
from itertools import combinations
from collections import deque
from utils import open_file

dir_path = __file__.split("/")
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
STRING = """"""


def parse_input():
    nums = open_file(day, year)
    # nums = TESTSTRING.split('\n')
    return [int(n) for n in nums]


def run1(nums, preamble):
    i = 0
    j = preamble
    while True:
        pre_nums = nums[i:j]
        target = nums[j]
        if any(i + j == target for i, j in combinations(pre_nums, 2)):
            i += 1
            j += 1
        else:
            return target


def run2(nums, number):
    dnums = deque()
    nums = iter(nums)
    while True:
        s = sum(dnums)
        if s < number:
            dnums.append(next(nums))
        elif s > number:
            dnums.popleft()
        else:
            return min(dnums) + max(dnums)


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs, 25)
    g = run2(inputs, f)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
