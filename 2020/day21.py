import itertools
import time
from collections import defaultdict

from utils import open_file
import numpy as np
import networkx as nx
import scipy as sp

dir_path = __file__.split("/")
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
STRING = """"""


class Packet:
    def __init__(self, ingredients, allergens):
        self.ingredients = ingredients
        self.allergens = allergens


def parse_input():
    f = open_file(day, year)
    # f= TESTSTRING.split('\n')
    inputs = []
    for i in f:
        ingredients, allergens = i.strip().split(" (contains ")
        ingredients = ingredients.split(" ")
        allergens = allergens[:-1].split(", ")
        inputs.append(Packet(set(ingredients), set(allergens)))
    return inputs


def run1(data):
    all_allergens = set(itertools.chain.from_iterable([d.allergens for d in data]))
    all_ingredients = set(itertools.chain.from_iterable([d.ingredients for d in data]))
    possible = {a: all_ingredients.copy() for a in all_allergens}
    counts = defaultdict(int)
    for d in data:
        for al in d.allergens:
            possible[al] &= d.ingredients

        for ing in d.ingredients:
            counts[ing] += 1

    sus_ingredients = set(itertools.chain(*possible.values()))
    safe_ingredients = all_ingredients - sus_ingredients

    part1 = sum(counts[safe] for safe in safe_ingredients)
    definite = {}
    while len(definite) < len(possible):
        singletons = [(k, f) for k, f in possible.items() if len(f) == 1]
        for k, p in singletons:
            i = p.pop()
            definite[k] = i
            for v in possible.values():
                v.discard(i)

    part2 = ",".join(definite[k] for k in sorted(definite.keys()))
    return part1, part2


def run2(data):
    pass


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f, g = run1(inputs)
    # g = run2(inputs)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
