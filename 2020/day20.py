import time
from collections import defaultdict

from utils import open_file, prod
import numpy as np
import networkx as nx
import scipy as sp

dir_path = __file__.split('/')
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = '''Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...'''
STRING = ''''''

class Tile:
    def __init__(self,_id,pattern):
        self.id=_id
        self.pattern=pattern

    @property
    def left(self):
        return ''.join(i[0] for i in self.pattern)

    @property
    def right(self):
        return ''.join(i[-1] for i in self.pattern)

    def sides(self):
        return [self.left, self.right, self.left[::-1], self.right[::-1],self.top, self.bottom, self.top[::-1],self.bottom[::-1]]

    @property
    def top(self):
        return self.pattern[0]

    @property
    def bottom(self):
        return self.pattern[-1]

    def ends(self):
        return [self.top, self.bottom, self.top[::-1],self.bottom[::-1]]


def parse_input():
    with open(f"../inputs/input{day}{year}") as f:
        strings = f.read()
        # strings = TESTSTRING
    # strings = STRING
    inputs=[]
    for s in strings.strip().split('\n\n')[:-1]:
        s=s.split('\n')
        _,tile = s[0].strip()[:-1].split(' ')
        tile=int(tile)
        pattern=s[1:]
        inputs.append(Tile(tile,pattern))


    return inputs

def run1(data):
    side_joins=defaultdict(list)
    end_joins=defaultdict(list)
    for tile in data:
        for s in tile.sides():
            side_joins[s].append(tile.id)


    sides = [(k,v[0]) for k,v in side_joins.items() if len(v)==1]
    sides2={t.id:0 for t in data}
    for side,t in sides:
        sides2[t]+=0.5
    return prod(k for k,v in sides2.items() if v>=2)
    pass

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
