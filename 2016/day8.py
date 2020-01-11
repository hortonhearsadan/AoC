import time
import numpy as np
from utils import open_file
day = 0
year = 0

TESTSTRING = ''''''
STRING = open_file(8,2016)


def parse_rect(grid, s):
    cols,rows = s[1].split('x')
    grid[:int(rows),:int(cols)] = 1


def parse_rotate(grid, s):
    orientation = s[1]
    idx = int(s[2][2:])
    amount = int(s[4])
    if orientation == 'column':
        grid[:, idx]= np.roll(grid[:,idx], amount)
    elif orientation == 'row':
        grid[idx,:]= np.roll(grid[idx,:], amount)

def run1():
    grid = np.zeros((6,50))
    for s in STRING:
        s = s.strip().split(' ')
        if s[0] == 'rect':
            parse_rect(grid,s)
        elif s[0] == 'rotate':
            parse_rotate(grid,s)

    return np.count_nonzero(grid)

def run2():
    pass


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
