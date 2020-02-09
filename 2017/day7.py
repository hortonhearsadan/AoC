import time
from collections import defaultdict

import networkx as nx

from utils import open_file
day = 7
year = 2017

TESTSTRING = ''''''
STRING = open_file(day,year)


def get_graph(strings):
    g = nx.DiGraph()
    for s in strings:
        s = s.replace(',','').split(' ')
        node = s[0]
        weight=s[1].strip()[1:-1]
        g.add_node(node,weight=int(weight))
        if '->' in s:
            for t in s[3:]:
                g.add_edge(node,t.strip())


    return g


def run1():
    g = get_graph(STRING)
    path = list(nx.topological_sort(g))
    return path[0]

def run2():
    g = get_graph(STRING)
    path = list(nx.topological_sort(g))
    source = path[0]
    branches = list(g[source])
    for b in branches:
        twigs = list(g[b])
        balance = defaultdict(list)
        for c in twigs:
            weights = sum(g.nodes[node]['weight'] for node in nx.descendants(g,c))
            balance[weights].append(c)
        if len(balance.keys()) >1:
            for k,v in balance.items():
                print (k, len(v))

if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
