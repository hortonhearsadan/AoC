import time

import numpy as np

from utils import *

STRING = '''##.##
.#.##
##..#
#.#..
.###.'''

TEST_STRING = '''....#
#..#.
#..##
..#..
#....'''
TEST_STRING2 = ''''''
TEST_STRING3 = ''''''


def get_grid_from_string(string):
    grid = np.zeros((len(string), len(list(filter(None, string[0].replace('\n', ''))))))
    for i, s in enumerate(string):
        s = s.replace('\n', '')
        s = list(filter(None, s))
        for j, t in enumerate(s):
            if t == '#':
                grid[i, j] = 1

    return grid


def compute_neighbours(grid):
    buffer = (grid.shape[0] + 2, grid.shape[1] + 2)
    buffer_grid = np.zeros(buffer, dtype=int)
    buffer_grid[1:-1, 1:-1] = grid
    b_grid = np.roll(buffer_grid, 1, axis=1) + \
             np.roll(buffer_grid, -1, axis=1) + \
             np.roll(buffer_grid, 1, axis=0) + \
             np.roll(buffer_grid, -1, axis=0)
    neighbours = b_grid[1:-1, 1:-1]
    return neighbours


def run1():
    string = open_file(24, 2019)
    grid = get_grid_from_string(string)
    bios=set()
    while True:
        neighbours = compute_neighbours(grid)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                neigh = neighbours[i, j]
                if grid[i, j] == 0:

                    if neigh == 1 or neigh == 2:
                        grid[i, j] = 1
                else:
                    if neigh != 1:
                        grid[i, j] = 0
        bio = sum(2**i[0] for i, x in np.ndenumerate(grid.flatten()) if x ==1)
        if bio in bios:
            return bio
        bios.add(bio)

def run2():
    pass


if __name__ == "__main__":
    start_time = time.time()
    f = run1()
    g = run2()
    print(f"Part 1:", f)
    print(f"Part2:", g)
    print(time.time() - start_time)
