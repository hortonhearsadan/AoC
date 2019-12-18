import itertools
import time

import networkx as nx
import numpy as np

from utils import get_adjacent

tunnels = '''#################################################################################
#.........#q..#.......................#.#.....................#...#.............#
#.#####.#.###.#.#######.#############.#.#.###################.#.#.#.#######.###.#
#...#...#...#.....#...#g#...........#...#.#...........#.O.#...#.#.#...#...#.#...#
###.#.#####.#######.#.#.#####.###.#.###.#.#####.#####.#.#.#.###.#F###.#.#.#.#T###
#.#.#...#...#.......#...#...#...#.#.#...#.....#...#.#.#.#...#...#...#.#.#...#...#
#.#.###.#.###.###########.#.#####.###.#######.#.#.#.#.#.#####.#####.#.#.#########
#...#...#.....#...........#.....#.#y..#.#.....#.#.#...#.....#...#...#.#.#.......#
#.###.#########.#####.#########.#.#.###.#.#######.#.#######.###.#.###.#.#.#####.#
#...#.......#...#.....#.....#.....#.#...#.#.......#.....#.#...#.#.#.#.#.......#.#
#.#######.#.#.#########.###.#.#####.#.#.#.###.#########.#.#.#.#.#.#.#.#########.#
#.#.....#.#.#.#...#.......#.#.#.#...#.#.#...#.#...#...#...#.#.#.#.#...#.#.......#
###.###.###.#.#.#.#.#######.#.#.#.#####.###.#.#.#.###.###.#.#.#.#.###.#.#.#####E#
#...#.......#...#...#...#...#...#.#.....#.#...#.#.......#.#.#.#.#...#...#...#...#
#.#################.###.#.#######.#.#.###.#####.#########.#.###.###.#.#####.#.###
#.......#.....#...#...#.#.......#.#.#...#.................#.#...#.#.#.#.....#...#
#.#####.#.###.#.#.###.#.#######.#.#####.#.#########.#######.#.###.#.#.#.#######.#
#e#...#.#.#.#.#.#.#...........#.........#.#.......#.....#...#.#...#.#.#.#.C.#...#
#.#.###.#.#.#.#.#.#######.#############.#.#.#####.#######.#.#.#.#.#.#.#.#.#.#.###
#.#.#...#...#...#...#.....#...#...#.....#.#...#.#.....#...#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#####.#######.#######.#.#.#.#######.###.#.#####.#.#####.#.#.#.###.#.###.#.#
#...#.#...#.#.....#...#...#.#...#.......#.#...#...#...#.....#.#.#.#.....#.....#.#
###.#.#.#.#.#####.#####.#.#.###########.#.#.###.#.#.###.###.###.#.#######.#####.#
#...#...#.#.........#...#...#...#.......#.#.#...#.#.#.#...#.....#...#...#...#...#
#.#######.#########.###.#######.#.#########.#.###.#.#.#.#####.###.#.#.#.###.#.#.#
#.#.#.....#.......#.#...#.......#.#.#...#...#...#...#...#...#.#...#.#.#...#.#.#.#
#.#.#.#####.#####.#.#.###.#######.#.#.#.#.#####.#####.###.#.###.###.#.#####.###Z#
#...#.........#...#...#.#.........#..k#.#.#.....#.......#.#...#...#...#.....#...#
###############.#.#####.#.#########.###.#.#.#############.###.###.#####.#####.#.#
#...N...#...#...#.#...#...#.#...#...#...#.#.............#.#.......#...#.#....b#.#
#.#####.#.#.#.###.###.#.###.#.#.#.###.#.#.#############.#.#########.#.#.###.###.#
#.#.......#.#...#.....#.#...#.#...#...#.#.#...#.......#.#...#.....#.#.#.....#...#
#.#########.###.#######.#.#.#.#####.###.#.#.#.#####.###.###.#.###.#.#.#######.###
#.#...V.#.#.H.#.#.......#.#.#.....#...#.#...#.#...#.........#...#...#.......#...#
#.#.###.#.###.#.#.#######.#####.#####.###.###.#.#.###.#####.###.#########.#####.#
#.....#.#...#.#.#.#.......#.....#...#...#.#...#.#...#.#...#.#...#.......#.....#.#
#.#####.#.###.#.#.#######.#.#####.#.###.###.#.#.###.###.#.###.###.#####.###.#.#.#
#.#.#...#..a....#...#...#...#.....#...#.#...#.#...#.....#.....#.#.....#..h..#.#.#
#.#.#.#############.#.#.#####.#######.#.#.#######.#############.#####.#########A#
#...#.................#.......#.............................X.......#...........#
#######################################.@.#######################################
#.D.....#.....#.......#.....#.........................#.....#.......#.#...#...#.#
#.###.#.#.#.#.#.#####.#.###.#.#.#######.#.###########.#.#.#.#.#####.#.#I#.#.#.#.#
#i#...#.#.#.#...#.....#.#...#.#x......#.#.#.......#...#.#.#...#.......#.#...#.#.#
###.###.###.#.#####.###.#.###.#######.#.#.###.###.#.#.#.#.#####.#######.#####.#.#
#...#.......#.#...#.#...#...#.#.#.....#.#.....#.#.#.#.#.#v....#.#...#...#d..#...#
#.#######.#####.#.#.#.#####.#.#.#.#####.#######.#.#.###.#####.#.#.###.###.#####.#
#.#.....#.#....u#.#.#...#...#...#.#.#...#.#...#...#.#...#.....#.#.#...#.........#
#.#.###.#.#.#####.#.###.#.#####.#.#.#.###.#.#.#.###.#.###.#####.#.#.###.#########
#.S.#.#.#.#.....#.#...#.#...#...#.#.#.#.#...#.....#.#...#...#.....#...#...#..s..#
#.###.#.#.#.#####.#.###.###.#.###.#.#.#.#.#########.#.#####.#########.###.#####.#
#.#...#.#.#.#.....#.#...#...#.#.#.#.#...#.....#...#...#...#n..#.P...#.#.#.......#
#.#.#.#.###.#.#####.#.###.###.#.#.#.###.#######.#.#####.#.###.#.###.#.#.#######.#
#...#.#.....#.....#.#.#...#.....#.#...#.#...#...#.....#.#...#.#.#.#...#.......#.#
#####.###########.#.#.###.#######.#.###.#.#.#.#######.#.###.#.#.#.#########.#.#U#
#.....#.......#...#.#...#.#.......#.....#.#...#.....#...#.....#.#...........#.#.#
#.#########.#.#.###.###.#.#.#######.#####.#####.#.###.#####.###.#.#######.#####.#
#.#.......#.#.#.#..w#...#...#...#...#.K.#...#.#.#.....#...#.#...#.#.#...#.#.....#
#.#.#####.#.#.#.###.#.#######.###.###.#.#.#.#.#.#######.#.###.###.#.#.#.#.#.#####
#...#..p....#.#...#.#...#...#...#.....#.#.#.#.#...#.....#...#...#.#...#...#.....#
#.###########.###.#.###.#.#.#R#.#######.#.#.#.###.#.#######.###.#.###.#########.#
#.#.......#.....#.#.#...#.#.#.#.......#.#.#.#.....#.#.#.....#.#.#...#.#.......#.#
#.#.#####.#######.#.#####M###.#.#####.#.#.#.###.###.#.#.#####.#W#.#.###.#.###.#.#
#.#.#.#.........#.#.#...#...#.#...#..m#.#.#...#.#...#.#.#...#j..#.#.#...#.#...#.#
#.#.#.#.#######.#.#.#.#.###.#.###.#####.#.###.###.###.#.#.#.#######.#.###.#.###.#
#.#.#.....#...#...#...#...#...#...#.....#.#.#.....#...#...#.........#.#...#.Q.#.#
#.#.#####.#.#.###########.#.###.#.#.#####.#.#######.#.#####.###.#####.#.#.#####.#
#.#.....#.#.#.........#...#.#...#.#.#...#...#.......#.#.#...#.#.#.G...#.#.#...#.#
#######.###.#########.#J#####L###.#.#.#.###.###.#.###.#.#.###.#.#.#####.###.#.#.#
#.....#.......#...#...#.#...#.#...#...#.#.#...#.#.#.....#.#...#.#.#...#.....#.Y.#
#B###.#######.###.#.###.#.#.#.#########.#.###.#.#.#######.#.###.#.#.#############
#.#...#...#...#...#...#l..#...#.....#...#.#...#.#.......#.#.....#.#.........#...#
#.###.#.#.#.###.#####.#######.#.###.#.###.#.###.#######.#.#####.#.#.###.###.#.###
#...#...#.#.....#...#...#...#.#.#.#...#.#.#.#...#.......#.....#.#.#...#.#...#f..#
#.#.#####.#.#####.#.###.#.#.#.#.#.#####.#.#.#####.#####.#####.###.#####.#.#####.#
#.#.....#.#.#.....#.#...#r#...#.....#...#.#.....#.#...#.#...#..o#.#.....#.#.....#
#.#####.#.###.#####.#.#.###########.#.#.#.#####.#.#.###.###.###.#.#.#####.#.#.#.#
#...#.#.#.....#z..#...#.#.....#.....#.#.#c....#.#.#...#.....#...#...#....t#.#.#.#
###.#.#.#######.#.#######.###.#.#######.#.#.###.#.#.#.#####.#.#######.#######.#.#
#.....#.........#...........#...........#.#.......#.#.......#.................#.#
#################################################################################'''

