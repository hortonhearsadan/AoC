import time
from utils import open_file

dir_path = __file__.split("/")
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])
import networkx as nx

TESTSTRING = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

STRING = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


def parse_input():
    inputs = open_file(day, year)
    # inputs= TESTSTRING.split('\n')
    g = nx.DiGraph()
    for i in inputs:
        outer, inner = (
            i.strip()
            .replace("bags", "")
            .replace("bag", "")
            .replace(".", "")
            .strip()
            .split("contain")
        )
        outer = outer.strip()
        if "no other" in inner:
            g.add_node(outer)
            continue
        inner = inner.strip()
        inner_list = inner.split(",")
        for j in inner_list:
            if j.strip()[0].isdigit():
                real_inner_list = j.strip().split(" ")
                real_inner = real_inner_list[1] + " " + real_inner_list[2]
                weight = int(real_inner_list[0])
            else:
                real_inner = j
                weight = 1
            g.add_edge(outer, real_inner, weight=weight)
    return g


def run1(bags):
    return len(nx.ancestors(bags, "shiny gold"))


def run2(bags, u="shiny gold"):
    inner_bags = bags.successors(u)
    count = 0
    for v in inner_bags:
        count += bags.edges[u, v]["weight"] * (run2(bags, v) + 1)
    return count


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs)
    g = run2(inputs)
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
