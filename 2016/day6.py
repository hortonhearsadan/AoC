import time
from utils import open_file
import numpy as np
day = 6
year = 2016

TESTSTRING = ''''''
STRING = open_file(day,year)

def run1():
    grid = np.array([list(s.replace('\n','')) for s in STRING])
    word = []
    for i in range(grid.shape[1]):
        letters,counts = np.unique(grid[:,i],return_counts=True)
        l = letters[np.argmax(counts)]
        word.append(l)

    return ''.join(word)

def run2():
    grid = np.array([list(s.replace('\n', '')) for s in STRING])
    word = []
    for i in range(grid.shape[1]):
        letters, counts = np.unique(grid[:, i], return_counts=True)
        l = letters[np.argmin(counts)]
        word.append(l)
    return ''.join(word)


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
