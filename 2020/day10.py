import time
from itertools import combinations

import networkx as nx

from utils import open_file
dir_path = __file__.split('/')
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''
STRING = ''''''

def parse_input():
    f = open_file(day,year)
    # f = TESTSTRING.split('\n')
    return [int(i) for i in f]

def run1(voltages):
    voltages = sorted(voltages)
    one_v,three_v =0,0
    outlet = 0
    device = max(voltages) + 3
    for i,j in zip([outlet]+voltages,voltages+[device]):
        diff = j-i
        if diff ==1:
            one_v+=1
        elif diff ==3:
            three_v +=1
    return one_v *three_v




def run2(voltages):
    outlet = 0
    device = max(voltages) + 3
    g = nx.DiGraph()
    g.add_node(outlet)
    g.add_node(device)
    voltages = voltages + [device,outlet]
    for i,j in combinations(voltages,2):
        diff = j-i
        if abs(diff) <=3:
            g.add_edge(*sorted((i,j)))
    print(len(g.nodes()),len(g.edges()))
    # return sum(1 for i in nx.all_simple_paths(g, outlet,device,cutoff=98))
    c=dfs(g,outlet,device)

    return c

def dfs(g,u, t):
    if u == t:
        return 1
    else:
        # if not u.npaths:
        # assume sum returns 0 if u has no children
        npaths = sum(dfs(g,c, t) for c in list(g[1]))
        return npaths

if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs)
    g = run2(inputs)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
