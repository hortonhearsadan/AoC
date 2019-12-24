import itertools
import time

import networkx as nx

from utils import *
import dwave_networkx as dw

STRING = ''''''

TEST_STRING = ''''''
TEST_STRING2 = ''''''
TEST_STRING3 = ''''''
day=9
year=2015


def get_graph_from_string(string):
    g = nx.Graph()
    for s in string:
        s = s.replace('\n','').split(' ')
        g.add_edge(s[0],s[2],weight=int(s[4]))
    return g


def run1():
    string = open_file(day,year)
    graph = get_graph_from_string(string)

    pairs =list(itertools.combinations(list(graph.nodes),2))
    min_length=1000
    for p1,p2 in pairs:
        paths = list(nx.all_simple_paths(graph, p1,p2))
        paths = [path for path in paths if len(path) >= len(graph.nodes)]
        length = min([sum(graph.edges[p]['weight'] for p in zip(path,path[1:])) for path in paths])
        if length < min_length:
            min_length = length
    return min_length


def run2():
    string = open_file(day, year)
    graph = get_graph_from_string(string)

    pairs = list(itertools.combinations(list(graph.nodes), 2))
    max_length = 0
    for p1, p2 in pairs:
        paths = list(nx.all_simple_paths(graph, p1, p2))
        paths = [path for path in paths if len(path) >= len(graph.nodes)]
        length = max([sum(graph.edges[p]['weight'] for p in zip(path, path[1:])) for path in paths])
        if length > max_length:
            max_length = length
    return max_length

if __name__ == "__main__":
    start_time = time.time()
    f = run1()
    g = run2()
    print(f"Part 1:", f)
    print(f"Part2:", g)
    print(time.time() - start_time)