testunnel='''########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################'''


def reduce_graph(g, letters_pos):
    combinations = list(itertools.combinations(letters_pos, 2))
    letter_graph = nx.Graph()
    for u, v in combinations:
        weight = nx.shortest_path_length(g, u, v)
        letter_graph.add_edge(u, v, weight=weight)
    return letter_graph

def run1():
    string = testunnel
    string = string.split('\n')
    tunnel_array = np.array([list(s) for s in string])
    rows,columns = tunnel_array.shape
    paths = set()
    doors = set()
    keys = set()
    position = 0
    letters = {}
    for i in range(rows):

        for j in range(columns):
            e = tunnel_array[i, j]
            c = complex(j, -i)
            if e == '#':
                continue
            paths.add(c)
            if e == '@':
                position = c
            elif e != '.':
                letters[e]=c
                if e == e.upper():
                    doors.add(c)

                elif e == e.lower():
                    keys.add(c)
    g = nx.Graph()
    for p in paths:
        adj = get_adjacent(p)
        for a in adj & paths:
            g.add_edge(p, a)

    letters_pos = keys | doors | {position}
    letter_graph = reduce_graph(g,letters_pos)

    valid_nodes = keys

    s = nx.subgraph(letter_graph,keys)
    
    pass



def run2():
    pass


if __name__ == "__main__":
    start_time = time.time()
    f = run1()
    g = run2()
    print(f"Part 1:", f)
    print(f"Part2:", g)
    print(time.time() - start_time)
