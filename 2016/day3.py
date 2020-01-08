import time
from utils import open_file
import numpy as np

day = 0
year = 0

TESTSTRING = ''''''
STRING = ''''''


def run1():
    string = open_file(3, 2016)
    valid_triangles = []
    for s in string:
        triangle = chunk(s)
        if sum(triangle) > 2 * max(triangle):
            valid_triangles.append(triangle)
    return len(valid_triangles)


def parse(s):
    return list(filter(None, s.split(' ')))


def chunk(s):
    return [int(i) for i in parse(s)]


def run2():
    string = open_file(3, 2016)
    valid_triangles = []
    t = np.array([[chunk(s) for s in string]])
    trans = t.transpose()
    trans = trans[:, :, 0]
    trans = np.reshape(trans, (len(string), 3))
    for triangle in trans:
        if np.sum(triangle) > 2 * np.max(triangle):
            valid_triangles.append(triangle)
    return len(valid_triangles)


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
