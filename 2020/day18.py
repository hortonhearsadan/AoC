import time
from collections import defaultdict

from utils import open_file
import numpy as np
import networkx as nx
import scipy as sp

dir_path = __file__.split('/')
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = '''5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'''
STRING = ''''''


def parse_input():
    f = open_file(day,year)
    # f=TESTSTRING.split('\n')
    inputs =[]
    for eqn in f:
        line = eqn.strip().replace(" ","").strip()
        pri=0

        inputs.append(list(line))

    return inputs


def do_op(s, p,op):
    if op=="+":
        return int(s)+int(p)
    if op =="*":
        return int(s)*int(p)
    raise ValueError("bad op")


def calc(eqn):
    s=0
    op="+"
    for e in eqn:
        if e.isdigit():
            s= do_op(s,e,op)
        elif e in {"+","*"}:
            op=e
        elif e ==" ":
            continue
        else:
            raise ValueError("bad equation")
    return s

def run1(data):
    count=0
    for d in data:
        open_brackets=[i for i,s in enumerate(d) if "(" in s]
        close_brackets = [i for i,s in enumerate(d) if ")" in s]
        brackets_dict = {i:0 for i in open_brackets}
        for c in close_brackets:
            o = max(o for o in open_brackets if o<c)
            open_brackets.remove(o)
            brackets_dict[o]=c

        while "(" in d:
            used=[]
            for o,c in brackets_dict.items():
                if "(" in d[o+1:c]:
                    continue
                s= calc(d[o+1:c])
                d[o]=str(s)
                for i in range(o+1,c+1):
                    d[i]=" "
                used.append(o)
            for u in used:
                del brackets_dict[u]
        count+= calc(d)
    return count

def run2(data):
    pass


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs)
    g = run2(inputs)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
