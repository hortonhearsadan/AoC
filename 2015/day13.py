import itertools
import time
from collections import defaultdict

import networkx as nx

from utils import *

STRING = ''''''

TEST_STRING = ''''''
TEST_STRING2 = ''''''
TEST_STRING3 = ''''''


def get_graph_from_happiness(seating_happ, you=False):
    graph = nx.Graph()
    for peeps, happ in seating_happ.items():
        graph.add_edge(peeps[0],peeps[1], weight = happ)

    if you:
        for n in list(graph.nodes):
            graph.add_edge(n,'You',weight=0)
    return graph

def get_seating_happiness(string):
    happs = defaultdict(int)
    for s in string:
        s = s.replace('\n','').replace('.','')
        s = list(filter(None,s.split(' ')))
        p1 = s[0]
        p2 = s[-1]
        h = int(s[3])
        sign = s[2]
        if sign == 'lose':
            h = -h
        happs[tuple(sorted([p1,p2]))] += h
    return happs

def run1():
    string = open_file(13, 2015)
    seating_happ = get_seating_happiness(string)
    graph = get_graph_from_happiness(seating_happ)

    pairs = list(itertools.combinations(list(graph.nodes), 2))
    max_hap = 0
    for p1,p2 in pairs:
        paths = list(nx.all_simple_paths(graph, p1,p2))
        paths = [path for path in paths if len(path) >= len(graph.nodes)]
        length = max([sum(graph.edges[p]['weight'] for p in zip(path,path[1:]) )+ seating_happ.get((tuple(sorted([p1,p2]))),0) for path in paths])
        if length > max_hap:
            max_hap = length
    return max_hap

def run2():
    string = open_file(13, 2015)
    seating_happ = get_seating_happiness(string)
    graph = get_graph_from_happiness(seating_happ, you=True)

    pairs = list(itertools.combinations(list(graph.nodes), 2))
    max_hap = 0
    for p1, p2 in pairs:
        paths = list(nx.all_simple_paths(graph, p1, p2))
        paths = [path for path in paths if len(path) >= len(graph.nodes)]
        length = max(
            [sum(graph.edges[p]['weight'] for p in zip(path, path[1:])) + seating_happ[(tuple(sorted([p1, p2])))] for
             path in paths])
        if length > max_hap:
            max_hap = length
    return max_hap


if __name__ == "__main__":
    start_time = time.time()
    f = run1()
    g = run2()
    print(f"Part 1:", f)
    print(f"Part2:", g)
    print(time.time() - start_time)
