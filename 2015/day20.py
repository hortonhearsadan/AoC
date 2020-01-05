import math
import time
from collections import defaultdict

from utils import open_file

day = 0
year = 0

TESTSTRING = ''''''
STRING = ''''''


def get_factors(num):
    factors = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(int(num / i))
    return factors


def get_close_factors(num, limit):
    factors = set()
    for i in range(1, limit+1):
        if num % i == 0:
            v = int(num / i)
            # if v <= limit:
                # factors.add(i)
            factors.add(v)
    return factors


def run1():
    target = 29000000
    deliveries = 10
    real_target = target / deliveries
    house = 0
    presents = 0
    while presents < real_target:
        house += 1
        presents = sum(get_factors(house))

    return house


def run2():
    target = 29000000
    deliveries = 11
    real_target = target / deliveries
    houses = defaultdict(int)
    elf = 0
    visits = 50
    house = 0
    presents = 0

    # while True:
    #     elf += 1
    #     for i in range(1, visits + 1):
    #         house = i * elf
    #         houses[house] += elf
    #         if houses[house] >= real_target:
    #             return house, elf
    while presents < real_target:
        house += 1
        presents = sum(get_close_factors(house, visits))
    return house

if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
