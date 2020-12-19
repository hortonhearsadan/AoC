import time
from collections import defaultdict

from utils import open_file
import numpy as np
import networkx as nx
import scipy as sp

dir_path = __file__.split('/')
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = ''''''
STRING = ''''''

def parse_input():
    with open(f"../inputs/input{day}{year}") as f:
        strings = f.read()
    data=defaultdict(list)
    rules,messages = strings.strip().split('\n\n')
    for r in rules.split('\n'):
        key, v = r.split(': ')
        v2 = v.split(" | ")
        for v3 in v2:
            v4 = v3.strip().split(' ')
            v4[0] = v4[0].replace('"','')
            data[int(key)].append(v4)

    messages = [m.strip() for m in messages.split('\n')]

    return data, messages

def yield_messages(key,message,):
    pass


def run1(data, messages):
    msg=''
    for i in data[0]:
        for j in i:
            if not j.isdigit():
                msg += j


def run2(data):
    pass


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(*inputs)
    g = run2(inputs)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
