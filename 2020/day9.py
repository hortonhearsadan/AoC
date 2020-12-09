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
    pre_nums = deque(nums[i:preamble])
    nums = iter(nums[preamble:])
    while True:
        target = next(nums)
        if any(target - n in pre_nums for n in pre_nums):
            pre_nums.append(target)
            pre_nums.popleft()
        else:
            return target


def run2(nums, number):
    dnums = deque()
    nums = iter(nums)
    s = 0
    while True:
        if s < number:
            t = next(nums)
            dnums.append(t)
            s += t
        elif s > number:
            t = dnums.popleft()
            s -= t
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
