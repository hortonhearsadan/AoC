import itertools
import time
from collections import defaultdict
from functools import reduce

from utils import open_file, prod
import numpy as np
import networkx as nx
import scipy as sp

dir_path = __file__.split("/")
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
STRING = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""


class Data:
    def __init__(self, fields, my_ticket, other_tickets):
        self.other_tickets = other_tickets
        self.my_ticket = my_ticket
        self.fields = fields

    def all_tickets(self):
        return self.other_tickets + [self.my_ticket]


class Field:
    def __init__(self, name, ranges):
        self.name = name
        self.ranges = ranges

    def value_in_range(self,v):
        return any(l<=v<=u for l,u in self.ranges)

def parse_input():
    with open(f"../inputs/input{day}{year}") as f:
        strings = f.read()
        # strings = TESTSTRING
        # strings = STRING
    fields, my_ticket, other_tickets = strings.split("\n\n")
    my_ticket_info = my_ticket.split("\n")[1].split(",")
    my_ticket_info = [int(i) for i in my_ticket_info]

    tickets = []
    for o in other_tickets.strip().split("\n")[1:]:
        ticket = [int(i) for i in o.split(",")]
        tickets.append(ticket)

    field_info = []
    for f in fields.split("\n"):
        name, ranges = f.split(": ")
        ranges = ranges.split(" or ")
        range_info = []
        for r in ranges:
            lower, upper = r.split("-")
            lower, upper = int(lower), int(upper)
            range_info.append((lower, upper))
        field_info.append(Field(name, range_info))

    return Data(field_info, my_ticket_info, tickets)


def run1(data):
    ranges = list(itertools.chain.from_iterable([f.ranges for f in data.fields]))
    count = 0
    valid_tickets = []
    for ticket in data.other_tickets:
        ticket_valid = True
        for f in ticket:
            valid = any(lower <= f <= upper for lower, upper in ranges)
            if not valid:
                count += f
                ticket_valid = False
        if ticket_valid:
            valid_tickets.append(ticket)
    data.other_tickets = valid_tickets
    return count


def run2(data):
    pos = len(data.my_ticket)
    tickets = data.all_tickets()
    order = defaultdict(set)

    for p in range(pos):
        values = [t[p] for t in tickets]
        for f in data.fields:
            # if all(f.ranges[0][0] <= v <= f.ranges[0][1] or f.ranges[1][0] <= v <= f.ranges[1][1] for v in values):
            if all(f.value_in_range(v) for v in values):
                order[p].add(f.name)

    final_positions = {}

    while len(final_positions) < pos:
        singletons = [(k, f) for k, f in order.items() if len(f) == 1]
        if not singletons:
            raise ValueError
        for k, s in singletons:
            name = next(iter(s))
            final_positions[k] = name
            for v in order.values():
                v.discard(name)

    return prod([v for i, v in enumerate(data.my_ticket) if "departure" in final_positions[i]])


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs)
    g = run2(inputs)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
